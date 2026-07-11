# Claude Code Platform Adapter

The Claude Code adapter packages `clreq-skills` as a Claude Code skill while keeping the Universal Rule Package as the source of truth.

## Install

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --agent claude-code --global
```

The installable, self-contained package is in `../../skills/clreq/`. This adapter remains a platform-specific development reference.

## Invoke

Use `/clreq` in Claude Code when reviewing Web-facing Chinese Text or CSS that affects rendered Chinese text. The skill `description` also lets Claude Code load it automatically when relevant.

The skill maps Claude Code usage to:

- Reference Adapter Coarse Triggers in `../reference.md`
- Atomic Rule Cards in `../../rules/`
- Review Suggestion format in `../reference.md`
- Project Override behavior in `../reference.md`

The Claude Code adapter must not duplicate rule text. It should load relevant rule cards and fixtures from the Universal Rule Package.

## Behavior

- Produce Review Suggestions by default.
- Do not mutate files unless the user explicitly asks for edits.
- Work from files already in scope plus nearby localization or design-system context when needed.
- Respect host project instructions, localization config, design-system policy, and Project Overrides.
- Do not infer Simplified or Traditional Chinese from bare `zh`; follow each rule's Ambiguous Chinese Locale policy.

See `../../fixtures/claude-code-adapter-language-metadata.md` for a Claude Code-style smoke fixture.
