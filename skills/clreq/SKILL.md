---
name: clreq
description: Review Web-facing Chinese text and layout in websites and web apps. Use for files, diffs, directories, or repositories containing rendered Chinese UI or localization; relevant HTML/JSX/TSX/Vue/Svelte/Markdown/MDX/i18n/CSS; or questions about CLReq, punctuation, mixed Chinese-Western text, locale variants, line breaking, typography, vertical writing, ruby, pinyin, or Bopomofo.
---

# CLReq review

Review Web-facing Chinese text and layout. Return concise, source-aware suggestions.

## Workflow

1. Read `references/review-workflow.md` completely and follow its scope, exclusions, rule selection, overrides, output, and completion requirements.
2. Determine the requested scope, rendered surface, and locale; inspect nearby localization or design-system context when needed.
3. Account for every `*.json` rule card under `rules/`. Fully read each candidate before applying its detection signals, `ignore_when`, ambiguous-locale policy, and project overrides.
4. For explicit repository-wide scope, discover candidate files and maintain the reference workflow's file coverage ledger, batching without silently skipping files.
5. Finish only when every rule and in-scope candidate file has a disposition and all distinct unsuppressed findings or unresolved limitations are reported. Consolidate duplicate findings without dropping independent issues.
6. Modify files only when explicitly requested.
