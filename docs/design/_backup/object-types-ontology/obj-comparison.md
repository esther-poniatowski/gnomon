---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Comparison (object candidate)
---
# Object candidate — Comparison

## Role

A comparison relates two or more objects along a shared respect.

Its role is to state a comparative relation that matters for a question.

*Example*: comparing two models by predictive accuracy and interpretability is a comparison.

*Usages*:

- similarity
- difference
- ordering
- tradeoff
- equivalence

## Properties

**Truth-apt**: Yes, when the comparison asserts a comparative relation. Comparing objects is not truth-apt by itself.

**Functional stratum**: Comparative

**Internal structure**:

- **Relata.** Objects being compared.
- **Axis.** Respect along which the comparison is made.
- **Standard.** Criterion that makes the comparison meaningful.
- **Outcome.** Similarity, difference, ranking, tradeoff, or equivalence asserted.
- **Consequence** (context-dependent). Choice, distinction, classification, or evaluation supported by the comparison.

## Encoding options

### Comparative claim

**Category:** Subtype object

**Specification:** Use a comparative `CLAIM` about named target objects (e.g., model A is simpler than model B).

**Pros.**
- Fits truth-apt comparative judgments.

**Cons.**
- Needs explicit dimensions so comparison does not become a vague assertion.

### Comparison relation

**Category:** Relation (graph edge)

**Specification:** Use symmetric or ordered edges directly between the compared objects (e.g., similar-to or more-accurate-than).

**Pros.**
- Keeps simple equivalence, similarity, or contrast links lightweight.

**Cons.**
- Cannot represent criteria, evidence, or ranked results by itself.
- Fails when a criterion, evidence object, or result object must be stored.

### Evaluated comparison composite

**Category:** Composite object

**Specification:** Combine target objects with `NORM` or criterion objects, supporting `ARGUMENT`, and a result `CLAIM` (e.g., model A wins on predictive fit).

**Pros.**
- Supports multi-criterion comparison and review.
- Keeps finite comparison distinct from classification of a domain.
- Works when the comparison has reviewable grounds.

**Cons.**
- Heavier than needed for local comparative claims.

## Subtypes

Subtypes are meaningful along one dimension: the comparative relation asserted between the relata.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Similarity comparison | Identifies shared features across relata. | `COMPARISON` subtype with symmetric relation and shared axis. | Stable when analogy, classification, or transfer depends on shared structure. |
| Contrast comparison | Identifies differences across relata. | `COMPARISON` subtype with symmetric relation and contrast axis. | Stable when distinction or boundary work depends on the contrast. |
| Ordering comparison | Ranks relata along an ordered axis. | `COMPARISON` subtype with asymmetric or total-order relation. | Stable because direction and transitivity matter. |
| Tradeoff comparison | Relates gains on one axis to losses on another. | `COMPARISON` subtype with at least two axes and criterion weights. | Stable when evaluation must preserve competing criteria. |
| Equivalence comparison | States interchangeability or sameness under a criterion. | `COMPARISON` subtype with symmetric relation and equivalence scope. | Stable when substitution, reduction, or classification depends on equivalence. |
