# Synthetic fixture comparison

Frozen input files verified: 262.

Observed detection: 6/6 seeded defects.
Control false failures: 0/14.
Observed FAIL to PASS transitions: 6/6.

| Case | Baseline | Corrected | Original tickets |
| --- | --- | --- | --- |
| J02-fr | FAIL | PASS | QA-001 |
| J03-en | FAIL | PASS | QA-002 |
| J04-fr | FAIL | PASS | QA-003 |
| J07-fr | FAIL | PASS | QA-004 |
| J08-en | FAIL | PASS | QA-005 |
| J10-fr | FAIL | PASS | QA-006 |

## Limits

- Manifestation matching uses case identifiers, ticket linkage, and collected evidence; it does not prove a shared root cause.
- Unexpected failures require investigation and are not automatically false positives.
- The oracle describes this synthetic fixture only; this is not a measurement of general defect recall.
- Agent separation was procedural on a shared filesystem.
