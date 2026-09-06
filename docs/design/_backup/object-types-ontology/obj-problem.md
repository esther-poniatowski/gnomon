---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Problem (object candidate)
---
# Object candidate — Problem

## Role

A problem is a structured gap that calls for a determinate resolution.

Its role is to organize inquiry around a target state and a boundary between what is known and what remains open.

*Example*: constructing a counterexample to a universal conjecture is a problem.

*Examples of resolutions*:

- solution
- construction
- explanation
- proof
- decision
- design

## Properties

**Truth-apt**: No. A problem opens a task or inquiry; proposed answers and claims about its constraints are truth-apt.

**Functional stratum**: Erotetic

**Internal structure**:

- **Gap.** Unknown, obstacle, or unmet target state.
- **Target.** Solution, construction, explanation, proof, decision, or design sought.
- **Success criteria.** Conditions under which the problem counts as solved.
- **Constraints.** Limits on admissible answers or moves.
- **Resources** (context-dependent). Known results, tools, or data available for solution.

## Encoding options

### Constructive question

**Category:** Subtype object

**Specification:** Treat `PROBLEM` as a `QUESTION` subtype linked to a `METHOD`, artifact, proof, or construction target (e.g., construct a counterexample).

**Pros.**
- Preserves subquestions, presuppositions, candidate answers, and closure conditions.
- Covers constructive prompts such as "construct a non-normal subgroup of index 2" and constraint prompts such as "find parameters satisfying constraints C."
- Works when a target must satisfy explicit success conditions.

**Cons.**
- Makes the pragmatic strength of problems depend on question properties.

### Question reduction

**Category:** Reduction to another object

**Specification:** Use `QUESTION` alone with possible solution `CLAIM`s (e.g., which construction works?).

**Pros.**
- Avoids a weak boundary between questions and problems.
- Works when the problem adds no graph behavior beyond answer conditions.

**Cons.**
- Hides research program commitments that exceed a single answer condition.
- Weakens the distinction between productive necessity and ordinary answerhood.

## Subtypes

Subtypes are meaningful along one dimension: the closure condition that resolves the problem.

| Label                | Description                                                          | Encoding                                                              | Assessment                                                   |
| -------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------ |
| Proof problem        | Closes through a valid proof of a target claim.                      | `PROBLEM` subtype linked to `DERIVATION / PROOF`.                     | Stable in formal inquiry.                                    |
| Construction problem | Closes through an object, witness, or example.                       | `PROBLEM` subtype linked to `EXAMPLE` or `MODEL`.                     | Stable when production rather than assertion closes inquiry. |
| Design problem       | Closes through an artifact, model, or method satisfying constraints. | `PROBLEM` subtype linked to `METHOD`, `MODEL`, and `NORM`.            | Stable when constraints and output jointly matter.           |
| Decision problem     | Closes through a choice among alternatives.                          | `PROBLEM` subtype linked to `COMPARISON`, `NORM`, and result `CLAIM`. | Useful when criteria govern closure.                         |
| Explanation problem  | Closes through an explanation of a phenomenon.                       | `PROBLEM` subtype linked to `EXPLANATION`.                            | Stable when why or how is central.                           |
