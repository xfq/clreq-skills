# Web Smoke Sample

This sample is a small static web project for end-to-end agent smoke testing. It intentionally includes Chinese text and CSS patterns that should produce Review Suggestions through the adapters.

## Files

- `index.html`: rendered Chinese UI copy and language metadata.
- `styles.css`: CSS that affects Chinese text rendering.
- `expected-review.md`: expected Review Suggestions.

## Reference Adapter Prompt

```text
Use /path/to/clreq-skills/adapters/reference.md to review samples/web-smoke/index.html and samples/web-smoke/styles.css. Emit Review Suggestions only.
```

## Codex Prompt

```text
Use $clreq to review samples/web-smoke/index.html and samples/web-smoke/styles.css. Emit Review Suggestions only.
```

## Claude Code Prompt

```text
/clreq review samples/web-smoke/index.html and samples/web-smoke/styles.css. Emit Review Suggestions only.
```

## Expected Behavior

The agent should load the adapter, read only relevant rule cards, respect the ambiguous locale policy for bare `zh`, and produce short Review Suggestions matching `expected-review.md` at contract level.

The agent should not rewrite files unless the user explicitly asks for edits.
