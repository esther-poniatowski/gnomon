---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Definition (object candidate)
---
# Object candidate — Definition

## Role

A definition fixes the content of a semantic expression by giving a use condition or admissible formulation.

Its role is to stabilize how a concept can be used while preserving the difference between the concept and one formula for it.

A concept remains the semantic object. A definition gives admissible content to that concept or predicate. A notation assigns an expression to a referent.

*Example*: "a prime number is a natural number with exactly two positive divisors" is a definition.

*Variants*:

- canonical definition
- equivalent definition
- operational definition
- historical definition
- scope-restricted definition

## Properties

**Truth-apt**: Derivative. A definition fixes use; claims about adequacy, equivalence, or convention are truth-apt.

**Functional stratum**: Semantic

**Internal structure**:

- **Definiendum.** Concept, predicate, or term being fixed.
- **Definiens.** Content that fixes use.
- **Force.** Stipulative, descriptive, operational, canonical, or revisionary status.
- **Scope.** Domain where the definition applies.
- **Boundaries** (context-dependent). Borderline or ruled-out uses.

## Encoding options

### Definitional claim

**Category:** Subtype object

**Specification:** Use a definitional `CLAIM` for the truth-apt formulation, and link it to the `CONCEPT` whose use it fixes (e.g., "prime means exactly two positive divisors").

**Pros.**
- Keeps the truth-apt formulation addressable and contestable.

**Cons.**
- Needs a link to the `CONCEPT` whose meaning it fixes.

### Defines edge

**Category:** Relation (graph edge)

**Specification:** Use an asymmetric edge from a definitional `CLAIM` to a `CONCEPT` (e.g., "prime" defines `PRIME`).

**Pros.**
- Makes semantic circumscription explicit without adding a full object type.
- Works when the relation itself needs no separate debate object.

**Cons.**
- Cannot carry rich debate over competing definitions by itself.


## Subtypes

Subtypes are meaningful along one dimension: how the definition fixes concept use.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Stipulative definition | Introduces a use by decision or convention. | Definitional `CLAIM` linked to `CONCEPT`. | Stable when convention rather than discovery matters. |
| Descriptive definition | Records established use. | Definitional `CLAIM` with evidential or source support. | Often reducible to claim plus provenance. |
| Operational definition | Fixes use through a procedure or measurement. | Definitional `CLAIM` linked to `METHOD`. | Stable when procedure controls applicability. |
| Recursive definition | Fixes use through base clauses and generation rules. | Composite of `CLAIM`s and rule-like `METHOD`. | Stable in formal contexts. |
| Equivalence definition | Fixes use through equivalence with another concept or formulation. | Definitional `CLAIM` linked to both `CONCEPT`s. | Often a relation among concepts plus a claim. |
