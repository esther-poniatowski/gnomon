# Source-file cleanup handoff — files 2–11

> [!INFO] Status
> File 1 (`1-framework/content-adequacy.md`) is complete and serves as the canonical example. Files 2–11 await cleanup. This brief specifies the goal, the scope, the mechanics, and the per-file work plan. Read it once and execute file by file, pausing for user approval on every flagged item.
>
> **Hard prerequisite.** Three substantive TODOs added to `_framework-criteria.md` during the project pause must be resolved before resuming this cleanup. They edit headings and bodies in `_framework-criteria.md` (anchors `^t1-inquiry-content-and-progression`, `^t1-reasoning-understandability`, `^t1-activity-separation`) that this cleanup treats as stable migration targets. Resuming the cleanup before the TODOs are resolved risks deleting source-file content that a revised criterion may still need. The dependency chain and the recommended order to resume are in the [main handoff](_handoff).

---

## 1. Goal

Remove from active-tier and backup source files any content already integrated into `vendor/gnomon/docs/design/_framework-criteria.md`, replacing each migrated heading's body with a single `[!INFO] Migrated to ...` callout. The goal is to eliminate duplication between `_framework-criteria.md` and the source files it superseded, **without losing any substantive content** that has not yet been integrated into the framework-level criteria.

This is a **felicate task with irreversible consequences**. The discipline below is mandatory.

---

## 2. Hard rules

### 2.1 Cleanup eligibility

A source-file heading is **cleanup-eligible** only when its content is already integrated into `_framework-criteria.md`. Cleanup-eligibility does not extend to content integrated only into T2/T3 active-theme files — those will be cleaned in a later session.

### 2.2 Cleanup mode (option b)

For each cleanup-eligible heading:

- **Keep** the `### Heading ^anchor` line. The anchor must remain in place for inbound-reference resolution during Step C.
- **Replace the body** with a single `> [!INFO] Migrated to [criterion-label](_framework-criteria#^t1-anchor)` callout. The callout text may extend to multiple sentences if it must record where sub-claims went (see file 1 for examples).
- **Delete** the original prose body, the `*Source*: …` footers, and any other content that was migrated.
- **Do not** add R-redirects, restructure remaining sections, or modify file-level metadata beyond what this brief authorises.

### 2.3 Triage policy for substantive content not present in the criterion

When a source-file heading contains content not present in the integrated criterion, **flag it** to the user and propose one of three actions:

- **(i) Migrate now** — integrate the content into `_framework-criteria.md` first, then delete from source. Use this when the content is genuinely substantive and belongs in the framework-level criteria.
- **(ii) Move to backup** — move the content into a backup file as candidate material for a later T2/T3 decision. Use this when the content is candidate-material for a downstream decision recorded in `_classification-table.md` but the destination decision is not yet authored.
- **(iii) Accept loss** — confirm with the user that the content is not worth keeping. Use only after explicit confirmation.

**Never decide unilaterally on flagged content.** Pause for user approval before any irreversible deletion of substantive material.

### 2.4 Granularity

- Process **one heading at a time** within a file. Do not wholesale-rewrite a source file.
- Files that contain both migrated and non-migrated headings (notably `2-architecture/constraints.md`) are processed section-by-section. Non-migrated sections must stay intact.
- Process **one file per cycle**. Pause after each file for user review before moving to the next.

### 2.5 Flag-everything discipline

Default to flagging. The standard for "no flag needed" is: every sentence, list, table, and example in the source body is unambiguously covered by the corresponding criterion in `_framework-criteria.md`. If the source body has a sentence the criterion does not have, flag it. If the source body has a tighter formulation than the criterion, flag it. If the source body has an example or cross-reference the criterion lacks, flag it.

**A reminder from file 1**: an earlier agent silently dropped the `Determined by` column of the three-levels table under `^t1-intelligibility`. The column lists the **structural components** of each justification level (support+inferential pattern for Licensing; gap+objective+rationale for Strategic; gain for Explanatory). The user had to detect the loss and request restoration. That kind of silent flattening is the failure mode this discipline prevents. **When in doubt, flag.**

---

## 3. The integrated-criteria index

Before processing any source file, look up which criterion in `_framework-criteria.md` the source heading was migrated to. The current canonical mapping is:

| Source anchor | Source file | Migrated-to anchor in `_framework-criteria.md` | New label |
| --- | --- | --- | --- |
| `^t1-epistemic-adequacy` | `1-framework/content-adequacy.md` | `^t1-inquiry-content-and-progression` | Inquiry content and progression |
| `^t1-expressivity` | `1-framework/content-adequacy.md` | `^t1-reasoning-types-coverage` | Reasoning-types coverage |
| `^t1-non-arbitrary` | `1-framework/content-adequacy.md` | `^t1-goal-driven-reasoning` | Goal-driven reasoning |
| `^t1-concrete-execution` | `1-framework/content-adequacy.md` | `^t1-concrete-execution` | Concrete analytical execution |
| `^t1-intelligibility` | `1-framework/epistemic-adequacy.md` | `^t1-reasoning-understandability` | Reasoning understandability |
| `^t1-modularity` | `1-framework/structural-quality.md` | `^t1-reuse` and `^t1-addressability` (split) | Reuse / Addressability |
| `^t1-partial-formalization` | `1-framework/operational-quality.md` | `^t1-partial-formalization` | Partial formalization tolerance |
| `^t1-dual-usability` | `1-framework/operational-quality.md` | dropped (R against the cost-axis cluster) | n/a |
| `^t1-feasibility` | `1-framework/operational-quality.md` | `^t1-system-scale` (rename) + `^t1-human-action-cost` + `^t1-partial-formalization` (split) | System scale (machine-scale only) |
| `^t2-separation-of-concerns` | `2-architecture/constraints.md` | `^t1-activity-separation` | Activity separation |
| `^t2-non-redundancy` | `2-architecture/constraints.md` | `^t1-non-redundancy` | Non-redundancy |
| `^t2-graph-queryability` | `2-architecture/constraints.md` | `^t1-relational-queryability` | Relational queryability |
| `^t2-defeasibility` | `2-architecture/constraints.md` | `^t1-mixed-monotonicity` | Composition of warrant kinds |
| `^t2-snapshot-dag` | `2-architecture/constraints.md` | `^t1-no-circular-reasoning` | No circular reasoning |
| `^t2-mechanical-validation` | `2-architecture/constraints.md` | `^t1-read-side-automation` and `^t1-write-side-automation` (split) | Read-side automation / Write-side automation |
| `^t2-repr-vs-gen` | `2-architecture/constraints.md` | **retired in pass-5** — concerns absorbed into three sibling T1 criteria: `^t1-partial-formalization` (maturity), `^t1-activity-coverage` and `^t1-activity-separation` (activity-kind), `^t1-inquiry-content-and-progression` (static/dynamic) | n/a — this source heading carries a retirement callout, not a migration callout. The architectural decision `^t2-representation-vs-generation` (in `operations-and-modes.md`) is reframed as the chosen response to the three sibling criteria. |
| `^t2-revision-semantics` | `2-architecture/constraints.md` | `^t1-revision-accountability` | Revision accountability |
| `^t2-data-format-criteria` | `2-architecture/data-formats.md` | `^t1-rich-prose-expressivity` (only the prose+formulas+math sub-claim) | Rich prose expressivity |
| `^t3-discharge-accounting` | `3-aspect-specific/arguments-reasoning.md` | `^t1-no-silent-incompleteness` (criterion only; the discharge mechanism stays as `^t3-assumption-discharge-mechanism`) | No silent incompleteness |
| Core requirements row "Epistemic adequacy" | `_backup/criteria-framework.md` | `^t1-inquiry-content-and-progression` | Inquiry content and progression |
| Core requirements row "Expressivity and flexibility" | `_backup/criteria-framework.md` | `^t1-reasoning-types-coverage` | Reasoning-types coverage |
| Core requirements row "Intelligibility and Understanding" | `_backup/criteria-framework.md` | `^t1-reasoning-understandability` | Reasoning understandability |
| Core requirements row "Non-arbitrary chaining" | `_backup/criteria-framework.md` | `^t1-goal-driven-reasoning` | Goal-driven reasoning |
| Core requirements row "Concrete analytical execution" | `_backup/criteria-framework.md` | `^t1-concrete-execution` | Concrete analytical execution |
| Core requirements row "No infinite regress" | `_backup/criteria-framework.md` | `^t1-no-infinite-regress` | No infinite regress |
| Core requirements row "Modularity, Reusability" | `_backup/criteria-framework.md` | `^t1-reuse` and `^t1-addressability` | Reuse / Addressability |
| Core requirements row "Implementation feasibility" | `_backup/criteria-framework.md` | `^t1-system-scale` | System scale |
| Core requirements row "Usability" | `_backup/criteria-framework.md` | `^t1-human-action-cost` | Human action cost |
| Core requirements row "Human-AI compatibility" | `_backup/criteria-framework.md` | `^t1-human-read-cost` + `^t1-human-action-cost` + `^t1-read-side-automation` + `^t1-write-side-automation` | (cost-axis cluster) |
| Core requirements row "Audience-independent stability" | `_backup/criteria-framework.md` | `^t1-activity-separation` | Activity separation |
| Quality constraints (five-operation list) | `_backup/criteria-framework.md` | `^t1-cognitive-manipulability` | Cognitive manipulability |
| Functional criterion "unit of progression vs. unit of epistemic work" | `_backup/object-types-ontology/criteria-taxonomy-ontology.md` | `^t1-function-driven-typology` | Function-driven typology |
| Mandatory drafting gate paragraph | `_backup/registries-indexes.md` | `^t1-staleness-gating` | Staleness gating |
| Validation externality paragraph (top of file) | `_backup/tooling-validation.md` | `^t1-validation-externality` | Validation externality |
| Terminology enforcement row (Architecture table) | `_backup/tooling-validation.md` | `^t1-canonical-terminology` | Canonical terminology |

If a source heading is **not in this table**, it is **not cleanup-eligible** in this session — leave it alone.

---

## 4. Pass-4 and pass-5 structural commitments worth knowing

The current state of `_framework-criteria.md` reflects six structural commitments from pass-4 and pass-5 that the cleanup must respect.

### Pass-4 commitments (from earlier session)

- **Inquiry content and progression** (`^t1-inquiry-content-and-progression`, was `^t1-research-faithfulness`) — the renamed foundational criterion. Body: static dimension (epistemic content as it stands) + dynamic dimension (inferential progression). Two-bullet structure with explicit *static* and *dynamic* terms.
- **Stable boundaries** (`^t1-stable-boundaries`) — meta-integrity property of the framework's own components (object kinds, fields, relations, vocabularies, operations, layers). (Pass-5 moved this from *Reasoning integrity* to the new *Framework foundation* group.)
- **Activity coverage** (`^t1-activity-coverage`) — canonical seven-activity taxonomy: inquiry direction, content production, justification, critique, revision, exposition, navigation. (Pass-5 placed in *Expressive depth*.)
- **Function-driven typology** (`^t1-function-driven-typology`) — generalised body. The criterion talks about *epistemic units* (content, activity, operation), not only object types. (Pass-5 moved from *Operationality* to *Expressive depth*.)

### Pass-5 commitments (this session)

- **Group restructure**: the eight pass-4 groups become six — *Framework foundation*, *Expressive depth*, *Reasoning integrity*, *Modular content organization*, *Research activities and workflows*, *Cost and Ergonomics*. *Operationality* is gone (its three criteria moved into *Expressive depth*); *Understanding and Manipulability* merged into *Reasoning integrity*; *Workflow integrity* and *Separation of research activities* merged into *Research activities and workflows*. *Cost and Ergonomics* now sits last so that activity-side criteria immediately follow content-side criteria. *Function-driven typology* sits in *Framework foundation*. The Themes-table descriptions describe each group's unifying purpose, never enumerate members.
- **New criterion**: **Typed-object decomposition** (`^t1-typed-object-decomposition`) in *Framework foundation*, downstream of *Inquiry content and progression*. The framework decomposes inquiry content into typed objects of distinct kinds. The criterion does not prescribe how inferential progression is recorded — that is downstream.
- **Retired criterion**: **Representation versus generation** (`^t1-representation-vs-generation`) is dropped entirely. Its substantive concerns are absorbed into three sibling criteria — *Partial formalization tolerance* (maturity), *Activity coverage* and *Activity separation* (activity-kind), *Inquiry content and progression* (static/dynamic dimension). The architectural decision `^t2-representation-vs-generation` in `operations-and-modes.md` is reframed as the chosen response to the three sibling criteria.

If you encounter source content that anticipates any of these (e.g., a `Conceptual soundness` clause, a `Logic of inquiry` clause, a list of research activities, a "function distinguishes types" claim about objects only, a typed-object commitment, a "modes" framing), recognise that the integration has already happened in `_framework-criteria.md` and the source content is cleanup-eligible.

---

## 5. Per-file work plan

Process files in this order. After each file, summarise what was done and pause for user review. The user will say "next" or correct course.

### File 2 — `1-framework/epistemic-adequacy.md`

One migrated heading: `## Intelligibility and understanding ^t1-intelligibility` → `^t1-reasoning-understandability`.

**Substantive content to inventory carefully.** This file contains the **three-levels table** (Form / Question answered / Determined by / Examples) which has been restored in full to `_framework-criteria.md` during pass-4. It also contains:

- a "Levels are stages in a reasoning" paragraph naming a five-state transition (problem state → diagnostic → strategic response → local transformation → newly intelligible state),
- an "Independence of the levels" paragraph with examples of how each level varies independently,
- a `[!hint] Authoritative sources` callout citing **Toulmin** (claim–data–warrant–backing), **van Fraassen** (why-questions relative to contrast classes), **Polya** (heuristic theory, proof-strategic layer), **Detlefsen** and **Steiner** (mathematical-explanation analyses).

Verify each item against the current `^t1-reasoning-understandability` body before flagging. The five-state transition and the independence examples may not be in the criterion — flag for triage. The Authoritative-sources callout is almost certainly not in the criterion (citations were dropped during migration) — flag and propose option (i) migrate-now into the criterion's body or option (ii) move-to-backup as a research-methods record.

File-level fate: keep as stub, remove the `[!INFO] Tier and axis` opening callout (consistent with file 1's policy).

### File 3 — `1-framework/structural-quality.md`

One migrated heading: `## Modularity and reusability ^t1-modularity` → split into `^t1-reuse` + `^t1-addressability`.

Source body has three sub-bullets: addressability, reuse, audience-independent stability. The first two map cleanly to the split criteria. The third (*audience-independent stability*) was redirected per the classification table to `^t1-activity-separation`.

Likely clean — verify body coverage in the three target criteria (`^t1-reuse`, `^t1-addressability`, `^t1-activity-separation`) before deleting.

File-level fate: stub.

### File 4 — `1-framework/operational-quality.md`

Three migrated headings:

- `## Partial formalization tolerance ^t1-partial-formalization` → criterion of the same name. The body should already be covered after the pass-4 sharpening (with "intermediate contents admissible"). Verify.
- `## Human and machine usability ^t1-dual-usability` → **dropped** (R against the cost-axis cluster per classification table line 79). The body lists three sub-claims: multiple projections from one source (→ activity-separation), annotation burden scaling (→ partial-formalization), schema validation mechanical (→ write-side-automation). Each redirect is recorded in the classification table; verify that each sub-claim is in fact covered by its target before deleting.
- `## Implementation feasibility and scale ^t1-feasibility` → `^t1-system-scale` (rename, machine-side only). The annotation-cost clause was redirected to `^t1-human-action-cost` + `^t1-partial-formalization` per classification table line 80. Verify both halves are covered.

File-level fate: stub. Remove the `[!INFO] Tier and axis` opening callout if present.

### File 5 — `2-architecture/constraints.md` (subsections only)

This file is **not** a stub-the-whole-thing case. It contains many T2 sections; only the ones in the cleanup table above are eligible. **Process each migrated subsection individually**. Non-migrated subsections — including but not limited to `^t2-single-source-of-truth`, `^t2-dependency-management`, `^t2-layer-dependency`, `^t2-layer-replaceability`, `^t2-narrow-ontology`, `^t2-coverage-completeness`, `^t2-no-inheritance`, `^t2-subtype-safety`, `^t2-field-typing`, `^t2-closed-operational-core`, `^t2-multi-regime-reasoning`, `^t2-annotation-richness`, `^t2-justificatory-level-placement`, the open-questions G1–G5, and the tension records `^t2-x1`–`^t2-x4` — must stay intact.

The eight subsections to process are: `^t2-separation-of-concerns`, `^t2-non-redundancy`, `^t2-graph-queryability`, `^t2-defeasibility`, `^t2-snapshot-dag`, `^t2-mechanical-validation`, `^t2-repr-vs-gen`, `^t2-revision-semantics`. Each already has a callout from earlier passes — for seven of them a migration callout, for `^t2-repr-vs-gen` a **retirement callout** (the criterion was retired in pass-5; the callout points at the three sibling T1 criteria that absorbed its concerns rather than at a single migration target). The cleanup is to delete each subsection's body, leaving the heading + callout. Verify each body's content is fully covered in the target criterion (or for `^t2-repr-vs-gen`, in the three absorption targets) before deleting.

**Important.** Each of these subsections has a `*Source*: …` footer and may have additional cross-references inside the body (e.g., to T2 decisions in the validity-revision theme). Some cross-references are migration-relevant (i.e., they point to where the body's content was further refined in a T2 file) and should be preserved as part of the callout text. Flag those.

File-level fate: keep file fully intact except the eight migrated subsections become stubs.

### File 6 — `2-architecture/data-formats.md` (one subsection only)

One migrated heading: `### Format criteria ^t2-data-format-criteria` → only the *prose+formulas+math* sub-claim went to `^t1-rich-prose-expressivity`. The other five sub-claims (*readable*, *parseable*, *schema-checkable*, *controlled fields*, *stable Git diffs*) are R-redirects to existing criteria per classification table line 122.

The body is a 6-bullet list. After cleanup, the heading carries a callout listing **all six redirects** (one promoted, five R-redirects), then the bullet list is deleted.

The rest of `2-architecture/data-formats.md` is **not** cleanup-eligible (source-language and grammar decisions, schema, declaration tags, etc.) — leave intact.

### File 7 — `3-aspect-specific/arguments-reasoning.md` (one subsection only)

One migrated heading: `### Discharge accounting for assumptions ^t3-discharge-accounting` → the criterion clause migrated to `^t1-no-silent-incompleteness`; the discharge mechanism stays as the open decision `^t3-assumption-discharge-mechanism` in this same theme.

The cleanup here is partial: delete the criterion-level prose, but the source paragraph likely also contains decision-level content (the three candidate paths for handling assumed nodes: eliminate by downstream proof, absorb into the conclusion as a hypothesis, flag as unresolved residue) which belongs to `^t3-assumption-discharge-mechanism` and stays in this file. Flag carefully — what looks like criterion content may be decision content that has not yet been moved to its proper place.

The rest of `3-aspect-specific/arguments-reasoning.md` is **not** cleanup-eligible.

### File 8 — `_backup/criteria-framework.md`

Already restructured by pass-3 audit into one heading-per-row form with literal `[!INFO] Migrated to ...` callouts on each row. The cleanup is to delete the body bullet content beneath each callout, preserving the heading + callout structure. The entire `## Quality constraints` section's five-bullet operation list (Reconstruction / Contrast / Compression / Transfer / Diagnosis with their descriptions and the diagnosis sub-list) is migrated to `^t1-cognitive-manipulability` — verify coverage and clean.

Beware: the file also contains content that has **not** been integrated into `_framework-criteria.md`:

- the "Patterns" section (Encoding the conceptual effect of each step / Encoding alternatives and rejections / Encoding the statuses of content) is destined for T2/T3 decisions in the reasoning-fields and status-vocabulary themes per the classification table. **Not cleanup-eligible.** Leave intact.

### File 9 — `_backup/object-types-ontology/criteria-taxonomy-ontology.md`

One paragraph migrated: the *Functional criterion — distinction "unit of progression vs. unit of epistemic work"* paragraph → `^t1-function-driven-typology`. Already has an `[!INFO]` callout from pass-3.

Beware: the rest of the file (ontological criterion, three-condition stack, exclusion list, decision table, attributes-vs-objects content, inheritance-over-duplication content) is **not yet integrated** into `_framework-criteria.md`. The classification table records each as destined for T2 decisions (object-kind admission, ontology stability, etc.). **Not cleanup-eligible.** Process only the *Functional criterion* paragraph; leave the rest.

### File 10 — `_backup/registries-indexes.md`

One paragraph migrated: the *Mandatory drafting gate* paragraph → `^t1-staleness-gating`. Already has an `[!INFO]` callout from pass-3.

The rest of the file (Proposal 1, Proposal 2, registry types, edge types, internal subdistinction) is **not yet integrated** — destined for T2 decisions in the registries-indexes theme per the classification table. **Not cleanup-eligible.** Process only the drafting-gate paragraph.

### File 11 — `_backup/tooling-validation.md`

Two paragraphs migrated:

- the externality+hard-gate sentence at the top of the file → `^t1-validation-externality`. Already has an `[!INFO]` callout.
- the *Terminology enforcement* row of the Architecture table → `^t1-canonical-terminology` (pass-5 rename of `^t1-terminology-canonicity`). Already has an `[!INFO]` callout.

The rest of the file (architecture table other rows, schema requirements, status-transition rules, staging area, tooling, three-tool inventory) is destined for T2 decisions per the classification table. **Not cleanup-eligible.** Process only the two callouts' source paragraphs.

---

## 6. Workflow per file

For each file:

1. Read the entire file.
2. For each cleanup-eligible heading, read the corresponding criterion in `_framework-criteria.md`.
3. Build a diff: source body content vs. criterion content. List every sentence, table, list, example, callout, cross-reference in the source body and mark each as ✓-covered or **flag**.
4. Present the diff to the user with triage proposals (i/ii/iii) for each flagged item.
5. Wait for user approval.
6. Apply only the approved deletions. For approved migrations (i), draft the integration into `_framework-criteria.md` first, get user approval on the integration, then delete from source.
7. After cleanup, verify by grep that no stale prose or anchor references survive.
8. Run a brief consistency sweep against `_classification-table.md` and update any rows that record the source heading.
9. Summarise the cleanup for this file and stop. Wait for "next".

---

## 7. Discipline reminders

- **Never delete substantive content without explicit user approval.**
- **The classification table is the migration ledger.** When in doubt about whether content is cleanup-eligible, look up the row in `_classification-table.md` for the source heading. If the *Final state* cell records anything beyond an R-redirect to a `^t1-` anchor in `_framework-criteria.md`, the content is **not fully cleanup-eligible** in this session.
- **Flag tables before flattening to lists, lists before flattening to prose.** Multi-column tables in source files frequently encode structure that single-column lists lose.
- **Flag external citations.** Author names, methodology references, and external-document links are the kind of content that disappears silently.
- **Preserve anchors.** Inbound cross-references to source anchors must keep resolving until Step C executes the redirect sweep.
- **Pass-4 and pass-5 audit notes are recorded in `_handoff-refactor.md`.** Don't add new audit notes there; if substantive structural changes are needed during this cleanup pass, propose them to the user before adding them.

---

## 8. Output expectations per file

After processing each file, produce a short report:

- which headings were cleaned (anchor + new callout text);
- what was flagged and the user's decision for each flag;
- what was migrated into `_framework-criteria.md` (if anything);
- what was moved to backup (if anything);
- what was lost with explicit confirmation (if anything);
- any classification-table rows that were updated.

Then stop and wait for the next instruction.
