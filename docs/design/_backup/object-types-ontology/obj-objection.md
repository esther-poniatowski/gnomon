---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Objection (object candidate)
---
# Object candidate — Objection

## Role

An objection is a targeted attack against an epistemic object.

Its role is to state a defect in the target.

An objection may also serve as a premise in a counterargument.

*Example*: "the model omits a confounder" is an objection to a causal model.

*Examples of defects*:

- failure
- weakness
- overreach
- lack of warrant
- need for revision

## Properties

**Truth-apt**: Yes, when the objection asserts a defect in its target. Its attack relation is dialectical.

**Functional stratum**: Dialectical

**Internal structure**:

- **Target.** Claim, argument, mechanism, model, method, or interpretation attacked.
- **Locus.** Part of the target under attack.
- **Attack mode.** Undercutting, rebutting, limiting, ambiguity, counterexample, or underdetermination.
- **Content.** Claim or evidence that creates the attack.
- **Repair demand** (context-dependent). Revision, qualification, rejection, or further support required.

## Encoding options

### Adversarial argument

**Category:** Subtype object

**Specification:** Treat objection as an adversarial `ARGUMENT` with a target `CLAIM`, `ARGUMENT`, `MODEL`, or `MECHANISM` (e.g., counterexample against a universal claim).

**Pros.**
- Preserves premises, warrant, and defeat structure.
- Works when the challenge has premises and a warrant.

**Cons.**
- Too heavy for objections that only assert a defect.

### Targeted claim

**Category:** Subtype object

**Specification:** Use `CLAIM` as a truth-apt challenge aimed at a `CLAIM`, `ARGUMENT`, `MODEL`, or `MECHANISM` (e.g., the model omits a confounder).

**Pros.**
- Works when the objection content is a single truth-apt statement.

**Cons.**
- Hides dialectical structure unless defeat mode is explicit.

### Attack edge

**Category:** Relation (graph edge)

**Specification:** Use an asymmetric attack edge from a challenging `CLAIM`, `ARGUMENT`, `EXAMPLE`, or `EVIDENCE` object (e.g., black swan attacks universal claim).

**Pros.**
- Keeps simple attacks visible without a new object.
- Works when the challenging object already exists.

**Cons.**
- Cannot store backing, scope, or rebuttal structure by itself.

## Subtypes

Subtypes are meaningful along one dimension: how the objection attacks its target.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Rebutting objection | Attacks the target conclusion directly. | `OBJECTION` subtype targeting `CLAIM`. | Core case. |
| Undercutting objection | Attacks the warrant or support relation. | `OBJECTION` subtype targeting `ARGUMENT` or support edge. | Stable when defeat targets support rather than conclusion. |
| Counterexample objection | Uses an instance to refute a general target. | `OBJECTION` linked to `COUNTEREXAMPLE`. | Use `COUNTEREXAMPLE` when the case is independently important. |
| Scope objection | Challenges the range of applicability. | `OBJECTION` subtype targeting scope attribute or `EVALUATION`. | Often becomes a scope evaluation. |
| Adequacy objection | Challenges a model, method, mechanism, or explanation as insufficient. | `OBJECTION` subtype targeting non-claim object. | Stable when repair demands matter. |
