# Local multilingual demonstration

This fixture is a fictitious Atlas Studio website for validating the Multilingual Website Release QA skill. It runs entirely on loopback, uses Python's standard library, and has no external assets, credentials, analytics, message delivery, persistent submissions, or payment flows.

The business expectations and the twenty journey–language cases are in [product-contract.md](product-contract.md). An auditor should receive that contract, the skill, and the running baseline URL. Keep the implementation and the separate comparison oracle out of the auditor's context until its baseline report has been frozen. The inventory lives under `../oracle/`; it is test material, not a skill runtime resource.

## Prerequisites

- Python 3.10 or newer for the fixture server.
- An authorized interactive browser for functional execution. The server itself does not require Playwright.
- Two unused loopback TCP ports, 39175 and 39176 by default.

Run commands from the repository root. Inspection checks whether the two standard ports can be bound; it creates no files and performs no HTTP request:

```sh
python3 -B tests/demo/server.py --mode inspect
```

Start the baseline and corrected variants in separate terminals:

```sh
python3 -B tests/demo/server.py --mode serve --variant baseline --port 39175
```

```sh
python3 -B tests/demo/server.py --mode serve --variant corrected --port 39176
```

The server prints a readiness line after binding successfully. The URLs are `http://127.0.0.1:39175/en/` and `http://127.0.0.1:39176/en/`; replace `en` with `fr` for French. `GET /healthz` reports readiness and the selected variant. `GET /auth-required` deliberately returns HTTP 401 for a separate blocked-authentication check. Stop a server with Ctrl+C. Stopping it changes no fixture files.

## Execution and interpretation

Use one fresh browser context for each journey–language pair. The contract assigns desktop to journeys J01–J08 and a 390 × 844 narrow viewport to J09–J10. This is twenty pairs, not a complete device or browser matrix. No country verification is requested by the fixture.

The contact form is explicitly authorized for this synthetic campaign. Its submit handler changes local DOM content only; it does not send a request or save the fictional contact data. Other website submissions require their own authorization.

Baseline and corrected modes expose the same contract and routes. Their expected differences are deliberately separated into the oracle. Compare actual findings only after preserving the independent report, then use the corrected URL for an actual retest. Do not treat expected oracle counts as observed test results.

All HTML, CSS, and JavaScript are served by `server.py`. There is no build step or package download. Browser-derived evidence and campaign exports belong in a separate validation output directory; the skill runtime must not depend on this fixture or its absolute installation path.
