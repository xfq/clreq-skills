---
name: clreq
description: Review Web-facing Chinese Text in websites and web apps using the clreq-skills Universal Rule Package, from individual files, diffs, directories, or an entire repository. Use when Claude Code sees rendered Chinese UI copy, localized messages, HTML/JSX/TSX/Vue/Svelte/Markdown/MDX/i18n/CSS that affects Chinese text, repository-wide Chinese text audits, or requests about CLReq, Chinese punctuation, mixed Chinese-Western text, locale variants, line breaking, typography CSS, vertical writing, ruby, pinyin, Bopomofo, or Chinese web text review.
---

# clreq — Claude Code Adapter

Follow `../../reference.md` completely for Coarse Triggers, scope and exclusions, Repository Scan, Rule Selection, Review Completion, Project Overrides, and Output format. The Atomic Rule Cards under `../../../rules/` are the source of truth; this adapter does not restate them.

Platform deltas:

- Invoked as `/clreq`; slash-command arguments set the review scope. The skill description also enables auto-loading.
- First version: no hooks, permission grants, dynamic shell injections, or command-side effects.

See `../../../fixtures/claude-code-adapter-language-metadata.md` for the platform smoke example.
