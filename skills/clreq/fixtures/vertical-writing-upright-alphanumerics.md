# Fixture: short alphanumerics remain upright in vertical Chinese text

**Fixture id:** `vertical-writing.upright-single-alphanumerics`

**Related rule id:** `clreq.vertical-writing.upright-single-alphanumerics`

**Status:** Active Golden Review Fixture for mixed text in vertical writing.

**Input surface:** HTML and CSS

**Locale context:** Chinese text is rendered in vertical writing mode.

**Project Overrides:** None.

## Input

```html
<p class="vertical">今年<span>GDP</span>增长了。</p>
```

```css
.vertical {
  writing-mode: vertical-rl;
}
```

## Expected Review Suggestion

```text
[normal] clreq.vertical-writing.upright-single-alphanumerics: A standalone Latin letter, Arabic numeral, or initialism in vertical Chinese text is rendered sideways.

影响： CLReq commonly keeps these short alphanumeric runs in the same upright direction as Han characters, and CSS provides `text-orientation: upright` for that rendering.
Suggested change: Target the `GDP` inline run and set `text-orientation: upright;`. Do not apply it indiscriminately to ordinary Western words, sentences, or longer numeric runs.
Source: CLReq, Mixed text composition in vertical writing mode; CSS Writing Modes Level 4, text-orientation.
Confidence: medium
```
