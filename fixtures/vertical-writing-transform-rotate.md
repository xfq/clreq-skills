# Fixture: rotated text used as vertical Chinese layout

**Fixture id:** `vertical-writing.transform-rotate`

**Related rule id:** `clreq.vertical-writing.avoid-transform-rotate`

**Status:** Active Golden Review Fixture for vertical writing implementation.

**Input surface:** CSS

**Locale context:** Traditional Chinese (`zh-Hant`) section title is rendered as readable vertical text.

**Project Overrides:** None.

**Matching policy:** `contract`

## Input

```css
.section-title {
  transform: rotate(90deg);
}
```

## Expected Review Suggestion

```text
[normal] clreq.vertical-writing.avoid-transform-rotate: Web-facing Chinese Text is rotated visually instead of using vertical writing layout.

Why it matters: CSS transforms rotate the painted box, but vertical writing needs text layout behavior for line progression, punctuation, and mixed Latin or numeric text.
Suggested change: Use `writing-mode` with an appropriate vertical direction and review `text-orientation` for Latin text and numerals; keep visual rotation only for decorative or explicitly reviewed cases.
Source: CSS Writing Modes, writing-mode and text-orientation; CLReq, Writing modes.
Confidence: medium
```
