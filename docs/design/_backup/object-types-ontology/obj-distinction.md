# Object candidate — Distinction

## Role

A distinction separates objects that might otherwise be conflated. It can target concepts, claims, models, methods...

Its role is to state the contrast basis, the point of non-equivalence, and the consequence of confusing the targets.

*Example*: the contrast between "selection" and "gain" is a distinction when the two concepts risk conflation.

## Properties

**Truth-apt**: Yes, when the distinction asserts a non-equivalence or contrast. The contrast relation may also be encoded as a structured claim.

**Functional stratum**: Comparative

**Internal structure**:

- **Targets.** Concepts, claims, models, or methods being separated.
- **Axis.** Respect along which the targets differ.
- **Non-equivalence.** Feature that blocks interchangeability.
- **Conflation risk.** Reason the targets might be confused.
- **Consequence** (context-dependent). Error or insight that follows from keeping them apart.

## Encoding options

### Differentiates edge

**Category:** Relation (graph edge)

**Specification:** Use a typed edge between `CONCEPT`s (e.g., selection differs from gain).

**Pros.**
- Matches distinctions that only mark non-equivalence or contrast.

**Cons.**
- Cannot store history, objections, examples, or refinements.
- Too weak when the real object is contrast analysis rather than a bare relation.

### Comparative claim

**Category:** Subtype object

**Specification:** Use `CLAIM` to state that two `CONCEPT` or `CLAIM`s must not be conflated (e.g., selection is not gain).

**Pros.**
- Preserves structured contrast without a primitive type.
- Records targets, contrast basis, non-interchangeability, and conflation conditions.

**Cons.**
- Makes conceptual disambiguation depend on the claim layer.

### Reified distinction composite

**Category:** Composite object

**Specification:** Combine contrasted `CONCEPT`s with supporting `CLAIM`, `EXAMPLE`, and `OBJECTION`s (e.g., selection versus gain).

**Pros.**
- Works when a distinction becomes a durable object of debate.
- Allows examples, objections, and refinements to attach to the distinction itself.

**Cons.**
- Over-objectifies simple relational contrasts.

## Subtypes

No subtype exists a priori. Distinctions differ by target type and contrast basis, but those differences are best encoded as target links and contrast attributes.
