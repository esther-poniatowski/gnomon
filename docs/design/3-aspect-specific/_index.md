# Tier 3 — Aspect-specific decisions

Tier 3 files fill in what the architecture defers: vocabulary entries, field sets, validator diagnostics, and choices that belong to a single aspect. Each file follows a uniform structure:

1. **Header** — the architectural commitments the aspect instantiates and the upstream anchors.
2. **Criteria** — requirements that bind the theme, anchored as `^t3-<short>`.
3. **Decisions** — ratified choices, each opened by a `[!QUESTION]` callout that names the question the choice answers.
4. **Open questions** — pending subsidiary choices, each opened by a `[!QUESTION]` callout.

## Files

- [Reasoning-annotation field set](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields) — fields, types, and formalization profiles for each locus × content kind (instantiates [reasoning-annotation fields](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-fields), [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles)).
- [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary) — enum for revision kinds, enum for failure kinds, schema for revision objects, archival diagnostics, and examples of how changes propagate (instantiates [revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback) and its sub-questions).
- [Warrant vocabulary](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary) — enum for warrant kinds and the rule that combines incoming edges to determine whether a node can be defeated (instantiates [warrant kind on support relations](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation)).
- [Status vocabulary](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary) — status enums by object kind, the contrast between maturity and warrant kind, and how status changes propagate (instantiates [epistemic status as a maturity record](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status)).
- [Operation schemas](vendor/gnomon/docs/design/3-aspect-specific/operation-schemas) — constructors that generate operation schemas and the contents required under each reading of primitiveness (instantiates [whether operation schemas are primitive](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness), [where operation schemas live](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-schema-placement)).
- [Ontology of object kinds](vendor/gnomon/docs/design/3-aspect-specific/ontology) — test for admitting object kinds and criteria used in the decision table (stub; instantiates [object-kind admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission)).
- [Arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning) — criteria that assemblies must satisfy to count as good arguments (stub; traces to [t1-intelligibility](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility) and [promotion of assembly-local records](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-assembly-record-promotion)).
- [Semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations) — criteria for the typed vocabulary between relations (stub; traces to [typed relation vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary)).
- [Registries and indexes](vendor/gnomon/docs/design/3-aspect-specific/registries-indexes) — criteria for registries derived from source records (stub; traces to [relation storage locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus)).
- [Rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views) — criteria for the rendering layer and view specs (stub; traces to [derived artifacts](vendor/gnomon/docs/design/2-architecture/layering#^t2-derived-artifacts), [view specifications](vendor/gnomon/docs/design/2-architecture/layering#^t2-view-specifications)).
- [IDs, namespaces, versioning](vendor/gnomon/docs/design/3-aspect-specific/ids-versioning) — identifier and namespace criteria (stub).
- [Workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows) — criteria for inquiry workflows (stub).
- [Relevance vocabulary](vendor/gnomon/docs/design/3-aspect-specific/relevance-vocabulary) — relevance-kind vocabulary (stub).
- [Scope fields](vendor/gnomon/docs/design/3-aspect-specific/scope-fields) — criteria for fields that bound an inquiry's scope (stub).
