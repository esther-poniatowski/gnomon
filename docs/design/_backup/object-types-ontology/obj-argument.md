---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Argument (object candidate)
---
# Object candidate — Argument

## Role

An argument connects premises to a conclusion through an explicit warrant.

Its role is to make inferential support or attack explicit.

*Example*: the premises "all mammals are warm-blooded" and "whales are mammals" support the conclusion "whales are warm-blooded" through a deductive warrant.

*Usages*:

- support for a conclusion
- support for the strength of a claim
- attack against a target claim

## Properties

**Truth-apt**: No. An argument can be valid, strong, sound, or defeated; its conclusion is truth-apt.

**Functional stratum**: Inferential

**Internal structure**:

- **Conclusion.** Claim supported or attacked.
- **Premises.** Claims or evidence from which the argument proceeds.
- **Warrant.** Rule, pattern, or principle that licenses the move.
- **Force.** Deductive, inductive, abductive, analogical, or defeasible mode.
- **Defeaters** (context-dependent). Objections or counterconditions that weaken the move.

## Encoding options

### Reified inference

**Category:** Composite object

**Specification:** Reify the inferential move that connects premise `CLAIM`s to a conclusion `CLAIM`, with warrant and backing attached to the move rather than to the claims (e.g., P; if P then Q; so Q).

**Pros.**
- Preserves the warranted move from premises to conclusion as an addressable object.
- Distinguishes semantic dependence, evidential support, inferential derivation, and rhetorical adjacency.
- Allows several arguments with different warrants to support the same conclusion.

**Cons.**
- Its need comes from graph use and evaluation, not strict ontological irreducibility.

### Typed support edge

**Category:** Relation (graph edge)

**Specification:** Use asymmetric support edges from premise `CLAIM`s to a conclusion `CLAIM` (e.g., P supports Q).

**Pros.**
- Keeps the object taxonomy small when inferential moves need little internal structure.
- Works when the warrant need not be cited, attacked, or reused as a unit.

**Cons.**
- Diffuses warrant, backing, and defeat behavior across edge annotations.
- Makes validity assessment, warrant review, and defeater analysis harder to target.

### Primitive argument

**Category:** Primitive object

**Specification:** Promote the inferential move to a primitive object (e.g., a modus ponens step).

**Pros.**
- Makes the structure that gives reasons visible as the unit of evaluation.
- Supports attack, reuse, comparison, and mapping across argument tokens.
- Works when review targets the whole support act rather than any premise, conclusion, or edge alone.

**Cons.**
- Risks inflating structured relations into object kinds.

### Argument variant decomposition

**Category:** Variant decomposition

**Specification:** Replace generic `ARGUMENT` with variants sorted by warrant family: deductive proof, abductive argument, analogical argument, causal argument, and dialectical objection (e.g., best-explanation inference).

**Pros.**
- Preserves different evaluation criteria for different warrants.
- Fits warrant families whose evaluation differs.

**Cons.**
- Requires type-token links when a reusable argument pattern generates a particular argument.
- Loses a single generic object for mixed or underspecified inference.

## Subtypes

Subtypes are meaningful along one dimension: the warrant that licenses support from premises to conclusion.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Deductive argument | Premises entail the conclusion under a rule of validity. | `ARGUMENT` subtype; proof may use `DERIVATION / PROOF`. | Stable subtype because validity gives distinct evaluation. |
| Inductive argument | Premises support the conclusion with ampliative strength. | `ARGUMENT` subtype with strength assessment. | Stable when degree of support matters. |
| Abductive argument | Premises support the conclusion as best explanation. | `ARGUMENT` subtype linked to `EXPLANATION`. | Stable when explanatory fit supplies the warrant. |
| Analogical argument | An `ANALOGY` licenses transfer from source to target. | `ARGUMENT` subtype citing `ANALOGY`. | Keep distinct from analogy as mapping. |
| Dialectical argument | Premises attack or defend a target in dispute. | `ARGUMENT` subtype; `OBJECTION` covers attacks. | Stable when target and defeat relations matter. |
| Transcendental argument | Premises state conditions required for a practice or claim. | `ARGUMENT` subtype with condition-of-possibility warrant. | Useful in philosophical inquiry, less central in routine graphs. |
