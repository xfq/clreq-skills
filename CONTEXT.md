# Chinese Web Text Agent Rules

This context defines the domain language for packaging Chinese web text layout and copy-editing practices so coding agents can review web content consistently.

## Language

**Universal Rule Package**:
A platform-neutral collection of Chinese web text review rules, examples, and diagnostic guidance that can be reused by multiple coding agents.
_Avoid_: Skill, prompt, checklist

**Platform Adapter**:
A thin wrapper that maps the Universal Rule Package into a specific coding agent's installation, trigger, and output conventions.
_Avoid_: Rule package, integration

**Reference Adapter**:
A platform-neutral adapter written for general agent instruction files, used as the baseline for platform-specific adapters.
_Avoid_: Generic rules, fallback prompt

**Implementation Check**:
A review rule for web platform markup, styling, or localization implementation that affects how Web-facing Chinese Text is rendered or understood.
_Avoid_: CLReq-backed rule, lint rule

**Style Suggestion**:
A lower-priority review rule about wording, tone, terminology, or editorial consistency for Web-facing Chinese Text.
_Avoid_: CLReq-backed rule, mandatory fix

**Source Citation**:
A compact reference from an Atomic Rule Card to a relevant CLReq, W3C, Unicode, HTML, CSS, or other authoritative source, usually by title, URL, section, and version or retrieval marker.
_Avoid_: Quotation, evidence dump

**Source Group**:
A category inside an Atomic Rule Card that separates CLReq-related sources, Web Platform sources, and other sources so agents can explain the basis of a Review Suggestion accurately.
_Avoid_: Source type, reference bucket

**Review Severity**:
The review strength assigned to a rule or suggestion, using `blocking`, `strong`, `normal`, or `advisory` instead of linter-style error levels.
_Avoid_: Error level, lint severity

**Project Override**:
An explicit project-level decision that changes whether or how a rule is applied, such as default locale, enabled rules, severity, or style-suggestion policy, without changing the source facts behind the rule.
_Avoid_: Local fork, source override

**Golden Review Fixture**:
A paired input and expected Review Suggestion example used to show how an Atomic Rule Card should be applied by agents.
_Avoid_: Unit test, linter fixture

**Rule Admission Criteria**:
The minimum quality bar an Atomic Rule Card must meet before entering the first Universal Rule Package, including required metadata, applicability, examples, ignore conditions, Source Citations, locale handling, and fixture coverage.
_Avoid_: Definition of done, checklist

**Derived Guidance**:
Agent-facing guidance derived from CLReq and related sources, written in the rule package's own words and linked back to sources。
_Avoid_: Standard text

**clreq-skills**:
The chosen project name for the Universal Rule Package and its Platform Adapters.
_Avoid_: W3C skills

**Auto-fixable Rule**:
A rule whose correction is mechanical enough for an agent to apply when the user explicitly requests changes.
_Avoid_: Safe rule, mandatory fix

**Suggest-only Rule**:
A rule that requires context-sensitive judgment and should normally be reported as a Review Suggestion rather than applied automatically.
_Avoid_: Optional rule, weak rule

**Human-decision Rule**:
A rule whose correct outcome depends on a product, locale, brand, legal, or editorial decision that the agent should ask the user to resolve.
_Avoid_: Unsupported rule, blocker

**Atomic Rule Card**:
A single, self-contained rule definition with applicability, severity, detection guidance, sources, examples, and agent-facing review guidance.
_Avoid_: Article, checklist item, prompt fragment

**Coarse Trigger**:
A platform-specific decision that a task or file likely contains Web-facing Chinese Text and should load the Universal Rule Package.
_Avoid_: Detection rule, full scan

**Detection Signal**:
A rule-level clue that helps an agent decide whether an Atomic Rule Card applies to a specific piece of Web-facing Chinese Text.
_Avoid_: Trigger, linter rule

**Locale-specific Rule**:
A rule whose applicability or recommendation depends on a Chinese language tag, script, or region.
_Avoid_: localized rule

**Ambiguous Chinese Locale**:
A Chinese language context that does not provide enough script or region information to choose between locale-specific recommendations.
_Avoid_: zh