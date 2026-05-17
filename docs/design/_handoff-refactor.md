# Refactor handoff — design folder

This handoff owns the Step A-D refactor state. It does not repeat the project brief in [_handoff](_handoff) or the Step A.4 file-by-file mechanics in [_handoff-cleanup](_handoff-cleanup).

---

## Status

- **Step A.1 complete.** `_classification-table.md` records active criteria and decisions.
- **Step A.2 complete.** Selected backup decisions are integrated into the classification ledger.
- **Step A.3 complete, and superseded by a Tier-1 theme split.** Step A.3 produced the single file `_framework-criteria.md`. That file has since been **split into seven per-theme files under `1-framework/`** — `framework-foundations.md`, `expressive-depth.md`, `reasoning-integrity.md`, `modular-content-organization.md`, `research-activities-workflows.md`, `cost-ergonomics.md`, and the retained `external-interfaces.md`, indexed by `1-framework/_index.md`. `_framework-criteria.md` no longer exists. The canonical Tier-1 criteria are these theme files.
- **Step A.4 in progress.** The `1-framework/` portion is done — the four legacy stub files were deleted and their inbound links redirected. Files 5–11 (Tier-2/3 and backup sources) remain. Use [_handoff-cleanup](_handoff-cleanup).
- **Step A.5 pending.** Classification catch-up must run after Step A.4 and before Step B.
- **Step B blocked.** `_migration-table.md` is only a header until Step A.5 updates the ledger.
- **Step C blocked on Step B.**
- **Step D blocked on Step C — and partly already done for Tier 1.** The `1-framework/` folder is already reorganised by theme (see Step D).

The design folder still uses the tier layout for Tier 2 and Tier 3. Do not reorganize those folders until Step D.

---

## Step A.4 boundary

Step A.4 only removes duplicate Tier-1 source bodies that have already moved into a canonical criterion in its `1-framework/` theme file. It does not migrate Tier-2 or Tier-3 decisions, does not redirect references, and does not retire files wholesale except where the cleanup handoff says a file becomes a stub.

The cleanup must preserve anchors so inbound links keep resolving until Step C — except where the cleanup handoff records that a file's redirect sweep was already brought forward (the four deleted `1-framework/` stubs).

---

## Step A.5 scope ^step-a5

Step A.5 brings `_classification-table.md` current after Step A.4. It is authored classification work, not a mechanical extraction, so it belongs before Step B.

Required updates:

- Add rows for the post-A.3 tier-file anchors:
  - `^t3-epistemic-gap-subtypes`
  - `^t3-concept-type-taxonomy`
  - `^t3-definition-normal-form`
  - `^t3-reasoning-schemes`
  - `^t3-attack-target`
  - `^t3-undischarged-commitments`
  - `^t2-interpretive-hazard-lint`
- **`arguments-reasoning.md` Criteria section rebuilt as machinery decisions.** The file's entire `## Criteria` section — the eight legacy criteria *and* the nine cross-field-audit criteria added later — was removed and replaced by a machinery section: per-facet design questions about *how* each Tier-1 reasoning-integrity facet is implemented. Two are **decisions** (`^t3-d-warrant-completeness`, `^t3-d-cycle-detection`); the rest are **open questions** (`^t3-d-warrant-adequacy`, `^t3-d-warrant-generality`, `^t3-d-warrant-boundary`, `^t3-d-commitment-calibration`, `^t3-d-defeater-record`, `^t3-d-limitation-disclosure`, `^t3-d-gap-tree-check`, `^t3-d-gap-decomposition`, `^t3-d-rationale-record`, `^t3-d-idle-unit-detection`, `^t3-d-directness-measure`, `^t3-d-conceptual-effect`, `^t3-d-dependence-network`, `^t3-d-explanatory-depth`, `^t3-d-unification`, `^t3-d-strategic-hierarchy`, `^t3-d-pattern-transfer`, `^t3-d-weak-point-surfacing`, `^t3-d-comparison-analogy`, `^t3-d-worked-example`, `^t3-d-misconception`), plus the kept open question `^t3-assumption-discharge-mechanism`. The classification table must:
  - **retire the 17 old `^t3-` criterion rows** — eight legacy (`^t3-warrant-transparency`, `^t3-motivational-non-triviality`, `^t3-teleological-coherence`, `^t3-no-unsupported-derived-claim`, `^t3-no-opaque-transformation`, `^t3-no-hidden-branch-choice`, `^t3-discharge-accounting`, `^t3-snapshot-dag-acyclicity`) and nine cross-field-audit (`^t3-justification-adequacy`, `^t3-local-necessity`, `^t3-directness`, `^t3-defeater-treatment`, `^t3-dependence-network`, `^t3-explanatory-depth`, `^t3-unification`, `^t3-hierarchical-organisation`, `^t3-transferable-pattern`, plus `^t3-commitment-calibration`, `^t3-acknowledged-limitations`, `^t3-concrete-illustration`, `^t3-misconception-diagnosis`);
  - **add rows for the new `^t3-d-` machinery entries**, tagged **D** (decision or open question), theme home *arguments and reasoning*; they migrate with `arguments-reasoning.md` in Step D;
  - re-point classification-table rows that named a retired `^t3-` criterion as a redirect target — rows 202–209 (the mint rows for the eight legacy criteria), 284/287/288 (validation-rule redirects), 400–403 (explanatory-adequacy redirects), 768–772 (count rows). The audit source for the machinery questions is `vendor/gnomon/docs/references-methods/principles-reasoning-argumentation-cross-field.md`.
- Add provisional rows for unresolved candidates in `_fleeting-ideas.md` under `## Candidates`. Exclude `## Principled rejections`, `## Triage log`, explanatory preambles, and already-propagated references that merely point to an active tier anchor. These rows mark staged candidates only; they do not produce Step-B migration rows unless a candidate has become a real decision.
- Record the Step-D disposition for `_fleeting-ideas.md` and `_worked-examples.md`. Current assumption: both stay outside the theme reorganization as staging and reference files.
- Bring the classification table's Tier-1 records in line with the `1-framework/` theme split. Each Tier-1 criterion now lives in a named theme file; the table must record the theme placement and the current anchors:
  - `^t1-revision-accountability` is in `research-activities-workflows.md`.
  - `^t1-justification-levels` is in `reasoning-integrity.md` and uses five levels: Licensing, Teleological, Strategic, Explanatory, Manipulability. (Anchor was `^t1-recoverable-reasoning` before the split; the rename to `^t1-justification-levels` is propagated across the corpus.)
  - `^t1-activity-separation` was renamed to `^t1-activity-access-rights` (anchor and label both changed) and lives in `research-activities-workflows.md`; the inbound-reference sweep is done. The classification-table rows that named the old anchor (`^t2-separation-of-concerns` mint, `^t1-modularity` audience-stability redirect, "Audience-independent stability", `^t2-repr-vs-gen`, the registry and projection rows) now read `^t1-activity-access-rights`.
  - `^t1-single-source-of-truth` is a Tier-1 criterion in `research-activities-workflows.md` and needs its own row.
- **Reasoning-integrity restructure — five retired anchors, five new criteria.** The *Reasoning integrity* theme was restructured to one general T1 criterion per justification level. Five `^t1-` anchors are **retired**: `^t1-no-circular-reasoning`, `^t1-no-silent-incompleteness`, `^t1-mixed-monotonicity`, `^t1-goal-driven-reasoning`, `^t1-cognitive-manipulability`. Five new general per-level criteria **replace** them: `^t1-valid-licensing` (Licensing — absorbs the three retired licensing anchors as its three facets: no circular reasoning, no silent incompleteness, sound warrant composition), `^t1-served-goal` (Teleological), `^t1-apt-strategy` (Strategic), `^t1-explanatory-gain` (Explanatory — newly dedicated; previously the level had no criterion), `^t1-manipulable-reasoning` (Manipulability). The classification table must:
  - retire the five old anchors' rows and add rows for the five new criteria (all **F**, theme *Reasoning integrity*);
  - re-point every classification-table row that named a retired anchor as a redirect/migration target — notably the kept-F rows `^t1-non-arbitrary → ^t1-goal-driven-reasoning` (now → `^t1-served-goal` + `^t1-apt-strategy`) and the `^t1-cognitive-manipulability` BK-F row (now → `^t1-manipulable-reasoning`), plus the `^t2-snapshot-dag` / `^t2-defeasibility` migration targets (now → `^t1-valid-licensing`);
  - the Tier-2 implementation decisions (`^t2-snapshot-dag`, `^t2-defeasibility`, `^t2-multi-regime-reasoning`) are unchanged — they remain technical machinery realising the `^t1-valid-licensing` facets. The Tier-3 machinery is now the `^t3-d-` decisions and open questions in `arguments-reasoning.md` (see the bullet above): `^t3-snapshot-dag-acyclicity` was rebuilt as `^t3-d-cycle-detection`, and `^t3-discharge-accounting` as the open question `^t3-assumption-discharge-mechanism`. Inbound references in `_framework-criteria.md`, `constraints.md`, `arguments-reasoning.md`, `content-adequacy.md`, `_backup/criteria-framework.md`, `_fleeting-ideas.md`, and `_worked-examples.md` were re-pointed when the restructures were applied.
- Decide whether the relation-reification issue raised at `^t1-typed-object-decomposition` needs a new Tier-2 open-question anchor in `2-architecture/relations-graph.md` or should remain a known gap.

Step A.5 is complete when every active Tier-2/Tier-3 anchor and every staged candidate either appears in `_classification-table.md` or is explicitly marked outside refactor scope, and the table reflects the current Tier-1 labels and theme placements.

---

## Step B

Build `_migration-table.md` from `_classification-table.md`, one row per final-state bullet that describes migratable content.

Required columns:

| Entry | Initial path | Initial anchor | New path | New anchor | Action |
| --- | --- | --- | --- | --- | --- |

Extraction rules:

- Empty initial fields mean the classification creates a new entry.
- Empty new fields mean the entry is removed or repaired in place.
- Multi-bullet classification rows produce multiple migration rows.
- Rename targets and final anchors come from the classification table.
- Provisional staged-candidate rows from Step A.5 are not extracted unless the table promotes them to real decisions.

---

## Step C

Use the migration table as the redirect source of truth. Run batches in this order:

```text
Ir -> If / Id -> R -> G -> F -> A -> D -> P
```

Batch meanings:

| Tag | Action |
| --- | --- |
| `Ir` | Repair in place unless the row names a move or rename. |
| `If` | Fold useful rationale into the named host, then remove the standalone entry. |
| `Id` | Remove and surface orphaned references. |
| `R` | Redirect inbound references to the named upstream anchor; backup rows stay historical. |
| `G` | Replace a narrow entry with the broader named anchor. |
| `F` | Keep or create a Tier-1 criterion in its `1-framework/` theme file. |
| `A` | Keep or create a theme-local criterion. |
| `D` | Keep, move, copy, or create a decision or open question. |
| `P` | Fold into the named host decision. |
| `T` | Keep as cross-criterion metadata. |

After each batch, sweep inbound links and repair broken anchors before starting the next batch.

---

## Step D

After Step C, reorganize the design folder by theme. **Tier 1 is already done** — the `1-framework/` folder holds one file per theme. Step D therefore applies to **Tier 2 and Tier 3** (the `2-architecture/` and `3-aspect-specific/` folders), bringing them into the same per-theme layout. The target theme files use this structure:

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

## Refactor editing rules

- Every anchored heading has the form `### Human-readable label ^anchor-slug`.
- Decision and open-question sections start with a `[!QUESTION]` callout.
- Static path-like links should become role-naming links to block anchors.
- Duplicate substance should become a cross-reference to the owning source.
- Cosmetic Markdown warnings are secondary. Fix true parsing errors, broken links, missing anchors, malformed table rows, and missing question callouts.
