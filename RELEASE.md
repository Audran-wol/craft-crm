# craft-crm v0.1.0

Prepared 24 October 2026 for public distribution at [Audran-wol/craft-crm](https://github.com/Audran-wol/craft-crm), under the MIT license selected by the maintainer. The canonical repository, skill name and archive root are `craft-crm`.

## Reproduce verification

Python 3.9 or newer, standard library only:

```sh
python3 skills/craft-crm/scripts/validate_bundle.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/package_release.py
```

Optional Node logic probes:

```sh
node evaluations/verify_audit.cjs
node examples/sales/verify_storage.cjs
```

Packaging runs the validator and Python tests, then writes `dist/craft-crm-0.1.0.zip` and its SHA-256 checksum. It excludes internal trial results, caches, Git metadata and dependency/build trees, and rejects output inside included source trees. Contents, timestamps and permissions are deterministic for the same inputs and Python/zlib implementation.

The public source includes only synthetic example data and a scoped field-report summary. The private project transcript, account details and filesystem logs are excluded. Installed skill copies include the MIT notice. `agents/openai.yaml` uses YAML's JSON subset for complete standard-library validation.

## Installation smoke tests

Before release, run the actual Skills CLI against a clean extracted archive for both `-a claude-code --copy` and `-a codex --copy` in disposable projects, and compare the installed bytes with the release. Verify the public repository source after publishing. A fresh live agent session, Windows, physical phones and assistive technologies are separate checks; do not claim them from a successful copy.

Earlier local trials exercised 22 token-contrast pairs and 33 storage-engine cases. The six audit-fixture probes reproduce known defects rather than certify the fixture. See evaluations/RESULTS.md for what was observed and what remains unverified.
