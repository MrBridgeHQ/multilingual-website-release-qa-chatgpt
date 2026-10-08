# Campaign data contract

The JSON schemas in [config.schema.json](../schemas/config.schema.json) and [results.schema.json](../schemas/results.schema.json) are the portable contract. The helper requires Python 3.12 and `jsonschema==4.10.3`; it does not need Playwright, PyYAML, a provider SDK, or an MCP client. Browser execution belongs to the agent and its available tools.

## Commands

Run from the repository root; adapt the relative skill path after installation:

```sh
python3 -B skills/recette-web-multilingue/scripts/qa.py validate-config skills/recette-web-multilingue/assets/config.example.json
python3 -B skills/recette-web-multilingue/scripts/qa.py validate-observations /absolute/campaign/observations.json
python3 -B skills/recette-web-multilingue/scripts/qa.py finalize /absolute/campaign/observations.json /absolute/campaign/tickets.json --output /absolute/new-report
python3 -B skills/recette-web-multilingue/scripts/qa.py validate-results /absolute/new-report/results.json
```

Validation is read-only. Finalization requires an existing parent and a new absolute output directory. It never overwrites, deletes, moves, or cleans files. On a partial write, preserve the directory and use a different new destination after diagnosing the error.

The shipped configuration is a synthetic twenty-case example. Its exact localized business expectations are in the repository's `tests/demo/product-contract.md`; this test-only reference is not a dependency for campaigns on other sites. Replace the example contract with the user's explicit expectations. Unknown expectations use `expected: null` and `expectation_basis: "PRODUCT_QUESTION"`; ask or record an assumption before treating a preference as mandatory.

## Configuration

Use an explicit `cases` list linking journey, language, profile, and an optional requested country. Never silently generate a Cartesian product. `languages`, profile locale/timezone, country, and output language are separate settings. `url_mappings` records corresponding localized routes. Scope origins omit trailing slashes and paths; path prefixes match segment boundaries.

Authentication stores a non-secret reference only. A declared action records the intended authorization boundary; it does not grant authority beyond the user or environment. Read budgets before execution and record any limit that prevented coverage. The helper validates declarations but does not enforce browser traffic itself.

## Observations and finalized results

An observation document has `schema_version: "1.0"`, `campaign`, `cases`, `evidence`, and an initially empty `tickets` array. `summary` may be omitted for observation validation; finalization derives it. A finalized `results.json` must include the reconciled summary. A supplied summary is checked rather than trusted.

A case records its actual URL, language, viewport/device class, observed browser version, UTC or offset-aware times, preconditions, fictional or masked test data, step results, attempts, country check, evidence IDs, limitations, and uncertainties. The campaign is the parent campaign identifier for every case. Each step uses `number`, `action`, `expected`, `observed`, `status`, and `evidence_ids`. Case IDs are unique within their campaign; use a new campaign for later retests.

The aggregate status follows actual step outcomes: a demonstrated `FAIL` remains a failure even if later steps are `NOT_RUN`; otherwise an obstacle produces `BLOCKED`, remaining unexecuted steps produce `NOT_RUN`, completed relevant steps can produce `PASS`, and a fully inapplicable case is `NOT_APPLICABLE`. An inapplicable step needs an observed explanation. A browser/tool incident is `BLOCKED` with classification `TOOLING_INCIDENT`, not a website defect.

Attempt numbers and step numbers start at 1 and are consecutive. The latest attempt agrees with the final case outcome. Preserve earlier attempts and their evidence; do not discard inconvenient failures. A case is not a success merely because one early step passed.

## Evidence

Each evidence record contains `id`, `path`, `sha256`, `kind`, `captured_at`, and `description`. Paths start with `evidence/` and are relative to the observation/results file's directory. Kinds are `SCREENSHOT`, `DOM`, `NETWORK`, `CONSOLE`, `TRACE`, and `TEXT`. Calculate SHA-256 from the actual bytes after redaction.

The helper verifies file presence, hash, normalized relative paths, absence of symlinks, and referential integrity. Finalization copies only registered evidence into the new bundle. Failed steps require evidence. Unregistered files are not exported. A hash proves that bytes match a record; it does not prove that the observation is truthful or sufficient.

Remove passwords, cookies, tokens, authorization headers, and unnecessary personal data before capture/export. Crop or mask screenshots before registering their final checksum. The helper rejects obvious credential fields and token-shaped text; this is a limited detection heuristic, not comprehensive redaction. It cannot inspect screenshots or safely sanitize browser trace archives. Prefer minimal synthetic evidence and have the agent review every file intended for delivery.

A requested country can be `PASS` or `FAIL` only with a verified country, explicit same-network-context attestation, and linked `NETWORK` evidence. The agent must actually establish that the evidence refers to the network context used for the target request. Schema checks alone cannot establish that fact. Without that link, record `BLOCKED` or `NOT_RUN` and keep verified country null. Without a request, country is `NOT_APPLICABLE`; language, locale, timezone, and simulated geolocation are never substituted for a network country.

## Tickets and exports

Provide `tickets.json` as an array; the helper does not invent defects or root causes. Every ticket includes stable ID, title, impact, severity/rationale, separate confidence, observed scope, preconditions, non-sensitive data, numbered reproduction text, expected/observed behavior, case/evidence links, observed reproduction frequency, correction note with a hypothesis flag, acceptance criteria, and retest steps.

Tickets must refer to an actual failed case and evidence belonging to linked cases. Reproduction counts cannot exceed their recorded attempts/failures. Not every failed case must have a ticket before triage. Suspicions and product questions remain explicit case classifications, not invented blocking defects.

`results.json` is the source of truth. The helper derives `audit-report.md` and `tickets.csv` from the same in-memory record and copies its evidence. CSV keys and enums remain English. Cells beginning with spreadsheet formula characters are prefixed with an apostrophe for safe spreadsheet import; consult JSON for the exact source text.

Built-in report headings and boilerplate support `en` and `fr`:

```sh
python3 -B skills/recette-web-multilingue/scripts/qa.py finalize /absolute/campaign/observations.json /absolute/campaign/tickets.json --output /absolute/new-french-report --output-language fr
```

This flag translates headings, not authored narratives. The agent must write the report/ticket narratives in the requested language before export while retaining original quoted evidence and all normalized enums. Other output languages remain valid campaign requests, but the helper refuses unsupported automatic export: use an explicitly agent-authored translation and verify it against JSON; do not claim automatic translation support.

## Counts and limits

`summary.counts` reconciles all five statuses to the planned case count. `executed` counts completed `PASS` and `FAIL` outcomes; `attempted` additionally includes `BLOCKED`. A partially executed `NOT_RUN` case remains incomplete and its step-level work stays visible. Coverage always prints completed outcomes / all planned cases, including inapplicable entries in that explicit denominator.

Zero completed outcomes yields `NO_EXECUTION`. Demonstrated failures yield `ISSUES_FOUND`. Missing execution or uncovered critical cases yields `INCOMPLETE`. Otherwise the verdict is `READY_FOR_TESTED_SCOPE`, never a certification of the whole site. These calculations do not turn unavailable console collection into proof of no console errors, or a narrow viewport into a physical-device test.
