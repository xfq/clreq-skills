# Expected Review Suggestions

```text
[advisory] clreq.metadata.lang-specificity: The page uses a bare `zh` language tag for Web-facing Chinese Text.

影响： Some Chinese text recommendations depend on script or region, and the agent should not assume Simplified or Traditional Chinese from `zh` alone.
Suggested change: Confirm the intended locale and use a more specific BCP 47 language tag such as `zh-Hans` or `zh-Hant` when appropriate.
Source: HTML Standard; BCP 47; W3C Internationalization language tag guidance.
Confidence: medium

[normal] clreq.punctuation.chinese-pause-marks: Chinese prose is using ASCII sentence punctuation.

影响： CLReq describes Chinese pause punctuation as part of Chinese text layout, and ASCII punctuation can make Chinese UI copy look inconsistent unless a technical or editorial exception applies.
Suggested change: Replace the comma and sentence-final period with Chinese punctuation: `今天下单，明天发货。`
Source: CLReq, Categories and usage of punctuation marks; CLReq, Composition of Chinese and Western Mixed Texts.
Confidence: high

[normal] clreq.vertical-writing.avoid-transform-rotate: Web-facing Chinese Text is rotated visually instead of using vertical writing layout.

影响： CSS transforms rotate the painted box, but vertical writing needs text layout behavior for line progression, punctuation, and mixed Latin or numeric text.
Suggested change: Use `writing-mode` with an appropriate vertical direction and review `text-orientation` for Latin text and numerals; keep visual rotation only for decorative or explicitly reviewed cases.
Source: CSS Writing Modes, writing-mode and text-orientation; CLReq, Writing modes.
Confidence: medium
```
