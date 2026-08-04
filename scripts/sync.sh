#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

# Sync rules (exclude the README to avoid clobbering the packaged copy's README if it differs)
cp -r rules/ skills/clreq/rules/

# Sync fixtures
cp -r fixtures/ skills/clreq/fixtures/

# Sync schema
cp schema/rule-card.schema.json skills/clreq/schema/rule-card.schema.json

# Sync reference adapter
cp adapters/reference.md skills/clreq/references/review-workflow.md

echo "Sync complete. Running validation..."

./scripts/check-packaged-skill.sh

echo "All good — skill package is ready."
