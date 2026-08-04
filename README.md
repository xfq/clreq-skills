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

You can also simply say the following in Claude Code, Codex, or another agent that supports Agent Skills:

```text
install this skill: https://github.com/xfq/clreq-skills
```

## Use

Review selected files:

```text
Use $clreq to review src/components/Checkout.tsx for Chinese text and layout issues.
```

Review the current change:

```text
Use $clreq to review the files changed in the current diff.
```

Review the entire repository:

```text
Use $clreq to scan this repository for Chinese text and layout issues.
```

The skill works from the files or diff already in scope by default. It scans the entire repository when explicitly requested, while excluding dependencies, generated files, caches, and build outputs unless they are included by the user.

## Repository Structure

The project separates the reusable rule package from agent-specific integration:

- `skills/clreq/`: self-contained installable skill.
- `rules/`: authoring source for atomic rule cards.
- `fixtures/`: focused input and expected-review examples.
- `schema/`: JSON Schema for rule cards.
- `adapters/`: platform-specific development references.
- `samples/`: end-to-end review samples.

## Development

The installable skill lives in `skills/clreq/`. Its contents are synced copies of the authoring sources in the project root. After editing any source, sync the copies and verify.

### Sync sources to the packaged skill

After editing any source file (rules, fixtures, schema, or the reference adapter), sync the changes to `skills/clreq/`:

```sh
./scripts/sync.sh
```

This copies all source directories into the packaged skill, copies the reference adapter as the packaged review workflow, and runs `check-packaged-skill.sh` to verify the result.

### Verify

`check-packaged-skill.sh` diffs the source directories against the packaged copies and exits non-zero on any difference. Run it after every sync to confirm the skill is ready to install.

## Sources

Rules cite the sources they rely on. CLReq-backed rules link to [Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/) or related W3C internationalization material. Web implementation guidance cites relevant HTML, CSS, Unicode, or other authoritative sources.

## License

This project uses the W3C Software and Document License. See [LICENSE.md](LICENSE.md).
