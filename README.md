# clreq-skills

`clreq-skills` packages Chinese web text layout guidance for coding agents. It is based on [CLReq](https://github.com/w3c/clreq) and related sources.

## Project Shape

The core is a Universal Rule Package. Platform Adapters map that package into specific coding-agent environments.

- `rules/` hosts Atomic Rule Cards.
- `adapters/` hosts Platform Adapters.
- `fixtures/` hosts Golden Review Fixtures.
- `schema/` hosts rule-card schema material.
- `skills/clreq/` hosts the self-contained installable skill.
- `samples/` hosts smoke samples for agent review behavior.

## Install

Install the self-contained `clreq` skill from GitHub:

```sh
npx skills@latest add xfq/clreq-skills --skill clreq
```

To install it globally:

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --global
```

List the skills exposed by a local checkout before publishing changes:

```sh
npx skills@latest add . --list
```

## Use in an Agent

After installing the skill, give the agent a prompt such as:

```text
使用 $clreq 审查这个页面里的中文文本和排版。
```

The installable package lives in `skills/clreq/`. It is self-contained so copied installations do not depend on files outside the installed skill directory. Files under `adapters/` remain platform-specific development references rather than installation entry points.

The root `rules/`, `fixtures/`, `schema/`, and reference adapter remain the authoring sources. After changing them, update the packaged copies and verify that they are synchronized:

```sh
./scripts/check-packaged-skill.sh
```

## Attribution

Rules must cite the sources they rely on. CLReq-backed Rules should link back to CLReq, Chinese Gap Analysis, or closely related Chinese layout requirement material. Web Platform implementation guidance should cite the relevant HTML, CSS, Unicode, or related source.

## License

This scaffold uses the W3C Software and Document License. See `LICENSE.md`.
