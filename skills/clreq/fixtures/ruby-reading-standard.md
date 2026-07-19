# Fixture: unresolved reading standard context

**Fixture id:** `ruby.reading-standard`

**Related rule id:** `clreq.ruby.reading-standard`

**Status:** Active Golden Review Fixture for phonetic ruby reading standards.

**Input surface:** HTML

**Locale context:** Chinese text without language metadata, a distinguishable Simplified/Traditional script signal, a named reading standard, or an author preference. The rule cannot select the Traditional-Chinese or Simplified-Chinese fallback.

**Project Overrides:** None.

## Input

```html
<p>我<ruby>和<rt>ㄏㄜˊ</rt></ruby>你</p>
```

## Expected Review Suggestion

```text
[strong] clreq.ruby.reading-standard: The phonetic ruby lacks one resolved reading-standard decision.

影响： The text does not identify whether the Traditional-Chinese-to-Taiwan-MOE or Simplified-Chinese-to-普通话 fallback applies, so per-occurrence guessing can create inconsistent pronunciation guidance.
Suggested change: Ask once whether the text is Traditional Chinese or Simplified Chinese, or which named standard the author wants, and how tone sandhi should be marked; then apply both decisions consistently.
Source: CLReq, Usage of ruby; CLReq, Positioning of Romanized ruby.
Confidence: medium
```
