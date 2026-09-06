---
tags:
  - architecture
index: "[Architectural commitments](_index.md)"
aliases:
  - Reasoning structure
---
# Reasoning structure: assemblies vs. canonical objects

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions that govern reasoning relative to a target: how assemblies relate to canonical objects, where reasoning notes attach, and which records may live inside an assembly.
>
> Theme-local criteria bearing on this file: [object-kind set smallness](object-kinds.md#^t2-ontology-small). The meta-schema rule [field-typing discipline](object-kinds.md#^t2-field-typing) binds the reasoning-note fields declared here. Framework-level criteria bearing on this theme: [non-redundancy](../1-framework/modular-content-organization.md#^t1-non-redundancy); [justification levels](../1-framework/reasoning-integrity.md#^t1-justification-levels) — the five-level desideratum, whose intrinsic-vs-inquiry-dependent split and annotation-richness requirement are realised by [t2-reasoning-annotation-attachment](#^t2-reasoning-annotation-attachment) — and [reasoning-types coverage](../1-framework/expressive-depth.md#^t1-reasoning-types-coverage), the multi-regime requirement.

---

## Decisions

### Assemblies relative to a target ^t2-target-relative-assemblies

> [!QUESTION] How does the architecture represent an argument, reasoning episode, or minimal answer to a target question?

An assembly **selects and relates** canonical objects relative to a target. It may also carry records that belong only to the target: local motives, rejected alternatives, work metadata, applied operations, and state deltas. The allowed contents and the migration rule are fixed by [t2-assembly-record-promotion](#^t2-assembly-record-promotion). When reasoning introduces an object with independent identity, downstream reuse, or intrinsic validity conditions, that object moves to the canonical layer.

**Canonical object vs. assembly.** Both are persistent records in the source layer with their own identifiers and typed relations. They differ by which clauses of [t2-object-kind-admission](object-kinds.md#^t2-object-kind-admission) they satisfy:

- A **canonical object** satisfies the admission test in full.
- An **assembly** is a *structured citation*: it selects a target (a question, a goal, a thesis) and arranges canonical objects into a chain that bears on that target. The admission test fails on at least three clauses by construction:
	- **The assembly is the context.** Elsewhere it is cited as "the argument the author of inquiry I gave for target T"; its identity depends on `(I, T)`.
	- **Local validity depends on the target.** The same chain of canonical objects may fit one target but fail another; a lemma may serve as a *premise* in one assembly and a *conclusion* in another.
	- **Reuse does not erase context.** Two inquiries that cite the same canonical objects toward different targets create two assemblies, not one assembly cited twice.

An assembly is a record-with-identity that lives in a parallel store from canonical objects, governed by different admission rules.

### Locus of justificatory annotations ^t2-reasoning-annotation-attachment

> [!QUESTION] Which locus — canonical object or assembly — hosts each of the three justificatory levels?

The justificatory-level placement rule forbids loci that conflate the levels. Two loci suffice to honor that constraint, because licensing is intrinsic to the move while strategic and explanatory support depend on the inquiry that recruits the move:

| Justificatory level | Locus | Example fields |
| --- | --- | --- |
| **Licensing / inferential support** | Canonical object | content, status (per [t2-epistemic-status](object-kinds.md#^t2-epistemic-status)), applied operation schema, warrant kind on its support relations (per [t2-warrant-annotation](validity-revision.md#^t2-warrant-annotation)), preconditions |
| **Strategic / motivational support** | Assembly, at the moment the object is introduced into the inquiry | deficiency addressed (the *gap*), parent question advanced, route chosen, alternatives rejected, strategic role of the citation |
| **Explanatory / support for epistemic gain** | Assembly, after the object has contributed to the inquiry | the cognitive *gain* the contribution yielded: what became intelligible, why the inquiry now understands more |

**Canonical objects host no inquiry-dependent fields.** A canonical object carries no `motivation`, no `contribution`, and no aggregate of strategic or explanatory records. The same object participates in many inquiries, each with its own gap and its own gain; an intrinsic field would force a single inquiry's annotation to stand for all of them. "Which assemblies cite this object, with which gap and which gain" is answerable as a registry query over the typed relation graph (per [t2-relation-storage-locus](relations-graph.md#^t2-relation-storage-locus)) — derived, not canonical.

> [!important] Discarded alternative: storage-site loci
> Classifying notes by storage site (on a node, on an edge, or on an assembly) appears to give a third locus for warrant kind. That third locus is illusory: under [t2-relation-storage-locus](relations-graph.md#^t2-relation-storage-locus), the source object authors each edge, so a note "on the edge" is a field on the source object that describes a relation. The justificatory level determines where the note belongs; storage follows from that level, not the reverse.

### Promotion of assembly-local records ^t2-assembly-record-promotion

> [!QUESTION] An assembly carries records whose meaning depends on the inquiry. When does such a record cross over and become a canonical object, and who triggers the migration?

**Admissible assembly content.** An assembly authors three kinds of content:

- citations of canonical objects with typed relations and warrant kind on support edges (per [t2-warrant-annotation](validity-revision.md#^t2-warrant-annotation));
- the strategic and explanatory notes placed on the assembly by [t2-reasoning-annotation-attachment](#^t2-reasoning-annotation-attachment);
- substantive records whose meaning depends on the inquiry: work metadata, applied operations, state deltas, internal lemmas, named rejected routes, and support edges between endpoints that are not canonical.

**Promotion rule.** An assembly-local record is promoted to the canonical store when it satisfies [t2-object-kind-admission](object-kinds.md#^t2-object-kind-admission). The trigger is a property of the record, not of the inquiring author's intent.

**Promotability by kind.** The schema declares, for each kind of assembly-local record, whether it can be promoted:

- strategic and explanatory notes depend on the inquiry and are never promotable;
- internal lemmas, named rejected routes, and support endpoints inside an assembly can be promoted when the admission test holds;
- work metadata, records of applied operations, and state deltas describe the inquiry's process, not its content; they remain local and are never promotable.

**Build flags, author executes.** Promotion is a mutating action governed by [t2-build-vs-mutation](layering.md#^t2-build-vs-mutation). The build detects promotion candidates and emits diagnostics; the author performs the promotion (manually or via a maintenance command), which extracts the record into the canonical store with a new ID and rewrites the originating assembly to cite it.

**ID stability under promotion.** A promoted record receives a canonical ID at promotion time. Git history records the migration; no separate provenance index is required. Promotion is a *first* canonical entry, not a relocation of an existing canonical object.

> [!missing] Open subsidiary questions
> - **When promotion triggers.** The predicates in the admission test are stated at the criterion level in [t2-object-kind-admission](object-kinds.md#^t2-object-kind-admission). How the validator checks those predicates is deferred to [t2-validator-placement](validation-views.md#^t2-validator-placement).
> - **Citation rewrite on promotion.** Whether the rewrite of the originating assembly is performed by the maintenance command or by the author is unsettled.

### Fields for reasoning notes ^t2-reasoning-annotation-fields

> [!QUESTION] At each locus × content kind fixed by [t2-reasoning-annotation-attachment](#^t2-reasoning-annotation-attachment) and [t2-assembly-record-promotion](#^t2-assembly-record-promotion), which fields are mandatory, optional, or required only at stronger formalization profiles?

**Fields vary by profile.** Each locus × content kind has a mandatory spine and a structured optional layer. The formalization profile determines which optional fields become mandatory (per [t2-partial-formalization-profiles](granularity.md#^t2-partial-formalization-profiles)). The spine is mandatory at every profile; optional fields become mandatory at higher profiles.

The choice follows the pattern that [t1-partial-formalization](../1-framework/expressive-depth.md#^t1-partial-formalization) prescribes for tension [X2](../1-framework/_tensions.md#^t2-x2): each profile partitions fields into mandatory and optional sets, with named guarantees that weaken when the profile loosens. The minimal-spine regime leaves no surface to grade; the regime that structures only canonical records demotes the strategic and explanatory levels that the [locus of justificatory annotations](#^t2-reasoning-annotation-attachment) made first class.

**Architectural commitment only.** The actual field set for each cell, the field types, the `gain_kind` enum, and the named profiles are deferred to [fields for reasoning notes](../3-aspect-specific/reasoning-fields.md) and to [t2-partial-formalization-profiles](granularity.md#^t2-partial-formalization-profiles).
