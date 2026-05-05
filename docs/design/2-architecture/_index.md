# Tier 2 — Architectural commitments and decisions

Tier-2 files fix the structural decisions that compose the architecture: how layers relate, what objects are admitted, how relations are typed and queried, how reasoning is structured, how validity and revision interact, how validation is organized, and how operations and granularity are stratified.

## Structure

Each thematic file follows the same structure:

1. **Header** — the theme's scope and the cross-cutting Tier-2 criteria from [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints) that bear on its decisions.
2. **Decisions** — ratified architectural commitments, each opened by a `[!QUESTION]` callout that names the design question the decision answers.
3. **Open questions** — pending decisions, each opened by a `[!QUESTION]` callout with the alternatives.

Criteria that cut across themes live separately in [constraints](vendor/gnomon/docs/design/2-architecture/constraints); they constrain decisions across multiple themes.

## Files

- [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints) — cross-cutting Tier-2 criteria (structural, epistemic, operational), four irreducible tensions, and known gaps.
- [Layering and source-of-truth](vendor/gnomon/docs/design/2-architecture/layering) — meta vs. instance, canonical layer as source of truth, derived artifacts, view specifications, build vs. mutation, argument-aware indexes; open question on layer-feedback.
- [Object kinds and their admission](vendor/gnomon/docs/design/2-architecture/object-kinds) — object-kind admission test, common abstract base, Question-vs-Goal, epistemic status; open question on subtype discipline.
- [Relations and the dependency graph](vendor/gnomon/docs/design/2-architecture/relations-graph) — typed relation vocabulary, relation storage locus and authoring-vs-querying asymmetry.
- [Reasoning structure: assemblies vs. canonical objects](vendor/gnomon/docs/design/2-architecture/reasoning-structure) — assemblies relative to a target, where reasoning notes attach, gap and gain, records local to a target, and the field regime for reasoning notes.
- [Validity regimes, warrant, and revision](vendor/gnomon/docs/design/2-architecture/validity-revision) — warrant kind on edges, revision and feedback semantics (kinds, recording, archival, dependent flagging, propagation).
- [Validation rules and view profiles](vendor/gnomon/docs/design/2-architecture/validation-views) — validator placement (rules vs. implementations), view-profile placement, validation-mechanism scope.
- [Operation schemas and reasoning modes](vendor/gnomon/docs/design/2-architecture/operations-and-modes) — where operation schemas live, the representation/generation distinction, and open questions on primitiveness and planning/execution synchronization.
- [Granularity and partial formalization](vendor/gnomon/docs/design/2-architecture/granularity) — open questions on reasoning-record storage, granularity strata, partial-formalization profiles.
- [Source languages, metadata, and grammar](vendor/gnomon/docs/design/2-architecture/data-formats) — source languages, file metadata fields, declaration tags, rich content blocks, parser rules, and rejected format alternatives.
