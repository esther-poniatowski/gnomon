# Relations and the dependency graph

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how typed relations between objects are declared, authored, persisted, and queried — and about the dependency graph derived from them.
>
> Snapshot acyclicity of the dependency graph is a well-formedness property recorded in this file at [snapshot acyclicity](#^t2-snapshot-dag-property); it realises the no-circular-reasoning facet of [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing). The meta-schema rule [field-typing discipline](object-kinds#^t2-field-typing) binds the edge fields declared here. Framework-level criteria bearing on this theme: [relational queryability](../1-framework/modular-content-organization#^t1-relational-queryability) — the capability the relational graph implements — and [single source of truth](../1-framework/research-activities-workflows#^t1-single-source-of-truth).

---

## Decisions

### Typed relation vocabulary ^t2-typed-relation-vocabulary

> [!QUESTION] What discipline governs the relation vocabulary between objects: open or closed, typed or free-form?

The relation vocabulary is **closed and typed**:

- **Closed vocabulary.** The admissible relation labels (e.g. `supports`, `depends_on`, `answers`, `refines`, `uses`, `contrasts_with`, ...) are declared by the schema. The exact list is deferred to [the project TODO](vendor/gnomon/docs/TODO). No relation may exist outside the declared vocabulary.
- **Typed edges.** Every relation carries a type drawn from the vocabulary, with declared source and target types.

Queryability and addressability of the resulting graph are enforced by [relational queryability](../1-framework/modular-content-organization#^t1-relational-queryability).

The actual relation-vocabulary contents are aspect-specific; see [Semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations).

> [!missing] Tension with progressive relation formalization
> A staged proposal in [fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-relation-formalization) (concept-map linking phrases) argues for free-text relation labels that harden progressively into controlled types — `free linking phrase → controlled relation type → formal predicate`. This tensions with the closed-and-typed commitment here. The closed vocabulary applies partial formalization to *content* but not to *edges*; the proposal extends [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization) to the relation grain. The tension is recorded for whoever resolves the relation vocabulary; this decision is not reopened. Resolution must state whether a draft profile admits free linking phrases that a stricter profile later resolves to declared types, or whether closure holds at every maturity level.

### Relation storage locus ^t2-relation-storage-locus

> [!QUESTION] Where are typed relations between objects authored, and where are they read?

**Edges are authored on objects with an authoring-vs-querying asymmetry.**

- **Authoring locus.** Each object's file declares its outgoing relations as typed fields (e.g. `depends_on: [obj-42]`). Authors edit objects (local, contextual editing).
- **Read locus.** A build step parses the authored edges, validates them against the schema (vocabulary closure, type compatibility, dangling references), and produces a derived relation registry and dependency graph. Downstream consumers (structural indexes, argument bundles, view specifications, artifacts) read **only** the registry. Object-level edge fields are inputs to the build, not query targets.

The asymmetry preserves [t1-modularity](../1-framework/modular-content-organization#^t1-reuse) and [single source of truth](../1-framework/research-activities-workflows#^t1-single-source-of-truth).

The "edges authored on objects" rule covers every record with identity in the source layer, not only canonical objects. Per [assemblies relative to a target](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-target-relative-assemblies), assemblies are records with identity in their own parallel store; the inquiring author edits an assembly's outgoing edges and authored content directly in the assembly file. The build treats canonical objects and assemblies uniformly as sites that author edges. The asymmetry that survives is between **canonical** identity and identity **relative to a target** (governed by [t2-object-kind-admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission)), not between **authored** and **non-authored** records.

> [!missing] Build-error policy
> Dangling references, vocabulary violations, and type mismatches must be caught at build time and reported as build errors; they must not be silently dropped from the registry. The exact build-error policy is deferred to the validator work in [t2-validator-placement](vendor/gnomon/docs/design/2-architecture/validation-views#^t2-validator-placement).

### Relational graph representation ^t2-relational-graph-representation

> [!QUESTION] In what data structure are the typed relations exposed for querying?

**As a graph data structure** — nodes are objects, edges are typed relations — built from the object-authored edges. The graph is the chosen implementation of the framework-level [relational queryability](../1-framework/modular-content-organization#^t1-relational-queryability) capability; the alternatives considered and set aside are relational tables and triple stores.

The dependency graph carries semantic structure that cannot be reduced to the objects themselves: it is **explicit**, not a property inferred on demand from object-local fields. The build aggregates the object-authored edges (per [relation storage locus](#^t2-relation-storage-locus)) into this graph as a derived, addressable artifact — analogous to a build system's dependency graph. Downstream consumers query the graph, never the scattered object-level edge fields. Making the graph explicit lets the vault be read as a **reasoning or argument map** rather than a flat collection of documents.

The contrast that matters is **explicit vs. inferred-on-demand**, not object-local vs. centralized: relations *are* authored object-locally, and the build is what makes them an addressable structure.

**Snapshot acyclicity is a derived property of this graph.** ^t2-snapshot-dag-property
Within a single reasoning snapshot, the inferential-support sub-graph (`depends_on`, `supports`, and the sub-goal hierarchy) is a **directed acyclic graph**: a cycle is a hard build-time error. Acyclicity is not a separate commitment but a well-formedness property the build checks on the graph this decision derives. It realises the no-circular-reasoning facet of [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing): a step's justification must not ultimately rest on itself. The check **exempts** structures marked as a legitimate mutual constraint — co-definition or co-determination — rather than flagging them. Revision history is deliberately excluded from the acyclic sub-graph: revision episodes are recorded as objects, not edges, so the cyclic revision dependency of [revision accountability](../1-framework/research-activities-workflows#^t1-revision-accountability) does not violate snapshot acyclicity. Whether the inferential-support graph is one layer among several superimposed graphs is the open question [fundamental dependency kinds and graph layering](#^t2-dependency-graph-layers).

---

## Open questions

### Relation reification threshold ^t2-relation-reification

> [!QUESTION] When is a relation encoded as a standalone object rather than a directed field on its source?

A relation can be encoded in more than one way: as a directed field on the source object pointing to a reference; as a standalone object that names its participants; or as an entry in a separate registry. [Relation storage locus](#^t2-relation-storage-locus) fixes *where* edges are authored and read, but it assumes the field encoding throughout and does not say when a relation should instead be **reified** into an object of its own.

A relation needs its own object identity once it carries more structure than a bare typed link. A candidate threshold: **reify a relation as soon as it must carry its own warrant, status, scope, or further relations** — that is, as soon as the relation is itself something the framework reasons *about*, not merely *with*. A relation that is a bare label between two objects stays a field; a relation that bears annotations, or that other relations point at, becomes an object.

Resolution must state the threshold precisely and how it interacts with the [typed relation vocabulary](#^t2-typed-relation-vocabulary) (whether reification is per relation kind or per relation instance) and with [t1-typed-object-decomposition](../1-framework/framework-foundations#^t1-typed-object-decomposition) (a reified relation is itself a typed object).

### Fundamental dependency kinds and graph layering ^t2-dependency-graph-layers

> [!QUESTION] What fundamental kinds of dependency must the framework represent, and do they form one typed graph or several superimposed graphs?

[Typed relation vocabulary](#^t2-typed-relation-vocabulary) fixes that relation labels are closed and typed, and [relation storage locus](#^t2-relation-storage-locus) fixes where edges are authored and read. Both treat the relations as one graph distinguished only by edge label. Neither asks the prior question: which *fundamentally distinct* kinds of dependency the framework must carry, and whether those kinds belong in a single graph or in several **superimposed graphs** over the same objects.

Distinct dependency kinds plausibly differ in more than their label — in their acyclicity obligation, their propagation behaviour, and the activity that authors them. Two candidate partitions stand:

**Four-layer proposal — by structural authoring source.** The kinds are distinguished by where the edge originates in the framework's machinery.

- **Inferential support** — what licenses what; constrained to a DAG per [snapshot acyclicity](#^t2-snapshot-dag-property).
- **Gap decomposition** — the sub-goal / sub-question hierarchy; a separate well-foundedness obligation.
- **Revision dependency** — which objects a revision episode reaches; cyclic across snapshots per [t1-revision-accountability](../1-framework/research-activities-workflows#^t1-revision-accountability).
- **Definitional / terminological reference** — which content a definition or term draws on.

**Three-family proposal — by the role the edge plays in reading the graph.** The kinds are distinguished by *why* a reader must traverse the edge.

- **Semantic dependence** — required to *interpret* a statement (what content a meaning rests on); subsumes the four-layer proposal's definitional / terminological reference.
- **Justificatory dependence** — required to *validate or derive* a statement; subsumes the four-layer proposal's inferential support.
- **Inquiry relevance** — required because of the *current target question or methodological route*; not currently in the four-layer proposal, and orthogonal to the others in that it varies with the reader's target rather than being a permanent feature of the graph.

The two proposals partition the same edge population by different cuts. Resolution must identify the closed set of fundamental dependency kinds, state for each whether it is a layer of one shared graph or a graph of its own, state how the layering interacts with the closed [typed relation vocabulary](#^t2-typed-relation-vocabulary) and with the per-edge warrant kind at [t2-warrant-annotation](validity-revision#^t2-warrant-annotation), and clarify whether the three-family proposal's *inquiry relevance* is a permanent edge kind or a target-relative view computed by the [relevance index](../3-aspect-specific/registries-indexes#^t3-registry-component-taxonomy). It subsumes the broader reading of the former `^t2-revision-semantics` criterion, which named forward, revision, and propagation edges but stopped short of asking whether they constitute distinct graphs.

Bearing criteria: [t1-typed-object-decomposition](../1-framework/framework-foundations#^t1-typed-object-decomposition), [relational graph representation](#^t2-relational-graph-representation), [snapshot acyclicity](#^t2-snapshot-dag-property), [t1-revision-accountability](../1-framework/research-activities-workflows#^t1-revision-accountability).
