---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Rationale (object candidate)
---
# Object candidate — Rationale / Motivation / Decision

## Role

A rationale states why an epistemic content or move receives a specific status relative to alternatives.

Its role is to preserve the reasons that guide inquiry without treating local choices as self-evident.

Rationales matter when later reasoning depends on path choice, priority, or admissible search direction.

*Example*: "simulation is needed because direct data are sparse" is a rationale for using a simulation method.

*Examples of motivated moves*:

- asking a question
- introducing a concept
- imposing an assumption
- preferring a model or analogy
- choosing a strategy

## Properties

**Truth-apt**: Yes, when the rationale states why an epistemic move is justified, preferable, or required.

**Functional stratum**: Strategic

**Internal structure**:

- **Move.** Question, concept, assumption, method, model, or strategy being motivated.
- **Reason.** Consideration that supports the move.
- **Alternative** (context-dependent). Rejected or postponed option.
- **Priority.** Why the move matters now.
- **Consequence.** Inquiry path opened or avoided by the move.

## Encoding options

### Editorial annotation

**Category:** Annotation on another object

**Specification:** Attach motivation to the introduced `CLAIM`, `QUESTION`, `MODEL`, `METHOD`, or section object (e.g., why this assumption matters).

**Pros.**
- Avoids a separate object for editorial context.
- Works when motivation has no independent graph behavior.

**Cons.**
- Cannot track strategic dependencies.
- Hides why an object entered the inquiry when the motivation constrains later moves.

### Rationale claim

**Category:** Subtype object

**Specification:** Use `CLAIM` to assert why an object matters, why a route is justified, or why a choice is appropriate (e.g., simulation is needed because data are sparse).

**Pros.**
- Makes justifications contestable and linkable.

**Cons.**
- Does not capture non-propositional guidance well.

### Strategic rationale object

**Category:** Primitive object

**Specification:** Keep `RATIONALE` as a citable reason linked to `QUESTION`, `METHOD`, or `FRAMEWORK`s (e.g., why use simulation).

**Pros.**
- Makes strategy-level dependencies visible.
- Captures search guidance and object introduction when they are central to the inquiry.
- Works when other objects must cite the reason that introduced or prioritized another object.

**Cons.**
- Risks overlap with `QUESTION`, `METHOD`, and `FRAMEWORK`.

## Subtypes

Subtypes are meaningful along one dimension: the kind of move that the reason licenses.

| Label                | Description                                           | Encoding                                                           | Assessment                                               |
| -------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| Choice rationale     | States why one option is preferred over alternatives. | `RATIONALE` linked to `COMPARISON` and selected object.            | Stable when rejected alternatives matter.                |
| Priority rationale   | States why one task or object receives priority.      | `RATIONALE` linked to `STRATEGY` or `PROBLEM`.                     | Useful in planning graphs.                               |
| Constraint rationale | States why a constraint is imposed.                   | `RATIONALE` linked to `NORM`, `METHOD`, or `FRAMEWORK`.            | Stable when the constraint needs justification.          |
| Motivating rationale | States why an inquiry object is introduced.           | `RATIONALE` linked to `QUESTION`, `CONCEPT`, `MODEL`, or `METHOD`. | Stable when later graph use depends on the introduction. |
