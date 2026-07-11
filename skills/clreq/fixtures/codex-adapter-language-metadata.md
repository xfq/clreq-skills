# Fixture: Codex adapter language metadata smoke

**Fixture id:** `codex-adapter.language-metadata`

**Related rule id:** `clreq.metadata.lang-specificity`

**Related adapter:** Codex Platform Adapter

**Status:** Active Codex adapter smoke fixture.

**Input surface:** HTML

**Locale context:** Ambiguous Chinese Locale. The document uses bare `zh` and gives no script or region signal.

**Project Overrides:** None.

**Matching policy:** `contract`

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

## Expected Codex-Style Output

```text
[advisory] clreq.metadata.lang-specificity: The page uses a bare `zh` language tag for Web-facing Chinese Text.

Why it matters: Some Chinese text recommendations depend on script or region, and the agent should not assume Simplified or Traditional Chinese from `zh` alone.
Suggested change: Confirm the intended locale and use a more specific BCP 47 language tag such as `zh-Hans` or `zh-Hant` when appropriate.
Source: HTML Standard; BCP 47; W3C Internationalization language tag guidance.
Confidence: medium
```
