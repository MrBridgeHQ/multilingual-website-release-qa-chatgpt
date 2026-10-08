# Negative scenario validation

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
