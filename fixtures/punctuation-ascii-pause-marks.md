# Fixture: ASCII punctuation in Chinese prose

**Fixture id:** `punctuation.ascii-pause-marks`

**Related rule id:** `clreq.punctuation.chinese-pause-marks`

**Status:** Active Golden Review Fixture for Chinese pause punctuation.

**Input surface:** HTML

**Locale context:** Simplified Chinese (`zh-Hans`). The rule does not depend on region for this finding.

**Project Overrides:** None.

**Matching policy:** `contract`

## Input

```html
<p lang="zh-Hans">今天发布新功能, 请升级到最新版本.</p>
```

## Expected Review Suggestion

```text
[normal] clreq.punctuation.chinese-pause-marks: Chinese prose is using ASCII sentence punctuation.

影响： CLReq describes Chinese pause punctuation as part of Chinese text layout, and ASCII punctuation can make Chinese UI copy look inconsistent unless a technical or editorial exception applies.
Suggested change: Replace the comma and sentence-final period with Chinese punctuation: `今天发布新功能，请升级到最新版本。`
Source: CLReq, Categories and usage of punctuation marks; CLReq, Composition of Chinese and Western Mixed Texts.
Confidence: high
```
