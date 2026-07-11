# Fixture: context-dependent Simplified-Traditional conversion

**Fixture id:** `locale-sensitive-variants.contextual-conversion`

**Related rule id:** `clreq.variants.contextual-hans-hant-conversion`

**Status:** Active Golden Review Fixture for context-dependent Chinese variants.

**Input surface:** i18n

**Locale context:** Traditional Chinese (`zh-Hant`) target string. The source appears mechanically converted or copied from Simplified Chinese.

**Project Overrides:** None.

**Matching policy:** `contract`

## Input

```json
{
  "zh-Hant": {
    "headline": "新品发售：护发套装"
  }
}
```

## Expected Review Suggestion

```text
[strong] clreq.variants.contextual-hans-hant-conversion: This Traditional Chinese string appears to need context-sensitive variant review.

Why it matters: CLReq notes that Simplified-Traditional mappings are not always one-to-one, so mechanical conversion can choose the wrong character for the intended meaning.
Suggested change: Confirm the target wording with a glossary or human reviewer; for this meaning, `新品發售：護髮套裝` is likely the intended Traditional Chinese form.
Source: CLReq, Characters used for Chinese Composition.
Confidence: medium
```
