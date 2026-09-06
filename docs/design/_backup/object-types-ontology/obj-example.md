---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Example (object candidate)
---
# Object candidate — Example

## Role

An example presents a determinate case relative to a target object.

Its role is to make a pattern accessible through a target-relative exhibition.

*Example*: a worked case where a model overfits the training data is an example of overfitting.

*Usages*:

- instance
- witness
- construction
- edge case
- boundary case
- counterexample

## Properties

**Truth-apt**: Derivative. The exhibited object is not truth-apt by itself; claims that it instantiates, witnesses, or refutes a target are truth-apt.

**Functional stratum**: Instantiative

**Internal structure**:

- **Case.** Exhibited object, construction, situation, or scenario.
- **Target.** Concept, claim, model, distinction, or criterion to which the case is attached.
- **Feature.** Pattern or property the case exhibits.
- **Use.** Instance, witness, illustration, edge case, or counterexample role.
- **Scope** (context-dependent). Conditions under which the case has that use.

## Encoding options

### Example relation

**Category:** Relation (graph edge)

**Specification:** Use asymmetric edges from a case object, `EVIDENCE`, or `CLAIM` to the `CONCEPT` or `CLAIM` that the example instantiates, tests, or refutes (e.g., this case instantiates overfitting).

**Pros.**
- Makes the example role explicit in graph behavior.
- Separates instantiating, boundary-probing, refuting, and illustrative uses.

**Cons.**
- Requires a controlled relation vocabulary.

### Claim subtype

**Category:** Subtype object

**Specification:** Use `CLAIM` as the carrier for a truth-apt instance statement plus a visible example role (e.g., this model overfits).

**Pros.**
- Fits examples whose content is fully truth-apt.
- Works when the example contributes only an instance statement.

**Cons.**
- Can hide concrete case structure when the example is a record rather than a statement.
- Damages graph behavior unless example status remains visible.

### Case composite

**Category:** Composite object

**Specification:** Combine a case object or `EVIDENCE` object with target links to `CONCEPT` or `CLAIM`s and optional existential `CLAIM` support (e.g., one observed overfitting case).

**Pros.**
- Preserves concrete cases without reducing them to a single claim.

**Cons.**
- Adds structure for examples that only need a role edge.

## Subtypes

Subtypes are meaningful along one dimension: the target-relative function of the case.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Instance | Shows that a case falls under a `CONCEPT` or `CLASSIFICATION`. | `EXAMPLE` with instantiates relation. | Core case. |
| Witness | Supplies a case that satisfies an existential or constructive claim. | `EXAMPLE` linked to target `CLAIM`. | Stable when existence support matters. |
| Boundary case | Tests the edge of a concept, criterion, or classification. | `EXAMPLE` linked to `CONCEPT`, `NORM`, or `CLASSIFICATION`. | Useful for concept refinement. |
| Counterexample | Refutes a target claim or criterion. | `COUNTEREXAMPLE` subtype or separate object. | Separate object when defeat behavior is central. |
| Construction | Gives a case produced by a method. | `EXAMPLE` linked to `METHOD` and target `CONCEPT` or `CLAIM`. | Use `METHOD` for the procedure itself. |
