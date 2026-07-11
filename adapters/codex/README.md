# Codex Platform Adapter

The Codex adapter packages `clreq-skills` as a Codex skill while keeping the Universal Rule Package as the source of truth.

## Install

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s /path/to/clreq-skills/adapters/codex/clreq "${CODEX_HOME:-$HOME/.codex}/skills/clreq"
```

Do not copy only `adapters/codex/clreq` unless you also preserve or rewrite its relative links back to the repository.

## Invoke

Use `$clreq` in Codex when reviewing Web-facing Chinese Text or CSS that affects rendered Chinese text.

The skill maps Codex invocation to:

- Reference Adapter Coarse Triggers in `../reference.md`
- Atomic Rule Cards in `../../rules/`
- Review Suggestion format in `../../docs/review-suggestion-format.md`
- Project Override behavior in `../reference.md`

The Codex adapter must not duplicate rule text. It should load relevant rule cards and fixtures from the Universal Rule Package.

## Behavior

- Produce Review Suggestions by default.
- Do not mutate files unless the user explicitly asks for edits.
- Respect host project instructions, localization config, design-system policy, and Project Overrides.
- Do not infer Simplified or Traditional Chinese from bare `zh`; follow each rule's Ambiguous Chinese Locale policy.

See `../../fixtures/codex-adapter-language-metadata.md` for a Codex-style smoke fixture.
