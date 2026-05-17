# Refactor handoff — design folder

This handoff owns the Step A-D refactor state. It does not repeat the project brief in [_handoff](_handoff) or the Step A.4 file-by-file mechanics in [_handoff-cleanup](_handoff-cleanup).

---

## Status

- **Step A.1 complete.** `_classification-table.md` records active criteria and decisions.
- **Step A.2 complete.** Selected backup decisions are integrated into the classification ledger.
- **Step A.3 complete, and superseded by a Tier-1 theme split.** Step A.3 produced the single file `_framework-criteria.md`. That file has since been **split into six per-theme files under `1-framework/`** — `framework-foundations.md`, `expressive-depth.md`, `reasoning-integrity.md`, `modular-content-organization.md`, `research-activities-workflows.md`, `cost-ergonomics.md`, indexed by `1-framework/_index.md`. `_framework-criteria.md` no longer exists. The canonical Tier-1 criteria are these theme files. (An earlier seventh file, `external-interfaces.md`, was later folded into `framework-foundations.md` — its two criteria are scope-circumscription commitments.)
- **Step A.4 in progress.** The `1-framework/` portion is done — the four legacy stub files were deleted and their inbound links redirected. Files 5–11 (Tier-2/3 and backup sources) remain. Use [_handoff-cleanup](_handoff-cleanup).
- **Step A.5 largely done.** The post-A.3 restructures are reconciled into `_classification-table.md`; what remains is the class-count re-tally, rows for seven post-A.3 tier-file anchors, fleeting-candidate provisional rows, the Step-D disposition record, and the relation-reification decision (see Step A.5 scope).
- **Step B blocked.** `_migration-table.md` is only a header; Step A.5's residue should settle first.
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

**Largely done.** The post-A.3 restructures were already reconciled into the classification table: the Reasoning-integrity restructure (five retired `^t1-` anchors → `^t1-justification-levels` and its five per-level criteria), the `arguments-reasoning.md` machinery rebuild (17 legacy `^t3-` criterion rows retired → `^t3-d-` machinery rows), the `1-framework/` theme split (Tier-1 records repointed to per-theme files), the `^t1-activity-separation` → `^t1-activity-access-rights` rename, and the Functional-separation merge (`^t1-stable-boundaries` + `^t1-function-driven-typology` → `^t1-functional-separation` in `framework-foundations.md`). Every retired anchor now appears only as a historical-record mention; no live row targets one.

**What remains:**

- **Re-tally the numeric class counts.** The Summary-by-class table carries a `[!WARNING]`: its counts (R, D, F, A, …) predate the restructures and are stale. The prose notes are current; only the numbers need a recount. This can fold into Step B, which re-reads every row anyway.
- **Add rows for the post-A.3 tier-file anchors** not yet in the table: `^t3-epistemic-gap-subtypes`, `^t3-concept-type-taxonomy`, `^t3-definition-normal-form`, `^t3-reasoning-schemes`, `^t3-attack-target`, `^t3-undischarged-commitments`, `^t2-interpretive-hazard-lint`. (The `^t3-d-` machinery rows are already in the table; these seven tier-file open-question anchors are not.)
- **Add provisional rows for unresolved candidates** in `_fleeting-ideas.md` under `## Candidates`. None exist in the table yet. Exclude `## Principled rejections`, `## Triage log`, explanatory preambles, and already-propagated references that merely point to an active tier anchor. These rows mark staged candidates only; they do not produce Step-B migration rows unless a candidate has become a real decision.
- **Record the Step-D disposition** for `_fleeting-ideas.md` and `_worked-examples.md`. Current assumption: both stay outside the theme reorganization as staging and reference files.
- **Decide the relation-reification issue** raised at `^t1-typed-object-decomposition`: whether it needs a new Tier-2 open-question anchor in `2-architecture/relations-graph.md` or stays a known gap.

Step A.5 is complete when every active Tier-2/Tier-3 anchor and every staged candidate either appears in `_classification-table.md` or is explicitly marked outside refactor scope, the table reflects the current Tier-1 labels and theme placements, and the class counts are re-tallied.

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
