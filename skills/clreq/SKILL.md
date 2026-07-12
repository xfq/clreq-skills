---
name: clreq
description: Review Web-facing Chinese text in websites and web apps, from individual files, diffs, directories, or an entire repository. Use for rendered Chinese UI copy, localized messages, HTML/JSX/TSX/Vue/Svelte/Markdown/MDX/i18n/CSS affecting Chinese text, repository-wide Chinese text audits, or questions about CLReq, punctuation, mixed Chinese-Western text, locale variants, line breaking, typography CSS, vertical writing, ruby, pinyin, or Bopomofo.
---

# CLReq review

Produce concise, source-aware review suggestions for Web-facing Chinese text. You may ask which output language the user prefers when that would be useful. If the user does not specify a language, default to Simplified Chinese; always follow an explicit language preference.

## Workflow

1. Read `references/review-workflow.md` for scope, rule selection, review completion, project overrides, and output format.
2. Determine the requested scope: named files, a diff, a directory, or the repository. For repository scope, discover candidate files using tracked files when possible, include supported Web and localization formats, and exclude dependency, build-output, generated, cache, vendored, and VCS directories unless explicitly requested.
3. Identify the locale and rendered surface from the files in scope. Inspect nearby localization or design-system context when needed.
4. Account for every rule card under `rules/` in an internal coverage ledger, then fully read each candidate selected by the reference workflow.
5. Apply each candidate rule's detection signals, `ignore_when` conditions, ambiguous-locale policy, and project overrides.
6. For a large repository, review candidates in batches and keep a file coverage ledger so no discovered candidate is silently skipped.
7. Finish only after every rule and every in-scope candidate file has a disposition and every distinct unsuppressed finding has been emitted, or the review limitation has been stated.
8. Consolidate duplicate findings without dropping independent issues.
9. Do not modify files unless the user explicitly asks for edits.

## Guardrails

- Do not scan the entire repository unless the user explicitly requests repository or project-wide scope.
- Do not review non-user-facing Chinese text unless requested.
- Do not infer Simplified or Traditional Chinese from bare `zh`.
- Do not mechanically convert between Simplified and Traditional Chinese.
- Translate rule-card templates and source descriptions into the selected output language instead of copying their wording mechanically. Keep rule ids, code, standard names, and URLs unchanged when appropriate.
- Use field labels in the selected output language. When no language preference is given, use Chinese labels and do not emit English field labels.
- Preserve quoted, legal, historical, branded, technical, and user-generated content when a rule says it is exempt.

## Resources

- `rules/`: atomic rule cards and their source citations.
- `references/review-workflow.md`: platform-neutral application workflow.
- `fixtures/`: example inputs and expected review suggestions.
- `schema/rule-card.schema.json`: rule-card schema.
