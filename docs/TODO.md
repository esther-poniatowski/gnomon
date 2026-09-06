---
tags:
  - tasks
index: "[gnomon documentation](_index.md)"
aliases:
  - Design TODO
---
# Advancing the design of `gnomon`

## Current state

The design now lives in three tiers under the [design folder](design). The tier folders are authoritative; older proposal files remain informational sources only.

- [Tier 1](design/1-framework/_index.md) records desiderata for the whole framework.
- [Tier 2](design/2-architecture/_index.md) records architectural commitments, constraints that cut across themes, and open architectural questions.
- [Tier 3](design/3-aspect-specific/_index.md) records criteria for each aspect, ratified contents, and open aspect decisions.

## Alignment audit

| Original task | Status after refactor | Current owner |
| --- | --- | --- |
| Extract common design principles and make the criteria coherent. | Done. Tier 1 and Tier 2 criteria now carry the common principles and constraints that cut across themes. | [Tier 1 index](design/1-framework/_index.md), [Tier 2 index](design/2-architecture/_index.md) |
| Fix the design model of the package. | Done for the architectural backbone. One architectural question remains: layer feedback. | [Layering](design/2-architecture/layering.md), [layer-feedback policy](design/2-architecture/layering.md#^t2-layer-feedback) |
| Fix the ontology of epistemic objects. | Still open. The admission rule is fixed, but the actual taxonomy and subtype discipline remain unsettled. | [Object-kind admission](design/2-architecture/object-kinds.md#^t2-object-kind-admission), [subtype discipline](design/2-architecture/object-kinds.md#^t2-subtype-discipline), [ontology](design/3-aspect-specific/ontology.md) |
| Determine the minimally sufficient semantic relations and how to encode them. | Partly done. Relation typing and storage locus are fixed; the relation vocabulary and build-error policy remain open. | [Relations graph](design/2-architecture/relations-graph.md), [semantic relations](design/3-aspect-specific/semantic-relations.md) |
| Determine common fields and fields for each type. | Partly done. The common abstract base and field typing are fixed; fields for each type remain downstream of ontology and schema field work. | [Common abstract base](design/2-architecture/object-kinds.md#^t2-common-abstract-base), [field-typing discipline](design/2-architecture/object-kinds.md#^t2-field-typing), [reasoning fields](design/3-aspect-specific/reasoning-fields.md), [ontology](design/3-aspect-specific/ontology.md) |
| Determine namespace, ID, and versioning conventions. | Still open. Criteria exist, but decisions have not been drafted. | [IDs, namespaces, versioning](design/3-aspect-specific/ids-versioning.md) |
| Determine how to represent and decompose questions. | Partly done. Question-vs-Goal is resolved; question decomposition, scope fields, and use in workflows remain open. | [Question vs. Goal](design/2-architecture/object-kinds.md#^t2-question-vs-goal), [granularity strata](design/2-architecture/granularity.md#^t2-granularity-strata), [workflows](design/3-aspect-specific/workflows.md), [scope fields](design/3-aspect-specific/scope-fields.md) |
| Determine how to encode terminal arguments and derivations. | Partly done. Assemblies relative to a target and annotation loci are fixed; argument internals and reasoning granularity remain open. | [Reasoning structure](design/2-architecture/reasoning-structure.md), [reasoning-record storage](design/2-architecture/granularity.md#^t2-reasoning-record-storage), [arguments and reasoning](design/3-aspect-specific/arguments-reasoning.md) |
| Determine module structure and workspace architecture. | Partly done. The structure of the design documents and the architectural layers are fixed; source tree layout for object stores, registries, and views remains open. | [Layering](design/2-architecture/layering.md), [registries and indexes](design/3-aspect-specific/registries-indexes.md), [IDs, namespaces, versioning](design/3-aspect-specific/ids-versioning.md) |
| Determine data formats. | Done. | [source languages, metadata, and grammar](design/2-architecture/data-formats.md) |
| Determine registries and indexes. | Partly done. Relation storage locus and argument-aware indexes are fixed; registry contents and build products remain open. | [Relation storage locus](design/2-architecture/relations-graph.md#^t2-relation-storage-locus), [argument-aware indexes](design/2-architecture/layering.md#^t2-registries-arguments), [registries and indexes](design/3-aspect-specific/registries-indexes.md) |
| Clarify the rendering layer strategy. | Partly done. Derived artifacts and view specifications are fixed; rendering manifests, projection types, and view contracts remain open. | [Derived artifacts](design/2-architecture/layering.md#^t2-derived-artifacts), [view specifications](design/2-architecture/layering.md#^t2-view-specifications), [rendering and views](design/3-aspect-specific/rendering-views.md) |
| Check whether the model optimizes understanding. | Partly done. Intelligibility and argument-quality criteria exist; the check must run again after argument, workflow, and rendering decisions are drafted. | [Intelligibility](design/1-framework/reasoning-integrity.md#^t1-justification-levels), [arguments and reasoning](design/3-aspect-specific/arguments-reasoning.md), [workflows](design/3-aspect-specific/workflows.md), [rendering and views](design/3-aspect-specific/rendering-views.md) |
| Establish concrete workflows. | Still open. Workflow criteria exist, but decisions have not been drafted. | [Workflows](design/3-aspect-specific/workflows.md), [scope fields](design/3-aspect-specific/scope-fields.md) |

## Current TODO

### Tier 2 architectural decisions

- [ ] Settle [layer-feedback policy](design/2-architecture/layering.md#^t2-layer-feedback).
- [ ] Settle [subtype discipline](design/2-architecture/object-kinds.md#^t2-subtype-discipline).
- [ ] Settle [operation-schema primitiveness](design/2-architecture/operations-and-modes.md#^t2-operation-primitiveness).
- [ ] Settle [planning-execution synchronization](design/2-architecture/operations-and-modes.md#^t2-planning-execution-sync).
- [ ] Settle [reasoning-record storage](design/2-architecture/granularity.md#^t2-reasoning-record-storage).
- [ ] Settle [granularity strata](design/2-architecture/granularity.md#^t2-granularity-strata).
- [ ] Settle [partial-formalization profiles](design/2-architecture/granularity.md#^t2-partial-formalization-profiles).
- [ ] Route the build-error policy from [relations graph](design/2-architecture/relations-graph.md#^t2-relation-storage-locus) into the validator-placement work.

### Tier 3 aspect decisions

- [ ] Draft the canonical object taxonomy in [ontology](design/3-aspect-specific/ontology.md).
- [ ] Draft the closed relation vocabulary in [semantic relations](design/3-aspect-specific/semantic-relations.md).
- [ ] Draft the namespace, identifier, and ontology versioning decisions in [IDs, namespaces, versioning](design/3-aspect-specific/ids-versioning.md).
- [ ] Draft registry contents, build products, and staging rules in [registries and indexes](design/3-aspect-specific/registries-indexes.md).
- [ ] Draft rendering manifests, view contracts, and projection types in [rendering and views](design/3-aspect-specific/rendering-views.md).
- [ ] Draft inquiry workflows in [workflows](design/3-aspect-specific/workflows.md).
- [ ] Draft scope-field decisions in [scope fields](design/3-aspect-specific/scope-fields.md).
- [ ] Draft argument and derivation internals in [arguments and reasoning](design/3-aspect-specific/arguments-reasoning.md).
- [ ] Settle the explanatory-gain enum, per-cell field selection, and named profile chain in [reasoning fields](design/3-aspect-specific/reasoning-fields.md).
- [ ] Settle assembly-internal warrant kinds and unresolved warrant classifications in [warrant vocabulary](design/3-aspect-specific/warrant-vocabulary.md).
- [ ] Settle status-transition propagation in [status vocabulary](design/3-aspect-specific/status-vocabulary.md).
- [ ] Settle transmitting relation set and priority combination in [revision vocabulary](design/3-aspect-specific/revision-vocabulary.md).
- [ ] Settle admissibility specifications for each constructor and compound schema naming in [operation schemas](design/3-aspect-specific/operation-schemas.md).
- [ ] Draft relevance-kind decisions in [relevance vocabulary](design/3-aspect-specific/relevance-vocabulary.md).

## Dispatch notes

The old TODO raised several decisions that now belong in specific tier files:

- **Object taxonomy** belongs in Tier 3 [ontology](design/3-aspect-specific/ontology.md), constrained by Tier 2 [object-kind admission](design/2-architecture/object-kinds.md#^t2-object-kind-admission) and [subtype discipline](design/2-architecture/object-kinds.md#^t2-subtype-discipline).
- **Relation vocabulary** belongs in Tier 3 [semantic relations](design/3-aspect-specific/semantic-relations.md), constrained by Tier 2 [typed relation vocabulary](design/2-architecture/relations-graph.md#^t2-typed-relation-vocabulary) and [relation storage locus](design/2-architecture/relations-graph.md#^t2-relation-storage-locus).
- **Question decomposition** splits across Tier 2 [granularity strata](design/2-architecture/granularity.md#^t2-granularity-strata), Tier 3 [workflows](design/3-aspect-specific/workflows.md), and Tier 3 [scope fields](design/3-aspect-specific/scope-fields.md).
- **Terminal arguments and derivations** split across Tier 2 [reasoning-record storage](design/2-architecture/granularity.md#^t2-reasoning-record-storage), Tier 2 [partial-formalization profiles](design/2-architecture/granularity.md#^t2-partial-formalization-profiles), and Tier 3 [arguments and reasoning](design/3-aspect-specific/arguments-reasoning.md).
- **Workspace layout** depends on Tier 3 [IDs, namespaces, versioning](design/3-aspect-specific/ids-versioning.md), Tier 3 [registries and indexes](design/3-aspect-specific/registries-indexes.md), and Tier 3 [rendering and views](design/3-aspect-specific/rendering-views.md).
- **Understanding optimization** is not a standalone design object. It is an audit pass over [arguments and reasoning](design/3-aspect-specific/arguments-reasoning.md), [workflows](design/3-aspect-specific/workflows.md), and [rendering and views](design/3-aspect-specific/rendering-views.md) after those decisions exist.

---
