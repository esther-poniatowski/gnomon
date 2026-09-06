---
tags:
  - criteria
index: "[Framework-level criteria](_index.md)"
aliases:
  - Framework foundations (criteria)
---
# Framework foundations — Framework-level criteria

## Language-tooling integration ^t1-language-tooling-integration

The framework provides an integrated system of **formal language and tooling**:

| Aspect              | Goal                                                                                                                                                                                                                      | Criteria                                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Formal language** | Express epistemic knowledge and processes. It encodes *statements* in general, record epistemic contents (e.g. definitions, questions, relations, claims, proofs, warrants), and the reasoning moves that transform them. | *Inquiry content and progression*, *Typed-object decomposition*, *Functional separation of concerns*                                                                                                     |
| **Tooling**         | Facilitate research activities. reads that recorded structure to check validity, index objects, query relations, navigate questions and arguments, visualize dependencies, gate activity.                                 | *Research activities and workflows* (validation externality, staleness gating), *Cost and Ergonomics* (read-side and write-side automation), *Relational queryability* in *Modular content organization* |

The language is primary: the tooling operates over what the language records. Tooling may expose, validate, or enforce structure, but the recorded language remains the source of truth for that structure.

**Failure mode prevented.** A framework whose language and tooling drift apart either becomes prose that tools cannot inspect or becomes an opaque tool state that readers cannot audit. In both failures, research content no longer has one stable form that humans and validators can share.

**Upstream dependencies.**

- None (root): the root system-identity criterion.

**Downstream consequences.**

- [Inquiry content and progression](#^t1-inquiry-content-and-progression) (sub-criterion): the formal language must record both standing content and the moves that transform it.
- [Formal expression of all content](#^t1-formal-expression) (sub-criterion): every semantically loaded field is grammar-bound; free prose is confined to fields with no epistemic load.
- [Typed-object decomposition](#^t1-typed-object-decomposition) (sub-criterion): the language must expose the object kinds and fields that tooling validates.
- [Functional separation of concerns](#^t1-functional-separation) (sub-criterion): language and tooling components are separated by function, each boundary carrying a separation-of-concerns rationale.
- [Component-set adequacy](#^t1-component-set-adequacy) (sub-criterion): the set of components the language and tooling provide must be sufficient, necessary, and adequately compressed.
- [Relational queryability](modular-content-organization#^t1-relational-queryability) (cross-group sub-criterion in *Modular content organization*): tooling can query relations only when the language records those relations explicitly.
- [Validation externality](research-activities-workflows#^t1-validation-externality) (cross-group sub-criterion in *Research activities and workflows*): validation tooling checks authored structure rather than replacing it.
- [Read-side automation](cost-ergonomics#^t1-read-side-automation) and [write-side automation](cost-ergonomics#^t1-write-side-automation) (cross-group sub-criteria in *Cost and Ergonomics*): automation remains bounded because tools operate over declared language structure.

## Formal expression of all content ^t1-formal-expression

The framework achieves expressivity **exclusively by formalization**, never by admitting free-form natural language as semantic content. Every field that any operation, validator, query, relation, or analysis reads conforms to a **known grammar** — a controlled vocabulary, a typed reference, a structured record, a mathematical expression, a closed-vocabulary tag, or any other shape declared in the language's schema. Natural language appears only in fields that are **strictly unessential to inquiry**: explicitly-marked authoring scratch (TODO, FIX), human-facing labels, external comments, exposition aimed at a reader. An unessential field is one that **no operation, validator, relation, or query reads** — a field whose removal would not change what the framework records, infers, or checks about the corpus.

This commitment partitions every field into two disjoint classes:

- **Semantic fields** — the content the framework manipulates. Grammar-bound, schema-declared, validator-checked. A claim's body, a warrant's licensing condition, a strategic move's rationale, a gap's diagnostic — all are semantic and therefore grammatical.
- **Unessential fields** — annotations the framework stores but does not interpret. Prose is permitted here; the framework treats their content as opaque.

**Failure mode prevented.** A framework that admits free prose inside semantic fields wears the appearance of formalization while reproducing the failure modes of conventional note-taking that the [project's stance](../../project-overview.md) targets — loss of dependency visibility, dilution of argumentative structure, mixing of epistemic roles. Half-predictable content forfeits the operationalization the framework exists to deliver: such fields cannot be queried by structure, manipulated by operations, validated for soundness, or analyzed for dependency. Permissiveness at the field level silently undoes typing at the object level.

> [!NOTE] Criterion scope
> This criterion fixes *how* content is expressed, not *what* content is admissible. It does not prescribe which grammars the semantic fields use, nor how rich each grammar must be. Those are downstream decisions per kind of content. It does require that wherever the framework currently lets a semantic field default to prose, a grammar must be supplied.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): the language is the source of truth that tooling operates over; tooling can manipulate, query, or validate a field only when that field is grammatical.

**Downstream consequences.**

- [Rich prose expressivity](expressive-depth#^t1-rich-prose-expressivity) (peer sub-criterion in *Expressive depth*): expressivity targets — formulas, multi-step derivations, diagrams — must be met by *formal* shapes (math grammars, structured derivation records, declarative diagram languages), not by prose bodies.
- [Partial formalization tolerance](expressive-depth#^t1-partial-formalization) (peer sub-criterion in *Expressive depth*): partial formalization means grammatical annotations may be **absent**; it never means a semantic field is filled with sub-formal prose.
- [Field-typing discipline](../2-architecture/object-kinds#^t2-field-typing) (decision in the object-kinds theme): the field-typing meta-schema must partition fields into semantic (grammar-bound) and unessential (free-prose, framework-opaque), and forbid free prose in any semantic position.
- [Object-kind admission test](../2-architecture/object-kinds#^t2-object-kind-admission) (decision in the object-kinds theme): no candidate kind is admissible whose canonical content is prose.
- Reasoning-field grammars (open question, to be staged in [the fleeting-ideas catalogue](../_fleeting-ideas.md)): strategic rationale, explanatory gain, route selection, and rejected-alternative records require grammars rather than prose defaults.
- Validator obligation (cross-group consequence in [validation views](../2-architecture/validation-views.md)): a validator checks that no semantic field contains ungrammatical content.

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

## No run-time inference engine ^t1-no-runtime-inference

The [framework's tooling](#^t1-language-tooling-integration) **records and validates authored reasoning, but it does not perform automated inference**. No run-time inference engine evaluates warrant conditions or defeat conditions: argument validity is fixed by authored objects and authored revision events, never derived by an automated reasoner. 

*Consequence*: Automated inference must be run it outside the framework.

**Failure mode prevented.** A framework with a run-time prover or argument engine can change what is warranted without any authored change to the corpus, inducing a hidden evaluation layer rather than a traceable revision process. Defeasibility would then be a silent derivation rather than an authored, inspectable record. 

> [!HINT] Future extension
> Automated inference may be a future extension, but admitting it now would be a significant departure from the current design.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): the criterion fixes the boundary of the *tooling* half — which activities the tooling performs and which it excludes.
- [Valid licensing](reasoning-integrity#^t1-valid-licensing) (cross-group criterion in *Reasoning integrity*): warrant kinds and defeat conditions must be recorded explicitly, since no reasoner derives them.
- [Revision accountability](research-activities-workflows#^t1-revision-accountability) (cross-group criterion in *Research activities and workflows*): upstream changes must reach dependents through traceable revision events, since no reasoner re-evaluates them.

**Downstream consequences.**

- [Warrant-kind annotation on support relations](2-architecture/validity-revision#^t2-warrant-annotation) (decision in the validity-revision theme): support edges record warrant kinds so that propagation can be parameterized without run-time warrant evaluation.
- [Revision and feedback semantics](2-architecture/validity-revision#^t2-revision-feedback) (decision in the validity-revision theme): all changes that affect warrants are revision events driven by the author.
- [Dependent flagging](2-architecture/validity-revision#^t2-dependent-flagging) (decision in the validity-revision theme): tooling computes stale marks from the registry and emits diagnostics for the author, rather than mutating dependents automatically.
- [Relational queryability](modular-content-organization#^t1-relational-queryability) (cross-group sub-criterion in *Modular content organization*): query tools retrieve authored and derived registry structure; they do not infer new warrants at run time.

## No version history ^t1-no-version-history

The framework **does not reimplement a version-history system**. It records and reasons about the *current state* of an inquiry — the standing content and the authored revision events that produced it — but it maintains no parallel store of past versions, no commit graph, no per-reference version pinning. 

*Consequence*: Tracking the history of files is left to the researcher's choice: an external version-control system, a manual archival process, or none. The framework neither requires nor integrates with a particular one.

**Failure mode prevented.** A framework that maintains its own version-history layer duplicates whatever the researcher's version-control system already keeps; references, supersession, and current-state queries are recorded twice. The opposite over-reach — pinning every reference to a past version — would fragment the active corpus into historical snapshots and lose the single shared current state of the inquiry.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): the criterion fixes a scope boundary of the framework as a system — what its language records (current state) and what it does not (file history).

**Downstream consequences.**

- [Revision and feedback semantics](2-architecture/validity-revision#^t2-revision-feedback) (decision in the validity-revision theme): revision objects record in-state revision events, not version history.
- [Archival](2-architecture/validity-revision#^t2-archival) (decision in the validity-revision theme): outdated objects move within the source tree rather than into a parallel history store.
- [Epistemic status as a maturity record](object-kinds#^t2-epistemic-status) (decision in the object-kinds theme): supersession is excluded from the maturity vocabulary; status records the object's current standing.

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
- [Functional separation of concerns](#^t1-functional-separation) (peer sub-criterion): function — not surface form — is what distinguishes object kinds, and each kind boundary carries a separation-of-concerns rationale.
- [Component-set adequacy](#^t1-component-set-adequacy) (cross-reference): the object-kind set this criterion commits to is one component set the adequacy standard judges.
- [Addressability](modular-content-organization#^t1-addressability) (cross-group sub-criterion in *Modular content organization*): typed-object decomposition makes content addressable by giving each unit a kind-tagged identity.

## Component-set adequacy ^t1-component-set-adequacy

The framework's components — object kinds, fields, relations, vocabularies, operations, layers — must together form a **set that represents research reasoning with no gap and no distorting surplus**. Three conditions state the standard:

- **Sufficient.** The component set covers every aspect of research reasoning the framework must represent — the static epistemic content, the dynamic logic of inquiry, and the activities through which inquiry advances. Nothing a researcher must record falls outside the admitted components.
- **Necessary.** Each admitted component earns its place: it represents something no other component already represents. A component whose function another component already discharges is not admitted.
- **Compressed under operational adequacy.** Among the sufficient and necessary sets, the framework prefers the one that introduces the fewest components — but compression stops wherever a further merge would erase a distinction that materially improves intelligibility, force heterogeneous content into one schema, or shift essential content into opaque fields. Expressivity and function-faithfulness are the targets; compression is the discipline applied only as far as they allow.

**Failure mode prevented.** A component set that is insufficient forces research content outside the framework, where it cannot be validated or related. A set carrying unnecessary components proliferates kinds, raising per-action cost and inviting misclassification between near-synonymous components. Over-compression is the opposite failure: merging components that differ in epistemic function, dependency profile, or graph behaviour flattens distinctions that carry intelligibility, so the set ceases to be optimally expressive.

> [!NOTE] Criterion scope
> This criterion is a standard the design must meet, not a procedure for meeting it. It does not name *which* components satisfy it. Each component theme operationalises the standard at its own grain — the object-kind admission test and the object-kind smallness criterion in the object-kinds theme apply it to the object set; the closed-vocabulary and relation-vocabulary decisions apply it to the controlled vocabularies; the operation-library decisions apply it to the operation set.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): the component inventory whose set this criterion judges — object kinds, fields, relations, vocabularies, operations, layers — is exactly the inventory the integrated language and tooling provide.

**Downstream consequences.**

- [Functional separation of concerns](#^t1-functional-separation) (peer sub-criterion): functional separation draws each component boundary; component-set adequacy judges whether the resulting set has the right members. The two are complementary — one governs boundaries, the other coverage.
- [Object-kind admission test](object-kinds#^t2-object-kind-admission) (decision in the object-kinds theme): the object-kind specialisation — the five-condition test by which a candidate kind is judged sufficient and necessary.
- [Object-kind smallness](object-kinds#^t2-ontology-small) (theme-local criterion): the compression condition at the object-kinds grain, bounded there too by role purity and coverage.
- [Admissibility under the five-condition test](3-aspect-specific/ontology#^t3-admissibility-five-conditions) and [primary-content, operational, and non-distortion conditions](3-aspect-specific/ontology#^t3-primary-content-conditions) (criteria in the ontology theme): the object-kind-set consequences of this standard — sufficiency, necessity, and non-distortion stated for the canonical object set.
- [Non-redundancy](modular-content-organization#^t1-non-redundancy) (cross-group sub-criterion in *Modular content organization*): the necessity condition extends to content instances, not only to components.

## Functional separation of concerns ^t1-functional-separation

The framework's components — object kinds, fields, relations, vocabularies, operations, layers — are separated **by function**. Two commitments make this concrete:

- **Function draws the boundary.** Boundaries between components track their *roles* or *contributions* in inquiry. A boundary is never drawn on superficial structure or syntactic form.
- **Every boundary carries a stated rationale.** Each component's scope, its admissible values, and its distinction from its neighbours are stated unambiguously, accounting for the *separation of concerns* it realises.

**Failure mode prevented.** A taxonomy keyed on surface form collapses or proliferates when the form drifts, and becomes unstable and prone to misclassifications. Function-keyed boundaries survive reformatting; rationale-bearing boundaries can be checked.

**Upstream dependencies.**

- [Language-tooling integration](#^t1-language-tooling-integration) (parent criterion): a clear scope for each component is what lets tooling check and enforce structure.
- [Inquiry content and progression](#^t1-inquiry-content-and-progression) (parent criterion): function — the role a component plays in inquiry — is what the representation must capture and what the boundaries must track.
- [Component-set adequacy](#^t1-component-set-adequacy) (peer sub-criterion): functional separation draws each component boundary; component-set adequacy judges whether the set of components so bounded is sufficient, necessary, and adequately compressed.

**Downstream consequences.**

- [Object-kind admission test](object-kinds#^t2-object-kind-admission) (decision): the admission test decides a candidate kind by its function, ensuring each kind boundary is well-defined and functionally justified.
- Motivation-encoding mechanism (decision in the reasoning-structure theme): implements the function-vs-form split at the motivation grain.
- Epistemic-work-encoding mechanism (decision in the reasoning-structure theme): implements the function-vs-form split at the work grain.
- Activity admission (decision in the workflows theme): tests candidate activities by their function in inquiry progression, not by surface resemblance to existing workflows.
- [Canonical terminology](modular-content-organization#^t1-canonical-terminology) (cross-group sub-criterion in *Modular content organization*): canonical names are one mechanism by which component boundaries remain unambiguous in prose.

> [!NOTE] Criterion scope
> The boundaries at stake are those of the framework's *own components* (object kinds, fields, relations, vocabularies, operations, layers), **not** the *concepts* the inquiry manipulates (e.g. a scientific notion such as "geometry"). A concept appearing inside the content may have a vague or contested boundary without violating this criterion; how the framework handles content concepts with unstable boundaries is the candidate-set machinery of [the definition normal form](3-aspect-specific/ontology#^t3-definition-normal-form).