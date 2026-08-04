#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_root"

diff -ru --exclude=README.md rules skills/clreq/rules
diff -ru --exclude=README.md fixtures skills/clreq/fixtures
diff -u schema/rule-card.schema.json skills/clreq/schema/rule-card.schema.json
diff -u adapters/reference.md skills/clreq/references/review-workflow.md
