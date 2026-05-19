# Advancing the design of `gnomon`

## Current state

The design now lives in three tiers under the [design folder](vendor/gnomon/docs/design). The tier folders are authoritative; older proposal files remain informational sources only.

- [Tier 1](vendor/gnomon/docs/design/1-framework/_index) records desiderata for the whole framework.
- [Tier 2](vendor/gnomon/docs/design/2-architecture/_index) records architectural commitments, constraints that cut across themes, and open architectural questions.
- [Tier 3](vendor/gnomon/docs/design/3-aspect-specific/_index) records criteria for each aspect, ratified contents, and open aspect decisions.

## Alignment audit

| Original task | Status after refactor | Current owner |
| --- | --- | --- |
| Extract common design principles and make the criteria coherent. | Done. Tier 1 and Tier 2 criteria now carry the common principles and constraints that cut across themes. | [Tier 1 index](vendor/gnomon/docs/design/1-framework/_index), [Tier 2 index](vendor/gnomon/docs/design/2-architecture/_index) |
| Fix the design model of the package. | Done for the architectural backbone. One architectural question remains: layer feedback. | [Layering](vendor/gnomon/docs/design/2-architecture/layering), [layer-feedback policy](vendor/gnomon/docs/design/2-architecture/layering#^t2-layer-feedback) |
| Fix the ontology of epistemic objects. | Still open. The admission rule is fixed, but the actual taxonomy and subtype discipline remain unsettled. | [Object-kind admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission), [subtype discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-subtype-discipline), [ontology](vendor/gnomon/docs/design/3-aspect-specific/ontology) |
| Determine the minimally sufficient semantic relations and how to encode them. | Partly done. Relation typing and storage locus are fixed; the relation vocabulary and build-error policy remain open. | [Relations graph](vendor/gnomon/docs/design/2-architecture/relations-graph), [semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations) |
| Determine common fields and fields for each type. | Partly done. The common abstract base and field typing are fixed; fields for each type remain downstream of ontology and schema field work. | [Common abstract base](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-common-abstract-base), [field-typing discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-field-typing), [reasoning fields](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields), [ontology](vendor/gnomon/docs/design/3-aspect-specific/ontology) |
| Determine namespace, ID, and versioning conventions. | Still open. Criteria exist, but decisions have not been drafted. | [IDs, namespaces, versioning](vendor/gnomon/docs/design/3-aspect-specific/ids-versioning) |
| Determine how to represent and decompose questions. | Partly done. Question-vs-Goal is resolved; question decomposition, scope fields, and use in workflows remain open. | [Question vs. Goal](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-question-vs-goal), [granularity strata](vendor/gnomon/docs/design/2-architecture/granularity#^t2-granularity-strata), [workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows), [scope fields](vendor/gnomon/docs/design/3-aspect-specific/scope-fields) |
| Determine how to encode terminal arguments and derivations. | Partly done. Assemblies relative to a target and annotation loci are fixed; argument internals and reasoning granularity remain open. | [Reasoning structure](vendor/gnomon/docs/design/2-architecture/reasoning-structure), [reasoning-record storage](vendor/gnomon/docs/design/2-architecture/granularity#^t2-reasoning-record-storage), [arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning) |
| Determine module structure and workspace architecture. | Partly done. The structure of the design documents and the architectural layers are fixed; source tree layout for object stores, registries, and views remains open. | [Layering](vendor/gnomon/docs/design/2-architecture/layering), [registries and indexes](vendor/gnomon/docs/design/3-aspect-specific/registries-indexes), [IDs, namespaces, versioning](vendor/gnomon/docs/design/3-aspect-specific/ids-versioning) |
| Determine data formats. | Done. | [source languages, metadata, and grammar](vendor/gnomon/docs/design/2-architecture/data-formats) |
| Determine registries and indexes. | Partly done. Relation storage locus and argument-aware indexes are fixed; registry contents and build products remain open. | [Relation storage locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus), [argument-aware indexes](vendor/gnomon/docs/design/2-architecture/layering#^t2-registries-arguments), [registries and indexes](vendor/gnomon/docs/design/3-aspect-specific/registries-indexes) |
| Clarify the rendering layer strategy. | Partly done. Derived artifacts and view specifications are fixed; rendering manifests, projection types, and view contracts remain open. | [Derived artifacts](vendor/gnomon/docs/design/2-architecture/layering#^t2-derived-artifacts), [view specifications](vendor/gnomon/docs/design/2-architecture/layering#^t2-view-specifications), [rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views) |
| Check whether the model optimizes understanding. | Partly done. Intelligibility and argument-quality criteria exist; the check must run again after argument, workflow, and rendering decisions are drafted. | [Intelligibility](vendor/gnomon/docs/design/1-framework/epistemic-adequacy#^t1-intelligibility), [arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning), [workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows), [rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views) |
| Establish concrete workflows. | Still open. Workflow criteria exist, but decisions have not been drafted. | [Workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows), [scope fields](vendor/gnomon/docs/design/3-aspect-specific/scope-fields) |

## Current TODO

### Tier 2 architectural decisions

- [ ] Settle [layer-feedback policy](vendor/gnomon/docs/design/2-architecture/layering#^t2-layer-feedback).
- [ ] Settle [subtype discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-subtype-discipline).
- [ ] Settle [operation-schema primitiveness](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness).
- [ ] Settle [planning-execution synchronization](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-planning-execution-sync).
- [ ] Settle [reasoning-record storage](vendor/gnomon/docs/design/2-architecture/granularity#^t2-reasoning-record-storage).
- [ ] Settle [granularity strata](vendor/gnomon/docs/design/2-architecture/granularity#^t2-granularity-strata).
- [ ] Settle [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles).
- [ ] Route the build-error policy from [relations graph](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus) into the validator-placement work.

### Tier 3 aspect decisions

- [ ] Draft the canonical object taxonomy in [ontology](vendor/gnomon/docs/design/3-aspect-specific/ontology).
- [ ] Draft the closed relation vocabulary in [semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations).
- [ ] Draft the namespace, identifier, and ontology versioning decisions in [IDs, namespaces, versioning](vendor/gnomon/docs/design/3-aspect-specific/ids-versioning).
- [ ] Draft registry contents, build products, and staging rules in [registries and indexes](vendor/gnomon/docs/design/3-aspect-specific/registries-indexes).
- [ ] Draft rendering manifests, view contracts, and projection types in [rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views).
- [ ] Draft inquiry workflows in [workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows).
- [ ] Draft scope-field decisions in [scope fields](vendor/gnomon/docs/design/3-aspect-specific/scope-fields).
- [ ] Draft argument and derivation internals in [arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning).
- [ ] Settle the explanatory-gain enum, per-cell field selection, and named profile chain in [reasoning fields](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields).
- [ ] Settle assembly-internal warrant kinds and unresolved warrant classifications in [warrant vocabulary](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary).
- [ ] Settle status-transition propagation in [status vocabulary](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary).
- [ ] Settle transmitting relation set and priority combination in [revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).
- [ ] Settle admissibility specifications for each constructor and compound schema naming in [operation schemas](vendor/gnomon/docs/design/3-aspect-specific/operation-schemas).
- [ ] Draft relevance-kind decisions in [relevance vocabulary](vendor/gnomon/docs/design/3-aspect-specific/relevance-vocabulary).

## Dispatch notes

The old TODO raised several decisions that now belong in specific tier files:

- **Object taxonomy** belongs in Tier 3 [ontology](vendor/gnomon/docs/design/3-aspect-specific/ontology), constrained by Tier 2 [object-kind admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission) and [subtype discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-subtype-discipline).
- **Relation vocabulary** belongs in Tier 3 [semantic relations](vendor/gnomon/docs/design/3-aspect-specific/semantic-relations), constrained by Tier 2 [typed relation vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary) and [relation storage locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus).
- **Question decomposition** splits across Tier 2 [granularity strata](vendor/gnomon/docs/design/2-architecture/granularity#^t2-granularity-strata), Tier 3 [workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows), and Tier 3 [scope fields](vendor/gnomon/docs/design/3-aspect-specific/scope-fields).
- **Terminal arguments and derivations** split across Tier 2 [reasoning-record storage](vendor/gnomon/docs/design/2-architecture/granularity#^t2-reasoning-record-storage), Tier 2 [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles), and Tier 3 [arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning).
- **Workspace layout** depends on Tier 3 [IDs, namespaces, versioning](vendor/gnomon/docs/design/3-aspect-specific/ids-versioning), Tier 3 [registries and indexes](vendor/gnomon/docs/design/3-aspect-specific/registries-indexes), and Tier 3 [rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views).
- **Understanding optimization** is not a standalone design object. It is an audit pass over [arguments and reasoning](vendor/gnomon/docs/design/3-aspect-specific/arguments-reasoning), [workflows](vendor/gnomon/docs/design/3-aspect-specific/workflows), and [rendering and views](vendor/gnomon/docs/design/3-aspect-specific/rendering-views) after those decisions exist.

---
