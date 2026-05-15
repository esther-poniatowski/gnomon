# Relations and the dependency graph

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how typed relations between objects are declared, authored, persisted, and queried — and about the dependency graph derived from them.
>
> Cross-cutting Tier-2 criteria that constrain decisions in this file: see [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints), in particular [t2-dependency-management](vendor/gnomon/docs/design/2-architecture/constraints#^t2-dependency-management), [t2-graph-queryability](vendor/gnomon/docs/design/2-architecture/constraints#^t2-graph-queryability), [t2-snapshot-dag](vendor/gnomon/docs/design/2-architecture/constraints#^t2-snapshot-dag), [t2-single-source-of-truth](vendor/gnomon/docs/design/2-architecture/constraints#^t2-single-source-of-truth), [t2-field-typing](vendor/gnomon/docs/design/2-architecture/constraints#^t2-field-typing).

---

## Decisions

### Typed relation vocabulary ^t2-typed-relation-vocabulary

> [!QUESTION] What discipline governs the relation vocabulary between objects: open or closed, typed or free-form?

The relation vocabulary is **closed and typed**:

- **Closed vocabulary.** The admissible relation labels (e.g. `supports`, `depends_on`, `answers`, `refines`, `uses`, `contrasts_with`, ...) are declared by the schema. The exact list is deferred to [the project TODO](vendor/gnomon/docs/TODO). No relation may exist outside the declared vocabulary.
- **Typed edges.** Every relation carries a type drawn from the vocabulary, with declared source and target types.

Queryability and addressability of the resulting graph are enforced by [t2-graph-queryability](vendor/gnomon/docs/design/2-architecture/constraints#^t2-graph-queryability).

The actual relation-vocabulary contents are aspect-specific; see [Semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations).

> [!missing] Tension with progressive relation formalization
> A staged proposal in [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-relation-formalization) (concept-map linking phrases) argues for free-text relation labels that harden progressively into controlled types — `free linking phrase → controlled relation type → formal predicate`. This tensions with the closed-and-typed commitment here. The closed vocabulary applies partial formalization to *content* but not to *edges*; the proposal extends [t1-partial-formalization](vendor/gnomon/docs/design/_framework-criteria#^t1-partial-formalization) to the relation grain. The tension is recorded for whoever resolves the relation vocabulary; this decision is not reopened. Resolution must state whether a draft profile admits free linking phrases that a stricter profile later resolves to declared types, or whether closure holds at every maturity level.

### Relation storage locus ^t2-relation-storage-locus

> [!QUESTION] Where are typed relations between objects authored, and where are they read?

**Edges are authored on objects with an authoring-vs-querying asymmetry.**

- **Authoring locus.** Each object's file declares its outgoing relations as typed fields (e.g. `depends_on: [obj-42]`). Authors edit objects (local, contextual editing).
- **Read locus.** A build step parses the authored edges, validates them against the schema (vocabulary closure, type compatibility, dangling references), and produces a derived relation registry and dependency graph. Downstream consumers (structural indexes, argument bundles, view specifications, artifacts) read **only** the registry. Object-level edge fields are inputs to the build, not query targets.

The asymmetry preserves [t1-modularity](vendor/gnomon/docs/design/1-framework/structural-quality#^t1-modularity) and [t2-single-source-of-truth](vendor/gnomon/docs/design/2-architecture/constraints#^t2-single-source-of-truth).

The "edges authored on objects" rule covers every record with identity in the source layer, not only canonical objects. Per [assemblies relative to a target](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-target-relative-assemblies), assemblies are records with identity in their own parallel store; the inquiring author edits an assembly's outgoing edges and authored content directly in the assembly file. The build treats canonical objects and assemblies uniformly as sites that author edges. The asymmetry that survives is between **canonical** identity and identity **relative to a target** (governed by [t2-object-kind-admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission)), not between **authored** and **non-authored** records.

> [!missing] Build-error policy
> Dangling references, vocabulary violations, and type mismatches must be caught at build time and reported as build errors; they must not be silently dropped from the registry. The exact build-error policy is deferred to the validator work in [t2-validator-placement](vendor/gnomon/docs/design/2-architecture/validation-views#^t2-validator-placement).
