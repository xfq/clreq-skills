# Reference Adapter

The Reference Adapter is the platform-neutral way to use `clreq-skills` from any coding agent instruction file. It maps likely Web-facing Chinese Text to the Universal Rule Package, then asks the agent to emit Review Suggestions without mutating files by default.

`clreq-skills` is for coding agents.

## When To Load

Load this adapter when the task or changed files include Web-facing Chinese Text in a website or web application.

Coarse Triggers include:

- HTML, JSX, TSX, Vue, Svelte, Markdown, MDX, i18n, or CSS containing rendered Chinese UI copy, article content, labels, headings, navigation, forms, errors, captions, or localized messages.
- Chinese locale metadata such as `lang="zh"`, `zh-Hans`, `zh-Hant`, `zh-CN`, `zh-TW`, `zh-HK`, or i18n resource keys for Chinese locales.
- CSS that can affect rendered Chinese layout, wrapping, fonts, punctuation, vertical writing, or ruby annotations.
- User requests that mention Chinese typography, CLReq, punctuation, mixed Chinese-Western text, locale variants, vertical writing, ruby, pinyin, Bopomofo, or Web-facing Chinese Text review.

Do not treat this as a full repository scan. Use the files already in scope for the agent task, plus nearby localization or design-system files only when needed to understand applicability or Project Overrides.

## What To Ignore By Default

Do not comment on non-user-facing Chinese text unless the user explicitly asks for it:

- source comments
- internal documentation
- debug logs
- test fixture prose
- generated snapshots
- code identifiers
- quoted source material that must be preserved

## Review Flow

1. Identify the surface: HTML, JSX, TSX, Vue, Svelte, Markdown, MDX, i18n, or CSS.
2. Identify the locale context from `lang`, route, i18n key, project config, or Project Override.
3. If the context is bare `zh` and a rule depends on script or region, follow the rule's Ambiguous Chinese Locale policy.
4. Build the candidate rule set using the Rule Selection procedure below.
5. Read every candidate Atomic Rule Card and apply its Detection Signals, `ignore_when` conditions, Ambiguous Chinese Locale policy, and Project Overrides.
6. Check the Review Completion conditions below; do not stop after the first finding.
7. Emit Review Suggestions using the Output format below.
8. Do not modify files unless the user explicitly asks for edits.

## Rule Selection

Create an internal coverage ledger for every `*.json` Atomic Rule Card under `rules/`. The ledger is working state and does not need to appear in the final response.

For each rule, inspect `id` and `applies_to`, then mark it as a candidate when all applicable selectors allow it:

- `surfaces` intersects the rendered surfaces in scope.
- Any declared `scripts`, `locales`, or `regions` matches the known context. When that context is missing or ambiguous, do not exclude the rule solely for that reason; keep it as a candidate and apply its `ambiguous_locale_policy` rather than silently assuming a locale.
- Any declared `writing_modes` matches the observed writing mode. If the scoped code contains evidence that writing mode is being established or simulated, such as `writing-mode`, `text-orientation`, or text rotation, inspect the corresponding writing-mode rules.
- Project Overrides have not disabled the rule for the scoped path.

Do not choose rules from filenames or remembered categories alone. Account for every current rule card in the ledger as `candidate`, `not applicable`, or `disabled by override`, with a short reason. Fully read each candidate before deciding whether its Detection Signal is present or an `ignore_when` condition suppresses it.

## Review Completion

The review is complete only when:

- Every current Atomic Rule Card has a ledger status and reason.
- Every candidate rule has been checked against all files and rendered text in scope, including relevant nearby locale or design-system context.
- Ambiguous locale cases have followed the rule's policy instead of being silently excluded.
- Every distinct unsuppressed finding has been emitted; consolidate duplicate instances of the same underlying issue, but do not omit independent findings to keep the output short.
- If no findings remain, report that no applicable issues were found in the reviewed scope.

If required context cannot be inspected, state the limitation and which candidate rules remain unresolved rather than claiming the review is complete.

## Project Overrides

A Project Override is an explicit host-project decision that changes how an agent applies `clreq-skills` in that project. Overrides may live in agent instructions, localization docs, design-system docs, or a project-specific config note.

Supported override fields:

- `default_locale`: the locale to assume when files omit language metadata.
- `enabled_rules`: rule ids to enable, disable, or limit by path.
- `severity_overrides`: rule ids mapped to `blocking`, `strong`, `normal`, or `advisory`.
- `style_suggestion_policy`: whether Style Suggestions are enabled, disabled, or advisory-only.
- `locale_policy`: project decisions for `zh`, `zh-Hans`, `zh-Hant`, region, and script handling.
- `design_system_policy`: font, wrapping, vertical writing, ruby, and component exceptions.
- `preservation_policy`: content classes that must remain unchanged, such as legal text, quoted titles, user-generated content, or historical material.

Project Overrides change project policy only. They do not change CLReq, Web Platform, Unicode, or other source facts. If an override conflicts with a Source Citation, mention the override as the reason for suppressing, downgrading, or changing the action, not as a change to the source.

## Output

Use this shape unless the host platform adapter requires a different wrapper:

```text
[<severity>] <rule id>: <problem summary>

Why it matters: <one sentence>
Suggested change: <concrete change or human decision request>
Source: <short Source Citation or "No source citation">
Confidence: high | medium | low
```

When multiple findings apply, consolidate duplicates into the smallest useful set without dropping distinct applicable findings. Avoid long typography explanations.

## Reference Smoke Fixture

See `../fixtures/reference-adapter-language-metadata.md` for a Reference Adapter smoke fixture that applies `clreq.metadata.lang-specificity` without duplicating the rule card in this adapter.
