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
4. Read the relevant Atomic Rule Cards from `rules/`; do not duplicate or rewrite them in the adapter.
5. Apply rule-level Detection Signals and `ignore_when` conditions.
6. Emit Review Suggestions using the Output format below.
7. Do not modify files unless the user explicitly asks for edits.

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

When multiple findings apply, prefer the smallest useful set. Avoid long typography explanations.

## Reference Smoke Fixture

See `../fixtures/reference-adapter-language-metadata.md` for a Reference Adapter smoke fixture that applies `clreq.metadata.lang-specificity` without duplicating the rule card in this adapter.
