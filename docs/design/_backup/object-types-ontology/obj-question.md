# Object candidate — Question

## Role

A question specifies an erotetic gap: what blocks current inquiry or what current understanding lacks.

Its role is to open and organize inquiry by guiding what can count as a relevant answer or required object.

Deferred or unresolved questions need explicit tracking so they do not collapse into problem resolution.

*Example*: "what explains the anomaly?" is a question.

## Properties

**Truth-apt**: No

**Functional stratum**: Erotetic

**Internal structure**:

- **Gap.** Missing element or obstacle that blocks current inquiry.
- **Presupposed claims.** Commitments required for the question to arise.
- **Answer type.** Kind of object expected as an answer.
- **Answer criteria.** Conditions under which the question counts as answered.
- **Subquestions** (context-dependent). Dependent questions that break down the gap.

## Encoding options

### Inquiry primitive

**Category:** Primitive object

**Specification:** Keep `QUESTION` as the object that governs which `CLAIM`, `CONCEPT`, `MODEL`, `METHOD`, or `EXPLANATION`s can count as answers (e.g., what explains the anomaly?).

**Pros.**
- Preserves answer conditions, admissible answer types, and inquiry structure without converting them into truth conditions.
- Keeps questions distinct from claims about ignorance, because a question specifies what would close inquiry.

**Cons.**
- Needs explicit links from presuppositions and candidate answers to `CLAIM`.
- Needs type-token tracking when the same inquiry pattern appears in several contexts.

### Claim partition

**Category:** Reduction to another object

**Specification:** Replace the question with a partition of possible answer `CLAIM`s (e.g., yes, no, or unknown).

**Pros.**
- Fits formal erotetic settings where questions act as partitions of logical space.

**Cons.**
- Loses presuppositions, answer constraints, and subquestion behavior in research contexts.
- Turns erotetic structure into a logical partition and hides why subclaims enter the inquiry.
- Fails when inquiry control or subquestion structure must remain visible.

### Method directive

**Category:** Reduction to another object

**Specification:** Use `METHOD` plus unresolved `CLAIM` targets (e.g., test whether the effect exists).

**Pros.**
- Works for narrow task prompts that only trigger a procedure.
- Fits questions that merely instruct a procedure.

**Cons.**
- Obscures what counts as an answer and why subquestions enter the inquiry.
- Conflates the target of inquiry with the procedure for reaching it.

### Subquestion relation

**Category:** Relation (graph edge)

**Specification:** Use an asymmetric edge between `QUESTION`s (e.g., answering Q1 helps answer Q2).

**Pros.**
- Preserves subquestion structure without treating each subquestion as a different object kind.
- Works when the child question is part of the parent question's answer path.

**Cons.**
- The edge alone cannot store answer constraints or presuppositions.

## Subtypes

Subtypes are meaningful along one dimension: the expected answer type.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Whether-question | Expects a yes, no, or suspended answer. | `QUESTION` subtype with answer `CLAIM` partition. | Stable when answer space is closed. |
| What-question | Expects an object, concept, classification, or value. | `QUESTION` subtype linked to expected object type. | Stable when answer type controls graph behavior. |
| Why-question | Expects an explanation. | `QUESTION` subtype linked to `EXPLANATION`. | Stable because explanatory relevance differs from truth alone. |
| How-question | Expects a mechanism, method, or process. | `QUESTION` subtype linked to `MECHANISM` or `METHOD`. | Stable when procedure or production is sought. |
| Comparison question | Expects a comparative judgment. | `QUESTION` subtype linked to `COMPARISON`. | Stable when dimensions and target set matter. |
| Subquestion | Contributes to answering another question. | `QUESTION` linked by asymmetric subquestion edge. | Usually a relation, not a subtype. |
