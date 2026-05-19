# Object candidate — Claim / Proposition

## Role

A claim is a truth-apt proposition that asserts content.

Its role is to carry commitments whose epistemic status can change under support or challenge.

A claim has truth conditions. A concept fixes meaning. A method guides operations.

==TODO: Name choice: "statement", "proposition", "judgment", "claim", or "thesis"? Possible split: the framework language supports *statements* in general (meaningful expressions used inside objects, encoded formally but that could be translated into sentences), while `CLAIM` names objects that assert an evaluable position.==

*Example*: "the output is stable under small perturbations" is a claim.

*Usages*:

- hypothesis
- conjecture
- evaluative commitment
- explanatory thesis

## Properties

**Truth-apt**: Yes

**Functional stratum**: Assertoric

**Internal structure**:

- **Content.** Proposition asserted.
- **Scope.** Domain or conditions under which the claim applies.
- **Modality** (context-dependent). Necessity, possibility, typicality, normativity, or empirical force.
- **Status.** Accepted, conjectural, refuted, open, or suspended standing.
- **Support** (context-dependent). Evidence, argument, proof, or framework commitment linked to the claim.

## Encoding options

### Truth-apt primitive

**Category:** Primitive object

**Specification:** Keep truth-apt commitment in one object type so other objects can cite, answer, support, refute, or presuppose the same proposition (e.g., the model is stable).

**Pros.**
- Preserves the difference between propositional commitment and other epistemic roles.
- Allows claims to serve as premises, conclusions, assumptions, defeaters, and answers without changing object kind.

**Cons.**
- A broad claim type needs controlled subtypes or attributes for axioms, theorems, conjectures, hypotheses, norms, and meta-claims.
- Logical expressibility does not guarantee graph adequacy when downstream operations differ.

### Claim variant decomposition

**Category:** Variant decomposition

**Specification:** Replace generic `CLAIM` with variants sorted by graph behavior: result linked to proof, axiom that grounds a framework, conjecture targeted by inquiry, normative claim, interpretive claim, and reflexive meta-claim (e.g., this argument is weak).

**Pros.**
- Preserves proof obligations, status, scope, and target behavior without forcing all content with truth conditions through one object type.
- Fits variants whose graph behavior differs.

**Cons.**
- Can proliferate subtypes if rhetorical role rather than graph behavior drives the split.
- Loses a single generic carrier for simple assertions with truth conditions.

### Reflexive meta-claim

**Category:** Subtype object

**Specification:** Use a `CLAIM` whose target is an `ARGUMENT`, `MODEL`, `METHOD`, `CLAIM`, or `FRAMEWORK` (e.g., this method is unreliable).

**Pros.**
- Supports claims about argument quality, object status, or model adequacy.
- Fits propositions that evaluate another object.

**Cons.**
- Overlaps with `EVALUATION` when the assessment needs criteria, evidence, and outcome structure.

## Subtypes

Subtypes are meaningful only when graph behavior differs, not merely because rhetoric or topic differs. Three dimensions matter, in order:

- proof or support regime
- dependency position in an inquiry
- target behavior toward other objects

| Label                    | Description                                                    | Encoding                                                                 | Assessment                                                    |
| ------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Result claim             | Proposition established by a proof or derivation.              | `CLAIM` subtype linked to `DERIVATION / PROOF`.                          | Stable when proof linkage changes citation, reuse, and audit. |
| Conjecture or Hypothesis | Proposition under active inquiry without settled support.      | `CLAIM` subtype targeted by `QUESTION`, `PROBLEM`, or `METHOD`.          | Stable when unresolved status drives graph behavior.          |
| Axiom or Postulate       | Foundational proposition introduced inside a `FRAMEWORK`.      | `CLAIM` subtype linked to `FRAMEWORK` as grounding commitment.           | Stable when dependency direction matters.                     |
| Assumption               | Proposition accepted within a local scope.                     | `CLAIM` subtype with scope relation to `ARGUMENT`, `MODEL`, or `METHOD`. | Often an attribute, but subtype status helps scope tracking.  |
| Definitional claim       | Proposition that fixes the use of a `CONCEPT`.                 | `CLAIM` subtype linked to `CONCEPT` by defines relation.                 | Stable at the concept boundary.                               |
| Empirical claim          | Proposition about observed or measured content.                | `CLAIM` subtype linked to `EVIDENCE`.                                    | Useful when evidential provenance matters.                    |
| Normative claim          | Proposition that states a standard, permission, or preference. | `CLAIM` subtype or `NORM` object.                                        | Use `NORM` when the standard governs many objects.            |
| Meta-claim               | Proposition about another epistemic object.                    | `CLAIM` subtype targeting `ARGUMENT`, `MODEL`, `METHOD`, or `FRAMEWORK`. | Stable when reflexive target behavior matters.                |
