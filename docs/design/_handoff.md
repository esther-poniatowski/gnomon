# Handoff — gnomon design

This is the handoff document for continuing the gnomon design work in a fresh conversation. Read this in full, then load the top-level index: [design index](_index). The next agent should also read the [refactor handoff](_handoff-refactor) and the [cleanup handoff](_handoff-cleanup) before acting on Step A.4 or later refactor steps.

---

## What this project is

`gnomon` is an early design for a knowledge architecture centered on objects. It organizes complex theoretical frameworks: research notes, definitions, arguments, and proofs. The user is building it as the substrate for their PhD research.

The project's goal and the failure modes it addresses are stated in [project overview](../project-overview). The design itself has been settled progressively through structured deliberation. Decisions and open questions now live in three tiers under the design folder. **Treat the tier folders as authoritative**. The inactive proposals have been moved into [backup proposals](_backup); they are informational only and superseded by the tiered state.

---

## How to work with the user

The user is rigorous, fast, and has strong epistemic discipline. Pattern that has worked across many turns:

- **Surface tradeoffs and constraints, do not choose in advance.** When resolving an open question, present the alternatives literally, the criteria that bear on each, the source arbitrations, and the constraints from resolved questions. Let the user choose. Recommend only when explicitly asked.
- **Cite cross-references with anchors.** Use an in-file anchor target when the source lives in the same file, and a repo-root target plus anchor when the source lives elsewhere. The Obsidian block-anchor syntax `^anchor-name` is the convention.
- **Ratify before committing.** When the user proposes a resolution, assess it against resolved-question constraints; flag tensions or downstream implications before applying.
- **Audit substantively, not just on the surface.** After applying a resolution, run a substantive pass: which alternatives are now closed, which subsidiary questions now open, and which downstream resolutions inherit new constraints. Record closures as `[!important]` callouts in the resolved question; record new tensions as `[!missing]` callouts in the affected questions; record obligations to reformulate alternatives as ==TODO: ...== in the affected sections.
- **Apply edits in stages.** Long restructures are broken into multiple tool calls per logical step.
- **No verbatim duplication, no mere reformulation.** Each paragraph must introduce a genuinely new idea. Cross-references replace recalls. This rule is enforced everywhere — callouts, summaries, indexes.
- **Body prose gets priority over headings during style cleanup.** Headings may keep compact technical labels when anchors depend on them. Prose bodies, callouts, bullets, tables, and index descriptions should avoid nominalizations and compound noun stacks.
- **Markdown linter false positives.** MD051 warnings on `#^anchor-name` references are false positives (the linter does not recognize Obsidian block anchors). MD032 warnings on lists are pre-existing throughout the design files. Real warnings (MD012 multiple blank lines, MD060 table formatting) need real fixes.
- **No emojis.** The user has not invited them.
- **Argue principled rejection, not narrative supersession.** When a resolution rejects an option, frame the rejection by the architectural principle that excludes it (Tier-2 constraint, admission-test clause, etc.), not as a chronological "earlier draft was wrong."

---

## File structure

```text
design/
  _index.md                   — top-level index: tier definitions, axes, folder pointers
  _handoff.md                 — this file: the project-level brief
  _handoff-refactor.md        — refactor state, Step A–D plan
  _handoff-cleanup.md         — source-file cleanup brief (Step A.4 of the refactor)
  _framework-criteria.md      — canonical reference for every framework-level (T1) criterion
  _classification-table.md    — migration ledger feeding Step B
  _alias-table.md             — alias clusters across active and backup files
  _migration-table.md         — placeholder, populated by Step B
  _fleeting-ideas.md          — staging area for candidate solutions pending triage
  _worked-examples.md         — concrete expressivity test cases and their resolutions
  _backup/                    — inactive source proposals, superseded by tier files
  1-framework/                — Tier 1 desiderata (per axis); see _index.md
  2-architecture/             — Tier 2 commitments and decisions (per theme); see _index.md
  3-aspect-specific/          — Tier 3 vocabularies and per-aspect decisions; see _index.md
```

The three handoff files form a nested hierarchy: the project-level brief covers the whole project; the refactor handoff covers the Step A–D programme that reorganises the design folder; the cleanup handoff covers Step A.4 — the per-file source-cleanup sub-step.

Within each tier:

- **Tier 1** files are the criteria themselves, grouped by axis (content / epistemic / structural / operational / interface).
- **Tier 2** uses [constraints](2-architecture/constraints) for criteria that cut across themes, and per-theme files for commitments and decisions. Each commitment/decision section opens with a `[!QUESTION]` callout naming the design question it answers.
- **Tier 3** files mix per-theme criteria, commitments, and open questions in a uniform structure.

Anchor convention: `^t1-<short>`, `^t2-<short>`, `^t3-<short>`, all in flat per-tier namespaces with no collisions.

---

## Architectural state in one page

> [!important] Two levels of "object" — do not conflate them
> "Object-oriented" enters this design at two distinct levels. **Level 1**: the framework's *representation language* — it is built out of OOP-inspired epistemic objects (`Claim`, `Definition`, `Proof`, …) with kinds, fields, and a common abstract base. **Level 2**: what the epistemic *content speaks about* — statements and ideas refer to concepts and relations that can themselves be read as objects (a network is a system, a property a property). A commitment, criterion, or candidate lives at exactly one level; applying a level-1 commitment (e.g. `^t2-no-inheritance`) to a level-2 content taxonomy, or vice versa, is a recurring error. The fuller statement, with per-candidate cross-links, is in the [_fleeting-ideas paradigm-catalogue preamble](_fleeting-ideas#^fleeting-paradigm-catalogue).

### Backbone (Tier 2 commitments, all ratified)

Located in [Tier 2 folder](2-architecture). Compactly:

- **Layering** ([Layering and source-of-truth](2-architecture/layering)) — schema/meta vs. instance distinction, canonical layer as source of truth, derived artifacts, view specifications, build vs. mutation, argument-aware indexes.
- **Object kinds** ([Object kinds and their admission](2-architecture/object-kinds)) — admission test, common abstract base (`EpistemicObject`), Question-vs-Goal collapse, per-kind status enums.
- **Relations and graph** ([Relations and the dependency graph](2-architecture/relations-graph)) — closed typed vocabulary, edges authored on objects with derived registry as the single legal read-source.
- **Reasoning structure** ([Reasoning structure: assemblies vs. canonical objects](2-architecture/reasoning-structure)) — assemblies relative to a target, justificatory-level placement, gap-and-gain on the assembly, local records admitted with promotion rule, field requirements that vary by profile.
- **Validity and revision** ([Validity regimes, warrant, and revision](2-architecture/validity-revision)) — per-edge warrant kind, revision and feedback semantics.
- **Validation and views** ([Validation rules and view profiles](2-architecture/validation-views)) — rule/implementation split.
- **Operations and modes** ([Operation schemas and reasoning modes](2-architecture/operations-and-modes)) — operation schemas in meta-schema, dual representation/generation.
- **Source languages and grammar** ([Source languages, metadata, and grammar](2-architecture/data-formats)) — source languages, file metadata fields, declaration tags, rich content blocks, parser rules, and rejected format alternatives.

### Cross-cutting Tier-2 criteria

In [Architectural constraints](2-architecture/constraints). 21 criteria covering structural, epistemic, and operational concerns; four irreducible tensions (X1–X4); five known gaps (G1–G5).

### Tier-1 framework desiderata

In [Tier 1 folder](1-framework). 10 framework-level criteria across five axes, including the two newest external-interface commitments: `^t1-git-delegation` (versioning delegated to git) and `^t1-no-runtime-inference` (no run-time inference engine; defeasibility manifests through author edits).

### Tier-3 aspect-specific work

In [Tier 3 folder](3-aspect-specific). 14 thematic files; some carry real decisions (revision vocabulary, warrant vocabulary, status vocabulary, operation schema constructors, reasoning fields), others are stubs awaiting their aspect work: ontology, arguments and reasoning, semantic relations, registries and indexes, rendering views, IDs and versioning, workflows, relevance vocabulary, and scope fields.

---

## Pending work and how it depends

Three concurrent tracks of pending work coexist. They are not independent: the **refactor track** has a hard ordering, the **architectural-decisions track** runs in parallel under one constraint, and the **idea-triage track** has items that must be resolved before specific refactor steps.

### Track 1 — Refactor (hard sequential ordering)

The refactor reorganises the design folder from a tier-based layout to a theme-based layout. Steps run in strict order; each step's prerequisites must be satisfied before the next begins. The detailed plan is in the [refactor handoff](_handoff-refactor); per-file mechanics for Step A.4 are in the [cleanup handoff](_handoff-cleanup).

- **Step A.1, A.2, A.3** — Complete. The classification table is the migration ledger; `_framework-criteria.md` holds every framework-level criterion under its final theme.
- **Step A.4 — Source-file cleanup.** File 1 done; files 2–11 pending. Removes duplicated bodies from source files whose content was migrated to `_framework-criteria.md`. Per-file user-approval discipline applies.
- **Step B — Migration table.** Mechanical extraction from the classification table, one row per *Final state* bullet. Becomes the redirect source-of-truth for Step C.
- **Step C — Migrate and convert** in batches `Ir → If/Id → R → G → F → A → D → P`. Each batch followed by a cross-reference sweep.
- **Step D — Theme reorganisation.** Retires the `1-framework/`, `2-architecture/`, `3-aspect-specific/` split.

### Track 2 — Open architectural decisions (parallel, with one constraint)

These Tier-2 decisions are independent of the refactor and can be resolved at any time. The one constraint: any decision that changes a heading or anchor referenced by the classification table requires updating that table before Step B runs.

- **[Layer-feedback policy](2-architecture/layering#^t2-layer-feedback)** — strict one-way is closed by argument-aware indexes; surviving alternatives are revision-edge feedback or mixed bidirectional.
- **[Subtype discipline](2-architecture/object-kinds#^t2-subtype-discipline)** — tagged unions, schema refinement, or hybrid (OOP inheritance ruled out).
- **[Operation-schema primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness)** — definitional fiat, proof that schemas terminate, schema calculus, or open library. Tension X1 favors deriving schemas from a small calculus.
- **[Planning-execution synchronization](2-architecture/operations-and-modes#^t2-planning-execution-sync)** — implicit, explicit two-graph, `StateDelta`, or single bidirectional reasoning graph.
- **[Reasoning-record storage](2-architecture/granularity#^t2-reasoning-record-storage)** — three surviving alternatives (the canonical-annotations alternative is closed by [locus of justificatory annotations](2-architecture/reasoning-structure#^t2-reasoning-annotation-attachment)).
- **[Granularity strata](2-architecture/granularity#^t2-granularity-strata)** — three / four / two strata or mixed.
- **[Partial-formalization profiles](2-architecture/granularity#^t2-partial-formalization-profiles)** — profile vocabulary and per-profile mandatory partitions.

Pending Tier-3 decisions: see each thematic file's "Open questions" section. Most Tier-3 stubs depend on a Tier-2 decision that bounds them.

### Track 3 — Idea triage (gating items in Track 1)

Two staging documents collected work during the project pause:

- **Three TODOs in [_framework-criteria.md](_framework-criteria)** — local edits to specific criteria. They are upstream of Step A.4:
  1. **[Inquiry content and progression](_framework-criteria#^t1-inquiry-content-and-progression)** — commit explicitly to the static/dynamic split as state + state-transforming process toward well-defined goals (the "strategic game" framing).
  2. **[Reasoning understandability](_framework-criteria#^t1-reasoning-understandability)** — reorganise the *Reasoning integrity* theme: place understandability first and position the sibling criteria under one of its three levels (Licensing / Strategic / Explanatory). Specifically, *Goal-driven reasoning* sits under Strategic; *Cognitive manipulability* sits under Explanatory.
  3. **[Activity separation](_framework-criteria#^t1-activity-separation)** — soften the criterion. Activities legitimately interact (revision edits content). Replace "distinct loci" with per-activity read/write rights. Clarify the content-vs-exposition distinction by saying exposition *derives from* canonical content rather than asserting new claims.

- **Fleeting ideas in [_fleeting-ideas.md](_fleeting-ideas)** — staging notes that need to be moved to the right destination:
  - **Concept-type taxonomy** (system / subtype / property / process). Candidate feeder for the Tier-3 [ontology](3-aspect-specific/ontology) decision. Independent of the refactor; resolve when the ontology stub is filled.
  - **Question-as-epistemic-gap hypothesis** with a five-type taxonomy (paradox, missing mechanism, incomplete characterisation, case mapping, comparison). Architecturally loaded: it touches the Tier-2 ratified [Question-vs-Goal collapse](2-architecture/object-kinds) and the Tier-1 [Goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning) criterion. May require reopening one ratified decision. Should be triaged before resolving TODO 2 above (the reorganisation of *Reasoning integrity*).

---

## Recommended order to resume

```text
   Track 3 (idea triage)             Track 1 (refactor)              Track 2 (open T2 decisions)
   ─────────────────────             ──────────────────              ────────────────────────────
   1. Triage fleeting ideas
      (gap taxonomy → may reopen
       Question-Goal collapse)
            │
            ▼
   2. Resolve the 3 TODOs in
      _framework-criteria.md
            │
            └──────────────────────► 3. Step A.4 (files 2–11)
                                          │
                                          ▼
                                     4. Step B (migration table)
                                          │
                                          ▼
                                     5. Step C (migrate in batches)        Open T2 decisions
                                          │                                run any time;
                                          ▼                                must not edit
                                     6. Step D (theme reorg)               classification-table
                                                                           targets after Step B
```

**Step 1 — Triage [_fleeting-ideas.md](_fleeting-ideas).** For each idea, decide: does it feed an existing TODO, a Tier-2 open decision, a Tier-3 stub, or none? The gap-taxonomy hypothesis is the most architecturally loaded and may reopen the Question-vs-Goal collapse; resolve it first if it does.

**Step 2 — Resolve the three TODOs in `_framework-criteria.md`.** The third (Activity separation) is the most consequential — it changes a criterion's scope and downstream consequences. Worth pausing on before applying.

**Step 3 — Resume Step A.4** (source-file cleanup, files 2–11) under the per-file user-approval discipline in the [cleanup handoff](_handoff-cleanup).

**Step 4 — Run Step B**. Mechanical extraction.

**Step 5 — Run Step C** in the prescribed batch order.

**Step 6 — Run Step D** (theme reorganisation).

**In parallel (Track 2)**: any open Tier-2 architectural decision can be resolved at any point, provided that no resolution edits a heading or anchor that the classification table records as a Step-B migration target.

---

## Discipline checklist for future resolutions

When resolving an open question, the agent should:

1. **Read the current state** of the relevant Tier-2 file (alternatives, bearing criteria, subsidiary questions).
2. **Surface constraints** from already-resolved questions and from the Tier-2 cross-cutting criteria in [Architectural constraints](2-architecture/constraints).
3. **List alternatives that remain meaningful** under those constraints. Prune alternatives excluded by prior resolutions.
4. **Ask the user to choose**, providing rationale for each surviving alternative.
5. **Apply the resolution.** Each ratified decision is recorded under the section's `[!QUESTION]` callout, with the chosen design stated directly.
6. **Trim deliberation history** that does not survive the resolution.
7. **Update cross-references** if the resolution invalidates anchors used elsewhere.
8. **Run a substantive consistency audit.** Identify closed alternatives, opened subsidiary questions, downstream constraints. Record closures as `[!important]` callouts; new tensions as `[!missing]` callouts; reformulation obligations as ==TODO== in the affected sections.
9. **Verify no dead references** remain after the edit.

---

## What is *not* in scope for the next sessions

Downstream of the architecture, intentionally not yet addressed:

- The exact relation vocabulary (deferred to [the project TODO](../TODO); partly drafted in [Semantic relations](3-aspect-specific/semantic-relations) as criteria only).
- The exact object taxonomy (deferred to [the project TODO](../TODO); criteria in [Ontology of object kinds](3-aspect-specific/ontology)).
- The rendering layer strategy (deferred to [the project TODO](../TODO); criteria in [Rendering and views](3-aspect-specific/rendering-views)).
- Specific tooling implementations (commands, build scripts).
- The schema validation language itself (JSON Schema vs. custom DSL vs. another validator language). Source languages, file metadata, and block grammar are settled in [source languages, metadata, and grammar](2-architecture/data-formats).
- The inactive source proposals in [backup proposals](_backup), except as historical evidence when an active tier file explicitly points there.

Stay at the architectural construction level. If a question forces specifying any of these, surface that as a deferral to a downstream decision rather than committing prematurely.

---

## File locations

- Top-level index: [design index](_index).
- Refactor handoff: [_handoff-refactor](_handoff-refactor).
- Cleanup handoff (Step A.4): [_handoff-cleanup](_handoff-cleanup).
- Framework-level criteria: [_framework-criteria](_framework-criteria).
- Candidate-solutions staging area: [_fleeting-ideas](_fleeting-ideas).
- Worked expressivity examples: [_worked-examples](_worked-examples).
- Classification table: [_classification-table](_classification-table).
- Alias table: [_alias-table](_alias-table).
- Migration table (Step B target): [_migration-table](_migration-table).
- Tier 1: [Tier 1 index](1-framework/_index).
- Tier 2: [Tier 2 index](2-architecture/_index).
- Tier 3: [Tier 3 index](3-aspect-specific/_index).
- Problem statement: [project-overview](../project-overview).
- Project TODO: [Advancing the design of gnomon](../TODO).
- Source proposals (informational only, superseded): [layered model](_backup/architecture-1-layered-model), [architecture C](_backup/architecture-C), [architecture 2 spec](_backup/architecture-2-spec), [architecture 2 audit](_backup/architecture-2-audit).
