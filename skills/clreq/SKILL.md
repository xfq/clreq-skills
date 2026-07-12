---
name: clreq
description: Review Web-facing Chinese text in websites and web apps. Use for rendered Chinese UI copy, localized messages, HTML/JSX/TSX/Vue/Svelte/Markdown/MDX/i18n/CSS affecting Chinese text, or questions about CLReq, punctuation, mixed Chinese-Western text, locale variants, line breaking, typography CSS, vertical writing, ruby, pinyin, or Bopomofo.
---

# CLReq review

Produce concise, source-aware review suggestions for Web-facing Chinese text.

## Workflow

1. Read `references/review-workflow.md` for scope, rule selection, review completion, project overrides, and output format.
2. Identify the locale and rendered surface from the files already in scope. Inspect nearby localization or design-system context only when needed.
3. Account for every rule card under `rules/` in an internal coverage ledger, then fully read each candidate selected by the reference workflow.
4. Apply each candidate rule's detection signals, `ignore_when` conditions, ambiguous-locale policy, and project overrides.
5. Finish only after every rule has a disposition and every distinct unsuppressed finding has been emitted or the review limitation has been stated.
6. Consolidate duplicate findings without dropping independent issues.
7. Do not modify files unless the user explicitly asks for edits.

## Guardrails

- Do not scan the entire repository by default.
- Do not review non-user-facing Chinese text unless requested.
- Do not infer Simplified or Traditional Chinese from bare `zh`.
- Do not mechanically convert between Simplified and Traditional Chinese.
- Preserve quoted, legal, historical, branded, technical, and user-generated content when a rule says it is exempt.

## Resources

- `rules/`: atomic rule cards and their source citations.
- `references/review-workflow.md`: platform-neutral application workflow.
- `fixtures/`: example inputs and expected review suggestions.
- `schema/rule-card.schema.json`: rule-card schema.
