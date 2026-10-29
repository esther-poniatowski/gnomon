---
tags:
  - index
index: "[gnomon documentation](docs/_index.md)"
aliases:
  - Methods for reasoning
---
# Methods for reasoning

The external work grounding the design of `gnomon` is recorded on its own terms, before `gnomon` applies that work. Each of the five groups collects the material that plays one role.

## Reasoning principles

- [Reasoning principles by field](reasoning-argumentation-principles-by-field.md): what each discipline that has theorized reasoning demands of a valid argument, an explanation, and an understanding.
- [Reasoning principles across fields](reasoning-argumentation-principles-cross-field.md): the same material reorganized as a cross-domain taxonomy. The design consumes this form rather than the field-by-field inventory.

## Problem decomposition

- [Research gap against research problem](research-problems-vs-gap.jpg): an external figure separating what is missing in the literature from the issue that makes an investigation necessary.

## Reference formal reasoning domains

- [Formal reasoning domains overview](formal-frameworks-overview.md): six domains compared under one schema of four questions, from what constitutes the epistemic state to whether the domain accounts for why an inquiry advanced.
- [Proof theory](proof-theory.md): the sequent as epistemic state, and rule application as the step that transforms it.
- [Dependent type theory](dependent-type-theory.md): the typing context as epistemic state, and tactics that refine a goal type.
- [Classical AI planning](ai-planning-pddl.md): the world state as a set of ground atoms, complete by the closed-world assumption, and operators that add and delete atoms.
- [Hierarchical task network planning](hierarchical-task-network-planning.md): decomposing a task into subtasks, the substrate closest to the framework's own decomposition of goals.
- [Argumentation theory](argumentation-theory.md): arguments together with an attack relation, from which acceptable sets are computed.
- [Belief revision and dynamic epistemic logic](belief-revision-dynamic-epistemic-logic.md): how an epistemic state changes under new information, the component the proposed architecture leaves least specified.

## Design of a research formalism

- [Decision rules](decision-rules.md): the epistemic, argumentative, and stylistic rules governing note production, stratified by the aspect each one governs and weighted by note type and workflow stage.
- [Formal reasoning language principles](formal-language-principles.md): what a fully formal research-reasoning language must satisfy, from its ontological commitments through its operation taxonomy to the semantics under which those operations execute.
- [Incremental construction plan](construction-plan-incremental.md): the minimal viable trace as the unit of progress, and the phases that grow the formalism one reconstructed research episode at a time.
- [Formalism candidates](formalism-candidates.md): supplies the candidate formalisms to weigh when an open goal of the project is resolved
- [Adversarial statements](adversarial-statements.md): tests whether the records of `gnomon` can state research statements that resist formalization

## Knowledge interchange formats

- [Open Knowledge Format](open-knowledge-format.md): to decide whether `gnomon` should store its records in this format, emit bundles in it, or borrow its trust fields.
