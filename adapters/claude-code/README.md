# Claude Code Platform Adapter

The Claude Code adapter installs `clreq` as a Claude Code skill. The Universal Rule Package (`rules/`, `fixtures/`, `schema/`) is the source of truth, and `reference.md` defines the shared workflow; this adapter adds only Claude Code-specific behavior.

## Install

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --agent claude-code --global
```

## Invoke

Use `/clreq` (slash-command arguments set the review scope), or let the skill description auto-load it, when reviewing Web-facing Chinese Text or CSS that affects rendered Chinese text. The installable, self-contained package is `../../skills/clreq/`; this adapter remains a platform-specific development reference.
