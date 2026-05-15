# Architectural constraints

> [!INFO] Tier and scope
> **Tier 2 (architectural constraints).** This file holds the **cross-cutting** Tier-2 criteria: structural, epistemic, and operational requirements that constrain decisions across multiple themes. They cannot be overridden by aspect-specific (Tier 3) decisions and must be respected by every architectural commitment in the thematic files of this folder.
>
> Theme-internal architectural commitments and decisions live in the per-theme files of [Tier 2 index](vendor/gnomon/docs/design/2-architecture/_index). Tier 1 desiderata live in [Tier 1](vendor/gnomon/docs/design/1-framework/_index).

---

## Structural constraints

### Separation of concerns ^t2-separation-of-concerns

> [!INFO] Migrated to [activity separation](_framework-criteria#^t1-activity-separation)

Content and presentation are separated: canonical epistemic objects must be distinct from expository views, and neither may be edited through the other. This is the classical model-view separation (MVC, literate programming, source vs. executable).

*Source*: problem-statement-approach §Approach; architecture-1-layered-model §Canonical objects vs. View specifications.

### Single source of truth ^t2-single-source-of-truth

Each piece of epistemic content has exactly one canonical home. Derived views, registries, indexes, and rendered artifacts are regenerated from that canonical source, never edited directly. No artifact may become a primary source of truth; if it did, the architecture would collapse back into document-centric drift.

*Source*: problem-statement-approach §Approach; architecture-1-layered-model §Rendered artifacts vs. Canonical objects.

### Explicit dependency management ^t2-dependency-management

Dependencies between epistemic objects are first-class structures, not derivable properties of object-local fields. The dependency graph is maintained as an explicit structural layer with typed edges. This is analogous to a build system's dependency graph: the graph carries semantic information that cannot be reduced to the objects themselves.

*Source*: problem-statement-approach §Approach; registries-indexes-1; architecture-1-layered-model §Canonical objects vs. Graph structures.

### Strict layer dependency direction ^t2-layer-dependency

The architecture must enforce a strict dependency direction between layers. Each layer may only reference objects from the same layer or from layers it depends on. Dependency inversions (a canonical object depending on a rendered note; a graph edge created only in a note and not in the relation registry; an argument bundle containing content absent from the canonical layer) are forbidden.

*Source*: architecture-1-layered-model §Cross-layer dependency rules.

### Layer replaceability ^t2-layer-replaceability

Each layer must be replaceable without redefining the others. This is the test for whether a layer is principled or merely convenient: if replacing the rendering layer requires touching the canonical objects, the layering is leaking.

*Source*: architecture-1-layered-model §Core design principle.

### Narrow ontology, rich relations ^t2-narrow-ontology

The ontology of object kinds must remain small, closed, and role-pure. Rhetorical, procedural, target-relative, and presentational distinctions must be encoded as fields, statuses, or layer-specific annotations — not as new object kinds.

*Operational test* for whether a candidate deserves to be a new object kind:

| Criterion | Meaning |
|---|---|
| **Independent identity** | The object can be referred to, revised, compared, or reused without referring to a particular note, query, or rendering |
| **Context-transcendent reuse** | The same object can participate in multiple inquiries, bundles, and outputs |
| **Local validity conditions** | The object has intrinsic well-formedness criteria |
| **Independent editability** | Revising the object does not amount to merely changing an index, a path, or a display format |
| **Irreducibility** | The object cannot be faithfully encoded as a configuration of existing types without loss of structural information or inferential role |

A candidate that fails any condition belongs in a field, a status, a relation, or a higher-layer annotation.

*Source*: criteria-taxonomy §Ontological criterion, §Architectural criterion, §Attributes vs. Objects.

### Coverage completeness under narrowness ^t2-coverage-completeness

The narrowness of the ontology ([t2-narrow-ontology](#^t2-narrow-ontology)) does not excuse coverage gaps. The set of object kinds must span the full space of epistemic moves the framework is meant to support — formal derivation, mechanistic explanation, semantic grounding, motivational scaffolding, contrastive clarification, and inquiry direction. Narrowness and coverage are in tension: the tension is resolved by applying the operational test to each candidate, not by adding types freely or by dropping types dogmatically.

*Source*: criteria-taxonomy §Design constraints.

### Non-redundancy ^t2-non-redundancy

> [!INFO] Migrated to [non-redundancy](_framework-criteria#^t1-non-redundancy) (promoted T2 → T1).

Each interpretive point, result, or entity appears exactly once across the system. Duplication across notes, registries, or bundles is a hard error, not a style issue. This is the consistency condition that makes [t2-single-source-of-truth](#^t2-single-source-of-truth) enforceable.

*Source*: criteria-taxonomy (implicit via ontological compression); architecture-1-layered-model.

### Algebraic data types, not inheritance ^t2-no-inheritance

Subtype variations (e.g., `theorem`, `lemma`, `corollary` as variants of `claim`) must be modeled as tagged unions (sum types), not as OOP subtype polymorphism. The reason is that epistemic subtypes cannot stand in for one another by default: a lemma cannot stand in for a theorem in a proof context because their roles in the dependency graph differ structurally. An interface contract on the base type is appropriate; inheritance is not.

*Source*: criteria-taxonomy §No strict inheritance relation.

> [!missing] Reopen pending
> A staged proposal in [_fleeting-ideas](../_fleeting-ideas#^fleeting-python-oop) (Python-inspired OOP for epistemic objects) admits OOP inheritance as a candidate primitive for subtypes of epistemic objects. The reopen has been admitted; the counter-proposal — Haskell-style type classes / Scala traits / Rust traits — is also staged in the same fleeting entry and gives polymorphism without subtype substitutability. Re-ratification weighs both against the current ratified path.
>
> Downstream commitments that travel with this reopen — each must be re-evaluated together: [t2-subtype-safety](#^t2-subtype-safety), [t2-layer-replaceability](#^t2-layer-replaceability), [t2-common-abstract-base](object-kinds#^t2-common-abstract-base), and the open question [t2-subtype-discipline](object-kinds#^t2-subtype-discipline). The alternatives now on the table for the re-ratification: tagged unions (current ratified path), schema refinement, hybrid, OOP inheritance (from the Python proposal), and type classes / traits (from the Haskell/Scala/Rust assessment).

### Subtype safety ^t2-subtype-safety

Subtype labels must not imply that one subtype can stand in for another, shares the same validity semantics, or plays the same graph role when those properties do not hold. The architecture must ensure that introducing a subtype does not silently inherit interchangeability from a base type.

*Source*: promoted from the deleted architecture-construction log.

### Field-typing discipline ^t2-field-typing

Every field declared by any canonical kind, assembly kind, revision object, or operation schema must be one of: a scalar/enum, an embedded record, a typed reference, or a typed list of references. No field admits free composition outside this typed surface.

*Source*: ratified Tier-2 promotion (CT2-2). This was originally a Tier 3 criterion for fields and schema ("Field typing discipline"). It moved to Tier 2 because it is a meta-schema rule binding every theme that introduces fields, not a vocabulary choice internal to one aspect.

### Graph queryability ^t2-graph-queryability

> [!INFO] Migrated to [relational queryability](_framework-criteria#^t1-relational-queryability) (the F); the graph-representation mechanism becomes a T2 D in `relations-graph.md`.

The set of typed relations must be queryable as an addressable structure (e.g., for dependency analysis, reverse-impact, orphan detection). The dependency graph must exist as an addressable artifact, not merely as scattered references in prose.

*Source*: promoted from the queryability clause in the deleted architecture-construction log.

---

## Epistemic constraints

### Closed operational core ^t2-closed-operational-core

The framework must terminate reasoning-description at a finite library of primitive operation schemas with fixed functional semantics. A schema is admissible as primitive only if all of the following hold:

| Requirement | Meaning |
|---|---|
| **Fixed typed signature** | Exact input and output roles |
| **Explicit admissibility conditions** | When the schema may be used |
| **Explicit transformation semantics** | What the schema does |
| **Explicit success condition** | What completion means |
| **Explicit license kind** | How the schema is justified (deductive, empirical, methodological, definitional, interpretive...) |

*Source*: criteria-framework §Primitive operations; architecture-2-audit §Operation schema primitiveness.

### Revision semantics ^t2-revision-semantics

> [!INFO] Migrated to [revision accountability](_framework-criteria#^t1-revision-accountability) (promoted from T2 to T1, anchor renamed from `^t2-revision-semantics` to `^t1-revision-accountability`). The criterion now requires dependency tracking and correction propagation, not only the representation of revision events; the forward-edge / revision-edge / propagation specification becomes three separate T2 decisions (revision-recording, dependency-tracking, propagation) in the validity-revision theme.

The framework must represent how reasoning states are revised when sub-arguments fail, assumptions are weakened, or goals are reformulated. Without this, the framework can represent only completed reasoning, not research reasoning in progress.

Concretely, the architecture must support:

- **forward edges**: goal decomposition, operation application, object production,
- **revision edges**: goal revision triggered by operation failure, schema revision triggered by planning failure, question reformulation triggered by object revision,
- **propagation**: when an upstream object is revised, downstream objects are marked as potentially stale until re-validated.

The DAG acyclicity condition (enforced on individual reasoning snapshots) and the revision semantics (enforced across snapshots) are not in conflict — they describe different temporal slices.

*Source*: architecture-2-audit §Hidden assumptions; overview-formal-frameworks §AGM revision postulates.

### Defeasibility and regime stratification ^t2-defeasibility

> [!INFO] Migrated to [composition of warrant kinds](_framework-criteria#^t1-mixed-monotonicity) (the boundary-interface criterion; anchor unchanged, label retitled from "Mixed monotonicity" to "Composition of warrant kinds" to foreground the warrant-kind grain). The binary-classification clause is dropped — it is covered by the warrant-kind enum at `^t3-warrant-kind-enum`.

The framework must distinguish monotonic (proof-theoretic) and non-monotonic (argumentation-theoretic) validity regimes, and must specify the interface between them. At every node of the reasoning graph, the validity regime must be explicit so that a downstream consumer can determine whether the node's conclusion is retractable.

*Source*: architecture-2-audit §Monotonicity vs. defeasibility; overview-formal-frameworks §Interface problems.

### Multi-regime reasoning ^t2-multi-regime-reasoning

The framework is not specialized to one validity. It must admit deductive, abductive, evidential, exploratory, and analogical reasoning as legitimate reasoning kinds.

*Source*: promoted from the deleted architecture-construction log.

### Annotation richness ^t2-annotation-richness

Every inferential node must record more than the rule that licenses its conclusion. Some form of strategic or explanatory annotation is required in addition to the warrant.

*Source*: promoted from the deleted architecture-construction log.

### Snapshot DAG acyclicity ^t2-snapshot-dag

> [!INFO] Migrated to [no circular reasoning](_framework-criteria#^t1-no-circular-reasoning) (the F); DAG acyclicity becomes a derived T2 property, recorded in the classification table as `^t2-snapshot-dag-property` on the relational-graph representation, to be created during Step C of the refactor.

At a fixed time, the relations (`depends_on`, `supports`, ...) and the sub-goal or sub-question hierarchy must form a directed acyclic graph. Cycles in a snapshot indicate circular reasoning and are a hard error.

*Source*: promoted from the deleted architecture-construction log.

### Justificatory-level discrimination ^t2-justificatory-level-placement

The [three justificatory levels (t1-intelligibility)](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility) — licensing, strategic, explanatory — are functionally distinct: 

- licensing is intrinsic to the *inferential move*, 
- strategic and explanatory support depend on the *inquiry* that recruits the move. 

The architecture must respect this distinction wherever a reasoning annotation is recorded. A locus that conflates the levels is forbidden, because it asserts that inquiry-dependent content is intrinsic. For instance, a single intrinsic field on a canonical object must not mix licensing and strategic content.

*Source*: [t1-intelligibility](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility).

### Mechanical validation ^t2-mechanical-validation

> [!INFO] Migrated to [read-side automation](_framework-criteria#^t1-read-side-automation) and [write-side automation](_framework-criteria#^t1-write-side-automation) (split + promoted T2 → T1).

Schema validators must check whether objects, relations, and structures relative to a target are well formed; human judgment must not do that work. Examples of mechanical validators: required-field checks, edge typing, warrant presence, DAG acyclicity within snapshots, discharge accounting.

Motivational adequacy, explanatory relevance, and teleological usefulness can be audited by rules or heuristics, but their full assessment may still require human judgment.

*Source*: promoted from the deleted architecture-construction log.

---

## Operational constraints

### Representation vs. generation disambiguation ^t2-repr-vs-gen

> [!INFO] Retired in pass-5. The pass-4 promotion to `^t1-representation-vs-generation` was reversed: pass-5 audit found that the "modes" framing conflated three distinct axes already covered by sibling T1 criteria — [partial formalization tolerance](_framework-criteria#^t1-partial-formalization) (maturity), [activity coverage](_framework-criteria#^t1-activity-coverage) and [activity separation](_framework-criteria#^t1-activity-separation) (activity-kind), and [inquiry content and progression](_framework-criteria#^t1-inquiry-content-and-progression) (static-vs-dynamic). The architectural decision `^t2-representation-vs-generation` (in `operations-and-modes.md`) is reframed as the chosen response to these three sibling criteria. The blanket per-criterion mode-annotation requirement is dropped.

The framework distinguishes two modes, each with different requirements:

- **Representation mode**: post-hoc annotation of completed reasoning. Requires completeness of the representation language but not operability.
- **Generation mode**: operative guidance during research. Requires operability and decidable applicability but admits partial specification.

Every aspect-specific criterion must declare which mode it applies to, and what degradation occurs in the other mode. A criterion that conflates the two modes is ill-formed.

*Source*: architecture-2-audit §Representation vs. generation.

---

## Irreducible tensions

Four tensions across the criteria are irreducible. They cannot be dissolved by better design; they must be recorded at each design decision so that the chosen tradeoff is explicit and auditable.

### X1 — Expressivity vs. non-arbitrariness ^t2-x1

[t1-expressivity](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-expressivity) demands support for reasoning patterns not anticipated by the schema inventory. [t1-non-arbitrary](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-non-arbitrary) demands that operations be schema-governed. Either the schema inventory is closed (and expressivity is bounded) or it is open (and non-arbitrariness is nominal).

*Resolution pattern*: adopt a schema calculus — a small set of primitive schema constructors from which schemas for domains are derived. This bounds the schema space structurally while admitting new schemas under principled construction. Settled at [t2-operation-primitiveness](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness) (open) and instantiated in [Operation schemas](vendor/gnomon/docs/design/3-aspect-specific/operation-schemas).

### X2 — Formalization depth vs. usability ^t2-x2

[t1-intelligibility](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility) demands that every step carry licensing, strategic, and explanatory justification. [t1-partial-formalization](vendor/gnomon/docs/design/1-framework/operational-quality#^t1-partial-formalization) and [t1-feasibility](vendor/gnomon/docs/design/1-framework/operational-quality#^t1-feasibility) demand that the annotation burden not exceed what researchers tolerate. These are in irreducible tension for moderately complex proofs and informal arguments.

*Resolution pattern*: each profile partitions fields into mandatory and optional sets, with named guarantees that weaken when the profile loosens. Selected at [t2-reasoning-annotation-fields](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-fields) and instantiated in [Reasoning-annotation field set](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields). Profile contents deferred to [t2-partial-formalization-profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles).

### X3 — Narrow ontology vs. coverage completeness ^t2-x3

[t2-narrow-ontology](#^t2-narrow-ontology) demands few object kinds. [t1-expressivity](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-expressivity) and [t2-coverage-completeness](#^t2-coverage-completeness) demand that the ontology span all epistemic moves.

*Resolution pattern*: the operational test in [t2-narrow-ontology](#^t2-narrow-ontology) (five conditions) is the discriminator. A candidate is admitted only if it passes all five; otherwise it becomes a field, status, relation, or annotation. Recorded at [t2-object-kind-admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission).

### X4 — Acyclicity vs. revision ^t2-x4

Reasoning snapshots must be DAGs ([t2-snapshot-dag](#^t2-snapshot-dag), discharge accounting). Research reasoning is inherently cyclic (revision, retraction, goal reformulation). The representations must support both.

*Resolution pattern*: the framework distinguishes snapshot slices (DAG-valid) from revision history (cyclic edges allowed, with temporal stamps). A snapshot is a temporal cross-section; revisions move the system from one snapshot to another. Recorded at [t2-revision-feedback](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback).

---

## Known gaps

The following are demanded by the reference frameworks and by the internal audits but are not yet operationalized. They are blocking gaps for Phase 1 of the operational route and must be filled before aspect-specific decisions are frozen.

- **G1 — Partial formalization policy** ([t1-partial-formalization](vendor/gnomon/docs/design/1-framework/operational-quality#^t1-partial-formalization)). What exactly is mandatory vs. optional at each note type and each formalization profile? Currently undefined; addressed at [t2-partial-formalization-profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles) (open).
- **G2 — Revision propagation semantics** ([t2-revision-semantics](#^t2-revision-semantics)). When an upstream object is revised, what exactly happens to downstream bundles, arguments, and rendered notes? Settled at [t2-revision-feedback](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback) and its sub-questions.
- **G3 — Validity regime interface** ([t2-defeasibility](#^t2-defeasibility)). How do monotonic and non-monotonic regions of the reasoning graph interoperate at their boundary? Settled at [t2-warrant-annotation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation) together with [t2-propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation).
- **G4 — Closed operational core termination** ([t2-closed-operational-core](#^t2-closed-operational-core)). The current treatment asserts primitivity without deriving it. Addressed at [t2-operation-primitiveness](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness) (open).
- **G5 — Representation-vs-generation bifurcation** ([t2-repr-vs-gen](#^t2-repr-vs-gen)). Several documents oscillate between the two modes. A clean separation with distinct guarantees is missing; addressed at [t2-representation-vs-generation](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-representation-vs-generation) and [t2-partial-formalization-profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles) (open).
