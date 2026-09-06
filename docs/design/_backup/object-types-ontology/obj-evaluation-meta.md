---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Meta-epistemic evaluation (object candidate)
---
# Object candidate — Evaluation (meta-epistemic)

## Role

A meta-epistemic evaluation states the epistemic status of another object or relation.

Its role is to track epistemic standing along a specified dimension.

*Example*: "this argument is weak because its warrant is defeated" is a meta-epistemic evaluation.

*Evaluation dimensions*:

- support
- defeat
- robustness
- confidence
- validity scope
- controversy

## Properties

**Truth-apt**: Yes, when the evaluation states an epistemic status or dependence relation.

**Functional stratum**: Meta-epistemic

**Internal structure**:

- **Target.** Object or relation whose epistemic status is evaluated.
- **Dimension.** Aspect being evaluated, such as support, defeat, robustness, or confidence.
- **Value.** Status assigned along the dimension.
- **Basis.** Evidence, argument, norm, or framework that supports the value.
- **Scope.** Domain or conditions under which the value holds.

## Encoding options

### Reflexive claim

**Category:** Subtype object

**Specification:** Use a reflexive `CLAIM` whose target is another object, such as an `ARGUMENT`, `MODEL`, `CLAIM`, or `METHOD` (e.g., this model is inadequate).

**Pros.**
- Keeps evaluative judgments explicit and contestable.
- Fits evaluations that assert a proposition about another object.

**Cons.**
- Needs reflexive target constraints to avoid ordinary object-level claims.

### Status annotation

**Category:** Annotation on another object

**Specification:** Attach a controlled status directly to the evaluated object (e.g., accepted, rejected, or open).

**Pros.**
- Fits scalar or controlled status values.

**Cons.**
- Cannot express reasons for the status without linked claims or arguments.
- Fails when a separate reason, criterion, or support object must be represented.

### Evaluation composite

**Category:** Composite object

**Specification:** Combine the evaluated object with `NORM` or criterion objects, cited `EVIDENCE`, supporting `ARGUMENT`, and a resulting status `CLAIM` (e.g., model accepted for fit).

**Pros.**
- Supports audit, comparison, and revision of the evaluation.

**Cons.**
- Adds structure for cases where a status value suffices.

## Subtypes

Subtypes are meaningful along one dimension: the assessed dimension of epistemic standing.

| Label                 | Description                                           | Encoding                                                         | Assessment                                                  |
| --------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| Support evaluation    | Rates how strongly an object supports another object. | `EVALUATION` subtype linked to `ARGUMENT` or `EVIDENCE`.         | Stable when support strength is queried.                    |
| Confidence evaluation | Assigns confidence or credibility.                    | Status annotation or `EVALUATION` subtype.                       | Subtype only when reasons and criteria need representation. |
| Robustness evaluation | Tests whether a result persists under changes.        | `EVALUATION` subtype linked to `MODEL`, `METHOD`, or `EVIDENCE`. | Useful when perturbation behavior matters.                  |
| Defeat evaluation     | Records attack, defeat, or undercutting status.       | `EVALUATION` subtype linked to `OBJECTION` or attack edge.       | Stable in dialectical graphs.                               |
| Scope evaluation      | States where a claim, model, or method applies.       | `EVALUATION` subtype linked to target scope.                     | Often an annotation unless scope is contested.              |
