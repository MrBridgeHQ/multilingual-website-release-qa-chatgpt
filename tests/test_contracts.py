#!/usr/bin/env python3
"""Behavioral tests for the deterministic QA contract and export helper.

inspect is read-only. run preserves every generated fixture/export in a unique
tests/contracts/runs directory; it never cleans up or replaces earlier files.
"""
from __future__ import annotations

import argparse
import copy
import csv
import importlib.util
import json
import os
from pathlib import Path
import uuid
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "contracts"
qa = None


def fixture():
    return qa.load_json(FIXTURES / "observations.json")


def tickets():
    return qa.load_json(FIXTURES / "tickets.json")


def config():
    return qa.load_json(ROOT / "skills" / "recette-web-multilingue" / "assets" / "config.example.json")


def new_directory():
    result = FIXTURES / "runs" / ("contract-" + uuid.uuid4().hex)
    result.mkdir()
    return result


def write_new_json(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


class ContractTests(unittest.TestCase):
    def validate(self, value):
        return qa.validate_results(value, FIXTURES, observations=True)

    def test_example_config_has_exact_twenty_cases(self):
        result = qa.validate_config(config())
        self.assertEqual(result, {"valid": True, "planned_cases": 20, "profiles": 2, "languages": 2})

    def test_action_authorization_note_is_not_a_secret_header(self):
        value = config()
        value["authorized_actions"][0]["authorization"] = "The user authorized navigation of the local demo."
        qa.validate_config(value)
        with self.assertRaises(qa.ContractError):
            qa.secret_check({"headers": {"authorization": "Bearer this-is-a-realistic-sensitive-token"}})

    def test_masked_secret_is_allowed_but_actual_secret_is_not(self):
        qa.secret_check({"password": "[REDACTED]"})
        with self.assertRaises(qa.ContractError):
            qa.secret_check({"password": "private-value-never-export"})
        with self.assertRaises(qa.ContractError):
            qa.secret_check({"note": "Authorization: Bearer abcdefghijklmnopqrstuvwxyz"})

    def test_config_rejects_external_scope(self):
        value = config()
        value["start_url"] = "https://outside.invalid/en/"
        with self.assertRaisesRegex(qa.ContractError, "outside"):
            qa.validate_config(value)

    def test_config_rejects_excluded_path_and_prefix_collision(self):
        value = config()
        value["start_url"] = value["scope"]["allowed_origins"][0] + "/auth-required"
        with self.assertRaisesRegex(qa.ContractError, "outside"):
            qa.validate_config(value)
        scope = {"allowed_origins": ["https://example.test"], "allowed_paths": ["/shop"],
                 "excluded_origins": [], "excluded_paths": []}
        self.assertFalse(qa.within_scope("https://example.test/shopping", scope))
        self.assertTrue(qa.within_scope("https://example.test/shop/item", scope))

    def test_config_rejects_unknown_matrix_reference(self):
        value = config()
        value["cases"][0]["profile_id"] = "unconfigured-phone"
        with self.assertRaisesRegex(qa.ContractError, "Unknown profile"):
            qa.validate_config(value)

    def test_config_unknown_expectation_becomes_product_question(self):
        value = config()
        step = value["journeys"][0]["steps"][0]
        step["expected"] = None
        with self.assertRaisesRegex(qa.ContractError, "PRODUCT_QUESTION"):
            qa.validate_config(value)
        step["expectation_basis"] = "PRODUCT_QUESTION"
        qa.validate_config(value)

    def test_config_rejects_blank_expectation(self):
        value = config()
        value["journeys"][0]["steps"][0]["expected"] = "   "
        with self.assertRaises(qa.ContractError):
            qa.validate_config(value)

    def test_config_does_not_infer_requested_country(self):
        value = config()
        value["cases"][0]["country"] = "FR"
        with self.assertRaisesRegex(qa.ContractError, "not explicitly requested"):
            qa.validate_config(value)

    def test_config_rejects_duplicate_cases_and_zero_budget(self):
        value = config()
        value["cases"].append(copy.deepcopy(value["cases"][0]))
        with self.assertRaisesRegex(qa.ContractError, "Duplicate"):
            qa.validate_config(value)
        value = config()
        value["budgets"]["max_requests"] = 0
        with self.assertRaises(qa.ContractError):
            qa.validate_config(value)

    def test_observations_without_tickets_are_valid_before_triage(self):
        summary = self.validate(fixture())
        self.assertEqual(summary["counts"]["FAIL"], 1)
        self.assertEqual(summary["verdict"], "ISSUES_FOUND")

    def test_invalid_status_is_rejected_by_schema(self):
        value = fixture()
        value["cases"][0]["status"] = "SUCCESS"
        with self.assertRaises(qa.ContractError):
            self.validate(value)

    def test_zero_executed_cases_cannot_be_ready(self):
        value = fixture()
        case = value["cases"][0]
        case["status"] = "NOT_RUN"
        case["classification"] = "PRODUCT_QUESTION"
        case["steps"][0]["status"] = "NOT_RUN"
        case["steps"][0]["observed"] = "The required product expectation was not provided."
        case["attempts"] = []
        summary = self.validate(value)
        self.assertEqual(summary["verdict"], "NO_EXECUTION")
        self.assertEqual(summary["coverage"], {"numerator": 0, "denominator": 1})
        self.assertEqual(summary["critical_uncovered"], ["fixture-case"])

    def test_partial_journey_cannot_be_pass(self):
        value = fixture()
        case = value["cases"][0]
        case["steps"][0]["status"] = "PASS"
        case["steps"].append({"number": 2, "action": "Reach the next state.",
                              "expected": "A completed next state.",
                              "observed": "The browser became unavailable.",
                              "status": "BLOCKED", "evidence_ids": []})
        case["status"] = "PASS"
        case["classification"] = "NONE"
        case["attempts"][0]["status"] = "PASS"
        with self.assertRaisesRegex(qa.ContractError, "contradicts"):
            self.validate(value)
        case["status"] = "BLOCKED"
        case["classification"] = "TOOLING_INCIDENT"
        case["attempts"][0]["status"] = "BLOCKED"
        summary = self.validate(value)
        self.assertEqual(summary["counts"]["BLOCKED"], 1)

    def test_failure_remains_failure_when_later_steps_are_not_run(self):
        value = fixture()
        value["cases"][0]["steps"].append({
            "number": 2, "action": "Continue after the failed prerequisite.",
            "expected": "A completed next state.", "observed": "Not executed after the failed prerequisite.",
            "status": "NOT_RUN", "evidence_ids": []})
        self.assertEqual(self.validate(value)["counts"]["FAIL"], 1)

    def test_inapplicable_is_not_execution_or_automatic_approval(self):
        value = fixture()
        case = value["cases"][0]
        case["status"] = case["steps"][0]["status"] = "NOT_APPLICABLE"
        case["steps"][0]["observed"] = "This fixture has no applicable form."
        case["classification"] = "NONE"
        case["attempts"] = []
        self.assertEqual(self.validate(value)["verdict"], "NO_EXECUTION")

    def test_failed_step_needs_evidence(self):
        value = fixture()
        value["cases"][0]["steps"][0]["evidence_ids"] = []
        with self.assertRaisesRegex(qa.ContractError, "no evidence"):
            self.validate(value)

    def test_missing_evidence_and_checksum_mismatch_are_reported(self):
        value = fixture()
        value["evidence"][0]["path"] = "evidence/missing.txt"
        with self.assertRaisesRegex(qa.ContractError, "Missing evidence"):
            self.validate(value)
        value = fixture()
        value["evidence"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(qa.ContractError, "checksum mismatch"):
            self.validate(value)

    def test_evidence_path_traversal_is_rejected(self):
        value = fixture()
        value["evidence"][0]["path"] = "evidence/../../SKILL.md"
        with self.assertRaisesRegex(qa.ContractError, "beneath"):
            self.validate(value)

    def test_evidence_symlink_is_rejected(self):
        directory = new_directory()
        (directory / "evidence").mkdir()
        (directory / "evidence" / "linked.txt").symlink_to(
            FIXTURES / "evidence" / "synthetic-observation.txt")
        with self.assertRaisesRegex(qa.ContractError, "symlinks"):
            qa.safe_evidence_path(directory, "evidence/linked.txt")

    def test_stale_evidence_timestamp_is_rejected(self):
        value = fixture()
        value["evidence"][0]["captured_at"] = "2020-01-01T00:00:00Z"
        with self.assertRaisesRegex(qa.ContractError, "capture time"):
            self.validate(value)

    def test_country_claim_requires_same_context_network_proof(self):
        value = fixture()
        country = value["cases"][0]["country"]
        country.update(requested="FR", verified="FR", status="PASS",
                       same_network_context=True, evidence_ids=[])
        with self.assertRaisesRegex(qa.ContractError, "same-network-context"):
            self.validate(value)
        country["evidence_ids"] = ["fixture-text"]
        with self.assertRaisesRegex(qa.ContractError, "network evidence"):
            self.validate(value)

    def test_unproven_country_blocks_a_passing_case(self):
        value = fixture()
        case = value["cases"][0]
        case["status"] = case["steps"][0]["status"] = case["attempts"][0]["status"] = "PASS"
        case["classification"] = "NONE"
        case["country"].update(requested="FR", status="NOT_RUN",
                               note="No evidence links a country check to the target network context.")
        with self.assertRaisesRegex(qa.ContractError, "geographic check"):
            self.validate(value)

    def test_tool_failure_cannot_be_reported_as_site_defect(self):
        value = fixture()
        value["cases"][0]["classification"] = "TOOLING_INCIDENT"
        with self.assertRaises(qa.ContractError):
            self.validate(value)

    def test_summary_must_reconcile(self):
        value = fixture()
        value["summary"] = qa.summarize(value)
        value["summary"]["counts"]["PASS"] = 12
        with self.assertRaisesRegex(qa.ContractError, "reconcile"):
            self.validate(value)

    def test_ticket_unknown_case_and_invented_frequency_are_rejected(self):
        value = fixture()
        value["tickets"] = tickets()
        value["tickets"][0]["case_ids"] = ["never-executed"]
        with self.assertRaisesRegex(qa.ContractError, "unknown case"):
            self.validate(value)
        value["tickets"] = tickets()
        value["tickets"][0]["reproduction"] = {"reproduced": 2, "attempted": 2}
        with self.assertRaisesRegex(qa.ContractError, "frequency"):
            self.validate(value)

    def test_ticket_scope_cannot_claim_untested_language(self):
        value = fixture()
        value["tickets"] = tickets()
        value["tickets"][0]["scope"]["languages"].append("de")
        with self.assertRaisesRegex(qa.ContractError, "scope exceeds"):
            self.validate(value)

    def test_exports_are_derived_and_relocatable(self):
        directory = new_directory()
        output = directory / "english"
        result = qa.finalize(FIXTURES / "observations.json", FIXTURES / "tickets.json", output)
        self.assertEqual(result["tickets"], 1)
        loaded = qa.load_json(output / "results.json")
        self.assertEqual(qa.validate_results(loaded, output)["counts"]["FAIL"], 1)
        with (output / "tickets.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), len(loaded["tickets"]))
        self.assertEqual(rows[0]["id"], loaded["tickets"][0]["id"])
        self.assertIn("1/1", (output / "audit-report.md").read_text(encoding="utf-8"))
        before = (output / "results.json").read_bytes()
        with self.assertRaisesRegex(qa.ContractError, "already exists"):
            qa.finalize(FIXTURES / "observations.json", FIXTURES / "tickets.json", output)
        self.assertEqual(before, (output / "results.json").read_bytes())

    def test_french_headings_preserve_english_enums_and_original_quotes(self):
        directory = new_directory()
        output = directory / "french"
        qa.finalize(FIXTURES / "observations.json", FIXTURES / "tickets.json", output, "fr")
        text = (output / "audit-report.md").read_text(encoding="utf-8")
        self.assertIn("Matrice des tests", text)
        self.assertIn("ISSUES_FOUND", text)
        self.assertIn("The fixture submit control is disabled.", text)
        self.assertEqual(qa.load_json(output / "results.json")["campaign"]["output_language"], "fr")

    def test_unknown_output_language_is_an_explicit_export_limitation(self):
        directory = new_directory()
        output = directory / "german"
        with self.assertRaisesRegex(qa.ContractError, "supports en/fr"):
            qa.finalize(FIXTURES / "observations.json", FIXTURES / "tickets.json", output, "de")
        self.assertFalse(output.exists())

    def test_csv_formula_prefix_is_neutralized(self):
        self.assertEqual(qa.csv_safe("=1+1"), "'=1+1")
        self.assertEqual(qa.csv_safe("@SUM(A1)"), "'@SUM(A1)")
        self.assertEqual(qa.csv_safe("Safe prose"), "Safe prose")


def main():
    global qa
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect", "run"))
    parser.add_argument("--helper", type=Path, default=Path(os.environ.get(
        "QA_HELPER_PATH", str(ROOT / "skills" / "recette-web-multilingue" / "scripts" / "qa.py"))))
    args = parser.parse_args()
    names = unittest.defaultTestLoader.getTestCaseNames(ContractTests)
    if args.mode == "inspect":
        print(json.dumps({"helper": str(args.helper.resolve()), "tests": names,
                          "count": len(names), "writes": "run creates new preserved fixture directories"}, indent=2))
        return 0
    spec = importlib.util.spec_from_file_location("qa_helper", args.helper)
    qa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qa)
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
