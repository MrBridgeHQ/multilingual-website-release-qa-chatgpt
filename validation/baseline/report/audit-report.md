# Multilingual Website Release QA

## Scope and environment

- **Campaign:** baseline-blind-20261008
- **Environment:** LOCAL
- **Starting URL:** http://127.0.0.1:39175
- **Execution period:** 2026-10-08T11:43:40.730Z → 2026-10-08T11:44:03.494Z

### Observed tool capabilities

- extraction: true
- interaction: true
- screenshots: true
- network: true
- console: true
- traces: false
- geography: false

## Summary

- **Scoped verdict:** ISSUES_FOUND
- **Executed case outcomes / planned cases:** 20/20
- **Critical cases without a completed outcome:** None

This verdict applies only to the explicitly planned cases and observed environment.

| Status | n |
| --- | ---: |
| PASS | 14 |
| FAIL | 6 |
| BLOCKED | 0 |
| NOT_RUN | 0 |
| NOT_APPLICABLE | 0 |

## Test matrix

| Case | Journey | Language | Profile | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| J01-en | J01 | en | desktop | PASS | [J01-en-a1-s1-state](evidence/J01-en-a1-s1-state.json), [J01-en-a1-s1-viewport](evidence/J01-en-a1-s1-viewport.png), [J01-en-a1-s2-state](evidence/J01-en-a1-s2-state.json), [J01-en-a1-s2-viewport](evidence/J01-en-a1-s2-viewport.png), [J01-en-a1-s3-state](evidence/J01-en-a1-s3-state.json), [J01-en-a1-s3-viewport](evidence/J01-en-a1-s3-viewport.png), [J01-en-a1-network](evidence/J01-en-a1-network.json), [J01-en-a1-console](evidence/J01-en-a1-console.json), [J01-en-a1-attempt](evidence/J01-en-a1-attempt.json) |
| J01-fr | J01 | fr | desktop | PASS | [J01-fr-a1-s1-state](evidence/J01-fr-a1-s1-state.json), [J01-fr-a1-s1-viewport](evidence/J01-fr-a1-s1-viewport.png), [J01-fr-a1-s2-state](evidence/J01-fr-a1-s2-state.json), [J01-fr-a1-s2-viewport](evidence/J01-fr-a1-s2-viewport.png), [J01-fr-a1-s3-state](evidence/J01-fr-a1-s3-state.json), [J01-fr-a1-s3-viewport](evidence/J01-fr-a1-s3-viewport.png), [J01-fr-a1-network](evidence/J01-fr-a1-network.json), [J01-fr-a1-console](evidence/J01-fr-a1-console.json), [J01-fr-a1-attempt](evidence/J01-fr-a1-attempt.json) |
| J02-en | J02 | en | desktop | PASS | [J02-en-a1-s1-state](evidence/J02-en-a1-s1-state.json), [J02-en-a1-s1-viewport](evidence/J02-en-a1-s1-viewport.png), [J02-en-a1-s2-state](evidence/J02-en-a1-s2-state.json), [J02-en-a1-s2-viewport](evidence/J02-en-a1-s2-viewport.png), [J02-en-a1-s3-state](evidence/J02-en-a1-s3-state.json), [J02-en-a1-s3-viewport](evidence/J02-en-a1-s3-viewport.png), [J02-en-a1-network](evidence/J02-en-a1-network.json), [J02-en-a1-console](evidence/J02-en-a1-console.json), [J02-en-a1-attempt](evidence/J02-en-a1-attempt.json) |
| J02-fr | J02 | fr | desktop | FAIL | [J02-fr-a1-s1-state](evidence/J02-fr-a1-s1-state.json), [J02-fr-a1-s1-viewport](evidence/J02-fr-a1-s1-viewport.png), [J02-fr-a1-s2-state](evidence/J02-fr-a1-s2-state.json), [J02-fr-a1-s2-viewport](evidence/J02-fr-a1-s2-viewport.png), [J02-fr-a1-s3-state](evidence/J02-fr-a1-s3-state.json), [J02-fr-a1-s3-viewport](evidence/J02-fr-a1-s3-viewport.png), [J02-fr-a1-network](evidence/J02-fr-a1-network.json), [J02-fr-a1-console](evidence/J02-fr-a1-console.json), [J02-fr-a1-attempt](evidence/J02-fr-a1-attempt.json), [J02-fr-a2-s1-state](evidence/J02-fr-a2-s1-state.json), [J02-fr-a2-s1-viewport](evidence/J02-fr-a2-s1-viewport.png), [J02-fr-a2-s2-state](evidence/J02-fr-a2-s2-state.json), [J02-fr-a2-s2-viewport](evidence/J02-fr-a2-s2-viewport.png), [J02-fr-a2-s3-state](evidence/J02-fr-a2-s3-state.json), [J02-fr-a2-s3-viewport](evidence/J02-fr-a2-s3-viewport.png), [J02-fr-a2-network](evidence/J02-fr-a2-network.json), [J02-fr-a2-console](evidence/J02-fr-a2-console.json), [J02-fr-a2-attempt](evidence/J02-fr-a2-attempt.json) |
| J03-en | J03 | en | desktop | FAIL | [J03-en-a1-s1-state](evidence/J03-en-a1-s1-state.json), [J03-en-a1-s1-viewport](evidence/J03-en-a1-s1-viewport.png), [J03-en-a1-s2-state](evidence/J03-en-a1-s2-state.json), [J03-en-a1-s2-viewport](evidence/J03-en-a1-s2-viewport.png), [J03-en-a1-s3-state](evidence/J03-en-a1-s3-state.json), [J03-en-a1-s3-viewport](evidence/J03-en-a1-s3-viewport.png), [J03-en-a1-s4-state](evidence/J03-en-a1-s4-state.json), [J03-en-a1-s4-viewport](evidence/J03-en-a1-s4-viewport.png), [J03-en-a1-network](evidence/J03-en-a1-network.json), [J03-en-a1-console](evidence/J03-en-a1-console.json), [J03-en-a1-attempt](evidence/J03-en-a1-attempt.json), [J03-en-a2-s1-state](evidence/J03-en-a2-s1-state.json), [J03-en-a2-s1-viewport](evidence/J03-en-a2-s1-viewport.png), [J03-en-a2-s2-state](evidence/J03-en-a2-s2-state.json), [J03-en-a2-s2-viewport](evidence/J03-en-a2-s2-viewport.png), [J03-en-a2-s3-state](evidence/J03-en-a2-s3-state.json), [J03-en-a2-s3-viewport](evidence/J03-en-a2-s3-viewport.png), [J03-en-a2-s4-state](evidence/J03-en-a2-s4-state.json), [J03-en-a2-s4-viewport](evidence/J03-en-a2-s4-viewport.png), [J03-en-a2-network](evidence/J03-en-a2-network.json), [J03-en-a2-console](evidence/J03-en-a2-console.json), [J03-en-a2-attempt](evidence/J03-en-a2-attempt.json) |
| J03-fr | J03 | fr | desktop | PASS | [J03-fr-a1-s1-state](evidence/J03-fr-a1-s1-state.json), [J03-fr-a1-s1-viewport](evidence/J03-fr-a1-s1-viewport.png), [J03-fr-a1-s2-state](evidence/J03-fr-a1-s2-state.json), [J03-fr-a1-s2-viewport](evidence/J03-fr-a1-s2-viewport.png), [J03-fr-a1-s3-state](evidence/J03-fr-a1-s3-state.json), [J03-fr-a1-s3-viewport](evidence/J03-fr-a1-s3-viewport.png), [J03-fr-a1-s4-state](evidence/J03-fr-a1-s4-state.json), [J03-fr-a1-s4-viewport](evidence/J03-fr-a1-s4-viewport.png), [J03-fr-a1-network](evidence/J03-fr-a1-network.json), [J03-fr-a1-console](evidence/J03-fr-a1-console.json), [J03-fr-a1-attempt](evidence/J03-fr-a1-attempt.json) |
| J04-en | J04 | en | desktop | PASS | [J04-en-a1-s1-state](evidence/J04-en-a1-s1-state.json), [J04-en-a1-s1-viewport](evidence/J04-en-a1-s1-viewport.png), [J04-en-a1-s2-state](evidence/J04-en-a1-s2-state.json), [J04-en-a1-s2-viewport](evidence/J04-en-a1-s2-viewport.png), [J04-en-a1-s3-state](evidence/J04-en-a1-s3-state.json), [J04-en-a1-s3-viewport](evidence/J04-en-a1-s3-viewport.png), [J04-en-a1-network](evidence/J04-en-a1-network.json), [J04-en-a1-console](evidence/J04-en-a1-console.json), [J04-en-a1-attempt](evidence/J04-en-a1-attempt.json) |
| J04-fr | J04 | fr | desktop | FAIL | [J04-fr-a1-s1-state](evidence/J04-fr-a1-s1-state.json), [J04-fr-a1-s1-viewport](evidence/J04-fr-a1-s1-viewport.png), [J04-fr-a1-s2-state](evidence/J04-fr-a1-s2-state.json), [J04-fr-a1-s2-viewport](evidence/J04-fr-a1-s2-viewport.png), [J04-fr-a1-s3-state](evidence/J04-fr-a1-s3-state.json), [J04-fr-a1-s3-viewport](evidence/J04-fr-a1-s3-viewport.png), [J04-fr-a1-network](evidence/J04-fr-a1-network.json), [J04-fr-a1-console](evidence/J04-fr-a1-console.json), [J04-fr-a1-attempt](evidence/J04-fr-a1-attempt.json), [J04-fr-a2-network](evidence/J04-fr-a2-network.json), [J04-fr-a2-console](evidence/J04-fr-a2-console.json), [J04-fr-a2-attempt](evidence/J04-fr-a2-attempt.json), [J04-fr-a2-s1-state](evidence/J04-fr-a2-s1-state.json) |
| J05-en | J05 | en | desktop | PASS | [J05-en-a1-s1-state](evidence/J05-en-a1-s1-state.json), [J05-en-a1-s1-viewport](evidence/J05-en-a1-s1-viewport.png), [J05-en-a1-s2-state](evidence/J05-en-a1-s2-state.json), [J05-en-a1-s2-viewport](evidence/J05-en-a1-s2-viewport.png), [J05-en-a1-s3-state](evidence/J05-en-a1-s3-state.json), [J05-en-a1-s3-viewport](evidence/J05-en-a1-s3-viewport.png), [J05-en-a1-s4-state](evidence/J05-en-a1-s4-state.json), [J05-en-a1-s4-viewport](evidence/J05-en-a1-s4-viewport.png), [J05-en-a1-network](evidence/J05-en-a1-network.json), [J05-en-a1-console](evidence/J05-en-a1-console.json), [J05-en-a1-attempt](evidence/J05-en-a1-attempt.json) |
| J05-fr | J05 | fr | desktop | PASS | [J05-fr-a1-s1-state](evidence/J05-fr-a1-s1-state.json), [J05-fr-a1-s1-viewport](evidence/J05-fr-a1-s1-viewport.png), [J05-fr-a1-s2-state](evidence/J05-fr-a1-s2-state.json), [J05-fr-a1-s2-viewport](evidence/J05-fr-a1-s2-viewport.png), [J05-fr-a1-s3-state](evidence/J05-fr-a1-s3-state.json), [J05-fr-a1-s3-viewport](evidence/J05-fr-a1-s3-viewport.png), [J05-fr-a1-s4-state](evidence/J05-fr-a1-s4-state.json), [J05-fr-a1-s4-viewport](evidence/J05-fr-a1-s4-viewport.png), [J05-fr-a1-network](evidence/J05-fr-a1-network.json), [J05-fr-a1-console](evidence/J05-fr-a1-console.json), [J05-fr-a1-attempt](evidence/J05-fr-a1-attempt.json) |
| J06-en | J06 | en | desktop | PASS | [J06-en-a1-s1-state](evidence/J06-en-a1-s1-state.json), [J06-en-a1-s1-viewport](evidence/J06-en-a1-s1-viewport.png), [J06-en-a1-s2-state](evidence/J06-en-a1-s2-state.json), [J06-en-a1-s2-viewport](evidence/J06-en-a1-s2-viewport.png), [J06-en-a1-s3-state](evidence/J06-en-a1-s3-state.json), [J06-en-a1-s3-viewport](evidence/J06-en-a1-s3-viewport.png), [J06-en-a1-network](evidence/J06-en-a1-network.json), [J06-en-a1-console](evidence/J06-en-a1-console.json), [J06-en-a1-attempt](evidence/J06-en-a1-attempt.json) |
| J06-fr | J06 | fr | desktop | PASS | [J06-fr-a1-s1-state](evidence/J06-fr-a1-s1-state.json), [J06-fr-a1-s1-viewport](evidence/J06-fr-a1-s1-viewport.png), [J06-fr-a1-s2-state](evidence/J06-fr-a1-s2-state.json), [J06-fr-a1-s2-viewport](evidence/J06-fr-a1-s2-viewport.png), [J06-fr-a1-s3-state](evidence/J06-fr-a1-s3-state.json), [J06-fr-a1-s3-viewport](evidence/J06-fr-a1-s3-viewport.png), [J06-fr-a1-network](evidence/J06-fr-a1-network.json), [J06-fr-a1-console](evidence/J06-fr-a1-console.json), [J06-fr-a1-attempt](evidence/J06-fr-a1-attempt.json) |
| J07-en | J07 | en | desktop | PASS | [J07-en-a1-s1-state](evidence/J07-en-a1-s1-state.json), [J07-en-a1-s1-viewport](evidence/J07-en-a1-s1-viewport.png), [J07-en-a1-s2-state](evidence/J07-en-a1-s2-state.json), [J07-en-a1-s2-viewport](evidence/J07-en-a1-s2-viewport.png), [J07-en-a1-s3-state](evidence/J07-en-a1-s3-state.json), [J07-en-a1-s3-viewport](evidence/J07-en-a1-s3-viewport.png), [J07-en-a1-s4-state](evidence/J07-en-a1-s4-state.json), [J07-en-a1-s4-viewport](evidence/J07-en-a1-s4-viewport.png), [J07-en-a1-network](evidence/J07-en-a1-network.json), [J07-en-a1-console](evidence/J07-en-a1-console.json), [J07-en-a1-attempt](evidence/J07-en-a1-attempt.json) |
| J07-fr | J07 | fr | desktop | FAIL | [J07-fr-a1-s1-state](evidence/J07-fr-a1-s1-state.json), [J07-fr-a1-s1-viewport](evidence/J07-fr-a1-s1-viewport.png), [J07-fr-a1-s2-state](evidence/J07-fr-a1-s2-state.json), [J07-fr-a1-s2-viewport](evidence/J07-fr-a1-s2-viewport.png), [J07-fr-a1-s3-state](evidence/J07-fr-a1-s3-state.json), [J07-fr-a1-s3-viewport](evidence/J07-fr-a1-s3-viewport.png), [J07-fr-a1-s4-state](evidence/J07-fr-a1-s4-state.json), [J07-fr-a1-s4-viewport](evidence/J07-fr-a1-s4-viewport.png), [J07-fr-a1-network](evidence/J07-fr-a1-network.json), [J07-fr-a1-console](evidence/J07-fr-a1-console.json), [J07-fr-a1-attempt](evidence/J07-fr-a1-attempt.json), [J07-fr-a2-s1-state](evidence/J07-fr-a2-s1-state.json), [J07-fr-a2-s1-viewport](evidence/J07-fr-a2-s1-viewport.png), [J07-fr-a2-s2-state](evidence/J07-fr-a2-s2-state.json), [J07-fr-a2-s2-viewport](evidence/J07-fr-a2-s2-viewport.png), [J07-fr-a2-s3-state](evidence/J07-fr-a2-s3-state.json), [J07-fr-a2-s3-viewport](evidence/J07-fr-a2-s3-viewport.png), [J07-fr-a2-s4-state](evidence/J07-fr-a2-s4-state.json), [J07-fr-a2-s4-viewport](evidence/J07-fr-a2-s4-viewport.png), [J07-fr-a2-network](evidence/J07-fr-a2-network.json), [J07-fr-a2-console](evidence/J07-fr-a2-console.json), [J07-fr-a2-attempt](evidence/J07-fr-a2-attempt.json) |
| J08-en | J08 | en | desktop | FAIL | [J08-en-a1-s1-state](evidence/J08-en-a1-s1-state.json), [J08-en-a1-s1-viewport](evidence/J08-en-a1-s1-viewport.png), [J08-en-a1-s2-state](evidence/J08-en-a1-s2-state.json), [J08-en-a1-s2-viewport](evidence/J08-en-a1-s2-viewport.png), [J08-en-a1-s3-state](evidence/J08-en-a1-s3-state.json), [J08-en-a1-s3-viewport](evidence/J08-en-a1-s3-viewport.png), [J08-en-a1-network](evidence/J08-en-a1-network.json), [J08-en-a1-console](evidence/J08-en-a1-console.json), [J08-en-a1-attempt](evidence/J08-en-a1-attempt.json), [J08-en-a2-s1-state](evidence/J08-en-a2-s1-state.json), [J08-en-a2-s1-viewport](evidence/J08-en-a2-s1-viewport.png), [J08-en-a2-s2-state](evidence/J08-en-a2-s2-state.json), [J08-en-a2-s2-viewport](evidence/J08-en-a2-s2-viewport.png), [J08-en-a2-s3-state](evidence/J08-en-a2-s3-state.json), [J08-en-a2-s3-viewport](evidence/J08-en-a2-s3-viewport.png), [J08-en-a2-network](evidence/J08-en-a2-network.json), [J08-en-a2-console](evidence/J08-en-a2-console.json), [J08-en-a2-attempt](evidence/J08-en-a2-attempt.json) |
| J08-fr | J08 | fr | desktop | PASS | [J08-fr-a1-s1-state](evidence/J08-fr-a1-s1-state.json), [J08-fr-a1-s1-viewport](evidence/J08-fr-a1-s1-viewport.png), [J08-fr-a1-s2-state](evidence/J08-fr-a1-s2-state.json), [J08-fr-a1-s2-viewport](evidence/J08-fr-a1-s2-viewport.png), [J08-fr-a1-s3-state](evidence/J08-fr-a1-s3-state.json), [J08-fr-a1-s3-viewport](evidence/J08-fr-a1-s3-viewport.png), [J08-fr-a1-s4-state](evidence/J08-fr-a1-s4-state.json), [J08-fr-a1-s4-viewport](evidence/J08-fr-a1-s4-viewport.png), [J08-fr-a1-s5-state](evidence/J08-fr-a1-s5-state.json), [J08-fr-a1-s5-viewport](evidence/J08-fr-a1-s5-viewport.png), [J08-fr-a1-network](evidence/J08-fr-a1-network.json), [J08-fr-a1-console](evidence/J08-fr-a1-console.json), [J08-fr-a1-attempt](evidence/J08-fr-a1-attempt.json) |
| J09-en | J09 | en | mobile | PASS | [J09-en-a1-s1-state](evidence/J09-en-a1-s1-state.json), [J09-en-a1-s1-viewport](evidence/J09-en-a1-s1-viewport.png), [J09-en-a1-s2-state](evidence/J09-en-a1-s2-state.json), [J09-en-a1-s2-viewport](evidence/J09-en-a1-s2-viewport.png), [J09-en-a1-s3-state](evidence/J09-en-a1-s3-state.json), [J09-en-a1-s3-viewport](evidence/J09-en-a1-s3-viewport.png), [J09-en-a1-s4-state](evidence/J09-en-a1-s4-state.json), [J09-en-a1-s4-viewport](evidence/J09-en-a1-s4-viewport.png), [J09-en-a1-network](evidence/J09-en-a1-network.json), [J09-en-a1-console](evidence/J09-en-a1-console.json), [J09-en-a1-attempt](evidence/J09-en-a1-attempt.json) |
| J09-fr | J09 | fr | mobile | PASS | [J09-fr-a1-s1-state](evidence/J09-fr-a1-s1-state.json), [J09-fr-a1-s1-viewport](evidence/J09-fr-a1-s1-viewport.png), [J09-fr-a1-s2-state](evidence/J09-fr-a1-s2-state.json), [J09-fr-a1-s2-viewport](evidence/J09-fr-a1-s2-viewport.png), [J09-fr-a1-s3-state](evidence/J09-fr-a1-s3-state.json), [J09-fr-a1-s3-viewport](evidence/J09-fr-a1-s3-viewport.png), [J09-fr-a1-s4-state](evidence/J09-fr-a1-s4-state.json), [J09-fr-a1-s4-viewport](evidence/J09-fr-a1-s4-viewport.png), [J09-fr-a1-network](evidence/J09-fr-a1-network.json), [J09-fr-a1-console](evidence/J09-fr-a1-console.json), [J09-fr-a1-attempt](evidence/J09-fr-a1-attempt.json) |
| J10-en | J10 | en | mobile | PASS | [J10-en-a1-s1-state](evidence/J10-en-a1-s1-state.json), [J10-en-a1-s1-viewport](evidence/J10-en-a1-s1-viewport.png), [J10-en-a1-s2-state](evidence/J10-en-a1-s2-state.json), [J10-en-a1-s2-viewport](evidence/J10-en-a1-s2-viewport.png), [J10-en-a1-s3-state](evidence/J10-en-a1-s3-state.json), [J10-en-a1-s3-viewport](evidence/J10-en-a1-s3-viewport.png), [J10-en-a1-s4-state](evidence/J10-en-a1-s4-state.json), [J10-en-a1-s4-viewport](evidence/J10-en-a1-s4-viewport.png), [J10-en-a1-network](evidence/J10-en-a1-network.json), [J10-en-a1-console](evidence/J10-en-a1-console.json), [J10-en-a1-attempt](evidence/J10-en-a1-attempt.json) |
| J10-fr | J10 | fr | mobile | FAIL | [J10-fr-a1-s1-state](evidence/J10-fr-a1-s1-state.json), [J10-fr-a1-s1-viewport](evidence/J10-fr-a1-s1-viewport.png), [J10-fr-a1-s2-state](evidence/J10-fr-a1-s2-state.json), [J10-fr-a1-s2-viewport](evidence/J10-fr-a1-s2-viewport.png), [J10-fr-a1-s3-state](evidence/J10-fr-a1-s3-state.json), [J10-fr-a1-s3-viewport](evidence/J10-fr-a1-s3-viewport.png), [J10-fr-a1-s4-state](evidence/J10-fr-a1-s4-state.json), [J10-fr-a1-s4-viewport](evidence/J10-fr-a1-s4-viewport.png), [J10-fr-a1-network](evidence/J10-fr-a1-network.json), [J10-fr-a1-console](evidence/J10-fr-a1-console.json), [J10-fr-a1-attempt](evidence/J10-fr-a1-attempt.json), [J10-fr-a2-s1-state](evidence/J10-fr-a2-s1-state.json), [J10-fr-a2-s1-viewport](evidence/J10-fr-a2-s1-viewport.png), [J10-fr-a2-s2-state](evidence/J10-fr-a2-s2-state.json), [J10-fr-a2-s2-viewport](evidence/J10-fr-a2-s2-viewport.png), [J10-fr-a2-s3-state](evidence/J10-fr-a2-s3-state.json), [J10-fr-a2-s3-viewport](evidence/J10-fr-a2-s3-viewport.png), [J10-fr-a2-s4-state](evidence/J10-fr-a2-s4-state.json), [J10-fr-a2-s4-viewport](evidence/J10-fr-a2-s4-viewport.png), [J10-fr-a2-network](evidence/J10-fr-a2-network.json), [J10-fr-a2-console](evidence/J10-fr-a2-console.json), [J10-fr-a2-attempt](evidence/J10-fr-a2-attempt.json) |

## Detailed defect tickets

### QA-001 — French desktop About navigation opens Search

**User impact:** A French desktop visitor selecting À propos is taken to Search and cannot reach the intended information through that primary link.

**Severity:** MAJOR
**Severity rationale:** An agreed primary navigation journey fails for the French desktop segment. Direct /fr/about and the tested French search-result route provide observed alternate access, so this is not a site-wide blocker.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/", "http://127.0.0.1:39175/fr/search"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 1440 × 900 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/ at 1440 × 900.
2. Click the visible À propos link #main-about.
3. Inspect the actual URL and #page-heading.

**Expected:** The destination is /fr/about, HTTP 200, html[lang]=fr, heading À propos d’Atlas Studio.

**Observed:** The link has href=/fr/search. Clicking it reaches /fr/search with heading Rechercher chez Atlas Studio; the document remains French.

**Evidence:** [J02-fr-a1-s1-state](evidence/J02-fr-a1-s1-state.json), [J02-fr-a1-s3-state](evidence/J02-fr-a1-s3-state.json), [J02-fr-a1-s3-viewport](evidence/J02-fr-a1-s3-viewport.png), [J02-fr-a2-s1-state](evidence/J02-fr-a2-s1-state.json), [J02-fr-a2-s3-state](evidence/J02-fr-a2-s3-state.json), [J02-fr-a2-s3-viewport](evidence/J02-fr-a2-s3-viewport.png)
**Related cases:** J02-fr
**Reproduction frequency:** 2/2

**Correction hypothesis:** The observed desktop #main-about href points at the search route. Correcting its route binding to /fr/about is a hypothesis to verify in implementation; no source was inspected.

**Acceptance criteria**

- Clicking #main-about from /fr/ reaches /fr/about and the approved localized heading.
- The English desktop primary navigation continues to reach /en/about.
- The already working French mobile #mobile-about route remains /fr/about.

**Retest procedure**

1. In a new campaign on the corrected origin, repeat J02-fr exactly.
2. Run J02-en and J09-fr as relevant navigation witnesses.

### QA-002 — Switching About from English to French loses the internal page

**User impact:** A visitor reading the English About page loses that page when selecting French and arrives at the French home page.

**Severity:** MAJOR
**Severity rationale:** The explicit context-preserving language-switch journey fails in one direction. The other direction and direct French About access work in the observed scope.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/en/about", "http://127.0.0.1:39175/fr/"], "languages": ["en"], "profiles": ["desktop"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 1440 × 900 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/en/about at 1440 × 900.
2. Click the Français control #language-switch.
3. Read the destination URL, html[lang] and #page-heading.

**Expected:** The destination is /fr/about with html[lang]=fr and heading À propos d’Atlas Studio.

**Observed:** #language-switch has href=/fr/. The actual destination is /fr/ and its heading is Bienvenue chez Atlas Studio. The language changes but the internal page is lost.

**Evidence:** [J03-en-a1-s1-state](evidence/J03-en-a1-s1-state.json), [J03-en-a1-s3-state](evidence/J03-en-a1-s3-state.json), [J03-en-a1-s4-viewport](evidence/J03-en-a1-s4-viewport.png), [J03-en-a2-s1-state](evidence/J03-en-a2-s1-state.json), [J03-en-a2-s3-state](evidence/J03-en-a2-s3-state.json), [J03-en-a2-s4-viewport](evidence/J03-en-a2-s4-viewport.png)
**Related cases:** J03-en
**Reproduction frequency:** 2/2

**Correction hypothesis:** The rendered language switch appears to use the French entry route rather than the equivalent About route. Derive the alternate target from the current route; root cause has not been inspected.

**Acceptance criteria**

- EN About → Français reaches /fr/about, preserving page identity.
- FR About → English still reaches /en/about.
- Both destination headings and html languages match their target routes.

**Retest procedure**

1. Repeat J03-en on the corrected origin with a fresh desktop context.
2. Repeat J03-fr to check the opposite direction.

### QA-003 — French legacy redirect switches the visitor to English

**User impact:** A visitor following the French legacy URL receives the English About page and loses the requested language.

**Severity:** MAJOR
**Severity rationale:** A supplied language-preserving entrypoint fails for French. Direct /fr/about works, giving an observed alternate entry route.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/legacy", "http://127.0.0.1:39175/en/about"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 1440 × 900 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/legacy at 1440 × 900.
2. Capture the redirect status and Location.
3. Inspect the final URL, document language and heading.

**Expected:** /fr/legacy returns HTTP 302 with Location /fr/about; the final page returns HTTP 200, html[lang]=fr and heading À propos d’Atlas Studio.

**Observed:** Both navigations return HTTP 302 Location /en/about, followed by HTTP 200 at /en/about, html[lang]=en and About Atlas Studio. Attempt 2 retained the actual DOM/network before a screenshot timeout; the timeout is not a website defect and no second screenshot is claimed.

**Evidence:** [J04-fr-a1-s2-state](evidence/J04-fr-a1-s2-state.json), [J04-fr-a1-s2-viewport](evidence/J04-fr-a1-s2-viewport.png), [J04-fr-a1-network](evidence/J04-fr-a1-network.json), [J04-fr-a2-s1-state](evidence/J04-fr-a2-s1-state.json), [J04-fr-a2-network](evidence/J04-fr-a2-network.json)
**Related cases:** J04-fr
**Reproduction frequency:** 2/2

**Correction hypothesis:** The redirect Location is visibly bound to the English route. Preserve the incoming language when selecting the About target; this implementation hypothesis has not been source-verified.

**Acceptance criteria**

- French legacy returns HTTP 302 to /fr/about, followed by a 200 French About document.
- English legacy still returns HTTP 302 to /en/about, followed by a 200 English About document.

**Retest procedure**

1. Repeat J04-fr on the corrected origin, collecting the 302 response and final DOM.
2. Repeat J04-en as the unchanged-language witness.

### QA-004 — French form validation errors are displayed in English

**User impact:** French visitors receive English instructions for correcting missing name and email fields.

**Severity:** MINOR
**Severity rationale:** Validation still prevents an empty confirmation and correctly exposes both invalid fields. The observed defect is localized guidance, with no demonstrated failure of validation itself.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/contact"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 1440 × 900 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {"name": "", "email": ""}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/contact at 1440 × 900.
2. Leave #contact-name and #contact-email empty.
3. Click #contact-submit once.
4. Read #name-error and #email-error.

**Expected:** Visible messages are Saisissez votre nom. and Saisissez une adresse e-mail valide.; both fields have aria-invalid=true and confirmation stays hidden.

**Observed:** Messages are Enter your name. and Enter a valid email address. on a French document. Both errors are visible, both aria-invalid values are true, and confirmation is hidden.

**Evidence:** [J07-fr-a1-s3-state](evidence/J07-fr-a1-s3-state.json), [J07-fr-a1-s4-state](evidence/J07-fr-a1-s4-state.json), [J07-fr-a1-s4-viewport](evidence/J07-fr-a1-s4-viewport.png), [J07-fr-a2-s4-state](evidence/J07-fr-a2-s4-state.json), [J07-fr-a2-s4-viewport](evidence/J07-fr-a2-s4-viewport.png)
**Related cases:** J07-fr
**Reproduction frequency:** 2/2

**Correction hypothesis:** The validation messages may be selected independently of the document language. Bind missing-name and missing/invalid-email copy to the active French locale; no validation source was read.

**Acceptance criteria**

- Empty French submission displays both exact approved French messages.
- Invalid fields remain marked aria-invalid=true; confirmation remains hidden.
- English empty validation and the French valid keyboard submission continue to work.

**Retest procedure**

1. Repeat J07-fr with empty fields on the corrected origin.
2. Run J07-en and J08-fr as validation and successful-submission witnesses.

### QA-005 — English contact form skips the required email field during keyboard entry

**User impact:** The contracted forward keyboard sequence cannot enter the required email, preventing English keyboard-only completion.

**Severity:** MAJOR
**Severity rationale:** A required field is skipped in an essential keyboard workflow. The French keyboard witness completes successfully. No working English keyboard workaround was verified.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/en/contact"], "languages": ["en"], "profiles": ["desktop"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 1440 × 900 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {"name": "Alex Test", "email": "alex@example.test"}

**Reproduction steps**

1. Open http://127.0.0.1:39175/en/contact at 1440 × 900.
2. Focus #contact-name and type Alex Test using keyboard input.
3. Press Tab exactly once.
4. Inspect document.activeElement.id and the visible focus outline. Do not click or fill the skipped email field.

**Expected:** The first Tab reaches #contact-email with a visible outline; after typing alex@example.test, the next Tab reaches #contact-submit and Enter displays the approved English confirmation.

**Observed:** The first Tab focuses #contact-submit, whose orange outline is visible. #contact-email stays empty and has tabindex=-1. The expected email step fails; subsequent email entry, submit and confirmation checks were NOT_RUN in both attempts.

**Evidence:** [J08-en-a1-s2-state](evidence/J08-en-a1-s2-state.json), [J08-en-a1-s3-state](evidence/J08-en-a1-s3-state.json), [J08-en-a1-s3-viewport](evidence/J08-en-a1-s3-viewport.png), [J08-en-a2-s3-state](evidence/J08-en-a2-s3-state.json), [J08-en-a2-s3-viewport](evidence/J08-en-a2-s3-viewport.png)
**Related cases:** J08-en
**Reproduction frequency:** 2/2

**Correction hypothesis:** The observed tabindex=-1 on #contact-email is consistent with exclusion from forward Tab order. Restore a normal focusable order and verify the visible focus indicator and complete keyboard submission; application source was not inspected.

**Acceptance criteria**

- The forward order is contact-name → contact-email → contact-submit.
- The focused email field and submit control have visible focus indications.
- Typing the supplied synthetic data and pressing Enter shows Thank you, Alex Test. Your local request is confirmed. without visible validation errors.
- The French keyboard form remains functional.

**Retest procedure**

1. Repeat J08-en exactly on the corrected origin, stopping if a focus transition is wrong.
2. Check every previously unexecuted later step through confirmation.
3. Repeat J08-fr as a keyboard witness.

### QA-006 — French mobile offer overflows horizontally and clips its description

**User impact:** At 390 CSS pixels, the offer card extends beyond the viewport and its description is clipped until the visitor scrolls horizontally.

**Severity:** MINOR
**Severity rationale:** The visible presentation is impaired, but the title, price, date and CTA remain readable, and the CTA was clicked successfully to /fr/contact. Functional obstruction beyond the clipped content was not demonstrated.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/offer"], "languages": ["fr"], "profiles": ["mobile"]}

**Preconditions**

- Fresh Chromium context, version 151.0.7922.34.
- Viewport 390 × 844 CSS pixels; locale en-GB; time zone UTC.
- Use the public synthetic baseline on port 39175; no login.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/offer with a 390 × 844 Chromium viewport.
2. Compare document.documentElement.scrollWidth with window.innerWidth.
3. Inspect the right edge of the offer card and description before interacting.
4. Click #offer-cta and record whether it remains visible and reaches French Contact.

**Expected:** scrollWidth is no greater than innerWidth + 1, the offer content fits without horizontal scrolling, and the visible CTA reaches /fr/contact.

**Observed:** Both attempts measure scrollWidth=556 and innerWidth=390, exceeding the one-pixel allowance by 165 pixels. The viewport screenshot clips the card and the sentence Un point de départ clair pour votre prochain site web. at the right edge. The CTA is inside the viewport and successfully reaches /fr/contact.

**Evidence:** [J10-fr-a1-s3-state](evidence/J10-fr-a1-s3-state.json), [J10-fr-a1-s3-viewport](evidence/J10-fr-a1-s3-viewport.png), [J10-fr-a1-s4-state](evidence/J10-fr-a1-s4-state.json), [J10-fr-a2-s3-state](evidence/J10-fr-a2-s3-state.json), [J10-fr-a2-s3-viewport](evidence/J10-fr-a2-s3-viewport.png), [J10-fr-a2-s4-state](evidence/J10-fr-a2-s4-state.json)
**Related cases:** J10-fr
**Reproduction frequency:** 2/2

**Correction hypothesis:** An offer-card width or minimum-width constraint may exceed the French mobile container. Constrain the card/content to available viewport width and allow wrapping; the CSS implementation was not inspected.

**Acceptance criteria**

- At 390 × 844, document scrollWidth <= innerWidth + 1 and the full description fits without horizontal page scrolling.
- Approved French title, price and date remain unchanged.
- The CTA remains inside the viewport, can be clicked and reaches /fr/contact.
- English offer layout and CTA continue to pass.

**Retest procedure**

1. Repeat all J10-fr checks on the corrected origin, capturing width measurements and a viewport screenshot.
2. Repeat J10-en as the layout and CTA witness.

## Case execution details

### J01-en — Open the requested home page

- URL: http://127.0.0.1:39175/en/
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:41.919Z → 2026-10-08T11:43:42.335Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/ | HTTP 200 and the requested home URL | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "home URL", "passed": true, "expected": "http://127.0.0.1:39175/en/", "actual": "http://127.0.0.1:39175/en/"}], "details": {}, "active_id": null} | PASS | [J01-en-a1-s1-state](evidence/J01-en-a1-s1-state.json), [J01-en-a1-s1-viewport](evidence/J01-en-a1-s1-viewport.png) |
| 2 | Inspect language and heading | Requested language and approved localized home heading | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/", "actual": "http://127.0.0.1:39175/en/"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "Welcome to Atlas Studio", "actual": "Welcome to Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J01-en-a1-s2-state](evidence/J01-en-a1-s2-state.json), [J01-en-a1-s2-viewport](evidence/J01-en-a1-s2-viewport.png) |
| 3 | Inspect canonical and alternate links | Current-route canonical without query and equivalent en/fr routes | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "canonical", "passed": true, "expected": "http://127.0.0.1:39175/en/", "actual": "http://127.0.0.1:39175/en/"}, {"check": "alternate en", "passed": true, "expected": "http://127.0.0.1:39175/en/", "actual": "http://127.0.0.1:39175/en/"}, {"check": "alternate fr", "passed": true, "expected": "http://127.0.0.1:39175/fr/", "actual": "http://127.0.0.1:39175/fr/"}], "details": {}, "active_id": null} | PASS | [J01-en-a1-s3-state](evidence/J01-en-a1-s3-state.json), [J01-en-a1-s3-viewport](evidence/J01-en-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J01-en-a1-s1-state", "J01-en-a1-s1-viewport", "J01-en-a1-s2-state", "J01-en-a1-s2-viewport", "J01-en-a1-s3-state", "J01-en-a1-s3-viewport", "J01-en-a1-network", "J01-en-a1-console", "J01-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J01-fr — Open the requested home page

- URL: http://127.0.0.1:39175/fr/
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:42.458Z → 2026-10-08T11:43:42.906Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/ | HTTP 200 and the requested home URL | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "home URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/", "actual": "http://127.0.0.1:39175/fr/"}], "details": {}, "active_id": null} | PASS | [J01-fr-a1-s1-state](evidence/J01-fr-a1-s1-state.json), [J01-fr-a1-s1-viewport](evidence/J01-fr-a1-s1-viewport.png) |
| 2 | Inspect language and heading | Requested language and approved localized home heading | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/", "actual": "http://127.0.0.1:39175/fr/"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": true, "expected": "Bienvenue chez Atlas Studio", "actual": "Bienvenue chez Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J01-fr-a1-s2-state](evidence/J01-fr-a1-s2-state.json), [J01-fr-a1-s2-viewport](evidence/J01-fr-a1-s2-viewport.png) |
| 3 | Inspect canonical and alternate links | Current-route canonical without query and equivalent en/fr routes | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "canonical", "passed": true, "expected": "http://127.0.0.1:39175/fr/", "actual": "http://127.0.0.1:39175/fr/"}, {"check": "alternate en", "passed": true, "expected": "http://127.0.0.1:39175/en/", "actual": "http://127.0.0.1:39175/en/"}, {"check": "alternate fr", "passed": true, "expected": "http://127.0.0.1:39175/fr/", "actual": "http://127.0.0.1:39175/fr/"}], "details": {}, "active_id": null} | PASS | [J01-fr-a1-s3-state](evidence/J01-fr-a1-s3-state.json), [J01-fr-a1-s3-viewport](evidence/J01-fr-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J01-fr-a1-s1-state", "J01-fr-a1-s1-viewport", "J01-fr-a1-s2-state", "J01-fr-a1-s2-viewport", "J01-fr-a1-s3-state", "J01-fr-a1-s3-viewport", "J01-fr-a1-network", "J01-fr-a1-console", "J01-fr-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J02-en — Follow primary navigation

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:42.990Z → 2026-10-08T11:43:43.529Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/ | HTTP 200 home page | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J02-en-a1-s1-state](evidence/J02-en-a1-s1-state.json), [J02-en-a1-s1-viewport](evidence/J02-en-a1-s1-viewport.png) |
| 2 | Click #main-about | Navigation actually occurs | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "navigation occurred", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J02-en-a1-s2-state](evidence/J02-en-a1-s2-state.json), [J02-en-a1-s2-viewport](evidence/J02-en-a1-s2-viewport.png) |
| 3 | Inspect the destination | Same-language /about, HTTP 200 and localized About heading | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J02-en-a1-s3-state](evidence/J02-en-a1-s3-state.json), [J02-en-a1-s3-viewport](evidence/J02-en-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J02-en-a1-s1-state", "J02-en-a1-s1-viewport", "J02-en-a1-s2-state", "J02-en-a1-s2-viewport", "J02-en-a1-s3-state", "J02-en-a1-s3-viewport", "J02-en-a1-network", "J02-en-a1-console", "J02-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J02-fr — Follow primary navigation

- URL: http://127.0.0.1:39175/fr/search
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:43.654Z → 2026-10-08T11:43:44.711Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/ | HTTP 200 home page | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J02-fr-a2-s1-state](evidence/J02-fr-a2-s1-state.json), [J02-fr-a2-s1-viewport](evidence/J02-fr-a2-s1-viewport.png) |
| 2 | Click #main-about | Navigation actually occurs | {"url": "http://127.0.0.1:39175/fr/search", "checks": [{"check": "navigation occurred", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J02-fr-a2-s2-state](evidence/J02-fr-a2-s2-state.json), [J02-fr-a2-s2-viewport](evidence/J02-fr-a2-s2-viewport.png) |
| 3 | Inspect the destination | Same-language /about, HTTP 200 and localized About heading | {"url": "http://127.0.0.1:39175/fr/search", "checks": [{"check": "URL", "passed": false, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/search"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": false, "expected": "À propos d’Atlas Studio", "actual": "Rechercher chez Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | FAIL | [J02-fr-a2-s3-state](evidence/J02-fr-a2-s3-state.json), [J02-fr-a2-s3-viewport](evidence/J02-fr-a2-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL", "evidence_ids": ["J02-fr-a1-s1-state", "J02-fr-a1-s1-viewport", "J02-fr-a1-s2-state", "J02-fr-a1-s2-viewport", "J02-fr-a1-s3-state", "J02-fr-a1-s3-viewport", "J02-fr-a1-network", "J02-fr-a1-console", "J02-fr-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL", "evidence_ids": ["J02-fr-a2-s1-state", "J02-fr-a2-s1-viewport", "J02-fr-a2-s2-state", "J02-fr-a2-s2-viewport", "J02-fr-a2-s3-state", "J02-fr-a2-s3-viewport", "J02-fr-a2-network", "J02-fr-a2-console", "J02-fr-a2-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J03-en — Switch language from an internal page

- URL: http://127.0.0.1:39175/fr/
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:44.796Z → 2026-10-08T11:43:46.069Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/about | HTTP 200 and localized About page | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J03-en-a2-s1-state](evidence/J03-en-a2-s1-state.json), [J03-en-a2-s1-viewport](evidence/J03-en-a2-s1-viewport.png) |
| 2 | Click #language-switch | Navigation actually occurs | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "navigation occurred", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J03-en-a2-s2-state](evidence/J03-en-a2-s2-state.json), [J03-en-a2-s2-viewport](evidence/J03-en-a2-s2-viewport.png) |
| 3 | Inspect destination route | Other-language /about route retains internal page | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "equivalent other-language route", "passed": false, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/"}], "details": {}, "active_id": null} | FAIL | [J03-en-a2-s3-state](evidence/J03-en-a2-s3-state.json), [J03-en-a2-s3-viewport](evidence/J03-en-a2-s3-viewport.png) |
| 4 | Inspect destination language and heading | Other-language document and localized About heading | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "URL", "passed": false, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": false, "expected": "À propos d’Atlas Studio", "actual": "Bienvenue chez Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | FAIL | [J03-en-a2-s4-state](evidence/J03-en-a2-s4-state.json), [J03-en-a2-s4-viewport](evidence/J03-en-a2-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 FAIL", "evidence_ids": ["J03-en-a1-s1-state", "J03-en-a1-s1-viewport", "J03-en-a1-s2-state", "J03-en-a1-s2-viewport", "J03-en-a1-s3-state", "J03-en-a1-s3-viewport", "J03-en-a1-s4-state", "J03-en-a1-s4-viewport", "J03-en-a1-network", "J03-en-a1-console", "J03-en-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 FAIL", "evidence_ids": ["J03-en-a2-s1-state", "J03-en-a2-s1-viewport", "J03-en-a2-s2-state", "J03-en-a2-s2-viewport", "J03-en-a2-s3-state", "J03-en-a2-s3-viewport", "J03-en-a2-s4-state", "J03-en-a2-s4-viewport", "J03-en-a2-network", "J03-en-a2-console", "J03-en-a2-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J03-fr — Switch language from an internal page

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:46.179Z → 2026-10-08T11:43:46.741Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/about | HTTP 200 and localized About page | {"url": "http://127.0.0.1:39175/fr/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/about"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": true, "expected": "À propos d’Atlas Studio", "actual": "À propos d’Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J03-fr-a1-s1-state](evidence/J03-fr-a1-s1-state.json), [J03-fr-a1-s1-viewport](evidence/J03-fr-a1-s1-viewport.png) |
| 2 | Click #language-switch | Navigation actually occurs | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "navigation occurred", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J03-fr-a1-s2-state](evidence/J03-fr-a1-s2-state.json), [J03-fr-a1-s2-viewport](evidence/J03-fr-a1-s2-viewport.png) |
| 3 | Inspect destination route | Other-language /about route retains internal page | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "equivalent other-language route", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}], "details": {}, "active_id": null} | PASS | [J03-fr-a1-s3-state](evidence/J03-fr-a1-s3-state.json), [J03-fr-a1-s3-viewport](evidence/J03-fr-a1-s3-viewport.png) |
| 4 | Inspect destination language and heading | Other-language document and localized About heading | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J03-fr-a1-s4-state](evidence/J03-fr-a1-s4-state.json), [J03-fr-a1-s4-viewport](evidence/J03-fr-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J03-fr-a1-s1-state", "J03-fr-a1-s1-viewport", "J03-fr-a1-s2-state", "J03-fr-a1-s2-viewport", "J03-fr-a1-s3-state", "J03-fr-a1-s3-viewport", "J03-fr-a1-s4-state", "J03-fr-a1-s4-viewport", "J03-fr-a1-network", "J03-fr-a1-console", "J03-fr-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J04-en — Follow a language-preserving redirect

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:46.850Z → 2026-10-08T11:43:47.235Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/legacy | Redirect occurs | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "redirect response captured", "passed": true, "expected": true, "actual": true}], "details": {"redirects": [{"at": "2026-10-08T11:43:46.865Z", "url": "http://127.0.0.1:39175/en/legacy", "status": 302, "resource_type": "document", "location": "/en/about", "redirected_from": null}]}, "active_id": null} | PASS | [J04-en-a1-s1-state](evidence/J04-en-a1-s1-state.json), [J04-en-a1-s1-viewport](evidence/J04-en-a1-s1-viewport.png) |
| 2 | Inspect the final document | Same-language /about and localized About heading | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J04-en-a1-s2-state](evidence/J04-en-a1-s2-state.json), [J04-en-a1-s2-viewport](evidence/J04-en-a1-s2-viewport.png) |
| 3 | Inspect redirect response | Initial HTTP 302, Location to same-language /about, final HTTP 200 | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "redirect HTTP status", "passed": true, "expected": 302, "actual": 302}, {"check": "redirect Location", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}], "details": {"redirects": [{"at": "2026-10-08T11:43:46.865Z", "url": "http://127.0.0.1:39175/en/legacy", "status": 302, "resource_type": "document", "location": "/en/about", "redirected_from": null}]}, "active_id": null} | PASS | [J04-en-a1-s3-state](evidence/J04-en-a1-s3-state.json), [J04-en-a1-s3-viewport](evidence/J04-en-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J04-en-a1-s1-state", "J04-en-a1-s1-viewport", "J04-en-a1-s2-state", "J04-en-a1-s2-viewport", "J04-en-a1-s3-state", "J04-en-a1-s3-viewport", "J04-en-a1-network", "J04-en-a1-console", "J04-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J04-fr — Follow a language-preserving redirect

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:47.357Z → 2026-10-08T11:43:52.855Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/legacy | The redirect occurs and can be inspected. | The browser navigated to /fr/legacy and captured the redirect response plus rendered destination DOM. Its screenshot then timed out. Actual DOM and network remain available; no second screenshot is claimed. | PASS | [J04-fr-a2-s1-state](evidence/J04-fr-a2-s1-state.json), [J04-fr-a2-network](evidence/J04-fr-a2-network.json) |
| 2 | Inspect the final document captured by the browser | Same-language /fr/about with html[lang]=fr and heading À propos d’Atlas Studio. | Independent post-capture inspection of the actual second-attempt DOM: URL http://127.0.0.1:39175/en/about, html[lang]=en, heading About Atlas Studio. This assessment requires no new navigation or interaction. | FAIL | [J04-fr-a2-s1-state](evidence/J04-fr-a2-s1-state.json), [J04-fr-a2-network](evidence/J04-fr-a2-network.json) |
| 3 | Inspect the captured redirect response | HTTP 302 Location /fr/about, then HTTP 200. | Independent post-capture inspection: /fr/legacy returned HTTP 302 with Location /en/about; /en/about returned HTTP 200. The requested French language was lost. | FAIL | [J04-fr-a2-network](evidence/J04-fr-a2-network.json) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 FAIL, 3 FAIL", "evidence_ids": ["J04-fr-a1-s1-state", "J04-fr-a1-s1-viewport", "J04-fr-a1-s2-state", "J04-fr-a1-s2-viewport", "J04-fr-a1-s3-state", "J04-fr-a1-s3-viewport", "J04-fr-a1-network", "J04-fr-a1-console", "J04-fr-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Post-capture adjudication of retained DOM/network confirms the same wrong-language redirect as attempt 1. The automatic driver stopped at screenshot capture, so its raw attempt record remains a tooling incident; no later browser actions or second screenshot are claimed.", "evidence_ids": ["J04-fr-a2-network", "J04-fr-a2-console", "J04-fr-a2-attempt", "J04-fr-a2-s1-state"]}]

**Limitations**

- Attempt 2 encountered a screenshot timeout after navigation, DOM capture and network capture had completed. Raw observations.json and the raw attempt artifact remain unchanged.
- Reviewed step 2 and step 3 inspect already captured evidence; they are not a third browser attempt. First-attempt screenshots remain the visual proof.
- Browser/driver incident: TimeoutError: Page.screenshot: Timeout 5000ms exceeded.
Call log:
  - taking page screenshot
  - waiting for fonts to load...
  - fonts loaded


**Uncertainties**

None

### J05-en — Search with a matching result

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:52.951Z → 2026-10-08T11:43:53.657Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/search | HTTP 200 search page | {"url": "http://127.0.0.1:39175/en/search", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J05-en-a1-s1-state](evidence/J05-en-a1-s1-state.json), [J05-en-a1-s1-viewport](evidence/J05-en-a1-s1-viewport.png) |
| 2 | Type atlas in #search-query and click #search-submit | Submitted query stays visible | {"url": "http://127.0.0.1:39175/en/search?q=atlas", "checks": [{"check": "query retained", "passed": true, "expected": "atlas", "actual": "atlas"}], "details": {}, "active_id": null} | PASS | [J05-en-a1-s2-state](evidence/J05-en-a1-s2-state.json), [J05-en-a1-s2-viewport](evidence/J05-en-a1-s2-viewport.png) |
| 3 | Inspect search results | Exactly one localized result and no empty state | {"url": "http://127.0.0.1:39175/en/search?q=atlas", "checks": [{"check": "result count", "passed": true, "expected": 1, "actual": 1}, {"check": "empty state absent", "passed": true, "expected": false, "actual": false}, {"check": "result title", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}], "details": {}, "active_id": null} | PASS | [J05-en-a1-s3-state](evidence/J05-en-a1-s3-state.json), [J05-en-a1-s3-viewport](evidence/J05-en-a1-s3-viewport.png) |
| 4 | Click #result-about | Same-language /about and localized About heading | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J05-en-a1-s4-state](evidence/J05-en-a1-s4-state.json), [J05-en-a1-s4-viewport](evidence/J05-en-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J05-en-a1-s1-state", "J05-en-a1-s1-viewport", "J05-en-a1-s2-state", "J05-en-a1-s2-viewport", "J05-en-a1-s3-state", "J05-en-a1-s3-viewport", "J05-en-a1-s4-state", "J05-en-a1-s4-viewport", "J05-en-a1-network", "J05-en-a1-console", "J05-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J05-fr — Search with a matching result

- URL: http://127.0.0.1:39175/fr/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:53.776Z → 2026-10-08T11:43:54.492Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/search | HTTP 200 search page | {"url": "http://127.0.0.1:39175/fr/search", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J05-fr-a1-s1-state](evidence/J05-fr-a1-s1-state.json), [J05-fr-a1-s1-viewport](evidence/J05-fr-a1-s1-viewport.png) |
| 2 | Type atlas in #search-query and click #search-submit | Submitted query stays visible | {"url": "http://127.0.0.1:39175/fr/search?q=atlas", "checks": [{"check": "query retained", "passed": true, "expected": "atlas", "actual": "atlas"}], "details": {}, "active_id": null} | PASS | [J05-fr-a1-s2-state](evidence/J05-fr-a1-s2-state.json), [J05-fr-a1-s2-viewport](evidence/J05-fr-a1-s2-viewport.png) |
| 3 | Inspect search results | Exactly one localized result and no empty state | {"url": "http://127.0.0.1:39175/fr/search?q=atlas", "checks": [{"check": "result count", "passed": true, "expected": 1, "actual": 1}, {"check": "empty state absent", "passed": true, "expected": false, "actual": false}, {"check": "result title", "passed": true, "expected": "À propos d’Atlas Studio", "actual": "À propos d’Atlas Studio"}], "details": {}, "active_id": null} | PASS | [J05-fr-a1-s3-state](evidence/J05-fr-a1-s3-state.json), [J05-fr-a1-s3-viewport](evidence/J05-fr-a1-s3-viewport.png) |
| 4 | Click #result-about | Same-language /about and localized About heading | {"url": "http://127.0.0.1:39175/fr/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/about"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": true, "expected": "À propos d’Atlas Studio", "actual": "À propos d’Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J05-fr-a1-s4-state](evidence/J05-fr-a1-s4-state.json), [J05-fr-a1-s4-viewport](evidence/J05-fr-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J05-fr-a1-s1-state", "J05-fr-a1-s1-viewport", "J05-fr-a1-s2-state", "J05-fr-a1-s2-viewport", "J05-fr-a1-s3-state", "J05-fr-a1-s3-viewport", "J05-fr-a1-s4-state", "J05-fr-a1-s4-viewport", "J05-fr-a1-network", "J05-fr-a1-console", "J05-fr-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J06-en — Search with no matching result

- URL: http://127.0.0.1:39175/en/search?q=zzzz-no-match
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:54.571Z → 2026-10-08T11:43:55.101Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/search | HTTP 200 search page | {"url": "http://127.0.0.1:39175/en/search", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J06-en-a1-s1-state](evidence/J06-en-a1-s1-state.json), [J06-en-a1-s1-viewport](evidence/J06-en-a1-s1-viewport.png) |
| 2 | Type zzzz-no-match and click #search-submit | Submitted query stays visible | {"url": "http://127.0.0.1:39175/en/search?q=zzzz-no-match", "checks": [{"check": "query retained", "passed": true, "expected": "zzzz-no-match", "actual": "zzzz-no-match"}], "details": {}, "active_id": null} | PASS | [J06-en-a1-s2-state](evidence/J06-en-a1-s2-state.json), [J06-en-a1-s2-viewport](evidence/J06-en-a1-s2-viewport.png) |
| 3 | Inspect the empty state | Zero results, visible approved localized empty-state text | {"url": "http://127.0.0.1:39175/en/search?q=zzzz-no-match", "checks": [{"check": "result count", "passed": true, "expected": 0, "actual": 0}, {"check": "query retained", "passed": true, "expected": "zzzz-no-match", "actual": "zzzz-no-match"}, {"check": "empty state visible", "passed": true, "expected": true, "actual": true}, {"check": "localized empty message", "passed": true, "expected": "No results found.", "actual": "No results found."}], "details": {}, "active_id": null} | PASS | [J06-en-a1-s3-state](evidence/J06-en-a1-s3-state.json), [J06-en-a1-s3-viewport](evidence/J06-en-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J06-en-a1-s1-state", "J06-en-a1-s1-viewport", "J06-en-a1-s2-state", "J06-en-a1-s2-viewport", "J06-en-a1-s3-state", "J06-en-a1-s3-viewport", "J06-en-a1-network", "J06-en-a1-console", "J06-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J06-fr — Search with no matching result

- URL: http://127.0.0.1:39175/fr/search?q=zzzz-no-match
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:55.200Z → 2026-10-08T11:43:55.772Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/search | HTTP 200 search page | {"url": "http://127.0.0.1:39175/fr/search", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J06-fr-a1-s1-state](evidence/J06-fr-a1-s1-state.json), [J06-fr-a1-s1-viewport](evidence/J06-fr-a1-s1-viewport.png) |
| 2 | Type zzzz-no-match and click #search-submit | Submitted query stays visible | {"url": "http://127.0.0.1:39175/fr/search?q=zzzz-no-match", "checks": [{"check": "query retained", "passed": true, "expected": "zzzz-no-match", "actual": "zzzz-no-match"}], "details": {}, "active_id": null} | PASS | [J06-fr-a1-s2-state](evidence/J06-fr-a1-s2-state.json), [J06-fr-a1-s2-viewport](evidence/J06-fr-a1-s2-viewport.png) |
| 3 | Inspect the empty state | Zero results, visible approved localized empty-state text | {"url": "http://127.0.0.1:39175/fr/search?q=zzzz-no-match", "checks": [{"check": "result count", "passed": true, "expected": 0, "actual": 0}, {"check": "query retained", "passed": true, "expected": "zzzz-no-match", "actual": "zzzz-no-match"}, {"check": "empty state visible", "passed": true, "expected": true, "actual": true}, {"check": "localized empty message", "passed": true, "expected": "Aucun résultat.", "actual": "Aucun résultat."}], "details": {}, "active_id": null} | PASS | [J06-fr-a1-s3-state](evidence/J06-fr-a1-s3-state.json), [J06-fr-a1-s3-viewport](evidence/J06-fr-a1-s3-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS", "evidence_ids": ["J06-fr-a1-s1-state", "J06-fr-a1-s1-viewport", "J06-fr-a1-s2-state", "J06-fr-a1-s2-viewport", "J06-fr-a1-s3-state", "J06-fr-a1-s3-viewport", "J06-fr-a1-network", "J06-fr-a1-console", "J06-fr-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J07-en — Submit an invalid local form

- URL: http://127.0.0.1:39175/en/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:55.853Z → 2026-10-08T11:43:56.415Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/contact | HTTP 200 and both fields empty | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "contact-name initially empty", "passed": true, "expected": "", "actual": ""}, {"check": "contact-email initially empty", "passed": true, "expected": "", "actual": ""}], "details": {}, "active_id": null} | PASS | [J07-en-a1-s1-state](evidence/J07-en-a1-s1-state.json), [J07-en-a1-s1-viewport](evidence/J07-en-a1-s1-viewport.png) |
| 2 | Click #contact-submit | Local validation runs | {"url": "http://127.0.0.1:39175/en/contact", "checks": [], "details": {"actual_action": "Clicked local form submit once with empty fields."}, "active_id": "contact-submit"} | PASS | [J07-en-a1-s2-state](evidence/J07-en-a1-s2-state.json), [J07-en-a1-s2-viewport](evidence/J07-en-a1-s2-viewport.png) |
| 3 | Inspect field validity and confirmation | Both errors visible, aria-invalid true on both fields, confirmation hidden | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "name-error visible", "passed": true, "expected": true, "actual": true}, {"check": "email-error visible", "passed": true, "expected": true, "actual": true}, {"check": "contact-name aria-invalid", "passed": true, "expected": "true", "actual": "true"}, {"check": "contact-email aria-invalid", "passed": true, "expected": "true", "actual": "true"}, {"check": "confirmation hidden", "passed": true, "expected": false, "actual": false}], "details": {}, "active_id": "contact-submit"} | PASS | [J07-en-a1-s3-state](evidence/J07-en-a1-s3-state.json), [J07-en-a1-s3-viewport](evidence/J07-en-a1-s3-viewport.png) |
| 4 | Read validation errors | Both approved error messages use the page language | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "name error copy", "passed": true, "expected": "Enter your name.", "actual": "Enter your name."}, {"check": "email error copy", "passed": true, "expected": "Enter a valid email address.", "actual": "Enter a valid email address."}], "details": {}, "active_id": "contact-submit"} | PASS | [J07-en-a1-s4-state](evidence/J07-en-a1-s4-state.json), [J07-en-a1-s4-viewport](evidence/J07-en-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J07-en-a1-s1-state", "J07-en-a1-s1-viewport", "J07-en-a1-s2-state", "J07-en-a1-s2-viewport", "J07-en-a1-s3-state", "J07-en-a1-s3-viewport", "J07-en-a1-s4-state", "J07-en-a1-s4-viewport", "J07-en-a1-network", "J07-en-a1-console", "J07-en-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J07-fr — Submit an invalid local form

- URL: http://127.0.0.1:39175/fr/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:56.495Z → 2026-10-08T11:43:57.733Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/contact | HTTP 200 and both fields empty | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "contact-name initially empty", "passed": true, "expected": "", "actual": ""}, {"check": "contact-email initially empty", "passed": true, "expected": "", "actual": ""}], "details": {}, "active_id": null} | PASS | [J07-fr-a2-s1-state](evidence/J07-fr-a2-s1-state.json), [J07-fr-a2-s1-viewport](evidence/J07-fr-a2-s1-viewport.png) |
| 2 | Click #contact-submit | Local validation runs | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [], "details": {"actual_action": "Clicked local form submit once with empty fields."}, "active_id": "contact-submit"} | PASS | [J07-fr-a2-s2-state](evidence/J07-fr-a2-s2-state.json), [J07-fr-a2-s2-viewport](evidence/J07-fr-a2-s2-viewport.png) |
| 3 | Inspect field validity and confirmation | Both errors visible, aria-invalid true on both fields, confirmation hidden | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "name-error visible", "passed": true, "expected": true, "actual": true}, {"check": "email-error visible", "passed": true, "expected": true, "actual": true}, {"check": "contact-name aria-invalid", "passed": true, "expected": "true", "actual": "true"}, {"check": "contact-email aria-invalid", "passed": true, "expected": "true", "actual": "true"}, {"check": "confirmation hidden", "passed": true, "expected": false, "actual": false}], "details": {}, "active_id": "contact-submit"} | PASS | [J07-fr-a2-s3-state](evidence/J07-fr-a2-s3-state.json), [J07-fr-a2-s3-viewport](evidence/J07-fr-a2-s3-viewport.png) |
| 4 | Read validation errors | Both approved error messages use the page language | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "name error copy", "passed": false, "expected": "Saisissez votre nom.", "actual": "Enter your name."}, {"check": "email error copy", "passed": false, "expected": "Saisissez une adresse e-mail valide.", "actual": "Enter a valid email address."}], "details": {}, "active_id": "contact-submit"} | FAIL | [J07-fr-a2-s4-state](evidence/J07-fr-a2-s4-state.json), [J07-fr-a2-s4-viewport](evidence/J07-fr-a2-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 FAIL", "evidence_ids": ["J07-fr-a1-s1-state", "J07-fr-a1-s1-viewport", "J07-fr-a1-s2-state", "J07-fr-a1-s2-viewport", "J07-fr-a1-s3-state", "J07-fr-a1-s3-viewport", "J07-fr-a1-s4-state", "J07-fr-a1-s4-viewport", "J07-fr-a1-network", "J07-fr-a1-console", "J07-fr-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 FAIL", "evidence_ids": ["J07-fr-a2-s1-state", "J07-fr-a2-s1-viewport", "J07-fr-a2-s2-state", "J07-fr-a2-s2-viewport", "J07-fr-a2-s3-state", "J07-fr-a2-s3-viewport", "J07-fr-a2-s4-state", "J07-fr-a2-s4-viewport", "J07-fr-a2-network", "J07-fr-a2-console", "J07-fr-a2-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J08-en — Complete the local form using the keyboard

- URL: http://127.0.0.1:39175/en/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:57.829Z → 2026-10-08T11:43:58.953Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/contact | HTTP 200 with visible associated labels | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "contact-name has visible associated label", "passed": true, "expected": true, "actual": true}, {"check": "contact-email has visible associated label", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J08-en-a2-s1-state](evidence/J08-en-a2-s1-state.json), [J08-en-a2-s1-viewport](evidence/J08-en-a2-s1-viewport.png) |
| 2 | Focus #contact-name, type Alex Test and press Tab once | Actual keyboard input and Tab event | {"url": "http://127.0.0.1:39175/en/contact", "checks": [], "details": {"key_sequence": ["focus #contact-name", "type Alex Test", "Tab"]}, "active_id": "contact-submit"} | PASS | [J08-en-a2-s2-state](evidence/J08-en-a2-s2-state.json), [J08-en-a2-s2-viewport](evidence/J08-en-a2-s2-viewport.png) |
| 3 | Inspect focus | #contact-email focused with a visible outline | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "active element after first Tab", "passed": false, "expected": "contact-email", "actual": "contact-submit"}, {"check": "email visible focus outline", "passed": false, "expected": true, "actual": false}], "details": {"email_outline": {"style": "none", "width": "3px", "color": "rgb(0, 0, 0)"}}, "active_id": "contact-submit"} | FAIL | [J08-en-a2-s3-state](evidence/J08-en-a2-s3-state.json), [J08-en-a2-s3-viewport](evidence/J08-en-a2-s3-viewport.png) |
| 4 | Type alex@example.test, press Tab once and Enter | #contact-submit focused before Enter | Not executed: the first Tab skipped the required email field. No direct fill or click workaround was used. | NOT_RUN | None |
| 5 | Inspect confirmation | Approved localized confirmation visible with no visible validation errors | Not executed: the contracted keyboard submission could not continue after the failed focus transition. | NOT_RUN | None |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 NOT_RUN, 5 NOT_RUN", "evidence_ids": ["J08-en-a1-s1-state", "J08-en-a1-s1-viewport", "J08-en-a1-s2-state", "J08-en-a1-s2-viewport", "J08-en-a1-s3-state", "J08-en-a1-s3-viewport", "J08-en-a1-network", "J08-en-a1-console", "J08-en-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 NOT_RUN, 5 NOT_RUN", "evidence_ids": ["J08-en-a2-s1-state", "J08-en-a2-s1-viewport", "J08-en-a2-s2-state", "J08-en-a2-s2-viewport", "J08-en-a2-s3-state", "J08-en-a2-s3-viewport", "J08-en-a2-network", "J08-en-a2-console", "J08-en-a2-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J08-fr — Complete the local form using the keyboard

- URL: http://127.0.0.1:39175/fr/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:59.071Z → 2026-10-08T11:43:59.877Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/contact | HTTP 200 with visible associated labels | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "contact-name has visible associated label", "passed": true, "expected": true, "actual": true}, {"check": "contact-email has visible associated label", "passed": true, "expected": true, "actual": true}], "details": {}, "active_id": null} | PASS | [J08-fr-a1-s1-state](evidence/J08-fr-a1-s1-state.json), [J08-fr-a1-s1-viewport](evidence/J08-fr-a1-s1-viewport.png) |
| 2 | Focus #contact-name, type Alex Test and press Tab once | Actual keyboard input and Tab event | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [], "details": {"key_sequence": ["focus #contact-name", "type Alex Test", "Tab"]}, "active_id": "contact-email"} | PASS | [J08-fr-a1-s2-state](evidence/J08-fr-a1-s2-state.json), [J08-fr-a1-s2-viewport](evidence/J08-fr-a1-s2-viewport.png) |
| 3 | Inspect focus | #contact-email focused with a visible outline | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "active element after first Tab", "passed": true, "expected": "contact-email", "actual": "contact-email"}, {"check": "email visible focus outline", "passed": true, "expected": true, "actual": true}], "details": {"email_outline": {"style": "solid", "width": "3px", "color": "rgb(195, 79, 0)"}}, "active_id": "contact-email"} | PASS | [J08-fr-a1-s3-state](evidence/J08-fr-a1-s3-state.json), [J08-fr-a1-s3-viewport](evidence/J08-fr-a1-s3-viewport.png) |
| 4 | Type alex@example.test, press Tab once and Enter | #contact-submit focused before Enter | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "active element after second Tab", "passed": true, "expected": "contact-submit", "actual": "contact-submit"}], "details": {"key_sequence": ["type alex@example.test", "Tab", "Enter"], "active_before_enter": "contact-submit"}, "active_id": "contact-submit"} | PASS | [J08-fr-a1-s4-state](evidence/J08-fr-a1-s4-state.json), [J08-fr-a1-s4-viewport](evidence/J08-fr-a1-s4-viewport.png) |
| 5 | Inspect confirmation | Approved localized confirmation visible with no visible validation errors | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "confirmation visible", "passed": true, "expected": true, "actual": true}, {"check": "localized confirmation", "passed": true, "expected": "Merci, Alex Test. Votre demande locale est confirmée.", "actual": "Merci, Alex Test. Votre demande locale est confirmée."}, {"check": "name-error hidden", "passed": true, "expected": false, "actual": false}, {"check": "email-error hidden", "passed": true, "expected": false, "actual": false}], "details": {}, "active_id": "contact-submit"} | PASS | [J08-fr-a1-s5-state](evidence/J08-fr-a1-s5-state.json), [J08-fr-a1-s5-viewport](evidence/J08-fr-a1-s5-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS, 5 PASS", "evidence_ids": ["J08-fr-a1-s1-state", "J08-fr-a1-s1-viewport", "J08-fr-a1-s2-state", "J08-fr-a1-s2-viewport", "J08-fr-a1-s3-state", "J08-fr-a1-s3-viewport", "J08-fr-a1-s4-state", "J08-fr-a1-s4-viewport", "J08-fr-a1-s5-state", "J08-fr-a1-s5-viewport", "J08-fr-a1-network", "J08-fr-a1-console", "J08-fr-a1-attempt"]}]

**Limitations**

None

**Uncertainties**

None

### J09-en — Open, use, and close the mobile menu

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:43:59.979Z → 2026-10-08T11:44:00.576Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/ at 390 by 844 | Toggle visible, panel hidden, aria-expanded false | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "toggle visible", "passed": true, "expected": true, "actual": true}, {"check": "panel hidden", "passed": true, "expected": false, "actual": false}, {"check": "aria-expanded", "passed": true, "expected": "false", "actual": "false"}], "details": {}, "active_id": null} | PASS | [J09-en-a1-s1-state](evidence/J09-en-a1-s1-state.json), [J09-en-a1-s1-viewport](evidence/J09-en-a1-s1-viewport.png) |
| 2 | Click #menu-toggle | Panel visible and aria-expanded true | {"url": "http://127.0.0.1:39175/en/", "checks": [{"check": "panel visible", "passed": true, "expected": true, "actual": true}, {"check": "aria-expanded", "passed": true, "expected": "true", "actual": "true"}], "details": {}, "active_id": "menu-toggle"} | PASS | [J09-en-a1-s2-state](evidence/J09-en-a1-s2-state.json), [J09-en-a1-s2-viewport](evidence/J09-en-a1-s2-viewport.png) |
| 3 | Click #mobile-about | Same-language /about with localized heading and closed menu | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/about", "actual": "http://127.0.0.1:39175/en/about"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "localized heading", "passed": true, "expected": "About Atlas Studio", "actual": "About Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "panel closed after navigation", "passed": true, "expected": false, "actual": false}], "details": {}, "active_id": null} | PASS | [J09-en-a1-s3-state](evidence/J09-en-a1-s3-state.json), [J09-en-a1-s3-viewport](evidence/J09-en-a1-s3-viewport.png) |
| 4 | Reopen menu and press Escape | Panel hidden, aria-expanded false, focus returns to toggle | {"url": "http://127.0.0.1:39175/en/about", "checks": [{"check": "panel hidden after Escape", "passed": true, "expected": false, "actual": false}, {"check": "aria-expanded after Escape", "passed": true, "expected": "false", "actual": "false"}, {"check": "focus returned to toggle", "passed": true, "expected": "menu-toggle", "actual": "menu-toggle"}], "details": {"reopened_with_toggle": true, "before_escape_panel_visible": true, "keys": ["Escape"]}, "active_id": "menu-toggle"} | PASS | [J09-en-a1-s4-state](evidence/J09-en-a1-s4-state.json), [J09-en-a1-s4-viewport](evidence/J09-en-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J09-en-a1-s1-state", "J09-en-a1-s1-viewport", "J09-en-a1-s2-state", "J09-en-a1-s2-viewport", "J09-en-a1-s3-state", "J09-en-a1-s3-viewport", "J09-en-a1-s4-state", "J09-en-a1-s4-viewport", "J09-en-a1-network", "J09-en-a1-console", "J09-en-a1-attempt"]}]

**Limitations**

- Mobile profile is viewport emulation only; is_mobile false and has_touch false.

**Uncertainties**

None

### J09-fr — Open, use, and close the mobile menu

- URL: http://127.0.0.1:39175/fr/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:44:00.763Z → 2026-10-08T11:44:01.487Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/ at 390 by 844 | Toggle visible, panel hidden, aria-expanded false | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "toggle visible", "passed": true, "expected": true, "actual": true}, {"check": "panel hidden", "passed": true, "expected": false, "actual": false}, {"check": "aria-expanded", "passed": true, "expected": "false", "actual": "false"}], "details": {}, "active_id": null} | PASS | [J09-fr-a1-s1-state](evidence/J09-fr-a1-s1-state.json), [J09-fr-a1-s1-viewport](evidence/J09-fr-a1-s1-viewport.png) |
| 2 | Click #menu-toggle | Panel visible and aria-expanded true | {"url": "http://127.0.0.1:39175/fr/", "checks": [{"check": "panel visible", "passed": true, "expected": true, "actual": true}, {"check": "aria-expanded", "passed": true, "expected": "true", "actual": "true"}], "details": {}, "active_id": "menu-toggle"} | PASS | [J09-fr-a1-s2-state](evidence/J09-fr-a1-s2-state.json), [J09-fr-a1-s2-viewport](evidence/J09-fr-a1-s2-viewport.png) |
| 3 | Click #mobile-about | Same-language /about with localized heading and closed menu | {"url": "http://127.0.0.1:39175/fr/about", "checks": [{"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/about", "actual": "http://127.0.0.1:39175/fr/about"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "localized heading", "passed": true, "expected": "À propos d’Atlas Studio", "actual": "À propos d’Atlas Studio"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}, {"check": "panel closed after navigation", "passed": true, "expected": false, "actual": false}], "details": {}, "active_id": null} | PASS | [J09-fr-a1-s3-state](evidence/J09-fr-a1-s3-state.json), [J09-fr-a1-s3-viewport](evidence/J09-fr-a1-s3-viewport.png) |
| 4 | Reopen menu and press Escape | Panel hidden, aria-expanded false, focus returns to toggle | {"url": "http://127.0.0.1:39175/fr/about", "checks": [{"check": "panel hidden after Escape", "passed": true, "expected": false, "actual": false}, {"check": "aria-expanded after Escape", "passed": true, "expected": "false", "actual": "false"}, {"check": "focus returned to toggle", "passed": true, "expected": "menu-toggle", "actual": "menu-toggle"}], "details": {"reopened_with_toggle": true, "before_escape_panel_visible": true, "keys": ["Escape"]}, "active_id": "menu-toggle"} | PASS | [J09-fr-a1-s4-state](evidence/J09-fr-a1-s4-state.json), [J09-fr-a1-s4-viewport](evidence/J09-fr-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J09-fr-a1-s1-state", "J09-fr-a1-s1-viewport", "J09-fr-a1-s2-state", "J09-fr-a1-s2-viewport", "J09-fr-a1-s3-state", "J09-fr-a1-s3-viewport", "J09-fr-a1-s4-state", "J09-fr-a1-s4-viewport", "J09-fr-a1-network", "J09-fr-a1-console", "J09-fr-a1-attempt"]}]

**Limitations**

- Mobile profile is viewport emulation only; is_mobile false and has_touch false.

**Uncertainties**

None

### J10-en — Read a localized offer on mobile

- URL: http://127.0.0.1:39175/en/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:44:01.586Z → 2026-10-08T11:44:02.154Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /en/offer at 390 by 844 | HTTP 200 offer page | {"url": "http://127.0.0.1:39175/en/offer", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J10-en-a1-s1-state](evidence/J10-en-a1-s1-state.json), [J10-en-a1-s1-viewport](evidence/J10-en-a1-s1-viewport.png) |
| 2 | Read offer title, price, date and CTA | Approved localized offer strings | {"url": "http://127.0.0.1:39175/en/offer", "checks": [{"check": "offer-title", "passed": true, "expected": "Starter plan", "actual": "Starter plan"}, {"check": "offer-price", "passed": true, "expected": "€19.90 / month", "actual": "€19.90 / month"}, {"check": "offer-date", "passed": true, "expected": "October 8, 2026", "actual": "October 8, 2026"}, {"check": "offer-cta", "passed": true, "expected": "Contact us", "actual": "Contact us"}], "details": {}, "active_id": null} | PASS | [J10-en-a1-s2-state](evidence/J10-en-a1-s2-state.json), [J10-en-a1-s2-viewport](evidence/J10-en-a1-s2-viewport.png) |
| 3 | Measure horizontal page overflow | Document scrollWidth <= window.innerWidth + 1 | {"url": "http://127.0.0.1:39175/en/offer", "checks": [{"check": "horizontal overflow", "passed": true, "expected": "scrollWidth <= innerWidth + 1", "actual": {"scrollWidth": 390, "innerWidth": 390}}], "details": {}, "active_id": null} | PASS | [J10-en-a1-s3-state](evidence/J10-en-a1-s3-state.json), [J10-en-a1-s3-viewport](evidence/J10-en-a1-s3-viewport.png) |
| 4 | Click #offer-cta | CTA visible within viewport, actually clickable, reaches same-language /contact | {"url": "http://127.0.0.1:39175/en/contact", "checks": [{"check": "CTA initially within viewport", "passed": true, "expected": true, "actual": true}, {"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/en/contact", "actual": "http://127.0.0.1:39175/en/contact"}, {"check": "html language", "passed": true, "expected": "en", "actual": "en"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {"cta_before_click": {"present": true, "text": "Contact us", "value": null, "visible": true, "href": "/en/contact", "aria_invalid": null, "aria_expanded": null, "tabindex": null, "disabled": false, "rect": {"x": 33, "y": 494.578125, "width": 125.1875, "height": 49.875, "right": 158.1875, "bottom": 544.453125}, "outline": {"style": "none", "width": "3px", "color": "rgb(255, 255, 255)"}, "box_shadow": "none", "labels": []}, "viewport_before_click": {"width": 390, "height": 844}, "actual_click": true}, "active_id": null} | PASS | [J10-en-a1-s4-state](evidence/J10-en-a1-s4-state.json), [J10-en-a1-s4-viewport](evidence/J10-en-a1-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "PASS", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 PASS, 4 PASS", "evidence_ids": ["J10-en-a1-s1-state", "J10-en-a1-s1-viewport", "J10-en-a1-s2-state", "J10-en-a1-s2-viewport", "J10-en-a1-s3-state", "J10-en-a1-s3-viewport", "J10-en-a1-s4-state", "J10-en-a1-s4-viewport", "J10-en-a1-network", "J10-en-a1-console", "J10-en-a1-attempt"]}]

**Limitations**

- Mobile profile is viewport emulation only; is_mobile false and has_touch false.

**Uncertainties**

None

### J10-fr — Read a localized offer on mobile

- URL: http://127.0.0.1:39175/fr/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T11:44:02.246Z → 2026-10-08T11:44:03.493Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No geographic verification requested."}

**Preconditions**

- Fresh browser context for each recorded attempt.
- Authorized loopback synthetic fixture; no authentication.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open /fr/offer at 390 by 844 | HTTP 200 offer page | {"url": "http://127.0.0.1:39175/fr/offer", "checks": [{"check": "HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {}, "active_id": null} | PASS | [J10-fr-a2-s1-state](evidence/J10-fr-a2-s1-state.json), [J10-fr-a2-s1-viewport](evidence/J10-fr-a2-s1-viewport.png) |
| 2 | Read offer title, price, date and CTA | Approved localized offer strings | {"url": "http://127.0.0.1:39175/fr/offer", "checks": [{"check": "offer-title", "passed": true, "expected": "Offre Découverte", "actual": "Offre Découverte"}, {"check": "offer-price", "passed": true, "expected": "19,90 € / mois", "actual": "19,90 € / mois"}, {"check": "offer-date", "passed": true, "expected": "8 octobre 2026", "actual": "8 octobre 2026"}, {"check": "offer-cta", "passed": true, "expected": "Contactez-nous", "actual": "Contactez-nous"}], "details": {}, "active_id": null} | PASS | [J10-fr-a2-s2-state](evidence/J10-fr-a2-s2-state.json), [J10-fr-a2-s2-viewport](evidence/J10-fr-a2-s2-viewport.png) |
| 3 | Measure horizontal page overflow | Document scrollWidth <= window.innerWidth + 1 | {"url": "http://127.0.0.1:39175/fr/offer", "checks": [{"check": "horizontal overflow", "passed": false, "expected": "scrollWidth <= innerWidth + 1", "actual": {"scrollWidth": 556, "innerWidth": 390}}], "details": {}, "active_id": null} | FAIL | [J10-fr-a2-s3-state](evidence/J10-fr-a2-s3-state.json), [J10-fr-a2-s3-viewport](evidence/J10-fr-a2-s3-viewport.png) |
| 4 | Click #offer-cta | CTA visible within viewport, actually clickable, reaches same-language /contact | {"url": "http://127.0.0.1:39175/fr/contact", "checks": [{"check": "CTA initially within viewport", "passed": true, "expected": true, "actual": true}, {"check": "URL", "passed": true, "expected": "http://127.0.0.1:39175/fr/contact", "actual": "http://127.0.0.1:39175/fr/contact"}, {"check": "html language", "passed": true, "expected": "fr", "actual": "fr"}, {"check": "last document HTTP status", "passed": true, "expected": 200, "actual": 200}], "details": {"cta_before_click": {"present": true, "text": "Contactez-nous", "value": null, "visible": true, "href": "/fr/contact", "aria_invalid": null, "aria_expanded": null, "tabindex": null, "disabled": false, "rect": {"x": 33, "y": 469.078125, "width": 166.46875, "height": 49.875, "right": 199.46875, "bottom": 518.953125}, "outline": {"style": "none", "width": "3px", "color": "rgb(255, 255, 255)"}, "box_shadow": "none", "labels": []}, "viewport_before_click": {"width": 390, "height": 844}, "actual_click": true}, "active_id": null} | PASS | [J10-fr-a2-s4-state](evidence/J10-fr-a2-s4-state.json), [J10-fr-a2-s4-viewport](evidence/J10-fr-a2-s4-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 PASS", "evidence_ids": ["J10-fr-a1-s1-state", "J10-fr-a1-s1-viewport", "J10-fr-a1-s2-state", "J10-fr-a1-s2-viewport", "J10-fr-a1-s3-state", "J10-fr-a1-s3-viewport", "J10-fr-a1-s4-state", "J10-fr-a1-s4-viewport", "J10-fr-a1-network", "J10-fr-a1-console", "J10-fr-a1-attempt"]}, {"number": 2, "status": "FAIL", "observed": "Actual step outcomes: 1 PASS, 2 PASS, 3 FAIL, 4 PASS", "evidence_ids": ["J10-fr-a2-s1-state", "J10-fr-a2-s1-viewport", "J10-fr-a2-s2-state", "J10-fr-a2-s2-viewport", "J10-fr-a2-s3-state", "J10-fr-a2-s3-viewport", "J10-fr-a2-s4-state", "J10-fr-a2-s4-viewport", "J10-fr-a2-network", "J10-fr-a2-console", "J10-fr-a2-attempt"]}]

**Limitations**

- Mobile profile is viewport emulation only; is_mobile false and has_touch false.

**Uncertainties**

None

## Limitations

- Synthetic local demo only; no production-readiness claim.
- Only Chromium with desktop 1440x900 and narrow 390x844 viewports; no physical mobile device.
- No geography verification or traces collected; no performance or comprehensive accessibility/SEO audit.
- Scope interception restricts target requests; browser-level background traffic is not independently firewall-verified.
- Retained Chromium process and profile avoid driver cleanup; each attempt used a fresh context.
- J04-fr was independently adjudicated from actual second-attempt DOM/network after a screenshot timeout. Raw observations remain unchanged; see independent-review.md. No additional browser request or retry was made.

## Recommended next work

Triage demonstrated defects, resolve product questions, and rerun fixed or blocked critical cases in a new campaign. This report does not certify other devices, countries, security, or legal compliance.
