# clreq-skills

English | [简体中文](README.zh-Hans.md)

CLReq-backed Chinese web text, i18n, and focused layout checks for coding agents.

This skill helps Codex, Claude Code, and other coding agents that support the Agent Skills format review user-facing Chinese text in HTML, JSX, TSX, Vue, Svelte, Markdown, MDX, localization resources, and CSS. It reports concise findings with a suggested action, confidence level, and source citation.

## See It in 30 Seconds

Given a page containing:

```html
<html lang="zh">
  <p>今天下单, 明天发货.</p>
</html>
```

and Chinese text rotated with CSS:

```css
.vertical-label {
  transform: rotate(90deg);
}
```

ask the agent:

```text
Use $clreq to review samples/web-smoke/index.html and samples/web-smoke/styles.css.
```

See the [complete smoke sample](samples/web-smoke/README.md) and its [expected review](samples/web-smoke/expected-review.md).

## Install

Install globally:

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --global
```

Install for the current project:

```sh
npx skills@latest add xfq/clreq-skills --skill clreq
```

The installable package is the self-contained `skills/clreq/` directory.

## Use

Review selected files:

```text
Use $clreq to review src/components/Checkout.tsx and src/locales/zh-Hans.json for user-facing Chinese text and layout issues.
```

Review the current change:

```text
Use $clreq to review the files changed in the current diff.
```

The skill works from the files or diff already in scope. It does not scan the entire repository by default.

## Repository Structure

The project separates the reusable rule package from agent-specific integration:

- `skills/clreq/`: self-contained installable skill.
- `rules/`: authoring source for atomic rule cards.
- `fixtures/`: focused input and expected-review examples.
- `schema/`: JSON Schema for rule cards.
- `adapters/`: platform-specific development references.
- `samples/`: end-to-end review samples.

## Development

The root `rules/`, `fixtures/`, `schema/`, and reference adapter are the authoring sources. After changing them, update the packaged copies and verify that the installable skill remains synchronized:

```sh
./scripts/check-packaged-skill.sh
```

## Sources

Rules cite the sources they rely on. CLReq-backed rules link to [Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/) or related W3C internationalization material. Web implementation guidance cites relevant HTML, CSS, Unicode, or other authoritative sources.

## License

This project uses the W3C Software and Document License. See [LICENSE.md](LICENSE.md).
