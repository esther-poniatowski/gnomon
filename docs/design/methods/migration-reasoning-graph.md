
# Migration towards a Reasoning Graph

## Objective

Transform the existing vault into the new architecture **progressively**, while preserving useful mathematical content and restoring global coherence. 

The migration must proceed as a **controlled refactoring of a reasoning system**. Begin by reconstructing the architecture that makes it possible to decide which notes should be preserved, split, merged, demoted, or rewritten.

## Global migration strategy

The migration should proceed in five phases:

1. **freeze the target architecture**
2. **inventory and diagnose the current vault**
3. **reconstruct the reasoning graph from the existing notes**
4. **triage notes into migration actions**
5. **migrate incrementally along priority fronts**

> [!WARNING] 
> Do not launch a mass editorial cleanup.
> Do not begin by rewriting notes. If rewriting begins before the graph and triage exist, the old incoherence will simply be reproduced in a new format.

### Phase 1: freeze the target architecture

Before touching the old notes, the new operating system of the vault must be stabilized.

The files described in the [workspace architecture](workspace-architecture.md) — the `governance/` files (rules, specs, contracts, audits, schemas, workflow), the `registries/` files, and `AGENTS.md` — should already exist in at least a first usable version. Perfection is not required; stability is.

The goal is to ensure that every migration decision will be made against a fixed reference system.

---

# III. Phase 2: inventory and diagnose the current vault

## 1. Create a migration registry

A dedicated registry (`registry/migration_index.yaml`) should enumerate all existing notes and track their migration status. Each entry contains: `legacy_id`, `path`, `provisional_title`, `status` (initially `unreviewed`), `note_type_guess`, four diagnostic scores (`atomicity`, `rigor_level`, `relevance_to_project`, `redundancy_level`), `action` (the migration action to apply), `target_note_id` (one or more target notes), and `comments`. This file becomes the control surface of the migration.

---

## 2. Separate diagnosis from rewriting

The first pass over the old notes should be **diagnostic only**.  
No rewriting, no cleanup, no style correction.

For each note, the purpose is to determine:

- what question it is trying to answer
    
- whether that question is atomic
    
- whether the content is mathematically valuable
    
- whether the note has a unique inferential role
    
- whether it overlaps with other notes
    
- whether it should survive in the new architecture
    

At this stage, the important output is not improved prose. It is **classification**.

---

## 3. Add a legacy review specification

A legacy review specification (`governance/specs/legacy_review.md`) standardizes the diagnostic pass. Each review contains the following sections:

- **Note identification**: path and provisional title.
- **Intended question**: what question the note appears to address.
- **Actual content**: what the note really does (which may differ from the intended question).
- **Four diagnostic scores**, each rated on a fixed scale:
  - Atomicity: `atomic` / `mixed` / `diffuse`
  - Mathematical value: `high` / `medium` / `low`
  - Coherence: `high` / `medium` / `low`
  - Redundancy: `none` / `partial overlap` / `major overlap`
- **Main problems**: free-form list of issues.
- **Valuable elements to preserve**: itemized by type — definitions, lemmas, proofs, examples, interpretations.
- **Migration action** (choose one): `preserve as is with light refactor`, `rewrite under contract`, `split into several notes`, `merge into another note`, `demote to scratch/reference`, `archive`.
- **Candidate target note(s)** and **Comments**.

This prevents premature rewriting and forces explicit triage.

---

# IV. Phase 3: reconstruct the reasoning graph from the existing vault

This is the decisive phase.

The current vault contains notes, but the new system needs a graph of **atomic inferential units**. Therefore the task is not to map one old note to one new note. It is to infer the latent reasoning structure that the old notes only partially realize.

## 1. Extract atomic questions from legacy notes

For each legacy note, identify:

- the main explicit question
    
- the implicit subquestions
    
- the results proved or attempted
    
- the reusable tools introduced
    
- the interpretations or syntheses it contains
    

In many cases, one old note will decompose into several atomic units:

- one result note
    
- one tool note
    
- one synthesis note
    
- one comparison note
    

This is normal.

---

## 2. Build a provisional migration graph

A dedicated file (`registry/migration_graph.yaml`) should describe how legacy materials map into the target architecture. Each entry in the `legacy_notes` array contains: `legacy_id`, `path`, and a `contains` array listing the target notes that draw material from this legacy note. Each `contains` entry has a `target_id` and a `role` (e.g., `partial_definition`, `partial_result`, `interpretive_seed`, `example_material`, `motivating_example`).

This file is extremely useful because it makes explicit that migration is often **many-to-many**:

- one legacy note may feed several target notes
    
- one target note may draw material from several legacy notes
    

---

## 3. Reconstruct the target note list before rewriting

Before any large-scale content migration begins, the new `reasoning_graph.yaml` should already contain the intended target notes and their roles, even if many are still empty.

Each target note should be registered with at minimum `id`, `type`, and `status: planned` — even if the note does not yet exist. This makes it possible to migrate toward a destination rather than editing in place without a map.

---

# V. Phase 4: triage legacy notes into actions

Each legacy note should receive one primary migration action. A useful action taxonomy is the following.

## 1. `preserve_lightly`

Use this when the note:

- already answers a reasonably atomic question
    
- has valuable mathematics
    
- has low redundancy
    
- mainly needs local restructuring and metadata
    

This should be relatively rare in a heavily drifted vault.

---

## 2. `rewrite_under_contract`

Use this when the note:

- addresses an important target question
    
- contains valuable material
    
- is currently too diffuse or poorly motivated
    
- should survive, but only after re-authoring under the new workflow
    

This will likely be the dominant category.

---

## 3. `split`

Use this when one legacy note actually contains multiple inferential units.

Typical indicators:

- several result-level results with different roles
    
- mixture of background, proof, interpretation, and synthesis
    
- abrupt changes of scope
    
- one section functioning as a reusable tool while another functions as an application
    

This category is extremely important. Many migration problems disappear once notes are split correctly.

---

## 4. `merge`

Use this when several legacy notes each contain incomplete fragments of the same target note.

This often happens when the vault evolved iteratively and similar thoughts were spread across multiple files.

---

## 5. `demote_to_reference`

Use this when the material is useful but should no longer count as part of the main reasoning graph.

Examples:

- exploratory derivations
    
- historical side paths
    
- alternative formulations not currently used
    
- useful examples but not central
    
- literature extracts
    

These can be moved into a reference or scratch layer.

---

## 6. `archive`

Use this when the note:

- has no unique value
    
- duplicates better material elsewhere
    
- contains exploratory dead ends with no lasting utility
    
- introduces conceptual confusion
    

Archiving is essential. Without it, the vault remains noisy and the agent continues to encounter obsolete material.

---

# VI. Phase 5: migrate incrementally along priority fronts

The migration should not proceed file-by-file in arbitrary order. It should proceed by **strategic fronts**.

A good priority order is:

## Front 1: foundational notes

These determine:

- terminology
    
- core definitions
    
- principal distinctions
    
- admissible assumptions
    

These notes should be migrated first because later notes depend on them.

## Front 2: result and tool notes

These establish the reusable mathematical machinery.

## Front 3: synthesis notes

These combine stabilized earlier notes.

## Front 4: peripheral references and examples

These can be migrated later or demoted.

This ordering prevents repeated rewriting caused by unstable foundations.

---

# VII. A concrete migration workflow

The following step-by-step process is recommended for each migration batch.

---

## Step 1: create a batch, not a single-note universe

Choose a small coherent cluster of legacy notes, typically:

- one foundational note and its close neighbors
    
- or two to five notes around one subproblem
    

Do not migrate the entire vault at once.

Create a planning file (e.g., `scratch/planning/migration_batch_001.md`) containing: the batch theme, legacy notes included, target notes expected, and risks (terminology instability, hidden overlap, uncertain result scope). This keeps migration local and inspectable.

---

## Step 2: review the legacy notes diagnostically

For each note in the batch:

- fill a legacy review
    
- update `migration_index.yaml`
    
- identify reusable content fragments
    

At this stage, no final drafting occurs.

---

## Step 3: define the target notes in the new reasoning graph

Before rewriting any content, register the target notes in:

- `reasoning_graph.yaml`
    
- `open_questions.yaml`
    
- `dependencies.yaml` when applicable
    

This fixes the destination.

---

## Step 4: create contracts for the target notes

For each target note in the batch:

- create a contract in `contracts/active/`
    
- specify which legacy notes provide raw material
    

Add a section to the contract specifying which legacy notes provide raw material, which elements to preserve if possible (specific proofs, examples, interpretations), and which elements to exclude (redundant exposition, speculative extensions). This is extremely useful for controlled reuse.

---

## Step 5: outline before drafting

Ask for outline-only migration for each target note:

- atomic question
    
- result or result
    
- proof route
    
- source fragments used
    
- excluded fragments
    
- stopping condition
    

Validate manually.

This is the most important supervision point.

---

## Step 6: draft the new note from the contract, not by editing the old note directly

This point is crucial.

In most cases, the new note should be written as a **new file** in `notes/`, rather than editing the legacy file in place. The old note should remain available as source material until migration is complete.

Reason:

- direct editing preserves old structure and encourages local patching
    
- new drafting under contract forces clean reconstruction
    

---

## Step 7: audit the migrated note

Run the normal audit procedure:

- coherence
    
- mathematical rigor
    
- redundancy
    
- integration
    

Then revise only against audit findings.

---

## Step 8: mark legacy notes as consumed, partially consumed, or obsolete

Update `migration_index.yaml` with states such as:

- `consumed`
    
- `partially_consumed`
    
- `superseded`
    
- `archived`
    

For each consumed note, the `migration_index.yaml` entry is updated with the final `status` (`consumed`, `partially_consumed`, `superseded`, `archived`), the `action` taken, the `target_note_id`(s), and `comments` explaining what was reused and what was discarded.

---

## Step 9: move or mark legacy notes physically

Once the migrated replacement is stable, the legacy note should not remain in the main active zone unchanged. Otherwise the agent will continue to consult both the old and new versions.

A useful directory policy is a dedicated `legacy/` directory with subdirectories `reviewed/`, `superseded/`, and `archived/` (matching the structure described in the [workspace architecture](workspace-architecture.md)). Each superseded note should contain a short header naming the replacement notes and stating that the file is not an authoritative source for new drafting. This reduces future confusion.

---

# VIII. Suggested files for migration management

In addition to the files previously described, the migration phase benefits from a few dedicated files.

## 1. `registry/migration_index.yaml`

Tracks each legacy note and its action.

## 2. `registry/migration_graph.yaml`

Tracks mappings between legacy fragments and target notes.

## 3. `governance/specs/legacy_review.md`

Standardizes diagnosis (see [Phase 2, section 3](#3-add-a-legacy-review-specification) above).

## 4. `scratch/planning/migration_batches.md`

Lists planned batches. Each batch entry contains: theme, legacy notes included, and target notes expected.

## 5. `07_legacy/`

A dedicated space for non-authoritative older notes.

---

# IX. How to supervise the migration personally

Personal intervention is most necessary at the following moments.

## 1. Determining the target architecture

This must remain under direct control because it requires research judgment:

- what are the true atomic questions
    
- what is foundational and what is derivative
    
- what belongs in the main argument and what should be demoted
    

## 2. Approving splits and merges

This is critical because it changes the inferential decomposition of the project.

## 3. Choosing what counts as mathematically valuable

Some notes may be diffuse but contain one deep insight. Others may be technically long but strategically useless. This discrimination requires domain judgment.

## 4. Validating result scope and proof routes

This remains one of the main control points.

## 5. Deciding when to archive

Archiving requires willingness to discard material that consumed time but no longer serves the architecture.

---

# X. What should not be done

Several migration habits should be avoided.

## 1. Do not rewrite notes in place by default

This tends to preserve old disorder under superficial cleanup.

## 2. Do not migrate by chronological order

The order should follow inferential priority, not historical creation date.

## 3. Do not let the agent decide alone whether a note is foundational

This decision affects the entire graph.

## 4. Do not preserve every mathematically interesting side path in the main vault

Demotion and archiving are necessary for clarity.

## 5. Do not attempt to make every legacy note survive

Some notes are raw material, not final components.

## 6. Do not begin with synthesis notes

Synthesis should come after foundations and result notes are stabilized.

---

# XI. A practical priority rubric

When deciding what to migrate first, score each note or cluster according to the following criteria:

|Criterion|Question|
|---|---|
|Foundationality|Does later work depend on this note?|
|Reusability|Does it contain definitions, lemmas, or constructions reused elsewhere?|
|Current confusion cost|Is this note currently causing conceptual drift or overlap?|
|Mathematical value|Does it contain genuinely useful derivations?|
|Migration tractability|Can it be cleanly reconstructed now?|

Notes with high foundationality and high confusion cost should be migrated first.

---

# XII. A recommended first migration sequence

A sound initial plan is the following.

## Stage A: migrate the conceptual foundations

- central definitions
    
- core assumptions
    
- main distinctions
    
- terminology normalization
    

## Stage B: migrate the core result chain

- main technical results
    
- reusable tools
    
- direct prerequisites for synthesis
    

## Stage C: migrate synthesis and interpretation

- how the technical results answer the research question
    
- comparison and integrative notes
    

## Stage D: process exploratory and peripheral material

- demote, archive, or selectively reintegrate
    

This keeps the center of the vault stable first.

---

# XIII. Example of one migration case

Suppose a legacy note contains:

- a partial definition of equivariance
    
- a result on covariance structure
    
- two examples
    
- a long discussion of empirical implications
    

This note should not be "cleaned up." It should likely be split into:

1. `equivariant_representation_map` as a result note
    
2. `covariance_block_structure` as a result note
    
3. `empirical_block_diagnostics` as a synthesis note
    
4. possibly one reference note for examples
    

The old note becomes source material, not the target object.

This example illustrates the general principle:

> Migration should recover the latent architecture hidden inside the old notes.

---

# XIV. Minimal operational migration protocol

If a lightweight but rigorous procedure is needed, the following protocol is sufficient.

For each migration batch:

1. review each legacy note using the legacy review template
    
2. update `migration_index.yaml`
    
3. define target note IDs in `reasoning_graph.yaml`
    
4. create one contract per target note
    
5. draft outline only
    
6. validate outline manually
    
7. draft new note
    
8. audit new note
    
9. revise from audit
    
10. mark old note as superseded or archived
    

This protocol is simple enough for daily use and strong enough to enforce the new architecture.

---

# XV. Final principle

The migration should be treated exactly like a refactoring of a large software system.

- legacy notes are the old codebase
    
- target notes are the refactored modules
    
- contracts are interface specifications
    
- the reasoning graph is the dependency graph
    
- audits are tests
    
- archiving is dead-code elimination
    

Under this perspective, the correct question is not:

> How should the old notes be improved?

The correct question is:

> What inferential modules should the final system contain, and which parts of the old vault are worth reusing to build them?

That shift in perspective is what makes the migration tractable and coherent.

A next useful step would be to design a concrete migration rubric and a `migration_index.yaml` schema adapted to the current categories of the vault.
