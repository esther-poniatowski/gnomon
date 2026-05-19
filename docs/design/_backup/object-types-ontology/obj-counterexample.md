# Object candidate — Counter-example

## Role

A counterexample is an example that defeats a target claim.

Its role is to show that a general commitment fails under a specific instance or construction.

*Example*: a black swan is a counterexample to the claim that all swans are white.

*Examples of defeated commitments*:

- universal claim
- modal claim
- equivalence claim
- classificatory claim

## Properties

**Truth-apt**: Yes. A counterexample asserts that an instance defeats a target claim.

**Functional stratum**: Dialectical

**Internal structure**:

- **Target.** Claim, criterion, proof step, or classification being defeated.
- **Instance.** Case or construction that creates the failure.
- **Defeat mode.** Universality, implication, equivalence, necessity, sufficiency, or proof step challenged.
- **Failure point.** Feature of the instance that makes the target fail.
- **Scope.** Range over which the defeat applies.

## Encoding options

### Refuting example subtype

**Category:** Subtype object

**Specification:** Use `EXAMPLE` as the carrier and require an asymmetric refutation relation to the universal or general `CLAIM` (e.g., a black swan refutes "all swans are white").

**Pros.**
- Preserves the example structure while marking defeat behavior.
- Keeps the target general claim explicit.

**Cons.**
- Depends on `EXAMPLE` as a stable subtype or case object.

### Objection pattern

**Category:** Composite object

**Specification:** Combine a case-level `EXAMPLE` with an `OBJECTION` that targets the defeated `CLAIM` (e.g., the black swan defeats the universal claim).

**Pros.**
- Makes the dialectical force explicit.

**Cons.**
- Heavier than needed for routine mathematical counterexamples.

### False instance claim

**Category:** Subtype object

**Specification:** Use a refuting `CLAIM` with a target relation to a universal `CLAIM` (e.g., there exists a black swan).

**Pros.**
- Fits simple universal refutations.
- Works when one instance statement exhausts the counterexample.

**Cons.**
- Hides the structural role of the case unless the target relation is explicit.
- Treats counterexample force as ordinary false-instance content.

## Subtypes

Subtypes are meaningful along one dimension: the defeat mode against the target.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Universal counterexample | Refutes a universal claim through one instance. | `COUNTEREXAMPLE` subtype targeting universal `CLAIM`. | Core case. |
| Modal counterexample | Refutes necessity, possibility, or impossibility. | `COUNTEREXAMPLE` subtype targeting modal `CLAIM`. | Stable when modal force guides evaluation. |
| Equivalence counterexample | Breaks a proposed biconditional or identity. | `COUNTEREXAMPLE` subtype with two-sided target relation. | Useful when each direction can fail separately. |
| Classificatory counterexample | Shows that a criterion misclassifies a case. | `COUNTEREXAMPLE` subtype targeting `CLASSIFICATION` or criterion `CLAIM`. | Stable near taxonomy revision. |
| Proof-step counterexample | Shows that a proof move or lemma fails. | `COUNTEREXAMPLE` subtype targeting `DERIVATION / PROOF` step. | Useful when refutation attaches to the warrant rather than the conclusion. |
