# Fixture: non-semantic ruby-like annotation markup

**Fixture id:** `ruby.semantic-markup`

**Related rule id:** `clreq.ruby.semantic-markup`

**Status:** Active Golden Review Fixture for ruby annotation semantics.

**Input surface:** HTML

**Locale context:** Simplified Chinese (`zh-Hans`) pronunciation annotation in horizontal writing.

**Project Overrides:** None.

**Matching policy:** `contract`

## Input

```html
<span class="annotated">汉<span class="annotation">han</span></span>
```

## Expected Review Suggestion

```text
[normal] clreq.ruby.semantic-markup: Ruby-like Chinese annotation is represented with non-semantic markup.

影响： CLReq describes ruby as annotation text attached to base text, and HTML provides `<ruby>`/`<rt>` semantics for that relationship across writing modes.
Suggested change: Use semantic ruby markup such as `<ruby>汉<rt>han</rt></ruby>`, then use CSS Ruby properties only for presentation details such as annotation position.
Source: HTML Standard, ruby; CSS Ruby Annotation Layout; CLReq, Usage of ruby.
Confidence: medium
```
