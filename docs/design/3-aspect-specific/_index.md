---
tags:
  - index
index: "[Design documentation](../_index.md)"
aliases:
  - Aspect-specific decisions
---
# Tier 3 — Aspect-specific decisions

Tier 3 files fill in what the architecture defers: vocabulary entries, field sets, validator diagnostics, and choices that belong to a single aspect. Each file follows a uniform structure:

1. **Header** — the architectural commitments the aspect instantiates and the upstream anchors.
2. **Criteria** — requirements that bind the theme, anchored as `^t3-<short>`.
3. **Decisions** — ratified choices, each opened by a `[!QUESTION]` callout that names the question the choice answers.
4. **Open questions** — pending subsidiary choices, each opened by a `[!QUESTION]` callout.

## Files

- [Reasoning-annotation field set](reasoning-fields.md) — fields, types, and formalization profiles for each locus × content kind (instantiates [reasoning-annotation fields](../2-architecture/reasoning-structure.md#^t2-reasoning-annotation-fields), [partial-formalization profiles](../2-architecture/granularity.md#^t2-partial-formalization-profiles)).
- [Revision vocabulary](revision-vocabulary.md) — enum for revision kinds, enum for failure kinds, schema for revision objects, archival diagnostics, and examples of how changes propagate (instantiates [revision and feedback semantics](../2-architecture/validity-revision.md#^t2-revision-feedback) and its sub-questions).
- [Warrant vocabulary](warrant-vocabulary.md) — enum for warrant kinds and the rule that combines incoming edges to determine whether a node can be defeated (instantiates [warrant kind on support relations](../2-architecture/validity-revision.md#^t2-warrant-annotation)).
- [Status vocabulary](status-vocabulary.md) — status enums by object kind, the contrast between maturity and warrant kind, and how status changes propagate (instantiates [epistemic status as a maturity record](../2-architecture/object-kinds.md#^t2-epistemic-status)).
- [Operation schemas](operation-schemas.md) — constructors that generate operation schemas and the contents required under each reading of primitiveness (instantiates [whether operation schemas are primitive](../2-architecture/operations-and-modes.md#^t2-operation-primitiveness), [where operation schemas live](../2-architecture/operations-and-modes.md#^t2-operation-schema-placement)).
- [Ontology of object kinds](ontology.md) — test for admitting object kinds and criteria used in the decision table (stub; instantiates [object-kind admission](../2-architecture/object-kinds.md#^t2-object-kind-admission)).
- [Arguments and reasoning](arguments-reasoning.md) — criteria that assemblies must satisfy to count as good arguments (stub; traces to [justification levels](../1-framework/reasoning-integrity.md#^t1-justification-levels) and [promotion of assembly-local records](../2-architecture/reasoning-structure.md#^t2-assembly-record-promotion)).
- [Semantic relations](semantic-relations.md) — criteria for the typed vocabulary between relations (stub; traces to [typed relation vocabulary](../2-architecture/relations-graph.md#^t2-typed-relation-vocabulary)).
- [Registries and indexes](registries-indexes.md) — criteria for registries derived from source records (stub; traces to [relation storage locus](../2-architecture/relations-graph.md#^t2-relation-storage-locus)).
- [Rendering and views](rendering-views.md) — criteria for the rendering layer and view specs (stub; traces to [derived artifacts](../2-architecture/layering.md#^t2-derived-artifacts), [view specifications](../2-architecture/layering.md#^t2-view-specifications)).
- [IDs, namespaces, versioning](ids-versioning.md) — identifier and namespace criteria (stub).
- [Workflows](workflows.md) — criteria for inquiry workflows (stub).
- [Relevance vocabulary](relevance-vocabulary.md) — relevance-kind vocabulary (stub).
- [Scope fields](scope-fields.md) — criteria for fields that bound an inquiry's scope (stub).
