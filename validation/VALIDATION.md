# Validation snapshot

This document is generated from the preserved synthetic campaign records. The instruction package and editorial resources are in English; French fixture text and observed quotations remain in their original language.

## Delivery state at capture

The skill was authored using Codex Skill Master, manually scaffolded under its optional initializer policy, and checked with the installed system quick_validate.py validator. The creator itself is not distributed.

Local discovery and an explicit fresh-session invocation succeeded. The corrected helper candidate passed verification. Promotion to the canonical qa.py and two instruction files is waiting for the exact file-replacement approval required by the account-wide preservation policy. Three development candidates will also be moved to retained private storage under that same requested approval. Backups and the complete diff are retained locally. No public repository or release commit is claimed by this snapshot.

## Observed campaigns

| Campaign | Planned | PASS | FAIL | BLOCKED | NOT_RUN | Coverage | Evidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [baseline](baseline/report/audit-report.md) | 20 | 14 | 6 | 0 | 0 | 20/20 | 259 |
| [fixed](fixed/report/audit-report.md) | 20 | 20 | 0 | 0 | 0 | 20/20 | 208 |
| [replay](replay/report/audit-report.md) | 6 | 0 | 6 | 0 | 0 | 6/6 | 31 |
| [negative](negative/delivery/audit-report.md) | 5 | 0 | 0 | 4 | 1 | 0/5 | 6 |

No campaign contains a NOT_APPLICABLE case. Counts are computed from results.json and reconciled with each summary.

## Blind baseline, ticket replay, and corrections

The independent baseline auditor received the skill and public product contract without the oracle or fixture implementation. The report was frozen before comparison: 6/6 seeded defects detected, 0 missed, and 0/14 control false failures. This is a synthetic-fixture result, not an estimated general recall rate.

A second agent received only the six reviewed tickets as business input and reproduced each defect once in a fresh browser context. The raw source, project contract, oracle, and first auditor driver were withheld. Shared filesystem separation was procedural, not an access-control boundary. Read the [independent replay assessment](replay/replay-assessment.md) and [additive ticket clarifications](replay/ticket-clarifications.md). The original frozen tickets and results were preserved.

The unchanged first-auditor driver then executed the corrected fixture. Observed FAIL-to-PASS transitions: 6/6. Original controls still passing: 14/14. The independent retest assessed 19/19 acceptance criteria as PASS. Stable original ticket IDs are linked in [retest-assessment.json](fixed/retest-assessment.json).

The second French redirect attempt experienced a screenshot timeout after actual DOM/network capture. Its independently reviewed classification uses those preserved observations; no replacement screenshot or extra attempt was invented. Read the [baseline provenance](baseline/public-provenance.md).

## Executed validation commands

The corrected helper passed 37 contract checks. The same captured command batch validated the configuration and all four result bundles. Exact outputs and return codes are in [candidate-checks.json](candidate-checks.json). The candidate is retained locally pending canonical promotion; its SHA-256 identifies the tested bytes.

Command families actually executed:

- `python3 -B <system-skills>/skill-creator/scripts/quick_validate.py <repository>/skills/recette-web-multilingue` — exit 0.
- `python3 -B <repository>/skills/recette-web-multilingue/scripts/qa-v4.py validate-config <repository>/skills/recette-web-multilingue/assets/config.example.json` — exit 0.
- `python3 -B tests/test_contracts.py run --helper <repository>/skills/recette-web-multilingue/scripts/qa-v4.py` — exit 0.
- `python3 -B tests/contracts/test_country_mismatch.py --helper <repository>/skills/recette-web-multilingue/scripts/qa-v4.py` — exit 0.
- `python3 -B tests/contracts/test_retry_outcomes.py --helper <repository>/skills/recette-web-multilingue/scripts/qa-v4.py` — exit 0.
- `python3 -B <repository>/skills/recette-web-multilingue/scripts/qa-v4.py validate-results validation/baseline/report/results.json` — exit 0.
- `python3 -B <repository>/skills/recette-web-multilingue/scripts/qa-v4.py validate-results validation/fixed/report/results.json` — exit 0.
- `python3 -B <repository>/skills/recette-web-multilingue/scripts/qa-v4.py validate-results validation/replay/report/results.json` — exit 0.
- `python3 -B <repository>/skills/recette-web-multilingue/scripts/qa-v4.py validate-results validation/negative/delivery/results.json` — exit 0.

Browser execution commands and their conditions are documented in the demonstration, replay, and negative-scenario sources. The portable replay driver changes only the original executed driver’s repository-root calculation; its help and inspection modes were executed, without claiming an additional browser run.

The deterministic comparison command was executed in inspect and create modes:

    python3 -B tests/compare_validation.py create --baseline validation/baseline/report/results.json --fixed validation/fixed/report/results.json --freeze validation/comparison-input-manifest.json --output validation/comparison

Choose a new output directory when repeating it. Existing evidence is never silently replaced.

## Installation and selection

The discovery symlink resolves to the canonical project skill directory. A fresh Codex CLI invocation explicitly named $recette-web-multilingue and read the instruction file and linked resources. See [installation-check.json](installation-check.json). This receipt records the package as it existed before the pending reviewed promotion.

A separate French functional request selected the skill; a translation-only request did not. See [selection-public-check.json](selection-public-check.json). The first selection attempt was rejected by the CLI because its working directory was not a Git repository; the successful fresh attempts used the project repository. No bypass flag was used.

## Limits

- J01–J08 use a 1440×900 desktop viewport; J09–J10 use a 390×844 narrow Chromium viewport. No physical phone, Safari, or Firefox was tested.
- Main and replay campaigns used Chromium 151.0.7922.34; the negative suite used Chromium 153.0.8010.12. Browser versions remain recorded per result.
- No real production website, client data, paid purchase, external message, or real account was involved.
- Network country was not established. The requested-country negative case remains BLOCKED; locale and timezone are not country evidence.
- Browser-unavailable, authentication 401, controlled protocol error, missing expectation, and unproved country scenarios retain their actual limitations. Zero completed negative checks produced NO_EXECUTION, not a site approval.
- The helper localizes English/French headings; the agent authors translated narratives. Unsupported automatic report languages fail explicitly.
- JSON/schema checks verify internal consistency, hashes, paths, and exports. They cannot prove that every screenshot is sufficient or certify accessibility, security, legality, or general release readiness.

## Public evidence and reproduction inputs

Public freeze manifests contain only publishable synthetic report artifacts with portable paths. Full local manifests, browser profiles, raw observations, machine configuration, and private command logs remain on the validation host. The reviewed synthetic ticket array is the one explicitly included source input for reproducing the ticket-only replay.

The README describes invocation, prerequisites, local installation, and updates. Final publication and installed-versus-published commit matching must be recorded after the pending canonical promotion.

## Resolution of the historical pending state — 2026-10-08

The six approved operations have completed. All canonical helper checks and the final explicit installation invocation passed. The earlier pending statements describe the preserved initial snapshot. See [the final verification](../docs/RELEASE.md), [release-checks.json](release-checks.json), and [installation-final-check.json](installation-final-check.json). Existing browser evidence and its limits remain unchanged.
