# Object candidate — Norm / Criterion / Rule / Principle

## Role

A norm or criterion states an epistemic standard.

Its role is to constrain judgment within a framework. A norm can attach locally to a method or globally to a framework.

*Example*: parsimony is a criterion when it ranks simpler models over more complex alternatives.

*Examples of constrained judgments*:

- admissibility
- adequacy
- validity
- acceptability
- preference

*Examples of criteria*:

- adequacy condition
- explanatory norm
- admissibility rule
- interpretation constraint
- model selection principle

## Properties

**Truth-apt**: Derivative. A norm guides judgment; claims that the norm applies or is adequate are truth-apt.

**Functional stratum**: Normative

**Internal structure**:

- **Standard.** Rule, criterion, or principle invoked.
- **Target.** Object or move governed by the standard.
- **Force.** Permission, requirement, prohibition, ranking, or preference.
- **Scope.** Domain or framework where the standard applies.
- **Ground** (context-dependent). Rationale or authority for the standard.

## Encoding options

### Normative claim

**Category:** Subtype object

**Specification:** Use `CLAIM` for a contestable proposition about what counts, guides, or constrains (e.g., prefer simpler models).

**Pros.**
- Keeps criteria and principles truth-apt and contestable.
- Separates normative force from ordinary descriptive assertion through modality.

**Cons.**
- Needs deontic properties so normative claims do not behave like descriptive claims.

### Method constraint

**Category:** Annotation on another object

**Specification:** Attach the norm to `METHOD` (e.g., preregister before testing).

**Pros.**
- Fits operational rules that govern method use.
- Works when the norm only governs how that method starts, proceeds, or stops.

**Cons.**
- Hides norms that also govern claims, models, or frameworks.
- Can make a contestable standard look like a method property.

### Framework standard

**Category:** Annotation on another object

**Specification:** Attach the norm to `FRAMEWORK` (e.g., Bayesian coherence).

**Pros.**
- Captures broad admissibility conditions.
- Works when the norm governs many `CLAIM`, `ARGUMENT`, `MODEL`, or `METHOD`s across the inquiry.

**Cons.**
- Can bury a contestable norm inside background structure.
- Needs links back to claims or arguments that justify the standard.

## Subtypes

Three independent dimensions organize norms and criteria:

- **Normative form.** What kind of standard the object is. This dimension drives subtypes.
- **Governed target.** Which object the standard governs. This dimension is encoded as a relation to another object.
- **Binding force.** How strongly the standard binds. This dimension is encoded as an attribute.

### Normative form

Normative form classifies the type of standard.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Criterion | Supplies a basis for assessment, comparison, or ranking. | `NORM` subtype. | Stable when scoring or selection matters. |
| Rule | States an explicit permission, requirement, or prohibition. | `NORM` subtype. | Stable when deontic form matters. |
| Principle | Gives a broad guiding standard across many cases. | `NORM` subtype. | Stable when scope exceeds one local target. |
| Constraint | Sets a boundary on what counts as admissible. | `NORM` subtype. | Stable when admissibility limits matter. |
| Preference | Ranks one option above another without strict exclusion. | `NORM` subtype. | Stable when tradeoffs are central. |

### Governed target

Governed target identifies what the norm constrains.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Methodological | Governs a `METHOD`. | Relation from `NORM` to `METHOD`. | Cross-cuts form: a methodological norm may be a rule, criterion, principle, constraint, or preference. |
| Evaluative | Governs an `EVALUATION` or `COMPARISON`. | Relation from `NORM` to `EVALUATION` or `COMPARISON`. | Cross-cuts form; often combines criterion and preference. |
| Interpretive | Governs an `INTERPRETATION`. | Relation from `NORM` to `INTERPRETATION`. | Useful when admissible readings depend on standards. |
| Evidential | Governs `EVIDENCE` or evidence use. | Relation from `NORM` to `EVIDENCE` or `ARGUMENT`. | Useful when admissible support depends on source quality. |
| Argumentative | Governs an `ARGUMENT` or support relation. | Relation from `NORM` to `ARGUMENT`. | Useful when warrant quality or defeat conditions matter. |
| Framework-level | Governs many objects through a `FRAMEWORK`. | Relation from `NORM` to `FRAMEWORK`. | Useful when the standard applies across a reasoning space. |

### Binding force

Binding force states how strongly the norm applies.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Mandatory | The target must satisfy the norm. | Force attribute on `NORM`. | Fits requirements and strict rules. |
| Permissive | The norm allows a move or object. | Force attribute on `NORM`. | Fits admissibility licenses. |
| Prohibitive | The norm rules out a move or object. | Force attribute on `NORM`. | Fits exclusions and bans. |
| Defeasible | The norm applies unless overridden. | Force attribute on `NORM`. | Fits standards with exceptions. |
| Preferential | The norm ranks one option above another. | Force attribute on `NORM`. | Fits non-strict priorities and tradeoffs. |
