# Supplemental ticket clarifications

These facts supplement the historical tickets. Frozen tickets, replay observations, results, assessments and evidence are unchanged. No browser campaign was rerun.

## QA-004: confirmation selector

After opening /fr/contact, leaving both fields empty and clicking #contact-submit once, inspect #confirmation alongside #name-error and #email-error.

The recorded element is a P with id="confirmation" and role="status". After the empty submission, hidden=true, visible=false, the text is empty and its recorded bounds have zero width and height. One matching ID appears in the captured DOM.

[Recorded validation DOM](report/evidence/REPLAY-QA-004-a1-validation.json). This observation concerns empty submission only; it does not verify successful confirmation.

## QA-006: exact independent replay configuration

To reproduce the independently observed environment, create a fresh Chromium context with the explicit settings below and open /fr/offer. Treat the profile as a narrow desktop Chromium viewport; do not claim a physical mobile-device test.

| Setting | Recorded value | Basis |
| --- | --- | --- |
| Browser | Chromium 151.0.7922.34 | Observed browser version |
| Playwright | 1.62.0 | Execution receipt |
| Viewport | 390 × 844 CSS pixels | Configured and observed |
| Locale | en-GB | Configured; navigator.language observed |
| Time zone | UTC | Configured and observed |
| device_scale_factor | 1 | Explicit context configuration |
| is_mobile | false | Explicit context configuration |
| has_touch | false | Explicit context configuration |
| service_workers | block | Explicit context configuration |
| Browser mode | --headless=new | Recorded launch command |
| Custom user-agent override | None supplied | Context configuration |
| Physical device | No | Viewport-based Chromium run |

[Recorded offer DOM](report/evidence/REPLAY-QA-006-a1-opened.json) and [portable driver configuration](../../tests/replay_from_tickets.py).

The actual user-agent string, runtime window.devicePixelRatio, and runtime touch APIs were not captured and remain unavailable. The configured scale factor and touch setting above must not be presented as separate runtime measurements. The full emulation settings of the original baseline attempts also remain unavailable; this supplement records the independent replay configuration only.
