#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

diff -ru --exclude=README.md rules skills/clreq/rules
diff -ru --exclude=README.md fixtures skills/clreq/fixtures
diff -u schema/rule-card.schema.json skills/clreq/schema/rule-card.schema.json
diff -u adapters/reference.md skills/clreq/references/review-workflow.md

# Validate every Atomic Rule Card in the source rules/ against the schema.
python3 scripts/validate-rules.py

# Check that local relative links in Markdown files resolve.
python3 scripts/check-relative-links.py
