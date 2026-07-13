# Universal Rule Package

This directory hosts Atomic Rule Cards for Web-facing Chinese Text.

First-version categories:

- language metadata
- Chinese punctuation
- Chinese-Western mixed text
- line breaking and wrapping
- typography CSS
- vertical writing
- ruby and annotations
- locale-sensitive variants

Every rule must satisfy the Rule Admission Criteria before it is included.

## Current Rule Cards

- `language-metadata/lang-specificity.json`: advisory Implementation Check for bare `zh` language metadata when Web-facing Chinese Text may need script or region context.
- `punctuation/chinese-pause-marks.json`: CLReq-backed review for ASCII sentence punctuation in Web-facing Chinese Text.
- `mixed-text/fullwidth-ascii.json`: CLReq-backed review for fullwidth ASCII forms in mixed Chinese-Western text.
- `locale-sensitive-variants/contextual-hans-hant-conversion.json`: CLReq-backed human-decision rule for context-dependent Simplified-Traditional conversion.
- `vertical-writing/avoid-transform-rotate.json`: Implementation Check for readable vertical Web-facing Chinese Text implemented with visual rotation.
- `vertical-writing/upright-single-alphanumerics.json`: CLReq-backed review for keeping standalone Latin letters, Arabic numerals, and initialisms upright in vertical Chinese text.
- `ruby-annotations/semantic-ruby-markup.json`: Implementation Check for ruby-like annotations that lack semantic HTML ruby markup.

Rule cards must validate against `../schema/rule-card.schema.json` and include source citations for factual guidance.
