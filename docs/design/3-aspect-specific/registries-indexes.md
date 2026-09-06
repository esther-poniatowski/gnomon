---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Registries and indexes
---
# Registries and indexes

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria for the derived registries and indexes the build produces. Traces to [relational graph representation](../2-architecture/relations-graph.md#^t2-relational-graph-representation), [single source of truth](../1-framework/research-activities-workflows.md#^t1-single-source-of-truth), [t1-dual-usability](../1-framework/cost-ergonomics.md#^t1-read-side-automation), and the read-locus rule fixed at [relation storage locus](../2-architecture/relations-graph.md#^t2-relation-storage-locus).

---

## Criteria

### Dependency graph as first-class derived structure ^t3-dependency-graph-first-class

The dependency graph is a first-class derived structure, not a property derivable on demand from object fields. The build emits it as an addressable artifact.

### Registry updates by re-derivation ^t3-registry-updates

Registry updates are written directly, with no staging area and no promotion-on-review step. Integrity of the read model is guaranteed not by gating the write but by **re-deriving the registry automatically from the canonical source on every build**: the registry is a derived structure, so a divergence between it and the canonical source is a build error, surfaced as a diagnostic rather than corrected by mutation. A staging-area-plus-human-review workflow would presuppose a hand-edited persistent registry, which [single source of truth](../1-framework/research-activities-workflows.md#^t1-single-source-of-truth) excludes.

### Orphan detection via reachability ^t3-orphan-detection

Orphans (objects unreachable from any inquiry root) are detectable by reachability analysis on the registry. The build emits a diagnostic, not a deletion.

---

## Decisions

### Typed references ^t3-typed-references

> [!QUESTION] How does an object record what it imports from other objects and what it exposes for import?

An object records its cross-object dependencies as **typed references** rather than bare identifiers, so that the registry distinguishes what exactly is imported from a source.

- **Typed imports.** Each import specifies the kind of object imported, the source object's ID (resolved through the source object's namespace), and optionally its exact use in the local context.
- **Typed outputs.** Each exportable output specifies an ID anchor in the local context.

**Rationale — fine-grained imports.** An object may not depend on another object as a whole; it may consume a specific internal attribute — a definition, a theorem, a construction. Coarse dependencies are one of the main causes of accidental overlap and hidden rederivations. The schema requires this typed form per [schema-specification meta-rule](../2-architecture/object-kinds.md#^t2-schema-specification); this decision fixes the format that realises it.

The import and output kinds are not a fixed global enum: the admissible types are whatever the object ontology offers, and each schema declares the import and output types appropriate to the function of the object it specifies. Validation checks an instance against its schema, not against a frozen enum.

Implementation:

- `imports`: array of typed imports, each with `kind` (the imported object's kind), `from` (source object ID), `target` (anchor within the source), and optionally `used_for` (role in the local context).
- `outputs`: array of typed outputs, each with `id` (anchor in the local context) and `type` (the output's kind).

### Registry-component taxonomy ^t3-registry-component-taxonomy

> [!QUESTION] What set of registries and indexes does the build derive, and what does each one answer?

The build derives a closed set of registry and index components. Each component answers a distinct query class over the canonical objects; several reuse a structure or vocabulary already fixed by another decision.

Three query classes partition the components:

| Class | Query | Example |
| --- | --- | --- |
| **Registries** | Lookup — given an ID, retrieve the object. | Given `DEF-014`, retrieve the object. |
| **Graph structures** | Relational — find objects on a path between two given objects. | Find all objects on a justificatory path from `ASM-003` to `ANS-002`. |
| **Analytic indexes** | Computed organizational — rank or group objects by a derived property. | Rank objects by load-bearing centrality for target `Q-001`. |

The components fall into the three classes as follows:

| Class | Component | Role | Home |
| --- | --- | --- | --- |
| **Registry** | **Identity registry** | Maps IDs to canonical objects. | The identifier discipline is fixed at [stable persistent identifiers](ids-versioning.md#^t3-stable-identifiers). |
| **Registry** | **Namespace registry** | Organizes objects by module, branch, or research thread. | Sub-decision of this taxonomy — not separately anchored. |
| **Registry** | **Terminology index** | Tracks canonical terms, notations, and aliases. | The capability is [canonical terminology](../1-framework/modular-content-organization.md#^t1-canonical-terminology); the linter realisation is deferred to the validation work. |
| **Registry** | **Relation registry** | Collects typed edges between object IDs. | The edge vocabulary is fixed at [typed relation vocabulary](../2-architecture/relations-graph.md#^t2-typed-relation-vocabulary). |
| **Graph structure** | **Dependency graph** | Directed graph for *justificatory* and *semantic* dependence respectively. | The capability is [relational queryability](../1-framework/modular-content-organization.md#^t1-relational-queryability); the data structure is [relational graph representation](../2-architecture/relations-graph.md#^t2-relational-graph-representation); its first-class derived status is [dependency graph as first-class derived structure](#^t3-dependency-graph-first-class). Its maintenance policy is the open question [dependency-graph artifact maintenance](#^t3-dependency-graph-artifact). |
| **Analytic index** | **Type index** | Groups objects by kind and subtype. | Sub-decision of this taxonomy — not separately anchored. |
| **Analytic index** | **Status index** | Groups objects by epistemic maturity. | The status grain is the open question [per-kind status enums](status-vocabulary.md#^t3-per-kind-status-enums). |
| **Analytic index** | **Reverse dependency index** | Tracks downstream impact of each object. | Sub-decision of this taxonomy — not separately anchored. |
| **Analytic index** | **Relevance index** | For each target question, ranks relevant objects and their roles. | Sub-decision of this taxonomy — not separately anchored. |
| **Analytic index** | **Integrity report structures** | Record missing links, broken references, cycles, and orphan nodes. | Sub-decision of this taxonomy; orphan detection is fixed at [orphan detection via reachability](#^t3-orphan-detection). |
| **Analytic index** | **Open-questions index** | Surfaces which `Question` / `Goal` objects to take up next, ordered by readiness and priority. | Schema fixed at [open-questions index schema](#^t3-open-questions-index). |

==TODO: These can be viewed as *projections* of the canonical source, in the database sense: each answers a distinct query class over the canonical objects.==

The version-graph component proposed in the source inventory is dropped: a version-history registry conflicts with [no version history](../1-framework/framework-foundations.md#^t1-no-version-history), which fixes version history as outside framework scope.

The five sub-decision components — type index, namespace registry, reverse dependency index, relevance index, and the integrity report structures beyond orphan detection — are not separately anchored. Each is settled within this taxonomy when the registries-and-indexes work fixes its schema.

### Open-questions index schema ^t3-open-questions-index

> [!QUESTION] What schema does the open-questions index carry, and which fields are derived from existing objects rather than stored locally?

The open-questions index is a derived view over the `Question` / `Goal` object kind (per [question vs. goal](../2-architecture/object-kinds.md#^t2-question-vs-goal)) that surfaces which inquiry to take up next, rather than relying on unaided intuition. The index entry per `Question` / `Goal` object carries the following fields:

- `id` — the object's stable identifier (per [stable persistent identifiers](ids-versioning.md#^t3-stable-identifiers)).
- `question` — the object's content statement.
- `status` — the object's maturity, governed by [per-kind status enums](status-vocabulary.md#^t3-per-kind-status-enums); for a `Question`, the candidate enum is `open` | `refined` | `answered` | `abandoned`.
- `prerequisite_objects` — derived from the object's outbound `depends_on` edges (per [relation storage locus](../2-architecture/relations-graph.md#^t2-relation-storage-locus)) and the dependency graph; not stored locally.
- `priority` — `high` | `medium` | `low`. Registry-local field; not derivable from object fields.
- `blocking_reason` — prose explaining why the inquiry cannot yet be taken up; registry-local.

The status, identifier, content, and prerequisite fields restate existing object fields and dependency-graph edges. The two registry-local fields are `priority` and `blocking_reason`. The index is re-derived from the canonical source on every build (per [registry updates by re-derivation](#^t3-registry-updates)); the registry-local fields are written into the index entries directly, since they have no upstream canonical source.

### Terminology-index schema ^t3-terminology-index-schema

> [!QUESTION] What schema does the terminology index carry, and what does each entry license the linter to enforce?

The terminology index realises [canonical terminology](../1-framework/modular-content-organization.md#^t1-canonical-terminology) at the schema grain: it lists each canonical term and the variant forms the linter must flag. Per entry:

- `canonical_name` — the authorised term.
- `forbidden_variants` — an array of strings the linter flags in the prose content of objects, with the canonical name as the proposed replacement.

The index is re-derived from the canonical source on every build (per [registry updates by re-derivation](#^t3-registry-updates)); the linter mechanism that consumes it is the validation-work decision deferred at the Terminology-index row of [registry-component taxonomy](#^t3-registry-component-taxonomy).

---

## Open questions

### Dependency-graph artifact maintenance ^t3-dependency-graph-artifact

> [!QUESTION] What is the maintenance policy of the derived dependency-graph artifact?

The dependency graph is a first-class derived structure (per [dependency graph as first-class derived structure](#^t3-dependency-graph-first-class)); the *existence* of the graph is committed by [relational queryability](../1-framework/modular-content-organization.md#^t1-relational-queryability) and [relational graph representation](../2-architecture/relations-graph.md#^t2-relational-graph-representation). This question concerns only how the artifact is kept current. Candidate policies:

- **Regenerated on every build** from the object-authored edges — no persistent storage beyond the build output; the default per [registry updates by re-derivation](#^t3-registry-updates).
- **Stored as a build artifact** in a registry slot, regenerated when canonical sources change.
- **Cached with explicit invalidation** triggered by canonical-source writes.
- **On-demand computation** with no persistence.

Resolution must pick a policy and hold it against [registry updates by re-derivation](#^t3-registry-updates), which already excludes a hand-edited persistent registry.

### Registry scope per vault scale ^t3-registry-scope-per-scale

> [!QUESTION] At which vault scale does each registry live, and what does each scale hold?

A registry need not be reproduced identically at every vault scale. A candidate stratification splits the content by level:

- **Workspace level** holds only the project catalogue and any global terminology shared across projects.
- **Project level** holds the authoritative reasoning architecture for the project — the canonical registries and the dependency graph.
- **Module level** holds a local index note only, not a copy of the project graph.

Duplicating the full registry at every scale would create several structures that drift apart, against [single source of truth](../1-framework/research-activities-workflows.md#^t1-single-source-of-truth). Resolution must fix which registries exist at each scale, state whether a narrower scale holds a strict subset (workspace catalogue) or a derived local view (module index), and confirm that the project level is the single authoritative locus.

### Registry serialization format ^t3-registry-serialization-format

> [!QUESTION] In what data format does the build serialize the derived registries and indexes?

The registries and indexes are derived structures the build re-emits from the canonical source on every run (per [registry updates by re-derivation](#^t3-registry-updates)). Their serialization format is independent of the source-file format fixed at [source languages](../2-architecture/data-formats.md#^t2-source-languages): a build may export its results in a format unlike the files it consumes. Candidate formats — YAML, JSON, CSV, or a database file (`.sqlite`, `.db`) — differ in query-ability, diff stability under version control, and the tooling each demands of a human supervisor, a program, and an AI agent that all read the registry.

Resolution must pick the format (or per-registry formats) and state how the choice serves the tri-consumer access fixed at [read-side automation](../1-framework/cost-ergonomics.md#^t1-read-side-automation), weighing query-ability against file-level diff stability.
