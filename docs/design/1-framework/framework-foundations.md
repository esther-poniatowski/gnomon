---
tags:
  - criteria
index: "[[_index|Framework-level criteria]]"
aliases:
  - Framework foundations (criteria)
---
# Framework foundations — Framework-level criteria

## Language-tooling integration ^t1-language-tooling-integration

The framework provides an integrated system of **formal language and tooling**:

| Aspect              | Goal                                                                                                                                                                                                                      | Criteria                                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Formal language** | Express epistemic knowledge and processes. It encodes *statements* in general, record epistemic contents (e.g. definitions, questions, relations, claims, proofs, warrants), and the reasoning moves that transform them. | *Inquiry content and progression*, *Typed-object decomposition*, *Stable boundaries*, *Function-driven typology*                                                                                         |
| **Tooling**         | Facilitate research activities. reads that recorded structure to check validity, index objects, query relations, navigate questions and arguments, visualize dependencies, gate activity.                                 | *Research activities and workflows* (validation externality, staleness gating), *Cost and Ergonomics* (read-side and write-side automation), *Relational queryability* in *Modular content organization* |

The language is primary: the tooling operates over what the language records. Tooling may expose, validate, or enforce structure, but the recorded language remains the source of truth for that structure.

**Failure mode prevented.** A framework whose language and tooling drift apart either becomes prose that tools cannot inspect or becomes an opaque tool state that readers cannot audit. In both failures, research content no longer has one stable form that humans and validators can share.

**Upstream dependencies.**

- None (root): the root system-identity criterion.

**Downstream consequences.**

- [Inquiry content and progression](#^t1-inquiry-content-and-progression) (sub-criterion): the formal language must record both standing content and the moves that transform it.
- [Typed-object decomposition](#^t1-typed-object-decomposition) (sub-criterion): the language must expose the object kinds and fields that tooling validates.
- [Stable boundaries](#^t1-stable-boundaries) (sub-criterion): language components and tooling components must have clear scopes.
- [Function-driven typology](#^t1-function-driven-typology) (sub-criterion): the shared language-tooling interface must classify components by their function in inquiry.
- [Relational queryability](modular-content-organization#^t1-relational-queryability) (cross-group sub-criterion in *Modular content organization*): tooling can query relations only when the language records those relations explicitly.
- [Validation externality](research-activities-workflows#^t1-validation-externality) (cross-group sub-criterion in *Research activities and workflows*): validation tooling checks authored structure rather than replacing it.
- [Read-side automation](cost-ergonomics#^t1-read-side-automation) and [write-side automation](cost-ergonomics#^t1-write-side-automation) (cross-group sub-criteria in *Cost and Ergonomics*): automation remains bounded because tools operate over declared language structure.

## Inquiry content and progression ^t1-inquiry-content-and-progression

The framework captures **research inquiry** as a **state-transforming process** which follows the structure of a **strategic game**. Two dimensions correspond to the two halves of that game:

| Dimension                | Nature                    | Description                                                                                                                                                                          | Examples                                                                            |
| ------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Static: the **state**    | *Epistemic contents*      | At any moment, an inquiry holds a set of standing contents that the inquiry has produced so far                                                                                      | claims, definitions, results, warrants...                                           |
| Dynamic: the **process** | *Inferential progression* | Research advances by *moves* that *transform* the state to bring it closer to resolving the goal of the inquiry. Every move is a legitimate step and is licensed by a stated reason. | producing new content, justifying it, revising or reformulating existing content... |

*Stages in a reasoning.* A reasoning move is a state transition that carries the inquiry from a partial understanding to a greater articulation by a recognizable operation:

> problem state diagnostic (gap) → strategic response (objective + rationale) → local transformation (operation) → newly intelligible state (gain)

**Failure mode prevented.** A formalism that records only end-state results without their progression strips the inquiry of its trajectory and reduces to a result database; a formalism that records only the progression without standing content cannot be used as a reference for what has been settled and reduces to a process log. A formalism that records moves without binding each move to a goal it advances captures a sequence of edits but not a strategy, and cannot distinguish inquiry from undirected accumulation.

> [!NOTE] Criterion scope
> The static and dynamic dimensions each call for their own objects and relations. These are downstream decisions.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): the formal language side of the framework must record the state and the moves of inquiry.

**Downstream consequences.**

- [Activity coverage](expressive-depth#^t1-activity-coverage) (sub-criterion): the dynamic dimension requires that the framework support the canonical activities through which inquiry progresses.
- [Concrete analytical execution](expressive-depth#^t1-concrete-execution) (sub-criterion): the per-step specialisation of the dynamic dimension — every step's progression must be recorded as actual epistemic work.
- Inferential-progression partition (decision in the reasoning-structure theme): how the framework segments the dynamic dimension into recordable steps.
- [Object-kind taxonomy fidelity](object-kinds#^t2-ontology-content-fidelity) (theme-local criterion): the kind set must cover the static dimension's substantive content without omission or distortion.
- [Subtype safety](object-kinds#^t2-ontology-subtype-safety) (theme-local criterion): subtype labels must not silently imply substitutability between kinds with different reasoning roles.
- [Move coverage](object-kinds#^t2-move-coverage) (theme-local criterion): the operation library must span every epistemic move the framework supports.
- [Valid licensing](reasoning-integrity#^t1-valid-licensing) (sub-criterion): the recorded reasoning must rest on checkable warrants — non-circular, complete, and soundly composed across warrant kinds.

## Typed-object decomposition ^t1-typed-object-decomposition

The framework decomposes inquiry content into a structured set of **typed objects of distinct kinds** (e.g. claims, definitions, proofs, questions, warrants, …). Specifically:

- Each unit of content has a *distinguishable type*, and carries a set of predictable properties (attributes, "fields") forming its internal structure.
- Epistemic objects interact through *typed relations* that connect specific types and/or properties.
- Operations apply only to objects of specific kinds, and their semantics is defined in terms of those kinds' properties.

**Failure mode prevented.** Without typed-object decomposition, the framework collapses into either a free-form note system of undifferentiated prose, or an untyped flat graph database. Such a system cannot apply kind-specific validation, enforce field requirements per kind, and license the typed operations that downstream automation depends on.

> [!NOTE] Criterion scope
> This criterion requires inquiry content to be decomposed into typed objects, but it does not prescribe:
> - *which* object types are admitted;
> - *how* inferential progression is recorded;
> - *how* relations between objects are encoded (open question: [relation reification threshold](2-architecture/relations-graph#^t2-relation-reification)).
>
> These decisions are downstream. The criterion does not guarantee that the decomposition is **unique**: the same content may yield different object sets at different grains of analysis.

**Upstream dependencies.**

- [Inquiry content and progression](#^t1-inquiry-content-and-progression) (parent criterion): typed-object decomposition is the chosen way to structure the static dimension of inquiry; the dynamic dimension is recorded through downstream progression-encoding decisions that operate over the typed objects this criterion commits to.

**Downstream consequences.**

- Object-kind admission test (decision in the object-kinds theme): determines which candidate kinds are admissible.
- Field typing (decision in the object-kinds theme): determines the admissible shapes of the field sets each kind carries.
- Progression-encoding decisions (in the relations-graph, reasoning-structure, and arguments-reasoning themes): how inferential progression is recorded over the typed objects.
- [Function-driven typology](#^t1-function-driven-typology) (peer sub-criterion): function — not surface form — is what distinguishes object kinds.
- [Addressability](modular-content-organization#^t1-addressability) (cross-group sub-criterion in *Modular content organization*): typed-object decomposition makes content addressable by giving each unit a kind-tagged identity.

## Stable boundaries ^t1-stable-boundaries

Every component of the framework — every object kind, field, relation, vocabulary, operation, layer — is **defined with stable boundaries**: its scope, its admissible values, and its distinction from neighbouring components are stated unambiguously, with minimal overlap to ensure a clear identity for each component, and with a clear rationale for why the boundary is drawn where it is.

**Failure mode prevented.** A component whose boundary is fuzzy admits content that should belong to another component, and rejects content that should belong to it. Drift accumulates over time, the system loses self-consistency.

**Upstream dependencies.**

- None (root): a meta-integrity commitment about the framework's own definitional clarity, independent of what content the framework records.

**Downstream consequences.**

- [Function-driven typology](#^t1-function-driven-typology) (peer sub-criterion): boundaries are stable when they track function rather than surface form.
- [Object-kind admission test](object-kinds#^t2-object-kind-admission) (decision): the test that determines whether a candidate is admissible as an object kind ensures the kind boundary is well-defined.
- [Canonical terminology](modular-content-organization#^t1-canonical-terminology) (cross-group sub-criterion in *Modular content organization*): canonical names are one mechanism by which boundaries remain unambiguous in prose.

> [!NOTE] Distinguishing the framework's own components from the content it discusses
> This criterion concerns the boundaries of the framework's *own components* (object kinds, fields, relations, vocabularies, operations, layers...), **not** the specific *concepts* that the inquiry manipulates (e.g. a scientific notion such as "geometry"). A concept appearing inside the content may have a vague or contested boundary without violating this criterion.

## Function-driven typology ^t1-function-driven-typology

Every component is distinguished by its **function** in the framework, not by its superficial structure or syntactic form. Boundaries between kinds track function across all unit types:

- content kinds are distinguished by the role each plays in inquiry;
- operation kinds by are distinguished by the transformation each performs;
- activity kinds by are distinguished by the contribution each brings to research.

**Failure mode prevented.** A taxonomy keyed on surface form collapses or proliferates when the form drifts. A function-keyed taxonomy survives reformatting and remains stable across notational and structural changes.

**Upstream dependencies.**

- [Inquiry content and progression](#^t1-inquiry-content-and-progression) (parent criterion): function is what the representation must capture, across both static and dynamic dimensions.
- [Stable boundaries](#^t1-stable-boundaries) (peer sub-criterion): function-keyed boundaries are the ones that remain stable; surface-keyed boundaries drift.

**Downstream consequences.**

- Motivation-encoding mechanism (decision in the reasoning-structure theme): implements the function-vs-form split at the motivation grain.
- Epistemic-work-encoding mechanism (decision in the reasoning-structure theme): implements the function-vs-form split at the work grain.
- [Object-kind admission](object-kinds#^t2-object-kind-admission) (decision): tests candidates by function, not by structural resemblance.
- Activity admission (decision in the workflows theme): tests candidate activities by their function in inquiry progression, not by surface resemblance to existing workflows.