# Tier 2 — Architectural commitments and decisions

Tier-2 files fix the structural decisions that compose the architecture: how layers relate, what objects are admitted, how relations are typed and queried, how reasoning is structured, how validity and revision interact, how validation is organized, and how operations and granularity are stratified.

## Structure

Each thematic file follows the same structure:

1. **Header** — the theme's scope and the criteria that bear on its decisions.
2. **Criteria** (where the theme has theme-local well-formedness requirements) — Tier-2 criteria binding only that theme, each linked to its upstream framework-level criterion.
3. **Decisions** — ratified architectural commitments, each opened by a `[!QUESTION]` callout that names the design question the decision answers.
4. **Open questions** — pending decisions, each opened by a `[!QUESTION]` callout with the alternatives.

Tier-2 criteria are theme-local: each lives in the `## Criteria` section of the theme it binds (for example, [object-kind set smallness](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-ontology-small) in object-kinds, [layer replaceability](vendor/gnomon/docs/design/2-architecture/layering#^t2-layering-replaceability) in layering). The one exception is the meta-schema rule [field-typing discipline](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-field-typing), which binds every field-declaring theme; it is hosted in object-kinds as the primary field-declaring surface and referenced cross-file.

## Files

- [Known gaps](vendor/gnomon/docs/design/2-architecture/_gaps) — registry of un-operationalized architectural gaps, each naming the criterion it leaves unmet and the decision that addresses it.
- [Layering and source-of-truth](vendor/gnomon/docs/design/2-architecture/layering) — criterion: layer replaceability. Decisions: meta vs. instance, canonical layer as source of truth, derived artifacts, view specifications, build vs. mutation, argument-aware indexes; open question on layer-feedback policy.
- [Object kinds and their admission](vendor/gnomon/docs/design/2-architecture/object-kinds) — criteria: object-kind set smallness, role purity, subtype safety, field-typing discipline. Decisions: object-kind admission test, common abstract base, Question-vs-Goal, epistemic status; open question on subtype discipline.
- [Relations and the dependency graph](vendor/gnomon/docs/design/2-architecture/relations-graph) — typed relation vocabulary, relation storage locus and authoring-vs-querying asymmetry, relational graph representation; open questions on relation reification and dependency-graph layering.
- [Reasoning structure: assemblies vs. canonical objects](vendor/gnomon/docs/design/2-architecture/reasoning-structure) — assemblies relative to a target, where reasoning notes attach, gap and gain, records local to a target, and the field regime for reasoning notes.
- [Validity regimes, warrant, and revision](vendor/gnomon/docs/design/2-architecture/validity-revision) — warrant kind on edges, revision and feedback semantics (kinds, recording, archival, dependent flagging, propagation).
- [Validation rules and view profiles](vendor/gnomon/docs/design/2-architecture/validation-views) — validator placement (rules vs. implementations), view-profile placement, validation-mechanism scope.
- [Operation schemas and reasoning modes](vendor/gnomon/docs/design/2-architecture/operations-and-modes) — where operation schemas live, the representation/generation distinction, and open questions on primitiveness and planning/execution synchronization.
- [Granularity and partial formalization](vendor/gnomon/docs/design/2-architecture/granularity) — open questions on reasoning-record storage, granularity strata, partial-formalization profiles.
- [Source languages, metadata, and grammar](vendor/gnomon/docs/design/2-architecture/data-formats) — source languages, file metadata fields, declaration tags, rich content blocks, parser rules, and rejected format alternatives.
