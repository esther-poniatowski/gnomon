---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Strategy (object candidate)
---
# Object candidate — Strategy / Planning

## Role

A strategy is a problem-specific plan for sequencing inquiry resources under constraints.

Its role is to guide a particular inquiry path under local constraints.

A method is reusable across contexts. A strategy selects and sequences methods for a particular problem.

*Example*: a plan to run an ablation study before comparing full models is a strategy for diagnosing model components.

*Examples of sequenced resources*:

- questions
- methods
- evidence
- decisions

## Properties

**Truth-apt**: No. A strategy guides action; claims about its promise, cost, or adequacy are truth-apt.

**Functional stratum**: Strategic

**Internal structure**:

- **Goal.** Problem or inquiry target being pursued.
- **Sequence.** Ordered priorities among questions, methods, and evidence.
- **Branches.** Conditional paths under uncertainty.
- **Constraints.** Resource, time, data, or admissibility limits.
- **Fallbacks.** Alternative moves if the main path fails.
- **Rationale** (context-dependent). Reason for choosing this path.

## Encoding options

### Planning composite

**Category:** Composite object

**Specification:** Combine a selected `METHOD` or process `MODEL` with governing `QUESTION`s and rationale or constraint `CLAIM`s (e.g., run ablation before comparison).

**Pros.**
- Captures plan structure without adding a primitive.

**Cons.**
- Stretches `METHOD` toward research planning.

### Method subtype

**Category:** Subtype object

**Specification:** Treat strategy as a `METHOD` subtype that sequences procedures for a target `QUESTION` (e.g., estimate data quality, then fit the model).

**Pros.**
- Keeps procedural and planning objects in one family.
- Works when strategy mainly sequences procedures.

**Cons.**
- Increases the load on an already broad method type.

## Subtypes

Subtypes are meaningful along one dimension: the inquiry path the plan organizes.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Search strategy | Orders exploration among questions, examples, or models. | `STRATEGY` subtype linked to `QUESTION` and `METHOD`. | Stable when search order matters. |
| Proof strategy | Sequences proof methods for a target result. | `STRATEGY` subtype linked to `DERIVATION / PROOF`. | Keep distinct from reusable proof `METHOD`. |
| Experimental strategy | Sequences data collection, intervention, and evaluation. | `STRATEGY` subtype linked to experimental `METHOD`s and `EVIDENCE`. | Stable when local constraints guide protocol choice. |
| Evaluation strategy | Orders criteria and tests for a target object. | `STRATEGY` subtype linked to `EVALUATION` and `NORM`. | Useful when assessment has stages. |
| Repair strategy | Plans how to respond to objections or failures. | `STRATEGY` subtype linked to `OBJECTION` and target object. | Stable in revision workflows. |

> [!WARNING] Strategy: types vs. tokens
> - A *reusable* strategic pattern (e.g., proof by induction, reductio ad absurdum) is a type-level `METHOD` schema for constructing `ARGUMENT` tokens.
> - A *specific* strategy plan for a local derivation is a `STRATEGY / PLANNING` instance.
> - The execution of a specific plan is an `ARGUMENT`: it applies the planned operations and produces intermediate results and a final result.

==TODO: Maybe the most convincing reason for separating STRATEGY from METHOD is that a strategy is tied to a specific problem while a method is reusable across multiple problems. ==
