# Refactor handoff — design folder

> [!INFO] Status
> Step A.1, Step A.2, and Step A.3 are complete. The [classification table](_classification-table) is the source of truth for all Step B and Step C work: class tags, target anchors, split/fold decisions, redirect targets, backup-sourced entries, and classification coherence rules are recorded there. The framework-level criteria now live in [_framework-criteria.md](_framework-criteria), grouped by theme and ordered by dependency.
>
> **Step A.4 — Source-file cleanup is in progress.** This sub-step removes duplicated bodies from the eleven source files whose content was migrated into `_framework-criteria.md`. File 1 (`1-framework/content-adequacy.md`) is complete; files 2–11 are pending. The detailed brief is in the [cleanup handoff](_handoff-cleanup).
>
> Before resuming Step A.4, three substantive TODOs added to `_framework-criteria.md` during the pause must be resolved (they edit headings and bodies that Step A.4 would otherwise treat as stable migration targets). See the [main handoff](_handoff) for the dependency chain.
>
> **Step B is blocked on Step A.4.** The migration table records anchors and headings; running Step B before Step A.4 stabilises them would force a re-sweep.

---

## Working State

The design folder still uses the legacy tier layout:

```text
vendor/gnomon/docs/design/
  1-framework/          framework-level criteria
  2-architecture/       architecture-level criteria, decisions, and open questions
  3-aspect-specific/    aspect-specific criteria, decisions, and open questions
  _backup/              inactive proposals and superseded drafts
  _classification-table.md
  _alias-table.md
  _handoff.md
  _handoff-refactor.md
  _handoff-cleanup.md
```

Current anchors use the flat tier prefixes `^t1-<short>`, `^t2-<short>`, and `^t3-<short>`. Backup-sourced target anchors use `^bk-<short>` until Step C decides their final names. The classification table records planned renames and final destinations.

---

## Next Steps

- [x] Step A.1 — Classify criteria and active theme-file decisions.
- [x] Step A.2 — Integrate selected backup decisions into the classification table.
- [x] Step A.3 — Extract all F entries into `_framework-criteria.md`, grouped by theme and ordered by dependency.
- [ ] **Step A.4 — Source-file cleanup.** File 1 complete; files 2–11 pending per the [cleanup handoff](_handoff-cleanup). Prerequisite: the three TODOs in `_framework-criteria.md` must be resolved first.
- [ ] **Step B** — Create `_migration-table.md` from the classification table, one row per *Final state* bullet. Prerequisite: Step A.4.
- [ ] **Step C** — Migrate and convert entries in batches, using the migration table as the redirect source of truth. Prerequisite: Step B.
- [ ] **Step D** — Reorganize the design folder by theme after migration settles. Prerequisite: Step C.

---

## Refactoring Plan

### Step A.1 — Classify Criteria + Theme-File Decisions ✅ Done ^step-a

Complete. The classification table records the classified entries, target actions, redirects, repairs, folds, and justifications. Do not redo this step unless the user explicitly asks for a new audit.

### Step A.2 — Integrate Remaining Decisions ✅ Done ^step-a2

Complete. The classification table records the selected backup decisions and the active T2/T3 decision entries. Backup object taxonomy files under `_backup/object-types-ontology/taxo-*.md` remain out of scope.

### Step A.3 — Framework Criteria ✅ Done ^step-a3

Complete. `vendor/gnomon/docs/design/_framework-criteria.md` contains 30 F sections — the 27 enumerated under [^step-a3-themes](#^step-a3-themes) (with substantial pass-3/pass-4/pass-5 revisions), plus `^t1-revision-accountability` (originally `^t2-revision-semantics`, promoted and renamed during pass-3), `^t1-stable-boundaries` (added in pass-4), `^t1-activity-coverage` (added in pass-4), and `^t1-typed-object-decomposition` (added in pass-5). The pass-4 promotion `^t1-representation-vs-generation` was retired in pass-5. Sections are grouped into six themes — Framework foundation, Expressive depth, Reasoning integrity, Modular content organization, Research activities and workflows, Cost and Ergonomics — ordered by dependency within each group. Pass-5 reordering placed Cost and Ergonomics last so that activity-side criteria immediately follow content-side criteria. (The original `^step-a3-themes` enumeration below preserves the pass-1 names as protocol-record audit trail; the Status callout reflects current naming.) Migration callouts have been added to every file from which an F body was sourced: the legacy F headings in `1-framework/`, the F-source headings in `2-architecture/constraints.md`, the `^t2-data-format-criteria` heading in `2-architecture/data-formats.md`, the `^t3-discharge-accounting` heading in `3-aspect-specific/arguments-reasoning.md`, and four backup files — `_backup/criteria-framework.md` (per-row inline pointers in the Core-requirements table plus a Quality-constraints callout), `_backup/object-types-ontology/criteria-taxonomy-ontology.md` for `^t1-function-driven-typology`, `_backup/registries-indexes.md` for `^t1-staleness-gating`, and `_backup/tooling-validation.md` for `^t1-validation-externality` and `^t1-canonical-terminology` (pass-5 rename of `^t1-terminology-canonicity`). Inbound R-redirects from legacy anchors are deferred to Step C.

Pass-2 audit fixes (per first adversarial review): added `^t2-revision-semantics` section (initially omitted); added a backing classification row for `^t1-human-read-cost` at line 281 of the classification table (previously listed only as a redirect target without a creation cell); replaced fabricated dependency edges (layer-replaceability under no-circular-reasoning; non-redundancy under terminology-canonicity; the addressability/queryability/automation cluster under staleness-gating; ontology-smallness under human-read-cost) with the edges actually recorded in the classification table; converted static-path links to anchor form; rewrote the no-silent-incompleteness criterion sentence to remove a process-noun subject.

Pass-3 audit fixes (per second adversarial review): moved the "move coverage" downstream edge from `^t1-reasoning-types-coverage` to `^t1-research-faithfulness` (where the classification-table line 149 actually records it); softened the "dependent-flagging feeds staleness-gating" claim under `^t2-revision-semantics` to acknowledge the table records no direct edge; dropped the "references resolve to the current state … not to a snapshot" clause from `^t1-addressability` (drift imported from `^t1-git-delegation`); replaced the `^t1-human-read-cost` downstream section with the recorded cost-axis-grid relationship to `^t1-system-scale`; converted the `_backup/criteria-framework.md` core-requirements table into one heading-per-row subsection so each sourced row carries a literal adjacent `> [!INFO] Migrated to ...` callout; fixed remaining link issues (folder-link to plain text, missing anchor on relations-graph, dropped misleading line-number references); rewrote one passive construction in `^t1-validation-externality`.

Pass-4 substantive rewrites (per user-led editorial review): renamed section "Reasoning quality" → "Reasoning integrity"; renamed `^t2-revision-semantics` → `^t1-revision-accountability` and rewrote its body around dependency tracking + correction propagation (in place of the descriptive "represents how revisions happen" framing); retitled `^t1-mixed-monotonicity` to "Composition of warrant kinds" (anchor preserved) and rewrote its body around warrant-kind boundaries; rewrote `^t1-goal-driven-reasoning` around analytical decomposition into a coherent question-network with success and admissibility conditions (in place of the topical "goal-oriented" framing) and reparented it under `^t1-reasoning-understandability` as the per-step specialisation of the strategic level; restored the full Reasoning-understandability table (Level / Question answered / Determined by / Examples) and added the framework's commitment to the three-level decomposition as a separate paragraph; rewrote `^t1-validation-externality` to drop the agent-specific framing in favour of "process distinct from authoring"; broadened `^t1-non-redundancy` from "interpretive point" to all content kinds; made the dual relationship between `^t1-no-circular-reasoning` and `^t1-no-silent-incompleteness` explicit; replaced "regime/regimes" terminology with "warrant kinds" (where it concerns warrant kinds) or "reasoning kinds" (where it concerns broader reasoning classifications); propagated all renames into the classification table (rows for revision-semantics, x4 tension, revision-feedback, defeasibility) and into the migration callouts in `2-architecture/constraints.md`. The original `^step-a3-themes` enumeration in the handoff retains the pass-1 names as a protocol-record audit trail; the Status callout above reflects current naming.

Pass-5 group restructure and criterion changes (per user-led editorial review): restructured the eight groups into six — *Adequacy and Expressivity* split into *Framework foundation* (the meta-commitments about what the framework *is*) and *Expressive depth* (what the framework must capture, support, and admit, with what range and at what depth); *Operationality* dissolved (its three criteria moved to *Expressive depth*); *Understanding and Manipulability* merged into *Reasoning integrity*; *Workflow integrity* and *Separation of research activities* merged into *Research activities and workflows*. Added a new criterion `^t1-typed-object-decomposition` in *Framework foundation* (downstream of `^t1-inquiry-content-and-progression`): the framework decomposes inquiry content into typed objects of distinct kinds; the criterion does not prescribe how inferential progression is recorded. Retired `^t1-representation-vs-generation` entirely: pass-5 audit found that the "modes" framing conflated three axes already covered precisely by `^t1-partial-formalization` (maturity), `^t1-activity-coverage` and `^t1-activity-separation` (activity-kind), and `^t1-inquiry-content-and-progression` (static/dynamic dimension). The architectural decision `^t2-representation-vs-generation` (in `operations-and-modes.md`) is reframed as the chosen response to the three sibling T1 criteria. Moved `^t1-stable-boundaries` from *Reasoning integrity* to *Framework foundation* (where it joins `^t1-inquiry-content-and-progression` and `^t1-typed-object-decomposition` as the three foundational meta-commitments). Moved `^t1-function-driven-typology` from *Operationality* to *Expressive depth*. Moved `^t1-concrete-execution` and `^t1-no-infinite-regress` from *Operationality* to *Expressive depth*. Moved `^t1-reasoning-understandability`, `^t1-goal-driven-reasoning`, `^t1-cognitive-manipulability` from *Understanding and Manipulability* into the merged *Reasoning integrity*. Renamed *Workflow integrity* + *Separation of research activities* to *Research activities and workflows* with `^t1-activity-separation`, `^t1-staleness-gating`, `^t1-validation-externality`. The Themes-table descriptions follow the discipline that they describe each section's unifying purpose, not enumerate its members. Propagated all changes into the classification table (rows 72, 111, 355, 360, 595) and into the `^t2-repr-vs-gen` migration callout in `2-architecture/constraints.md`. The cleanup-handoff brief (`_handoff-cleanup.md`) is updated in the same pass to reflect the post-refactoring state for the successor agent.

The protocol below is preserved for reference; do not redo unless the user explicitly asks for a re-extraction.

Create `vendor/gnomon/docs/design/_framework-criteria.md` containing every framework-level criterion from the classification table. The new file becomes the canonical reference for framework-level desiderata, replacing the scattered `1-framework/` thematic files.

#### F-extraction protocol ^step-a3-extraction

For each row in the classification table, extract an F entry if and only if the row's *Final state* cell contains at least one of the following bullet patterns:

- `**F**` — the row stays as F at its current anchor (with possible body sharpening).
- `**F (T1, kept)**` — the headline F survives at the original anchor, often with a rename target.
- `**F (T1, new)**` — a new F is minted at T1 (the bullet names the new anchor).
- `**F (T1)**` — promotion from T2 or backup to T1.
- `**F + D**` — hybrid notation in some justification cells; extract only the F prong.

Do **not** extract:

- Rows whose only F mention is a redirect target (e.g., a downstream row's `R against ^t1-X`).
- Rows reclassified to **R** in pass 9 from earlier F-tagged states (e.g., `^t2-closed-operational-core` whose F bullet was demoted to R against `^t1-no-infinite-regress`).
- The `**Failure-mode rule.**` heading text in the classification coherence rules (false positive on the literal regex `**F`).

For each extracted F:

1. **Anchor name**: use the rename target when the bullet specifies one (e.g., `rename target: ^t1-research-faithfulness` → use `^t1-research-faithfulness`); otherwise use the source anchor.
2. **Headline**: lift from the bullet's quoted body, not from the source-file heading. Body-sharpening clauses in the bullet (e.g., "*sharpened body restricted to which reasoning types the framework admits*") override the legacy source.
3. **Body**: import and reformulate the relevant content from the relevant source file, applying each body-refinement directive recorded in the classification bullet (trim, sharpen, rephrase). When the F was minted from a backup file or split off from another F, write a fresh body grounded in the source paragraph cited by the classification row's *Justification* cell.
4. **Justification structure** per F section: state the criterion, the motivating failure mode, the upstream dependencies (cite the dependency edges from the classification's Justification cells), and the downstream decisions the criterion justifies (cite the rows whose Final-state contains `Consequence of ^t1-X` or similar).

#### Thematic groups ^step-a3-themes

Group F entries by **conceptual theme**, not by legacy file. The eight groups below cover all the 27 target Fs in the classification table:

- **Adequacy and Expressivity** — `^t1-research-faithfulness` (rename of `^t1-epistemic-adequacy`), `^t1-reasoning-types-coverage` (rename of `^t1-expressivity`), , `^t1-rich-prose-expressivity`, `^t1-partial-formalization`.
- **Reasoning quality** —  `^t1-no-circular-reasoning`, `^t1-no-silent-incompleteness`, `^t1-mixed-monotonicity`.
- **Understanding and Manipulability** — `^t1-goal-driven-reasoning` (rename of `^t1-non-arbitrary`), `^t1-reasoning-understandability` (rename of `^t1-intelligibility`), `^t1-cognitive-manipulability`.
- **Operationality** — `^t1-concrete-execution`, `^t1-no-infinite-regress`, `^t1-function-driven-typology`.
- **Modularity and Separation of concerns** —  `^t1-activity-separation`, `^t1-representation-vs-generation`, `^t1-reuse`, `^t1-addressability`, `^t1-relational-queryability`, `^t1-non-redundancy`, `^t1-terminology-canonicity` (non-redundancy at the prose grain).
- **Cost and Ergonomics** — `^t1-human-read-cost`, `^t1-human-action-cost`, `^t1-read-side-automation`, `^t1-write-side-automation`, `^t1-system-scale` (rename of `^t1-feasibility`).
- **Workflow integrity** — `^t1-staleness-gating`, `^t1-validation-externality`. These two F's constrain the *workflow* (when activity is gated, who validates) rather than the content / reasoning / cost axes; they group together because both arose from hidden-F mechanism rows that the pass-9 audit promoted.

If the F-extraction protocol surfaces an F that does not fit any of the eight groups, mint a new group with a one-sentence justification rather than forcing it into an existing one.

#### Dependency-ordering protocol ^step-a3-ordering

Within each group, order F entries by dependency: foundational F's first, derived F's last. Build the dependency graph mechanically by scanning the classification table for each F row and recording the edges named in its *Justification* cell:

- **Consequence-of edges**: `Consequence of ^X` (e.g., `^t2-ontology-small`'s justification "Consequence of `^t1-human-action-cost` and `^t1-feasibility`" produces edges from those F's into the A; F-to-F instances appear directly in T1 justification cells).
- **Balanced-against edges**: `Balanced against ^Y per ^t2-xN` (records a tension; treat the F's as siblings in the order, with the tension entry itself as a footnote).
- **Justifies-downstream edges**: when a row says "Justifies `^t3-X`", `^t3-X` is downstream and does not affect the F-ordering directly.
- **Cross-group edges**: when an F in group A depends on an F in group B, place group A after group B in the file's section order.

Use the suggested top-level section order, except if you detect massive cross-group edges that require another order. For instance, here are some dependencies (use as starter; verify by reading the classification cells):

- `^t1-no-circular-reasoning` and `^t1-no-silent-incompleteness` are sub-decisions of `^t1-research-faithfulness`.
- *Workflow integrity* depends on every other group (they constrain how the framework is used at run-time).

#### Active-tier disposition during Step A.3 ^step-a3-disposition

Step A.3 only creates the new file; it does not delete the legacy source files (e.g. `1-framework/` files, decision files, backup files), that will be redirected during Step C (when inbound references update). Step A.3 should:

- Leave the legacy source files in place.
- For every F whose body was imported into `_framework-criteria.md`, add a one-line `> [!INFO] Migrated to [framework-criteria](_framework-criteria#^t1-X)` callout in **every file the body was sourced from**, including:
  - active-tier source files (`1-framework/` headings, T2 theme-file headings under `2-architecture/`, T3 theme-file headings under `3-aspect-specific/`),
  - backup files under `_backup/` whose paragraphs the F body was imported from (these include the rows the classification table tags as `BK/...`, e.g. `^t1-no-infinite-regress` and `^t1-cognitive-manipulability` from `_backup/criteria-framework.md`).

  Place the callout adjacent to the source paragraph (under the relevant heading or alongside the relevant table row). Backup files remain in place as historical reference per Step C policy; the callout is purely a forward pointer for readers.

- Do not yet R-redirect the legacy anchors. Step C's per-tag batches handle redirect sweeps.

The legacy files are retired wholesale during Step D (theme reorganization), not during Step A.3.

#### Acceptance criterion ^step-a3-acceptance

Step A.3 is complete when:

1. **Coverage**: every F bullet in the classification table appears as a section in `_framework-criteria.md`. Run `grep -oE "\\\\*\\\\*F[^*]*\\\\*\\\\*" _classification-table.md | sort | uniq -c` against the new file's section anchors to confirm a one-to-one match (modulo retracted F's recorded as such in the table).
2. **Section content**: every F section names the failure mode the criterion prevents, the upstream dependencies (with anchor links), and at least one downstream consequence (a D, an A, a tension, or a derived F).
3. **Ordering**: within each group, no F is placed before an F it depends on (per the dependency-ordering protocol).
4. **Cross-group ordering**: no group precedes a group that it strongly depends on.
5. **Migration callouts**: every legacy F source file carries `> [!INFO] Migrated to ...` callouts pointing to the new home.
6. **Writing constraints**: the new file complies with the [writing constraints](#^writing-constraints) — no verbatim duplication, anchor-and-label convention applied, no static cross-links, no unmotivated nominalizations, active voice in prose bodies. The constraints that this section explicitly inherits (otherwise nominally bound only to Steps C and D) are: rule 1 (no duplication), rule 2 (anchor convention), rule 4 (tone and style).

#### Hard prerequisite

Step A.3 has a hard prerequisite on Step A.2 being complete (the F set is not stable until backup decisions are classified). That prerequisite is met. Step A.3 has *no* hard prerequisite on Step B or Step C; the migration table and the per-tag batches operate downstream of `_framework-criteria.md`.

---

### Step B — Migration Table ^step-b

Create `vendor/gnomon/docs/design/_migration-table.md` with one row per *Final state* bullet:

| Entry | Initial path | Initial anchor | New path | New anchor | Action |
| --- | --- | --- | --- | --- | --- |
| Human-readable label | Existing source path, if any | Existing anchor, if any | Target path, if any | Target anchor, if any | Keep / move / copy / create / promote / split / fold / repair / rename / remove |

Rules:

- Empty initial fields mean the classification creates a new entry.
- Empty new fields mean the entry is removed or repaired in place.
- Multi-bullet classification rows produce multiple migration rows.
- Rename targets and final anchors come from the classification table.

---

### Step C — Migration Policy ^step-c

Use the classification table's *Final state* bullets as the migration source of truth.

| Tag | Migration action |
| --- | --- |
| **R** | Active entries are removed and inbound references redirect to the named upstream anchor. Backup R rows do not migrate; backups stay as historical references. |
| **Id** | Remove. Surface orphaned references for manual triage. |
| **If** | Remove the standalone entry and fold useful rationale into the named host. |
| **Ir** | Repair in place unless the bullet names a rename or move. |
| **D** | Keep, move, copy, or create the decision at the target named in the bullet. |
| **F** | Keep or promote/create at T1; all F entries belong in `_framework-criteria.md` after Step A.3. |
| **A** | Keep or create as a theme-local criterion in a T2 theme file. |
| **P** | Fold into the host decision named in the bullet. |
| **G** | Replace the narrow entry with the broader anchor named in the bullet. |
| **T** | Keep as cross-criterion metadata. |

Batch order: `Ir → If / Id → R → G → F → A → D → P`.

After each batch, run a cross-reference sweep and update inbound links according to the migration table.

---

### Step D — Theme Layout ^step-d

After Step C, reorganize the design folder by theme rather than by tier. Each theme file should use this structure:

```markdown
## Criteria

### Human-readable label ^anchor

## Decisions

### Human-readable label ^anchor

> [!QUESTION] Design question?

## Open questions

### Human-readable label ^anchor

> [!QUESTION] Open design question?
```

Theme order should follow dependency:

1. Foundational architecture: layering and functional strata.
2. Vocabularies and representations: object kinds, relations, reasoning structure, warrant, revision, status, operation schemas, reasoning fields.
3. Navigation and queries: registries, indexes, dependency graph, build outputs.
4. Derived exposition artifacts: rendering, views, identifiers, versioning, scope, relevance, data formats.
5. Operational usage: validation, workflows, and revision.

---

## Critical Writing Constraints ^writing-constraints

These rules govern every edit during Step C and Step D.

### 1. No verbatim duplication, no mere reformulation

Every paragraph must introduce a genuinely new idea. Restating an idea in different words, structure, or emphasis is forbidden. When a recall is needed, replace it with a lightweight cross-reference: one anchor link plus one short clause.

Honor this rule everywhere: callouts, tables, summaries, indexes, prose. In `[!important]`, `[!seealso]`, `[!missing]` callouts and cross-coupling map entries, link by anchor and name what relates; do not duplicate substance recorded at the source.

### 2. Anchor-and-label convention and cross-references

Every anchored heading takes the form `### Human-readable label ^anchor-slug`. Never use `### ^anchor-slug` alone.

Markdown linter false positive: **MD051 link-fragments** on `#^anchor-name` can be ignored because the linter does not recognize Obsidian block anchors.

Cross-links must be dynamic links, not static paths. Link text describes the target's role rather than displaying a path.

### 3. Decision and open-question sections start with `> [!QUESTION]`

The callout names the design question the section answers or leaves open.

### 4. Tone and writing style

Use active voice. Prefer verbs and direct formulations. Remove abstract nominalizations and complex noun phrases. Replace compound words in prose bodies with short phrases when doing so improves clarity.

Focus style cleanup on prose bodies, callouts, bullets, table cells, and index descriptions. Headings may keep compact technical labels when anchors and navigation depend on them. Expand new inline `(a)/(b)/(c)` and `(1)/(2)/(3)` enumerations into bullet lists.

### 5. Interaction discipline

- When the user proposes a resolution, assess it against existing constraints and flag tensions before applying.
- Surface tradeoffs and constraints; do not pre-decide alternatives unless the classification already resolves them.
- When the task is substantial or complex, proceed incrementally.
- Do not spend attention on cosmetic Markdown formatting issues that do not prevent parsing. Fix true parsing errors: broken pipe counts, missing rows, malformed cells, broken links, missing anchors, and missing question callouts.

### Opportunistic cleanup

If you encounter any of the following while editing active tier files, apply the specified resolution:

- **Duplicate paragraph or paraphrase across files**: replace the duplicate with a cross-reference to the source.
- **Abstract nominalization or compound phrase**: rewrite with active voice and shorter phrasing when clarity improves.
- **Static cross-link or path-like link text**: rewrite the link text so it names the target's role.
- **Link to an inactive proposal**: point to [backup proposals](_backup) or the specific backup file.
- **New `(a)/(b)/(c)` or `(1)/(2)/(3)` enumeration**: expand to a bullet list.
- **Broken link**: fix the target or replace it with a cross-reference to the source.
- **Heading without an anchor** in any Tier-2 or Tier-3 file: add an anchor following the `### Label ^t<n>-anchor-slug` pattern.
- **Decision or open-question section without a `[!QUESTION]` callout**: add the callout.
