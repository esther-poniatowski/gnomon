---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Concept (object candidate)
---
# Object candidate — Concept

## Role

A concept names a theoretical item and fixes what counts as an instance.

Its role is to give other epistemic objects a stable semantic handle.

Concepts therefore support reasoning without themselves asserting claims.

*Example*: "fitness" is a concept when it anchors claims about reproductive success.

*Examples of targets using concepts*:

- claims
- questions
- models
- distinctions
- definitions

## Properties

**Truth-apt**: No

**Functional stratum**: Semantic

**Internal structure**:

- **Referent.** Theoretical object, property, relation, or category named by the concept.
- **Labels.** Terms, symbols, or variants that refer to the concept.
- **Definitions.** Linked formulations that fix or refine use.
- **Boundary.** Conditions for inclusion and exclusion.
- **Neighbors** (context-dependent). Adjacent concepts that constrain meaning.

## Encoding options

### Thin semantic anchor

**Category:** Primitive object

**Specification:** Keep `CONCEPT` as the semantic anchor that `CLAIM`, `QUESTION`, `MODEL`, and `CLASSIFICATION`s can share without inheriting truth-apt content (e.g., fitness, validity).

**Pros.**
- Breaks the circularity in which claims require concepts while concepts derive from claims.
- Supports a [primitive operation schema](../../3-aspect-specific/ontology.md#^t3-concept-type-taxonomy) for concept definition with fixed semantics.

**Cons.**
- Leaves applicability and scope to linked `CLAIM`s rather than intrinsic concept content.

### Claim cluster

**Category:** Reduction to another object

**Specification:** Replace the concept with a handle that groups definitional, exclusionary, comparative, and inferential `CLAIM`s (e.g., claims that fix "fitness").

**Pros.**
- Fits systems that only need explicit propositional content in reasoning graphs.

**Cons.**
- Conflates asserting a proposition with fixing the meaning of terms used in propositions.

### Constitutive claim subtype

**Category:** Subtype object

**Specification:** Store explicit concept content in constitutive `CLAIM`s while the `CONCEPT` remains the target those claims define or circumscribe (e.g., "fitness means reproductive success").

**Pros.**
- Preserves the dual status of definitions as statements with truth conditions and concept anchors.

**Cons.**
- Requires a strict boundary between the semantic object and its propositional encoding.

## Subtypes

No subtype exists a priori. Concepts differ by domain, abstraction level, and theoretical role, but those differences belong to annotations or relations to definitions, claims, models, and classifications.
