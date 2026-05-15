# Ontology of object kinds

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria that constrain the ontology decision (which object kinds the canonical store admits). Traces to [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t2-coverage-completeness](vendor/gnomon/docs/design/2-architecture/constraints#^t2-coverage-completeness), and the [object-kind admission test](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission). The actual taxonomy is deferred to [the project TODO](vendor/gnomon/docs/TODO).

---

## Criteria

### Admissibility under the five-condition test ^t3-admissibility-five-conditions

A candidate becomes a canonical object kind only if it satisfies all five conditions of [the object-kind admission test](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission): independent identity, context-transcendent reuse, local validity, independent editability, irreducibility.

### Attributes vs. objects ^t3-attributes-vs-objects

A candidate that fails any of the five conditions belongs in a field, status, relation, or higher-layer annotation, not as a new object kind.

### Decision table with one row per candidate ^t3-decision-table-row-per-candidate

The ontology decision must be recorded as a table with one row per candidate kind and one justification per decision (admit, reject, route to field/status/relation).

### Primary-content, operational, and non-distortion conditions ^t3-primary-content-conditions

The set of object kinds must satisfy primary-content, operational, and non-distortion conditions: it carries the system's substantive content; it supports the operations the architecture requires; it does not distort an aspect into a shape that misrepresents it.

### Ontology stability under growth ^t3-ontology-stability

The ontology begins small, allows subtypes gradually under [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance), and is itself versioned so that taxonomic restructuring is recordable.

---

## Decisions

*To be drafted at the ontology work in [the project TODO](vendor/gnomon/docs/TODO).*

---

## Open questions

### Subtypes of the epistemic-gap kind ^t3-epistemic-gap-subtypes

> [!QUESTION] What are the admissible subtypes of the unified Question/Goal kind ratified in [t2-question-vs-goal](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-question-vs-goal), and what distinguishes them?

The ratified collapse treats Question and Goal as a single kind, distinguished operationally by an `objective` field. A deeper reading takes the kind to represent an **epistemic gap** that admits two framings (interrogative or imperative) through the `objective` field. The open question is whether the kind admits further ontological subtypes that classify the gap itself, independent of its framing.

Candidate subtypes (to be evaluated under [t3-admissibility-five-conditions](#^t3-admissibility-five-conditions) and [t2-subtype-discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-subtype-discipline)):

- **Paradox** — a contradiction between two or more propositions, observations, or properties. Example: "Why do large neural networks generalize better than small ones, despite their greater overfitting capacity?"
- **Missing mechanism** — a phenomenon that is observed but not explained by existing theory. Example: "How are hierarchical representations shaped during learning?"
- **Incomplete characterisation** — which properties of a system, phenomenon, or process are relevant, and which do not matter. Example: "Which properties of an architecture matter for its performance?"
- **Case mapping** — which case distinctions lead to different outcomes. Example: "Under which conditions do feedforward networks outperform recurrent ones?"
- **Comparison** — the differences and similarities between two or more entities. Example: "What differences and similarities hold between feedforward and recurrent networks?"

Bearing criteria: [t3-admissibility-five-conditions](#^t3-admissibility-five-conditions), [t2-subtype-discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-subtype-discipline), [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t1-function-driven-typology](vendor/gnomon/docs/design/_framework-criteria#^t1-function-driven-typology).

Downstream consequence: the chosen subtype set bounds the *Strategic*-level `gap` vocabulary in [reasoning understandability](vendor/gnomon/docs/design/_framework-criteria#^t1-reasoning-understandability). It also feeds the "strategic game" commitment under TODO at [inquiry content and progression](vendor/gnomon/docs/design/_framework-criteria#^t1-inquiry-content-and-progression).

### Concept-type taxonomy at the content-referent level ^t3-concept-type-taxonomy

> [!QUESTION] Within content kinds (definition, claim, …), do referent types — system, subtype, property, process — warrant a sub-categorization, or do they belong in a field or annotation?

The taxonomy cuts at the **content-referent level** (what a definition or claim refers to), not at the epistemic-kind level (claim, definition, proof) that [object kinds](vendor/gnomon/docs/design/2-architecture/object-kinds) governs. It is a candidate sub-categorization *within* content kinds.

Candidate referent types:

- **System** — an entity with defining properties. Example: "network" as a cognitive system; "neuron" as a biological system.
- **Subtype** (of a superclass) — characterised by properties that distinguish it from siblings. Example: "feedforward network" as a subtype of network architecture, distinguished by unidirectional information flow.
- **Property** (of a referent) — may have an antagonist. Example: "entanglement" as a property of a code or geometry, antagonist of "disentanglement".
- **Process** — a temporal transformation. Example: "integration" of inputs.

The open question is whether this cut warrants admission as a sub-categorization, given [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology) and the attributes-vs-objects rule at [t3-attributes-vs-objects](#^t3-attributes-vs-objects). A candidate failing the five-condition test routes to a field on the content kind rather than to a new kind.

Bearing criteria: [t3-attributes-vs-objects](#^t3-attributes-vs-objects), [t3-admissibility-five-conditions](#^t3-admissibility-five-conditions), [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t1-function-driven-typology](vendor/gnomon/docs/design/_framework-criteria#^t1-function-driven-typology).

### Normalized form of a definition ^t3-definition-normal-form

> [!QUESTION] What normal form does a definition take, and how does it reference terms the framework has not yet introduced?

A definition admits a **genus-and-differentia** normal form that assigns each fragment an explicit role:

- **Definiendum** — the concept being defined.
- **Genus** — the superordinate kind the definiendum specialises, recorded as a subtype relation.
- **Differentia** — the constraint that distinguishes the definiendum within the genus, decomposed into a *differentia attribute* (an attribute of the genus) and a *differentia value* (the value that attribute takes).

The differentia, and often the genus, reference further concepts and attributes. Requiring every referenced term to be defined upstream produces infinite regress and overburdens authoring. The framework instead admits **forward references**: a referenced term need not be defined before it is used. The draft profile of [t2-partial-formalization-profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles) governs which profiles tolerate undefined references.

For the role of a definition's components to remain clear while their referents are undefined, a forward reference is not a bare token. It is a **typed placeholder**: it carries a kind tag (which fixes what role the term plays — a genus is a system, a differentia attribute is a property) and an undefined status, and it is addressable per [t1-typed-object-decomposition](vendor/gnomon/docs/design/_framework-criteria#^t1-typed-object-decomposition). When the researcher later defines the term, the placeholder is **promoted** to a full definition without rewriting any content that referenced it.

> [!QUESTION] Is a typed-but-undefined placeholder a distinct object kind, a maturity state of a content kind, or a kind-annotated reference?
>
> The framing is left open. Three alternatives, with their bearing decisions:
>
> - **Distinct kind.** The placeholder is its own object kind, admitted or rejected under [the object-kind admission test](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission).
> - **Maturity state.** The placeholder is a content object (a definition or concept) at an `undefined`/`stub` status; it folds into [t1-partial-formalization](vendor/gnomon/docs/design/_framework-criteria#^t1-partial-formalization) and the per-kind status enums at [t2-epistemic-status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status). This option converges with the pre-formal `Idea` kind question staged in [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-kind-set) and with the four-way proof-status distinction staged in [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-proof-status).
> - **Kind-annotated reference.** The placeholder is not an object at all — it is a reference carrying a kind annotation, resolved when the target is introduced.

A second expert review of the motivating worked example contributed five refinements to the normal form, recorded here. The undischarged-commitment refinements it also produced — presuppositions, definitional force, commitment strength — are filed separately as [the undischarged-commitment open question](arguments-reasoning#^t3-undischarged-commitments), since they bear on silent incompleteness rather than on definition structure.

**Three separable operations.** The framework should not conflate three operations on a definition: *normalization* makes the internal roles explicit and is possible immediately; *definition completion* fully defines every referenced term and stays optional; *validation* checks that all references are well-formed and coherent and is delayed. A statement is accepted once normalized, before completion or validation. Bears on [t1-validation-externality](vendor/gnomon/docs/design/_framework-criteria#^t1-validation-externality) and [t1-write-side-automation](vendor/gnomon/docs/design/_framework-criteria#^t1-write-side-automation).

> [!WARNING] The three operations are not always separable
> The worked-example suite (example 37) shows a limit on this separation. Some concepts are *constitutively* defined by their test procedure — to say a feature "contributes to the task" is meaningful only relative to an admissible way of intervening on it, so the concept's content and its validation procedure are entangled, not merely sequenced. For such concepts, definition completion and validation cannot be fully prised apart. The three-operation split holds for definitions whose validation is extensional; it does not hold for concepts whose meaning is fixed by an intervention or test family. Resolution must state which concepts admit the separation and which are constitutively procedure-bound.

**A registry of definition templates.** The genus-differentia form is one of several normalized patterns. A definition is recognised by the template it instantiates, and each template fixes a structured parse with its own roles. Candidate templates:

| Surface pattern | Normalized role |
| --- | --- |
| `X is a Y` | subtype definition |
| `X is a Y where Z is W` | subtype with attribute constraint (genus-differentia) |
| `X is defined as Y` | definitional equivalence |
| `X refers to Y` | terminological definition |
| `X consists of A, B, C` | compositional definition |
| `X is characterized by P` | property-based characterization |
| `X differs from Y by P` | contrastive definition |
| `X is used to Y` | functional definition |
| `X measures Y` | operational definition |
| `X approximates Y` | methodological approximation |
| `X is not P but Q` | negative definition — defines X by rejecting a competing definition P and asserting Q |

The template registry connects to the reusable [reasoning schemes](arguments-reasoning#^t3-reasoning-schemes): a definition template is the definition-side analogue of an argument scheme.

The negative-definition template generalises to *multi-rejection*: a definition may reject several partial approximations at once — task-relevance is not decodability, not causal effect, not mutual information, since each captures only one aspect of the relation. The rejected definitions are a first-class part of the normalized form, not noise; each may be partially adequate rather than false, so the rejection carries an adequacy grade.

**Template-inferred hole kinds.** A placeholder's expected kind need not be declared by the author. It is inferred from the placeholder's *position* in the recognised template: the genus position implies a system kind, the attribute position implies a property kind, the value position implies a value kind. The template, once recognised, types every hole it contains.

**Ambiguity: a candidate set plus a resolution policy.** A placeholder's expected kind, or a term's referent, may be unresolved — a phrase such as an attribute-like expression may be admissible as an attribute, a process, a relation, or a dynamical property. An earlier draft modelled this as a four-valued ambiguity-status enum (unresolved / incompatible / deliberately-plural / defective); an adversarial audit found that enum carried the operative load of eight worked examples while stating no mechanism. It re-cuts into **two fields plus a separate claim**, each with a defined effect:

- **Candidate-set field.** The set of candidate kinds or referents the term ranges over, drawn from the [concept-type taxonomy](#^t3-concept-type-taxonomy). The set may be heterogeneous — a term may range over candidates of *different object kinds* (an activity vector, a subspace, an equivalence class, a causal role), not just instances of one kind. *Author stores:* the candidate set. *Validator checks:* every candidate resolves to an admissible kind or referent.
- **Resolution-policy field**, a three-valued enum stating whether and why the set will narrow:
  - `will-resolve` — one candidate will be selected later; the plurality is provisional. *Validator:* may warn if the placeholder persists past a profile-defined maturity stage.
  - `cannot-resolve` — the candidate aspects cannot be unified by any resolution; the plurality is forced by the object and is permanent. *Validator:* does not warn on persistence; treats the multi-valued binding as final.
  - `will-not-resolve` — the term is kept plural by an authored choice because the ambiguity carries cognitive value; resolution is declined, not deferred. A *time-bounded* sub-case ("plural for now") sets `will-not-resolve` with a review date. *Validator:* the canonicity check at [t1-canonical-terminology](vendor/gnomon/docs/design/_framework-criteria#^t1-canonical-terminology) must **exempt** a term marked `will-not-resolve` rather than flag it as drift.

The earlier `defective` status is **not an ambiguity status** and is removed from this field. A concept being defectively ambiguous — an overload or an unstable boundary that should be repaired — is an authored *claim about the concept*, not a state of its candidate set: it asserts the concept *ought to change*, where the resolution policy only records whether its candidate set *will* change. The defect claim is a first-class object connecting to the concept-as-object reading at [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-concept-metamodeling); `[!missing]` tension callouts on [t1-canonical-terminology](vendor/gnomon/docs/design/_framework-criteria#^t1-canonical-terminology) and [t1-stable-boundaries](vendor/gnomon/docs/design/_framework-criteria#^t1-stable-boundaries) record that a defect claim is a recordable boundary failure rather than a term to silently rename.

**Stable cross-statement placeholders, and the lexical/concept separation.** A placeholder is stable and shared: a later statement referencing the same term binds to the same placeholder, so resolving it once resolves it everywhere. This requires distinguishing five levels that prose conflates — the *lexical term* (the surface string), the *unresolved concept candidate* (the term used but not yet resolved to a concept), the *resolved concept*, the *local role* the term plays in a given statement, and the *global ontology class*. A term occurrence records its surface, its span, its local role, and its candidate referent. This converges with the concept-as-class versus concept-as-object distinction at [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-concept-metamodeling), and tensions mildly with [t1-canonical-terminology](vendor/gnomon/docs/design/_framework-criteria#^t1-canonical-terminology): a term may carry an *unresolved* candidate referent before it has a designated canonical concept.

A statement may also assert a **usage norm at the lexical-term level** — a fact about how a scientific community uses a term, e.g. "in neuroscience, 'represented' often means recoverable from activity" (worked-example suite, example 6). Unlike a placeholder's candidate referent, a usage-norm statement is a first-order checkable claim: it has a truth value, a source, and can be cited. It attaches to the lexical-term level and records, for a term, the usage a named community gives it — distinct from the framework's own canonical concept for that term.

**External precedents.** The normalization machinery has established precedents, recorded as citations rather than as candidates: frame semantics (a term evokes a structured frame with roles), typed feature structures (partially specified objects with typed attributes supporting underspecification), Abstract Meaning Representation (role-explicit sentence graphs keeping the original wording separate), and semantic-annotation systems (prose stays intact while structured annotations attach to spans). Description Logic with placeholders is a possible *export target* once holes are resolved, not an early-stage representation — consistent with the DL-review rejections at [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-rejections).

Bearing criteria: [t1-typed-object-decomposition](vendor/gnomon/docs/design/_framework-criteria#^t1-typed-object-decomposition), [t1-function-driven-typology](vendor/gnomon/docs/design/_framework-criteria#^t1-function-driven-typology), [t1-no-infinite-regress](vendor/gnomon/docs/design/_framework-criteria#^t1-no-infinite-regress), [t1-partial-formalization](vendor/gnomon/docs/design/_framework-criteria#^t1-partial-formalization).

The worked example that motivates this open question, and a candidate normalization pipeline and object model, are recorded at [_worked-examples](vendor/gnomon/docs/design/_worked-examples#^example-genus-differentia).
