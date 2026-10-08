#!/usr/bin/env python3
"""Read-only checks that later retries never erase an observed website defect."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--helper", type=Path, default=ROOT / "skills/recette-web-multilingue/scripts/qa.py")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("qa_retry_helper", args.helper)
    qa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qa)
    fixture_dir = ROOT / "tests/contracts"
    data = qa.load_json(fixture_dir / "observations.json")
    case = data["cases"][0]
    case["attempts"].append({"number": 2, "status": "BLOCKED",
                             "observed": "The synthetic retry browser became unavailable.",
                             "evidence_ids": []})
    summary = qa.validate_results(data, fixture_dir, observations=True)
    assert summary["counts"]["FAIL"] == 1
    case["attempts"][1].update(status="PASS",
                              observed="The synthetic retry did not reproduce the defect.")
    data["tickets"] = qa.load_json(fixture_dir / "tickets.json")
    data["tickets"][0]["reproduction"] = {"reproduced": 1, "attempted": 2}
    summary = qa.validate_results(data, fixture_dir, observations=True)
    assert summary["counts"]["FAIL"] == 1
    invalid = copy.deepcopy(data)
    invalid["tickets"] = []
    bad_case = invalid["cases"][0]
    bad_case["status"] = bad_case["steps"][0]["status"] = "PASS"
    bad_case["classification"] = "NONE"
    try:
        qa.validate_results(invalid, fixture_dir, observations=True)
    except qa.ContractError as error:
        assert "decisive attempt" in str(error)
    else:
        raise AssertionError("A successful retry must not erase the earlier failed attempt")
    invalid = copy.deepcopy(data)
    invalid["cases"][0]["attempts"][0]["evidence_ids"] = []
    try:
        qa.validate_results(invalid, fixture_dir, observations=True)
    except qa.ContractError as error:
        assert "failed attempt has no evidence" in str(error)
    else:
        raise AssertionError("Reproduction claims need actual per-attempt evidence")
    print(json.dumps({"valid": True, "checks": 4, "cases": [
        "failure_then_tool_block_remains_failure", "failure_then_pass_is_intermittent_one_of_two",
        "passing_retry_cannot_erase_failure", "failed_attempt_requires_evidence"]}, indent=2))


if __name__ == "__main__":
    main()
