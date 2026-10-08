#!/usr/bin/env python3
"""Validate portable QA records and export evidence-backed release reports.

This helper never drives a browser, invokes an MCP server, or contacts a site.
All writes create a new campaign directory; existing files are never replaced.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qsl, unquote, urlsplit

from jsonschema import Draft7Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
STATUSES = ("PASS", "FAIL", "BLOCKED", "NOT_RUN", "NOT_APPLICABLE")
SECRET_KEYS = {"password", "passwd", "access_token", "refresh_token", "api_key",
               "authorization", "cookie", "set-cookie", "secret"}
SECRET_PATTERN = re.compile(
    r"(?i)(?:bearer\s+[a-z0-9._-]{12,}|(?:password|api[_-]?key|access[_-]?token)"
    r"\s*[:=]\s*[\"']?[^\s\"',;]{6,})"
)
SCOPE_NOTE = "This verdict applies only to the explicitly planned cases and observed environment."


class ContractError(ValueError):
    """An input violates the campaign contract."""


def require(condition, message):
    if not condition:
        raise ContractError(message)


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key: " + key)
        result[key] = value
    return result


def load_json(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=unique_pairs,
                         parse_constant=lambda value: (_ for _ in ()).throw(
                             ContractError("Non-finite JSON value: " + value)))


def schema_check(data, name):
    schema = load_json(ROOT / "schemas" / name)
    validator = Draft7Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda e: str(list(e.path)))
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.path) or "<root>"
        raise ContractError(location + ": " + first.message)


def secret_check(value, location="<root>"):
    """Reject obvious credential material; this is not a complete privacy audit."""
    if isinstance(value, dict):
        for key, item in value.items():
            require(key.lower() not in SECRET_KEYS,
                    location + ": credential-like field must be removed or masked")
            secret_check(item, location + "." + key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            secret_check(item, location + "[" + str(index) + "]")
    elif isinstance(value, str):
        require(not SECRET_PATTERN.search(value),
                location + ": possible credential material requires redaction")
        if value.startswith(("http://", "https://")):
            parsed = urlsplit(value)
            require(parsed.username is None and parsed.password is None,
                    location + ": URL credentials are forbidden")
            require(not any(key.lower() in SECRET_KEYS for key, _ in parse_qsl(parsed.query)),
                    location + ": credential-bearing query string is forbidden")


def unique_ids(items, label):
    ids = [item["id"] for item in items]
    require(len(ids) == len(set(ids)), "Duplicate " + label + " IDs")
    return set(ids)


def url_origin(url):
    parsed = urlsplit(url)
    require(parsed.scheme in ("http", "https") and parsed.hostname,
            "Only absolute HTTP(S) URLs are supported")
    require(parsed.username is None and parsed.password is None,
            "URL credentials are forbidden")
    return parsed.scheme.lower() + "://" + parsed.netloc.lower()


def path_matches(path, prefix):
    if prefix == "/":
        return True
    prefix = prefix.rstrip("/")
    return path == prefix or path.startswith(prefix + "/")


def within_scope(url, scope):
    origin = url_origin(url)
    path = unquote(urlsplit(url).path) or "/"
    require("\\" not in path and ".." not in PurePosixPath(path).parts,
            "URL path traversal is not allowed")
    return (origin in scope["allowed_origins"]
            and origin not in scope["excluded_origins"]
            and any(path_matches(path, p) for p in scope["allowed_paths"])
            and not any(path_matches(path, p) for p in scope["excluded_paths"]))


def validate_config(data):
    schema_check(data, "config.schema.json")
    secret_check(data)
    scope = data["scope"]
    for origin in scope["allowed_origins"] + scope["excluded_origins"]:
        parsed = urlsplit(origin)
        require(origin == url_origin(origin) and not parsed.path and not parsed.query
                and not parsed.fragment, "Scope origins must omit paths, queries, and fragments")
    for path in scope["allowed_paths"] + scope["excluded_paths"]:
        require(path.startswith("/") and "\\" not in path
                and ".." not in PurePosixPath(unquote(path)).parts,
                "Scope paths must be absolute, non-traversing path prefixes")
    require(within_scope(data["start_url"], scope), "Start URL is outside the allowed scope")
    language_ids = {item["code"] for item in data["languages"]}
    require(len(language_ids) == len(data["languages"]), "Duplicate language codes")
    for item in data["languages"]:
        require(within_scope(item["entry_url"], scope), "Language entry URL is outside scope")
    unique_ids(data["url_mappings"], "URL mapping")
    for mapping in data["url_mappings"]:
        require(set(mapping["urls"]) <= language_ids, "URL mapping names an unknown language")
        for url in mapping["urls"].values():
            require(within_scope(url, scope), "Mapped URL is outside scope")
    profile_ids = unique_ids(data["profiles"], "profile")
    journey_ids = unique_ids(data["journeys"], "journey")
    unique_ids(data["cases"], "case")
    require(len(data["countries"]) == len(set(data["countries"])), "Duplicate countries")
    for journey in data["journeys"]:
        numbers = [step["number"] for step in journey["steps"]]
        require(numbers == list(range(1, len(numbers) + 1)),
                "Journey step numbers must be consecutive from 1")
        for step in journey["steps"]:
            require(step["expected"] is not None
                    or step["expectation_basis"] == "PRODUCT_QUESTION",
                    "A missing expected result must be a PRODUCT_QUESTION")
    for case in data["cases"]:
        require(case["journey_id"] in journey_ids, "Unknown journey reference")
        require(case["profile_id"] in profile_ids, "Unknown profile reference")
        require(case["language"] in language_ids, "Unknown language reference")
        require(case["country"] is None or case["country"] in data["countries"],
                "Case country is not explicitly requested")
    auth = data["authentication"]
    if auth["mode"] == "NONE":
        require(auth["reference"] is None, "NONE authentication cannot contain a credential reference")
    else:
        require(isinstance(auth["reference"], str) and auth["reference"].strip(),
                "Authentication needs a non-secret reference")
    require(set(data["output"]["formats"]) == {"JSON", "MARKDOWN", "CSV"},
            "A campaign exports JSON, MARKDOWN, and CSV together")
    return {"valid": True, "planned_cases": len(data["cases"]),
            "profiles": len(profile_ids), "languages": len(language_ids)}


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def chronological(start, finish, label):
    require(timestamp(start) <= timestamp(finish), label + ": end precedes start")


def aggregate_steps(steps):
    states = {step["status"] for step in steps}
    for status in ("FAIL", "BLOCKED", "NOT_RUN"):
        if status in states:
            return status
    if "PASS" in states:
        return "PASS"
    return "NOT_APPLICABLE"


def summarize(data):
    counts = {status: 0 for status in STATUSES}
    for case in data["cases"]:
        counts[case["status"]] += 1
    planned = len(data["cases"])
    executed = counts["PASS"] + counts["FAIL"]
    attempted = executed + counts["BLOCKED"]
    uncovered = [case["id"] for case in data["cases"]
                 if case["critical"] and case["status"] not in ("PASS", "FAIL")]
    if executed == 0:
        verdict = "NO_EXECUTION"
    elif counts["FAIL"]:
        verdict = "ISSUES_FOUND"
    elif counts["BLOCKED"] or counts["NOT_RUN"] or uncovered:
        verdict = "INCOMPLETE"
    else:
        verdict = "READY_FOR_TESTED_SCOPE"
    return {"planned": planned, "counts": counts, "executed": executed,
            "attempted": attempted,
            "coverage": {"numerator": executed, "denominator": planned},
            "critical_uncovered": uncovered, "verdict": verdict, "scope_note": SCOPE_NOTE}


def safe_evidence_path(base, relative):
    path = PurePosixPath(relative)
    require(not path.is_absolute() and len(path.parts) >= 2
            and path.parts[0] == "evidence" and ".." not in path.parts
            and "\\" not in relative and ":" not in relative,
            "Evidence path must remain beneath evidence/: " + relative)
    require(str(path) == relative and "." not in path.parts,
            "Evidence path must be normalized: " + relative)
    base = Path(base).resolve()
    candidate = base
    for part in path.parts:
        candidate = candidate / part
        require(not candidate.is_symlink(), "Evidence symlinks are forbidden: " + relative)
    require(candidate.is_file(), "Missing evidence file: " + relative)
    require(candidate.resolve().is_relative_to(base), "Evidence escapes campaign directory")
    return candidate


def check_refs(refs, known, label):
    require(len(refs) == len(set(refs)), label + ": duplicate evidence reference")
    require(set(refs) <= known, label + ": unknown evidence reference")


def validate_results(data, base, observations=False):
    candidate = copy.deepcopy(data)
    computed = summarize(candidate)
    if observations and "summary" not in candidate:
        candidate["summary"] = computed
    schema_check(candidate, "results.schema.json")
    secret_check(candidate)
    require(candidate["summary"] == computed, "Summary does not reconcile with case results")
    campaign = candidate["campaign"]
    chronological(campaign["started_at"], campaign["finished_at"], "Campaign")
    case_ids = unique_ids(candidate["cases"], "case")
    evidence_ids = unique_ids(candidate["evidence"], "evidence")
    unique_ids(candidate["tickets"], "ticket")
    evidence_by_id = {item["id"]: item for item in candidate["evidence"]}
    evidence_paths = [item["path"] for item in candidate["evidence"]]
    require(len(evidence_paths) == len(set(evidence_paths)), "Duplicate evidence paths")
    for evidence in candidate["evidence"]:
        path = safe_evidence_path(base, evidence["path"])
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == evidence["sha256"], "Evidence checksum mismatch: " + evidence["path"])
        if evidence["kind"] in ("TEXT", "DOM", "NETWORK", "CONSOLE"):
            try:
                secret_check(path.read_text(encoding="utf-8"), "evidence/" + evidence["id"])
            except UnicodeDecodeError:
                raise ContractError("Text evidence must be UTF-8: " + evidence["path"])
    by_id = {case["id"]: case for case in candidate["cases"]}
    for case in candidate["cases"]:
        label = case["id"]
        chronological(case["started_at"], case["finished_at"], label)
        require(timestamp(case["started_at"]) >= timestamp(campaign["started_at"])
                and timestamp(case["finished_at"]) <= timestamp(campaign["finished_at"]),
                label + ": case time is outside campaign time")
        url_origin(case["url"])
        require(case["profile"]["browser"]["version"] is not None or case["limitations"],
                label + ": unavailable browser version needs a limitation")
        require(case["profile"]["device_class"] != "REAL_MOBILE"
                or case["profile"].get("physical_device") is True,
                label + ": REAL_MOBILE needs an explicitly observed physical device")
        require(aggregate_steps(case["steps"]) == case["status"],
                label + ": case status contradicts its step results")
        numbers = [step["number"] for step in case["steps"]]
        require(numbers == list(range(1, len(numbers) + 1)),
                label + ": step numbers must be consecutive from 1")
        check_refs(case["evidence_ids"], evidence_ids, label)
        all_case_evidence = set(case["evidence_ids"])
        for step in case["steps"]:
            check_refs(step["evidence_ids"], evidence_ids, label + " step")
            all_case_evidence.update(step["evidence_ids"])
            if step["status"] == "FAIL":
                require(step["evidence_ids"], label + ": failed step has no evidence")
        attempts = case["attempts"]
        require([a["number"] for a in attempts] == list(range(1, len(attempts) + 1)),
                label + ": attempt numbers must be consecutive from 1")
        for attempt in attempts:
            check_refs(attempt["evidence_ids"], evidence_ids, label + " attempt")
            all_case_evidence.update(attempt["evidence_ids"])
        if case["status"] in ("PASS", "FAIL", "BLOCKED"):
            require(attempts and attempts[-1]["status"] == case["status"],
                    label + ": latest attempt must match the reported outcome")
        if case["status"] == "FAIL":
            require(case["classification"] == "DEFECT",
                    label + ": FAIL denotes a demonstrated site defect")
        require(case["classification"] != "TOOLING_INCIDENT" or case["status"] == "BLOCKED",
                label + ": a tooling incident must be BLOCKED, not a site failure")
        require(case["status"] not in ("BLOCKED", "NOT_RUN")
                or case["limitations"] or case["uncertainties"],
                label + ": incomplete cases require a stated limitation or uncertainty")
        country = case["country"]
        check_refs(country["evidence_ids"], evidence_ids, label + " country")
        if country["requested"] is None:
            require(country["verified"] is None and country["status"] == "NOT_APPLICABLE"
                    and not country["same_network_context"] and not country["evidence_ids"],
                    label + ": unrequested country verification must be NOT_APPLICABLE")
        elif country["status"] in ("PASS", "FAIL"):
            require(country["verified"] is not None and country["same_network_context"]
                    and country["evidence_ids"],
                    label + ": country outcome requires same-network-context evidence")
            require(any(evidence_by_id[ref]["kind"] == "NETWORK"
                        for ref in country["evidence_ids"]),
                    label + ": country verification needs network evidence")
            require((country["verified"] == country["requested"])
                    == (country["status"] == "PASS"),
                    label + ": country result contradicts requested/verified country")
        else:
            require(country["status"] in ("BLOCKED", "NOT_RUN")
                    and country["verified"] is None and not country["same_network_context"],
                    label + ": unproven geography must be BLOCKED or NOT_RUN")
            require(case["status"] != "PASS",
                    label + ": a required geographic check is not covered")
    for ticket in candidate["tickets"]:
        label = ticket["id"]
        require(set(ticket["case_ids"]) <= case_ids, label + ": unknown case reference")
        require(len(ticket["case_ids"]) == len(set(ticket["case_ids"])),
                label + ": duplicate case references")
        linked = [by_id[ref] for ref in ticket["case_ids"]]
        require(any(case["status"] == "FAIL" for case in linked),
                label + ": a defect ticket needs a demonstrated failed case")
        check_refs(ticket["evidence_ids"], evidence_ids, label)
        linked_refs = set()
        for case in linked:
            linked_refs.update(case["evidence_ids"])
            for step in case["steps"]:
                linked_refs.update(step["evidence_ids"])
            for attempt in case["attempts"]:
                linked_refs.update(attempt["evidence_ids"])
        require(set(ticket["evidence_ids"]) <= linked_refs,
                label + ": ticket evidence must belong to its linked cases")
        reproduction = ticket["reproduction"]
        attempted = sum(len(case["attempts"]) for case in linked)
        failures = sum(a["status"] == "FAIL" for case in linked for a in case["attempts"])
        require(reproduction["reproduced"] <= reproduction["attempted"] <= attempted,
                label + ": reproduction frequency exceeds observed attempts")
        require(reproduction["reproduced"] <= failures,
                label + ": reproduction frequency exceeds observed failures")
        require(set(ticket["scope"]["languages"]) <= {case["language"] for case in linked}
                and set(ticket["scope"]["profiles"]) <= {case["profile"]["id"] for case in linked},
                label + ": ticket scope exceeds observed linked configurations")
    return computed


LABELS = {
    "en": {
        "title": "Multilingual Website Release QA",
        "scope": "Scope and environment", "campaign": "Campaign", "environment": "Environment",
        "url": "Starting URL", "period": "Execution period", "summary": "Summary",
        "verdict": "Scoped verdict", "coverage": "Executed case outcomes / planned cases",
        "critical": "Critical cases without a completed outcome", "none": "None",
        "matrix": "Test matrix", "case": "Case", "journey": "Journey", "language": "Language",
        "profile": "Profile", "status": "Status", "tickets": "Detailed defect tickets",
        "impact": "User impact", "severity": "Severity", "confidence": "Diagnostic confidence",
        "rationale": "Severity rationale", "affected": "Observed scope",
        "preconditions": "Preconditions", "data": "Non-sensitive test data",
        "steps": "Reproduction steps", "expected": "Expected", "observed": "Observed",
        "evidence": "Evidence", "linked": "Related cases", "frequency": "Reproduction frequency",
        "correction": "Correction hypothesis", "proven": "Supported correction note",
        "acceptance": "Acceptance criteria", "retest": "Retest procedure",
        "details": "Case execution details", "browser": "Browser", "limits": "Limitations",
        "uncertainties": "Uncertainties", "country": "Geographic verification",
        "attempts": "Attempts", "action": "Action", "next": "Recommended next work",
        "next_text": "Triage demonstrated defects, resolve product questions, and rerun fixed or blocked critical cases in a new campaign. This report does not certify other devices, countries, security, or legal compliance.",
        "capabilities": "Observed tool capabilities", "scope_note": SCOPE_NOTE,
        "no_tickets": "No defect tickets were supplied; inspect the case matrix before drawing a conclusion.",
    },
    "fr": {
        "title": "Recette de site multilingue avant livraison",
        "scope": "Périmètre et environnement", "campaign": "Campagne", "environment": "Environnement",
        "url": "URL de départ", "period": "Période d’exécution", "summary": "Synthèse",
        "verdict": "Verdict limité au périmètre", "coverage": "Cas exécutés avec un résultat / cas prévus",
        "critical": "Cas critiques sans résultat complet", "none": "Aucun",
        "matrix": "Matrice des tests", "case": "Cas", "journey": "Parcours", "language": "Langue",
        "profile": "Profil", "status": "État", "tickets": "Tickets d’anomalie détaillés",
        "impact": "Impact utilisateur", "severity": "Gravité", "confidence": "Confiance dans le diagnostic",
        "rationale": "Justification de la gravité", "affected": "Périmètre observé",
        "preconditions": "Préconditions", "data": "Données de test non sensibles",
        "steps": "Étapes de reproduction", "expected": "Attendu", "observed": "Observé",
        "evidence": "Preuves", "linked": "Cas associés", "frequency": "Fréquence de reproduction",
        "correction": "Hypothèse de correction", "proven": "Piste de correction étayée",
        "acceptance": "Critères d’acceptation", "retest": "Procédure de nouveau test",
        "details": "Détail de l’exécution", "browser": "Navigateur", "limits": "Limites",
        "uncertainties": "Incertitudes", "country": "Vérification géographique",
        "attempts": "Tentatives", "action": "Action", "next": "Suite recommandée",
        "next_text": "Prioriser les défauts démontrés, résoudre les questions produit et rejouer les cas corrigés ou critiques bloqués dans une nouvelle campagne. Ce rapport ne certifie ni les autres appareils ou pays, ni la sécurité ou la conformité juridique.",
        "capabilities": "Capacités des outils observées",
        "scope_note": "Ce verdict concerne uniquement les cas explicitement prévus et l’environnement observé.",
        "no_tickets": "Aucun ticket d’anomalie n’a été fourni ; consulter la matrice avant toute conclusion.",
    },
}


def md(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def bullets(values, empty):
    return "\n".join("- " + str(value) for value in values) if values else empty


def report_markdown(data):
    lang = data["campaign"]["output_language"]
    require(lang in LABELS, "Built-in report headings support en/fr only; provide agent-authored translation for another language")
    labels = LABELS[lang]
    campaign, summary = data["campaign"], data["summary"]
    refs = {item["id"]: "[" + item["id"] + "](" + item["path"] + ")" for item in data["evidence"]}
    evidence_links = lambda ids: ", ".join(refs[ref] for ref in ids) or labels["none"]
    lines = ["# " + labels["title"], "", "## " + labels["scope"], "",
             "- **" + labels["campaign"] + ":** " + campaign["id"],
             "- **" + labels["environment"] + ":** " + campaign["environment"],
             "- **" + labels["url"] + ":** " + campaign["base_url"],
             "- **" + labels["period"] + ":** " + campaign["started_at"] + " → " + campaign["finished_at"],
             "", "### " + labels["capabilities"], "",
             "\n".join("- " + key + ": " + str(value).lower() for key, value in campaign["capabilities"].items()),
             "", "## " + labels["summary"], "",
             "- **" + labels["verdict"] + ":** " + summary["verdict"],
             "- **" + labels["coverage"] + ":** " + str(summary["executed"]) + "/" + str(summary["planned"]),
             "- **" + labels["critical"] + ":** " + (", ".join(summary["critical_uncovered"]) or labels["none"]),
             "", labels["scope_note"], "", "| " + labels["status"] + " | n |",
             "| --- | ---: |"]
    lines += ["| " + status + " | " + str(summary["counts"][status]) + " |" for status in STATUSES]
    lines += ["", "## " + labels["matrix"], "",
              "| " + " | ".join(labels[key] for key in ("case", "journey", "language", "profile", "status", "evidence")) + " |",
              "| --- | --- | --- | --- | --- | --- |"]
    for case in data["cases"]:
        lines.append("| " + " | ".join([md(case["id"]), md(case["journey_id"]), md(case["language"]),
                     md(case["profile"]["id"]), case["status"], evidence_links(case["evidence_ids"])]) + " |")
    lines += ["", "## " + labels["tickets"], ""]
    if not data["tickets"]:
        lines += [labels["no_tickets"], ""]
    for ticket in data["tickets"]:
        lines += ["### " + ticket["id"] + " — " + ticket["title"], "",
                  "**" + labels["impact"] + ":** " + ticket["impact"], "",
                  "**" + labels["severity"] + ":** " + ticket["severity"],
                  "**" + labels["rationale"] + ":** " + ticket["severity_rationale"],
                  "**" + labels["confidence"] + ":** " + ticket["confidence"], "",
                  "**" + labels["affected"] + ":** " + json.dumps(ticket["scope"], ensure_ascii=False), "",
                  "**" + labels["preconditions"] + "**", "", bullets(ticket["preconditions"], labels["none"]), "",
                  "**" + labels["data"] + ":** " + json.dumps(ticket["test_data"], ensure_ascii=False), "",
                  "**" + labels["steps"] + "**", ""]
        lines += [str(index) + ". " + step for index, step in enumerate(ticket["steps"], 1)]
        lines += ["", "**" + labels["expected"] + ":** " + ticket["expected"], "",
                  "**" + labels["observed"] + ":** " + ticket["observed"], "",
                  "**" + labels["evidence"] + ":** " + evidence_links(ticket["evidence_ids"]),
                  "**" + labels["linked"] + ":** " + ", ".join(ticket["case_ids"]),
                  "**" + labels["frequency"] + ":** " + str(ticket["reproduction"]["reproduced"])
                  + "/" + str(ticket["reproduction"]["attempted"]), "",
                  "**" + labels["correction" if ticket["correction"]["hypothesis"] else "proven"] + ":** "
                  + ticket["correction"]["note"], "",
                  "**" + labels["acceptance"] + "**", "", bullets(ticket["acceptance_criteria"], labels["none"]),
                  "", "**" + labels["retest"] + "**", ""]
        lines += [str(index) + ". " + step for index, step in enumerate(ticket["retest_steps"], 1)]
        lines.append("")
    lines += ["## " + labels["details"], ""]
    for case in data["cases"]:
        browser = case["profile"]["browser"]
        lines += ["### " + case["id"] + " — " + case["title"], "",
                  "- URL: " + case["url"],
                  "- **" + labels["browser"] + ":** " + browser["name"] + " " + str(browser["version"]),
                  "- **" + labels["period"] + ":** " + case["started_at"] + " → " + case["finished_at"],
                  "- **" + labels["country"] + ":** " + json.dumps(case["country"], ensure_ascii=False),
                  "", "**" + labels["preconditions"] + "**", "",
                  bullets(case["preconditions"], labels["none"]), "",
                  "| # | " + " | ".join(labels[k] for k in ("action", "expected", "observed", "status", "evidence")) + " |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for step in case["steps"]:
            lines.append("| " + " | ".join([str(step["number"]), md(step["action"]),
                         md(step["expected"]), md(step["observed"]), step["status"],
                         evidence_links(step["evidence_ids"])]) + " |")
        lines += ["", "**" + labels["attempts"] + ":** " + json.dumps(case["attempts"], ensure_ascii=False),
                  "", "**" + labels["limits"] + "**", "", bullets(case["limitations"], labels["none"]),
                  "", "**" + labels["uncertainties"] + "**", "", bullets(case["uncertainties"], labels["none"]), ""]
    lines += ["## " + labels["limits"], "", bullets(campaign["limitations"], labels["none"]),
              "", "## " + labels["next"], "", labels["next_text"], ""]
    return "\n".join(lines)


CSV_FIELDS = ("id", "title", "severity", "severity_rationale", "confidence", "impact",
              "pages", "languages", "profiles", "preconditions", "test_data",
              "steps", "expected", "observed", "evidence_ids", "case_ids",
              "reproduced", "attempted", "correction_hypothesis", "correction_note",
              "acceptance_criteria", "retest_steps")


def csv_safe(value):
    text = str(value)
    return "'" + text if text.startswith(("=", "+", "-", "@", "\t", "\r")) else text


def write_csv(data, path):
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for ticket in data["tickets"]:
            row = {key: ticket[key] for key in ("id", "title", "severity", "severity_rationale",
                   "confidence", "impact", "expected", "observed")}
            row.update({key: "\n".join(ticket[key]) for key in
                        ("preconditions", "steps", "evidence_ids", "case_ids",
                         "acceptance_criteria", "retest_steps")})
            row.update({key: "\n".join(ticket["scope"][key]) for key in ("pages", "languages", "profiles")})
            row.update(ticket["reproduction"])
            row["test_data"] = json.dumps(ticket["test_data"], ensure_ascii=False, sort_keys=True)
            row["correction_hypothesis"] = str(ticket["correction"]["hypothesis"]).lower()
            row["correction_note"] = ticket["correction"]["note"]
            writer.writerow({key: csv_safe(value) for key, value in row.items()})


def finalize(observations_path, tickets_path, output, output_language=None):
    observations_path = Path(observations_path)
    data = load_json(observations_path)
    validate_results(data, observations_path.parent, observations=True)
    tickets = load_json(tickets_path)
    require(isinstance(tickets, list), "Tickets input must be a JSON array")
    require(not data["tickets"], "Observations already contain tickets; preserve them in a new input instead")
    data["tickets"] = tickets
    if output_language is not None:
        data["campaign"]["output_language"] = output_language
    require(data["campaign"]["output_language"] in LABELS,
            "Built-in report export supports en/fr; another language needs an explicit agent translation")
    data["summary"] = summarize(data)
    validate_results(data, observations_path.parent)
    report = report_markdown(data)
    output = Path(output).expanduser()
    require(output.is_absolute(), "Output must be an explicit absolute new directory")
    require(not output.exists() and not output.is_symlink(), "Output directory already exists")
    require(output.parent.is_dir(), "Output parent must already exist")
    require(output.parent.resolve() == output.parent, "Output parent must be normalized and not a symlink")
    # No cleanup is attempted on a partial write: preserve the evidence and report the error.
    output.mkdir()
    (output / "evidence").mkdir()
    for evidence in data["evidence"]:
        source = safe_evidence_path(observations_path.parent, evidence["path"])
        destination = output / evidence["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as handle:
            handle.write(source.read_bytes())
    with (output / "results.json").open("x", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with (output / "audit-report.md").open("x", encoding="utf-8") as handle:
        handle.write(report)
    write_csv(data, output / "tickets.csv")
    validate_results(load_json(output / "results.json"), output)
    return {"created": str(output), "summary": data["summary"],
            "tickets": len(tickets), "evidence_files": len(data["evidence"])}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate-config", "validate-observations", "validate-results"):
        child = sub.add_parser(command)
        child.add_argument("path", type=Path)
    child = sub.add_parser("finalize")
    child.add_argument("observations", type=Path)
    child.add_argument("tickets", type=Path)
    child.add_argument("--output", required=True, type=Path)
    child.add_argument("--output-language", choices=("en", "fr"))
    args = parser.parse_args(argv)
    try:
        if args.command == "validate-config":
            result = validate_config(load_json(args.path))
        elif args.command in ("validate-results", "validate-observations"):
            result = {"valid": True, "summary": validate_results(
                load_json(args.path), args.path.parent,
                observations=args.command == "validate-observations")}
        else:
            result = finalize(args.observations, args.tickets, args.output, args.output_language)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ContractError, OSError, ValueError, KeyError, TypeError) as error:
        print("Validation failed: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
