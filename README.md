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

### Edit an existing rule

Edit the JSON rule card in `rules/<category>/`, then sync:

```sh
cp -r rules/ skills/clreq/rules/
./scripts/check-packaged-skill.sh
```

### Add a new rule

1. Create the JSON rule card under `rules/<category>/`.
2. Add a matching fixture under `fixtures/`.
3. Sync both:

   ```sh
   cp -r rules/ skills/clreq/rules/
   cp -r fixtures/ skills/clreq/fixtures/
   ./scripts/check-packaged-skill.sh
   ```

### Update the schema

```sh
cp schema/rule-card.schema.json skills/clreq/schema/rule-card.schema.json
./scripts/check-packaged-skill.sh
```

### Update the reference adapter

The reference adapter lives at `adapters/reference.md`. Its packaged copy at `skills/clreq/references/review-workflow.md` differs in one line (the output format reference). Apply the same transformation before syncing:

```sh
sed 's#using `docs/review-suggestion-format.md`#using the Output format below#' \
  adapters/reference.md > skills/clreq/references/review-workflow.md
./scripts/check-packaged-skill.sh
```

### Verify

`check-packaged-skill.sh` diffs the source directories against the packaged copies and exits non-zero on any difference. Run it after every sync to confirm the skill is ready to install.

## Sources

Rules cite the sources they rely on. CLReq-backed rules link to [Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/) or related W3C internationalization material. Web implementation guidance cites relevant HTML, CSS, Unicode, or other authoritative sources.

## License

This project uses the W3C Software and Document License. See [LICENSE.md](LICENSE.md).
