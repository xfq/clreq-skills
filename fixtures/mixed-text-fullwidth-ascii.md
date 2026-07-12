# Fixture: fullwidth ASCII forms in mixed Chinese-Western text

**Fixture id:** `mixed-text.fullwidth-ascii`

**Related rule id:** `clreq.mixed-text.fullwidth-ascii`

**Status:** Active Golden Review Fixture for mixed-text fullwidth ASCII forms.

**Input surface:** i18n

**Locale context:** Traditional Chinese (`zh-Hant`). The rule applies across `Hans` and `Hant` unless a Project Override says the fullwidth style is intentional.

**Project Overrides:** None.

**Matching policy:** `contract`

## Input

```json
{
  "zh-Hant": {
    "release": "支援 ＡＰＩ 版本 ２．０。"
  }
}
```

## Expected Review Suggestion

```text
[normal] clreq.mixed-text.fullwidth-ascii: Mixed Chinese-Western text is using fullwidth ASCII forms as stored text.

影响： Fullwidth ASCII as a historical layout workaround; modern layout engines can handle Latin letters and numerals with appropriate fonts.
Suggested change: Use ordinary ASCII in Latin and numeric runs, for example `支援 API 版本 2.0。`, unless the fullwidth form is an intentional brand or preservation requirement.
Source: CLReq, Composition of Chinese and Western Mixed Texts.
Confidence: high
```
