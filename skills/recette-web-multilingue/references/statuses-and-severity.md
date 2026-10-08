# Statuses, severity, and confidence

## Case and step states

| State | Meaning | Required context |
| --- | --- | --- |
| PASS | Executed and expected behavior observed | Actual observation and supporting evidence |
| FAIL | Executed and a mismatch demonstrated | Explicit expectation, actual mismatch, evidence |
| BLOCKED | An identified obstacle prevented execution/completion | Attempt and reason; retain completed steps |
| NOT_RUN | Planned but not executed | Reason, such as budget, missing prerequisite, or deferred decision |
| NOT_APPLICABLE | Outside the actual context | A concrete explanation |

A later PASS does not erase a prior failed attempt. Preserve the attempt sequence and report observed frequency. For a partially failed journey, a proven mismatch can support FAIL while later steps remain NOT_RUN. A partly successful journey stopped by unavailable authentication or a browser incident is BLOCKED, not PASS.

A tool crash, permission denial, selector implementation bug, or unavailable browser is a TOOLING_INCIDENT until website evidence says otherwise. An authentic HTTP 401 behind required authentication is a blocked precondition unless accessible unauthenticated behavior itself is an agreed requirement.

When the expected behavior is absent, use PRODUCT_QUESTION or an explicit assumption. SUSPECTED_INCONSISTENCY means a potential issue needs confirmation. Neither implies a demonstrated defect.

## Impact severity

| Severity | Use when demonstrated impact supports it |
| --- | --- |
| BLOCKER | A critical agreed release journey cannot be completed and there is no practical workaround |
| MAJOR | A substantial workflow or important language/device segment is impaired |
| MINOR | A limited defect exists with a practical workaround and modest user impact |
| COSMETIC | Presentation/copy inconsistency with no demonstrated functional obstruction |

Explain severity using the observed user impact, affected scope, criticality, and available workaround. Do not make every broken translation MINOR or every console message BLOCKER. Avoid extrapolating one profile to the entire site.

Keep HIGH/MEDIUM/LOW confidence separate from severity. State whether confidence concerns the observed behavior or the proposed cause; an observed failure can be certain while its cause is only a hypothesis. The ticket's correction field must say when a root-cause proposal is hypothetical.

## Completion and coverage

Derive counts from case records, not from prose. Keep every planned case in the denominator and make exclusions visible. Report the exact fractions being counted; a case with a demonstrated failure is executed but unsuccessful.

A scoped release verdict is not a certification. Any critical BLOCKED or NOT_RUN case prevents a clean approval of that scope. A campaign with zero executed cases cannot validate the website. All-NOT_APPLICABLE coverage is not a successful audit.

Ticket replay validates reproducibility, not necessarily the cause. Fixed-site verification needs new observations in a separate campaign and matching acceptance criteria. Preserve the old failure evidence.
