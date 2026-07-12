---
name: clreq
description: Review Web-facing Chinese Text in websites and web apps using the clreq-skills Universal Rule Package. Use when Claude Code sees rendered Chinese UI copy, localized messages, HTML/JSX/TSX/Vue/Svelte/Markdown/MDX/i18n/CSS that affects Chinese text, or requests about CLReq, Chinese punctuation, mixed Chinese-Western text, locale variants, line breaking, typography CSS, vertical writing, ruby, pinyin, Bopomofo, or Chinese web text review.
---

# clreq-skills Claude Code Adapter

## Overview

Use this skill to produce short, source-aware Review Suggestions for Web-facing Chinese Text. The Universal Rule Package remains the source of truth; this Claude Code adapter describes how to apply it inside Claude Code.

`clreq-skills` contains guidance for coding agents.

## Workflow

1. Check whether the current Claude Code task includes Web-facing Chinese Text or CSS that affects rendered Chinese text.
2. Read the Reference Adapter at `../../reference.md` for Coarse Triggers, Rule Selection, Review Completion, Project Overrides, and Review Suggestion shape.
3. Account for every Atomic Rule Card under `../../../rules/`, then fully read each candidate selected by the Reference Adapter; do not copy rule content into this adapter.
4. Apply rule-level Detection Signals, `ignore_when`, Ambiguous Chinese Locale policy, and Project Overrides.
5. Finish only after every rule has a disposition and every distinct unsuppressed finding has been emitted or the review limitation has been stated.
6. Emit Review Suggestions using the format in `../../../docs/review-suggestion-format.md`.
7. Do not modify files unless the user explicitly asks for edits.

## Claude Code Notes

Use the current task and any `/clreq` slash-command arguments as the review scope. Do not add hooks, permission grants, dynamic shell injections, or command-side effects for the first version.

Work from the files already in scope, plus nearby localization or design-system context only when needed. Do not run a full repository scan.

## Project Overrides

Respect host project instructions, localization configuration, design-system guidance, and project-specific override notes before applying a rule.

If locale intent is ambiguous, follow the rule's Ambiguous Chinese Locale policy. Do not assume Simplified or Traditional Chinese from bare `zh`.

## Output

Use concise Review Suggestions. Include severity, rule id, problem summary, why it matters, suggested change or human decision request, source, and confidence.

See `../../../fixtures/claude-code-adapter-language-metadata.md` for a Claude Code-style smoke example and `../../../fixtures/reference-adapter-language-metadata.md` for the platform-neutral equivalent.
