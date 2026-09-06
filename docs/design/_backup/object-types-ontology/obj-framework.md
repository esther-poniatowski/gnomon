---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Framework (object candidate)
---
# Object candidate — Framework / Paradigm

## Role

A framework is a coherent background of operative commitments that makes a research practice intelligible.

A framework:

- fixes a conceptual vocabulary
- sets admissible reasoning moves
- supplies evaluative standards
- prioritizes central questions
- anchors cross-framework comparison and conflict

*Examples*: 

 - Bayesian epistemology is a framework when it fixes probabilistic concepts, standards of coherence, and admissible forms of inference,
 - structural realism
 - constructivism
 - the Chomskyan generative program

## Properties

**Truth-apt**: No. A framework conditions reasoning; its component commitments and claims about it are truth-apt.

**Functional stratum**: Contextual

**Internal structure**:

- **Conceptual vocabulary.** Concepts and distinctions treated as basic.
- **Commitments.** Claims or assumptions treated as background.
- **Norms.** Standards for admissible reasoning and evaluation.
- **Methods.** Procedures privileged within the framework.
- **Questions.** Problems or questions treated as central.
- **Scope.** Domain or community in which the framework governs reasoning.
- **Entrenchment** (context-dependent). How resistant the framework is to revision.

## Encoding options

### Holistic composite

**Category:** Composite object

**Specification:** Reify the coordination among `CONCEPT`, `CLAIM`, `MODEL`, `METHOD`, and `NORM`s (e.g., Bayesian inference practice).

**Pros.**
- Preserves the conditioning background without forcing each component into one primitive.
- Keeps commitments, norms, exemplars, methods, and model preferences typed and queryable.
- Works when coordination among component objects governs admissible reasoning.

**Cons.**
- Needs internal structure so the framework does not become a residual category.

### Conditioning primitive

**Category:** Primitive object

**Specification:** Keep `FRAMEWORK` primitive as the integrated background for `CLAIM`, `NORM`, `METHOD`, and `MODEL`s (e.g., a Kuhnian paradigm).

**Pros.**
- Captures paradigm-level constraints on arguments, models, and explanations.
- Preserves the holistic behavior of research paradigms and research programs.
- Works when admissibility depends on the integrated background.

**Cons.**
- Risks becoming too broad unless commitments, norms, exemplars, and heuristics stay explicit.
- Can hide differences among Quinean background commitments, Kuhnian exemplars, Lakatosian heuristics, and Wittgensteinian hinges.

### Framework annotations

**Category:** Annotation on another object

**Specification:** Attach framework commitments to `CLAIM`, `METHOD`, or `MODEL`s (e.g., Bayesian, frequentist, mechanistic).

**Pros.**
- Avoids a heavyweight framework node for local background assumptions.
- Works when the commitment has only local force.

**Cons.**
- Distributes background constraints across the graph.
- Makes it harder to see when commitments and standards jointly condition admissible reasoning.

## Subtypes

Subtypes are meaningful along one dimension: scope and entrenchment of the governing background.

| Label              | Description                                                         | Encoding                                                               | Assessment                                                   |
| ------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| Formal framework   | Fixes a vocabulary, rules, and admissible constructions.            | `FRAMEWORK` subtype linked to axioms, definitions, and methods.        | Useful in formal and mathematical contexts.                  |
| Local framework    | Governs a bounded inquiry, project, or method family.               | `FRAMEWORK` subtype linked to local `QUESTION`, `METHOD`, and `NORM`s. | Stable when local admissibility differs from wider practice. |
| Research programme | Coordinates commitments, heuristics, and problem choices over time. | `FRAMEWORK` subtype with historical and strategic links.               | Stable for Lakatos-style dynamics.                           |
| Paradigm           | Governs a community's exemplars, standards, and normal problems.    | `FRAMEWORK` subtype with community and exemplar relations.             | Stable when entrenchment and exemplar force matter.          |
