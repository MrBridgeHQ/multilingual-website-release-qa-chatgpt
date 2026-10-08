#!/usr/bin/env python3
"""Read-only regression check for country mismatch versus website defect."""
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
    spec = importlib.util.spec_from_file_location("qa_country_helper", args.helper)
    qa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qa)
    fixture_dir = ROOT / "tests/contracts"
    data = qa.load_json(fixture_dir / "observations.json")
    data["evidence"][0]["kind"] = "NETWORK"
    data["campaign"]["capabilities"]["network"] = True
    data["campaign"]["capabilities"]["geography"] = True
    case = data["cases"][0]
    case["status"] = case["steps"][0]["status"] = case["attempts"][0]["status"] = "BLOCKED"
    case["classification"] = "TOOLING_INCIDENT"
    case["steps"][0]["observed"] = "The synthetic network fixture models a US exit where FR was required."
    case["country"].update(requested="FR", verified="US", status="FAIL",
                           same_network_context=True, evidence_ids=["fixture-text"],
                           note="Synthetic fixture only: both records model the same network context.")
    summary = qa.validate_results(data, fixture_dir, observations=True)
    assert summary["counts"]["BLOCKED"] == 1 and summary["counts"]["FAIL"] == 0
    invalid = copy.deepcopy(data)
    case = invalid["cases"][0]
    case["status"] = case["steps"][0]["status"] = case["attempts"][0]["status"] = "PASS"
    case["classification"] = "NONE"
    try:
        qa.validate_results(invalid, fixture_dir, observations=True)
    except qa.ContractError as error:
        assert "geographic check" in str(error)
    else:
        raise AssertionError("A mismatched required network country cannot produce PASS")
    print(json.dumps({"valid": True, "checks": 2,
                      "cases": ["country_mismatch_is_tooling_block", "country_mismatch_cannot_pass"]}, indent=2))


if __name__ == "__main__":
    main()
