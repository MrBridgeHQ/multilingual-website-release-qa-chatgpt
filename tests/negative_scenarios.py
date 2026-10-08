#!/usr/bin/env python3
"""Exercise honest negative outcomes against the synthetic loopback fixture.

Inspection is read-only. Creation preserves browser profiles and all observations;
existing output paths are refused. No browser or filesystem cleanup is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills" / "recette-web-multilingue" / "scripts" / "qa.py"


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def normalized_new_path(path: Path) -> Path:
    if not path.is_absolute() or path != path.resolve():
        raise ValueError("Use a normalized absolute path without symlink parents.")
    if path.exists() or path.is_symlink():
        raise FileExistsError(f"Refusing to replace existing path: {path}")
    if not path.parent.is_dir():
        raise ValueError(f"Parent must already exist: {path.parent}")
    return path


def inspect_environment(args: argparse.Namespace) -> dict[str, object]:
    packages = {}
    for package in ("playwright", "jsonschema"):
        try:
            packages[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            packages[package] = None
    return {
        "mode": "inspect",
        "helper_exists": HELPER.is_file(),
        "browser_exists": args.browser.is_file(),
        "browser_executable": os.access(args.browser, os.X_OK),
        "packages": packages,
        "output_available": not args.output.exists() and not args.output.is_symlink(),
        "work_available": not args.work.exists() and not args.work.is_symlink(),
        "base_url": args.base_url,
        "network_access": "No network request was made by inspection.",
    }


def create(args: argparse.Namespace) -> dict[str, object]:
    from playwright.sync_api import Error as PlaywrightError, sync_playwright

    parsed = urlsplit(args.base_url)
    if parsed.scheme != "http" or parsed.hostname != "127.0.0.1" or parsed.path not in ("", "/"):
        raise ValueError("Negative fixture tests require an explicit HTTP loopback origin.")
    if parsed.query or parsed.fragment or parsed.username is not None:
        raise ValueError("The loopback origin cannot contain queries, fragments, or credentials.")
    output = normalized_new_path(args.output)
    work = normalized_new_path(args.work)
    if not HELPER.is_file() or not args.browser.is_file():
        raise FileNotFoundError("The declared helper and browser must exist before creation.")
    output.mkdir()
    source = output / "source"
    source.mkdir()
    (source / "evidence").mkdir()
    work.mkdir()
    profile_path = work / "profile"
    profile_path.mkdir()
    evidence = []
    cases = []
    campaign_started = now()
    origin = args.base_url.rstrip("/")

    def add_evidence(identifier: str, kind: str, value: object, description: str, suffix: str = "json") -> str:
        relative = f"evidence/{identifier}.{suffix}"
        destination = source / relative
        captured_at = now()
        if isinstance(value, bytes):
            with destination.open("xb") as handle:
                handle.write(value)
        else:
            write_json(destination, value)
        evidence.append({
            "id": identifier, "path": relative,
            "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
            "kind": kind, "captured_at": captured_at, "description": description,
        })
        return identifier

    def profile(version: str | None, locale: str = "en-US") -> dict[str, object]:
        return {
            "id": "negative-desktop", "device_class": "DESKTOP",
            "viewport": {"width": 1440, "height": 900},
            "browser": {"name": "Chromium", "version": version},
            "locale": locale, "timezone": "Europe/Paris", "physical_device": False,
        }

    def append_case(identifier: str, title: str, started: str, url: str, language: str,
                    browser_profile: dict[str, object], steps: list[dict[str, object]],
                    status: str, classification: str, refs: list[str], limitations: list[str],
                    uncertainties: list[str] | None = None, country: dict[str, object] | None = None) -> None:
        cases.append({
            "id": identifier, "journey_id": identifier, "title": title, "critical": True,
            "started_at": started, "finished_at": now(), "url": url, "language": language,
            "profile": browser_profile,
            "preconditions": ["Synthetic local fixture only; no production site is under audit.",
                              "This scenario is separate from the twenty baseline journey-language pairs."],
            "test_data": {}, "steps": steps, "status": status, "classification": classification,
            "attempts": [] if status == "NOT_RUN" else [{
                "number": 1, "status": status, "observed": steps[-1]["observed"], "evidence_ids": refs,
            }],
            "country": country or {
                "requested": None, "verified": None, "status": "NOT_APPLICABLE",
                "same_network_context": False, "evidence_ids": [],
                "note": "No country assertion is requested for this scenario.",
            },
            "evidence_ids": refs, "limitations": limitations, "uncertainties": uncertainties or [],
        })

    def step(number: int, action: str, expected: str, observed: str, status: str, refs: list[str]) -> dict[str, object]:
        return {"number": number, "action": action, "expected": expected,
                "observed": observed, "status": status, "evidence_ids": refs}

    started = now()
    missing_browser = work / "deliberately-missing-browser"
    if missing_browser.exists():
        raise FileExistsError("Controlled missing-browser target unexpectedly exists.")
    try:
        subprocess.run([str(missing_browser), "--version"], check=True, capture_output=True, text=True)
    except FileNotFoundError as error:
        missing_observation = {
            "scenario_type": "CONTROLLED_MISSING_EXECUTABLE",
            "attempted_operation": "Execute a deliberately absent browser path with --version.",
            "error_type": type(error).__name__, "errno": error.errno,
            "message": str(error).replace(str(ROOT), "<PROJECT_ROOT>"),
            "environment_interpretation": "Intentional capability-failure injection; the actual installed Chromium remains available for independent cases.",
        }
    else:
        raise AssertionError("The controlled missing executable did not produce the expected OS error.")
    ref = add_evidence("N01-browser-unavailable", "TEXT", missing_observation,
                       "Actual FileNotFoundError from a controlled absent browser executable.")
    append_case("N01", "Unavailable browser capability is reported as a tooling block", started,
                origin + "/en/", "en", profile(None), [step(1, "Start the configured missing browser executable.",
                "A usable browser is required before functional site assertions.",
                f"Actual {missing_observation['error_type']} with errno {missing_observation['errno']}; no website navigation occurred.",
                "BLOCKED", [ref])], "BLOCKED", "TOOLING_INCIDENT", [ref],
                ["Controlled failure injection; this is not a claim that all browsers are unavailable in the environment.",
                 "The URL/profile are planned targets; browser version is unavailable because this executable never started."])

    with (work / "chromium.log").open("xb") as browser_log:
        command = [str(args.browser), "--headless=new", "--no-sandbox", "--disable-dev-shm-usage",
                   "--disable-background-networking", "--disable-component-update", "--disable-default-apps",
                   "--no-first-run", "--no-default-browser-check", "--disable-sync",
                   "--metrics-recording-only", "--password-store=basic", "--use-mock-keychain",
                   "--remote-debugging-port=0", "--remote-debugging-address=127.0.0.1",
                   "--user-data-dir=" + str(profile_path), "about:blank"]
        process = subprocess.Popen(command, stdout=browser_log, stderr=subprocess.STDOUT, start_new_session=True)
    endpoint_file = profile_path / "DevToolsActivePort"
    deadline = time.monotonic() + 20
    while not endpoint_file.is_file() and time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError("The real Chromium process exited; inspect the retained local log.")
        time.sleep(0.1)
    if not endpoint_file.is_file():
        raise TimeoutError("Chromium did not expose a CDP endpoint within twenty seconds.")
    endpoint_lines = endpoint_file.read_text(encoding="utf-8").splitlines()
    websocket = f"ws://127.0.0.1:{endpoint_lines[0]}{endpoint_lines[1]}"
    write_json(work / "browser-session.json", {"pid": process.pid, "endpoint": websocket,
               "profile": str(profile_path), "retained": True,
               "cleanup": "No browser close, termination, profile deletion, or temporary-directory cleanup was requested."})

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(websocket, timeout=15000)
        browser_version = browser.version
        context = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US", timezone_id="Europe/Paris")
        context.route("**/*", lambda intercepted: intercepted.continue_()
                      if urlsplit(intercepted.request.url).scheme in ("about", "data")
                      or intercepted.request.url.startswith(origin + "/") else intercepted.abort())

        started = now()
        auth_url = origin + "/auth-required"
        response = context.request.get(auth_url, fail_on_status_code=False, timeout=10000)
        auth_observation = {
            "operation": "Playwright APIRequestContext GET attached to the browser context.",
            "url": response.url, "status": response.status,
            "authentication_challenge_present": "www-authenticate" in response.headers,
            "body_excerpt": response.text()[:500],
            "interpretation": "An observed authentication obstacle. No credentials were supplied and no bypass was attempted.",
        }
        if response.status != 401:
            raise AssertionError(f"Local authentication fixture returned {response.status}, not 401.")
        ref = add_evidence("N02-authentication-response", "NETWORK", auth_observation,
                           "Actual HTTP 401 from the synthetic local endpoint using Playwright's browser-context API client.")
        append_case("N02", "Unavailable authentication blocks a protected journey", started, auth_url, "en", profile(browser_version),
                    [step(1, "Request the protected local endpoint without credentials.",
                     "Authorized credentials are required before checking the protected journey.",
                     "The endpoint returned HTTP 401 with an authentication challenge. Protected journey steps were not executed.",
                     "BLOCKED", [ref])], "BLOCKED", "NONE", [ref],
                    ["The actual HTTP response was collected through Playwright's API client; this is not a claim that a browser authentication dialog was visually inspected.",
                     "The fixture intentionally requires unavailable credentials; authentication failure is not a website defect."])

        started = now()
        page = context.new_page()
        page.goto(origin + "/en/", wait_until="domcontentloaded", timeout=10000)
        session = context.new_cdp_session(page)
        method = "NegativeScenario.intentionallyMissingMethod"
        try:
            session.send(method, {})
        except PlaywrightError as error:
            tool_observation = {
                "scenario_type": "CONTROLLED_INVALID_CDP_METHOD",
                "method": method, "url": page.url,
                "error_type": type(error).__name__, "message": str(error),
                "interpretation": "A deliberate client/protocol operation error, not evidence of a website defect.",
            }
        else:
            raise AssertionError("The deliberately invalid CDP method unexpectedly succeeded.")
        ref = add_evidence("N03-tool-operation-error", "TEXT", tool_observation,
                           "Actual CDP protocol error produced by an intentionally invalid tool method.")
        append_case("N03", "A failed browser operation is a tooling incident", started, page.url, "en", profile(browser_version),
                    [step(1, "Issue the deliberately invalid CDP method after local navigation.",
                     "A working diagnostic operation is needed before relying on its claimed measurement.",
                     tool_observation["message"], "BLOCKED", [ref])], "BLOCKED", "TOOLING_INCIDENT", [ref],
                    ["Controlled tool-error injection; the webpage was not assessed as defective.",
                     "No automatic retry was attempted because an invalid method is not a transient error."])

        started = now()
        ambiguous_input = {
            "scenario_type": "CONTROLLED_AMBIGUOUS_BUSINESS_REQUIREMENT",
            "request": "Check whether the localized offer is commercially correct.",
            "provided_acceptance_criteria": None,
            "product_question": "Which approved price, tax treatment, billing period, and market should this offer satisfy?",
            "decision": "Do not assert a required commercial value until the product owner supplies the expectation.",
            "website_assertion_executed": False,
        }
        ref = add_evidence("N04-missing-expectation", "TEXT", ambiguous_input,
                           "Declared negative-test input and the resulting unresolved product question; not a website observation.")
        append_case("N04", "Missing commercial expectations remain a product question", started, origin + "/en/offer", "en", profile(None),
                    [step(1, "Resolve the acceptance criterion before asserting commercial correctness.",
                     "No required price, tax treatment, or market was supplied in this isolated negative input.",
                     ambiguous_input["product_question"], "NOT_RUN", [ref])], "NOT_RUN", "PRODUCT_QUESTION", [ref],
                    ["This controlled input intentionally omits expectations; it does not replace the complete public baseline business contract.",
                     "No browser operation or commercial correctness assertion was performed for this case; URL/profile are planned targets and browser version is not applicable."],
                    ["Commercial correctness cannot be assessed without approved product expectations."])

        started = now()
        geo_context = browser.new_context(viewport={"width": 1440, "height": 900}, locale="fr-FR", timezone_id="Europe/Paris")
        geo_context.route("**/*", lambda intercepted: intercepted.continue_()
                          if intercepted.request.url.startswith(origin + "/") else intercepted.abort())
        geo_page = geo_context.new_page()
        geo_response = geo_page.goto(origin + "/fr/", wait_until="domcontentloaded", timeout=10000)
        geo_observation = geo_page.evaluate("""() => ({
            actual_url: location.href,
            document_language: document.documentElement.lang,
            browser_locale: navigator.language,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            heading: document.getElementById('page-heading').textContent,
            viewport_width: innerWidth,
            viewport_height: innerHeight
        })""")
        geo_observation.update({"requested_country": "FR", "verified_country": None,
                                "same_network_context_country_proof": False,
                                "http_status": geo_response.status if geo_response else None,
                                "measurement_available": "Document language, configured locale/timezone, and local page response only.",
                                "limitation": "No provider or measurement ties a network exit country to this loopback website request. These language and timezone observations are not country proof."})
        ref = add_evidence("N05-unproven-country-context", "DOM", geo_observation,
                           "Actual French page and browser context observations, explicitly insufficient to verify network country.")
        screenshot_ref = add_evidence("N05-french-page", "SCREENSHOT", geo_page.screenshot(full_page=True),
                                      "Actual French local page screenshot; it is not proof of geographic network origin.", "png")
        country = {"requested": "FR", "verified": None, "status": "BLOCKED",
                   "same_network_context": False, "evidence_ids": [ref],
                   "note": "French content, fr-FR locale, Europe/Paris timezone, and a loopback URL do not establish the country of a website request."}
        append_case("N05", "French locale does not prove a French network country", started, geo_page.url, "fr", profile(browser_version, "fr-FR"),
                    [step(1, "Open the French local page and inspect the actual context.",
                          "Collect only the language and browser facts the session exposes.",
                          f"Observed document language {geo_observation['document_language']}, locale {geo_observation['browser_locale']}, timezone {geo_observation['timezone']}.",
                          "PASS", [ref, screenshot_ref]),
                     step(2, "Verify that the website request uses the requested French network exit country.",
                          "Country evidence must concern the same network context as the website request.",
                          "No such measurement is available; verified country remains null and no geographic success is claimed.",
                          "BLOCKED", [ref])], "BLOCKED", "NONE", [ref, screenshot_ref],
                    ["Actual language observations were collected, but this case's requested geographic condition remains unverified.",
                     "No external geolocation service was contacted; the local browser is not a physical device."],
                    country=country)

    observations = {
        "schema_version": "1.0",
        "campaign": {
            "id": "synthetic-negative-scenarios", "started_at": campaign_started,
            "finished_at": now(), "base_url": origin, "environment": "LOCAL", "output_language": "en",
            "capabilities": {"extraction": True, "interaction": True, "screenshots": True,
                             "network": True, "console": False, "traces": False, "geography": False},
            "limitations": [
                "This is a negative-behavior validation campaign, separate from the twenty baseline release journeys.",
                "N01 and N03 inject controlled tool failures. N04 supplies a controlled incomplete business requirement. N02 and N05 record actual authentication and country-proof limitations.",
                "No complete release-check case is executed. Diagnostic observations and handling checks do not approve the website.",
                "No console stream or trace was collected. No full accessibility, performance, legal, or production audit was attempted.",
                "The Chromium process and its fresh profile are retained; no cleanup or deletion was requested.",
            ],
        },
        "cases": cases, "evidence": evidence, "tickets": [],
    }
    observations_path = source / "observations.json"
    tickets_path = source / "tickets.json"
    write_json(observations_path, observations)
    write_json(tickets_path, [])
    commands = [
        [sys.executable, "-B", str(HELPER), "validate-observations", str(observations_path)],
        [sys.executable, "-B", str(HELPER), "finalize", str(observations_path), str(tickets_path),
         "--output", str(output / "delivery"), "--output-language", "en"],
        [sys.executable, "-B", str(HELPER), "validate-results", str(output / "delivery" / "results.json")],
    ]
    command_results = []
    for index, command in enumerate(commands, 1):
        result = subprocess.run(command, capture_output=True, text=True)
        receipt = {"command": command, "returncode": result.returncode,
                   "stdout": result.stdout, "stderr": result.stderr}
        write_json(output / f"helper-command-{index}.json", receipt)
        command_results.append(receipt)
        if result.returncode != 0:
            raise RuntimeError(f"Helper command {index} failed; all artifacts were retained.")
    final_results = json.loads((output / "delivery" / "results.json").read_text(encoding="utf-8"))
    summary = final_results["summary"]
    expected_counts = {"PASS": 0, "FAIL": 0, "BLOCKED": 4, "NOT_RUN": 1, "NOT_APPLICABLE": 0}
    if summary["counts"] != expected_counts or summary["verdict"] != "NO_EXECUTION" or final_results["tickets"]:
        raise AssertionError("Negative results must retain four blocks, one product question, no defect tickets, and no execution approval.")
    check_receipt = {
        "status": "PASS", "meaning": "Negative handling assertions passed; this is not a website release verdict.",
        "case_count": len(cases), "evidence_files": len(evidence), "actual_http_status": auth_observation["status"],
        "controlled_missing_executable_error": missing_observation["error_type"],
        "controlled_tool_error": tool_observation["error_type"],
        "summary": summary, "tickets": len(final_results["tickets"]),
        "helper_returncodes": [item["returncode"] for item in command_results],
        "browser_version": browser_version,
    }
    write_json(output / "validation-checks.json", check_receipt)
    notes = """# Negative scenario validation

This campaign is separate from the twenty baseline journey-language cases. It tests honest handling of limitations, not production readiness.

- N01 actually attempts a deliberately absent browser executable and records the resulting OS error. This is controlled failure injection; installed Chromium remains available for other cases.
- N02 records an actual HTTP 401 using Playwright's browser-context API client. No credential is supplied and no authentication bypass is attempted. A browser login dialog is not claimed to have been visually inspected.
- N03 actually submits an invalid CDP method and records the protocol error as a tooling incident.
- N04 uses an explicitly incomplete commercial requirement and records a product question without inventing an expected price or tax rule. It does not alter the full baseline business contract.
- N05 observes a French page, browser locale, and timezone but retains a null verified country because none proves a network country for the same website request.

The exporter derives all counts from the recorded cases. The authoritative result is `delivery/results.json`; `delivery/audit-report.md`, `delivery/tickets.csv`, and the copied evidence are generated from that same input. `validation-checks.json` records handling assertions and actual helper exit codes. Its PASS means these negative handling checks succeeded, never that the website is ready.

The retained browser log, process receipt, and fresh profile remain in the selected `.work/negative-*` directory. They are not public audit evidence and are not automatically deleted. No external service was called. Browser routing is not claimed to be a comprehensive network firewall.

Reproduce from the repository root with an installed Chromium executable and new, absent absolute output/work paths:

```sh
python3 -B tests/negative_scenarios.py --mode inspect --browser /ABSOLUTE/PATH/TO/chrome --output /ABSOLUTE/NEW/negative-run --work /ABSOLUTE/NEW/negative-browser
python3 -B tests/negative_scenarios.py --mode create --browser /ABSOLUTE/PATH/TO/chrome --output /ABSOLUTE/NEW/negative-run --work /ABSOLUTE/NEW/negative-browser
```

The fixture must be running at `http://127.0.0.1:39175`; use `--base-url` to choose a different explicitly authorized loopback origin. Existing outputs are refused. Python dependencies are the pinned project requirements. The script invokes the skill helper's observation validation, finalization, and result validation commands and preserves their exact command/exit/output receipts.
"""
    with (output / "README.md").open("x", encoding="utf-8") as handle:
        handle.write(notes)
    return check_receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=("inspect", "create"))
    parser.add_argument("--browser", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--work", required=True, type=Path)
    parser.add_argument("--base-url", default="http://127.0.0.1:39175")
    args = parser.parse_args()
    result = inspect_environment(args) if args.mode == "inspect" else create(args)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
