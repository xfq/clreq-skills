# Fixture: Codex adapter language metadata smoke

**Fixture id:** `codex-adapter.language-metadata`

**Related rule id:** `clreq.metadata.lang-specificity`

**Related adapter:** Codex Platform Adapter

**Status:** Active Codex adapter smoke fixture.

**Input surface:** HTML

**Locale context:** Ambiguous Chinese Locale. The document uses bare `zh` and gives no script or region signal.

**Project Overrides:** None.

## Codex Invocation

```text
Use $clreq to review this HTML snippet.
```

## Input

```html
<html lang="zh">
  <body>
    <button>立即购买</button>
  </body>
</html>
```

The expected output is identical to the reference fixture: see `reference-adapter-language-metadata.md`.
