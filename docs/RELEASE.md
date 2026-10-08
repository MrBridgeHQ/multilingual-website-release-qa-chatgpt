# Final local release verification

This record supersedes the pending local-promotion state in the earlier validation snapshot. Historical reports are retained unchanged.

The 6 precisely approved operations completed. Backups were verified immediately before execution and remain private. The installed runtime contains the corrected canonical helper; development candidates were moved to private retained storage.

The canonical helper passed 37 contract checks. All captured validation commands returned zero, including the skill format check, configuration check, and validation of the baseline, corrected, ticket-replay, and negative result bundles.

A new explicit Codex invocation loaded the final skill and its requested resources. The 13 installed file hashes match the canonical source at capture. The linked installation follows this source checkout; it does not maintain a second Git copy.

## Evidence

- [Final command receipts](../validation/release-checks.json)
- [Final installation invocation](../validation/installation-final-check.json)
- [Machine-readable readiness](../validation/release-readiness.json)
- [Functional validation and limits](../validation/VALIDATION.md)
- [Baseline versus corrected comparison](../validation/comparison/comparison.md)
- [Independent ticket clarifications](../validation/replay/ticket-clarifications.md)

The baseline and corrected public freeze manifests were rechecked; original reports and evidence remain byte-identical. CSV files are excluded from Git text normalization so their recorded hashes survive checkout.

## Publication and updates

The target repository is https://github.com/MrBridgeHQ/recette-web-multilingue-chatgpt. After pushing, delivery verification checks its public visibility, anonymous access to the README and skill, and equality between the remote default-branch commit, local HEAD, and installed runtime files.

For updates, inspect local changes and upstream changes, follow the host preservation policy, and then use git pull --ff-only when authorized. The discovery symlink follows the checkout. Repeat configuration validation, contract checks, and an explicit Codex invocation after a meaningful update.

No new browser run is claimed for the helper promotion: the unchanged frozen functional evidence was revalidated with the corrected canonical helper. Physical mobile devices, additional browser engines, and verified country egress remain outside the demonstrated coverage.
