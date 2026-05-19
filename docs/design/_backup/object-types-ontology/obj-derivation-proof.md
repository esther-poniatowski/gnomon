# Object candidate — Derivation / Proof

## Role

A derivation or proof gives an ordered chain of warranted steps from accepted starting points to a target claim.

Its role is to certify why the target follows. Each proof has one target claim, while several distinct proofs may support the same claim.

*Example*: an induction proof that establishes a formula for all natural numbers is a derivation or proof.

## Properties

**Truth-apt**: No. A proof can be valid, complete, or defective; the proved claim is truth-apt.

**Functional stratum**: Inferential

**Internal structure**:

- **Target.** Claim or result to be proved.
- **Starting points.** Premises, axioms, assumptions, or prior results.
- **Rules.** Inference rules, algebraic moves, or admissible transformations.
- **Steps.** Ordered chain from starting points to target.
- **Gaps** (context-dependent). Missing, informal, or deferred steps.

## Encoding options

### Deductive argument subtype

**Category:** Subtype object

**Specification:** Treat proof as an `ARGUMENT` subtype whose warrant must be deductive and whose conclusion is a theorem-like `CLAIM` (e.g., the lemma follows by induction).

**Pros.**
- Reuses the premise, conclusion, warrant, and backing structure of `ARGUMENT`.

**Cons.**
- Needs extra proof-specific constraints to track rule validity and step dependency.

### Formal step composite

**Category:** Composite object

**Specification:** Compose proof steps from `CLAIM`s and rule applications, then close the composite with a theorem-like `CLAIM` (e.g., base case, induction step, theorem).

**Pros.**
- Matches formal logic practice where proof steps and inference rules carry the structure.

**Cons.**
- Makes the proof as a whole harder to attack, cite, or compare unless the composite is reified.

## Subtypes

Subtypes are meaningful along one dimension: the kind of warranted chain that certifies the target.

| Label              | Description                                           | Encoding                                                                | Assessment                                            |
| ------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------- |
| Formal proof       | Derives a target claim by explicit rules.             | `DERIVATION / PROOF` subtype linked to theorem-like `CLAIM`.            | Core subtype for audit and citation.                  |
| Calculation        | Transforms expressions to obtain a result.            | `DERIVATION / PROOF` subtype with algebraic or computational steps.     | Stable when transformation steps are the main object. |
| Proof sketch       | Gives partial structure without full step detail.     | `DERIVATION / PROOF` subtype with gap annotations; alternatively `STRATEGY / PLANNING` when it guides proof completion rather than certifying the target. | Useful when incompleteness must stay visible; use `STRATEGY / PLANNING` when the object is a plan rather than a partial warrant. |
| Construction proof | Produces an object that satisfies a target condition. | `DERIVATION / PROOF` subtype linked to `EXAMPLE` or constructed object. | Stable when the proof output is a witness.            |
