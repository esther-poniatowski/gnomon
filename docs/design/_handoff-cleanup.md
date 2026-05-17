# Source-file cleanup handoff — Step A.4

This handoff owns only Step A.4: removing source bodies whose Tier-1 content has already moved into the canonical framework criteria. For the broader refactor sequence, use [_handoff-refactor](_handoff-refactor).

> [!IMPORTANT] The canonical Tier-1 criteria are now the `1-framework/` theme files
> The single file `_framework-criteria.md` no longer exists. Its criteria were split into seven per-theme files under `1-framework/` — `framework-foundations.md`, `expressive-depth.md`, `reasoning-integrity.md`, `modular-content-organization.md`, `research-activities-workflows.md`, `cost-ergonomics.md`, and the retained `external-interfaces.md` — indexed by `1-framework/_index.md`. Wherever this handoff says "the target criterion", it means the criterion in its `1-framework/` theme file. The cleanup-target table below already names the new theme-file anchors.

---

## Status

- **The `1-framework/` portion of Step A.4 is complete.** The four migration-stub files — `content-adequacy.md`, `epistemic-adequacy.md`, `operational-quality.md`, `structural-quality.md` — have been deleted. Their criterion bodies were already migrated; the stubs were removed and every inbound link across the Tier-2/Tier-3 theme files re-pointed to the new `1-framework/` theme-file anchor (Step C's redirect sweep was brought forward for these files). `external-interfaces.md` is **retained** — its two criteria (`^t1-git-delegation`, `^t1-no-runtime-inference`) have full bodies and were never migrated.
- **Files 5–11 (Tier-2/3 and backup sources) remain pending.** Their migrated bodies still sit under `[!INFO] Migrated to ...` callouts and must be removed; the callouts already point to the correct `1-framework/` theme-file anchors.
- `_classification-table.md` still contains prose mentions of the deleted `1-framework/` file paths (mint rows, count rows); reconciling those is Step A.5 ledger work.

---

## Cleanup rule

A heading is cleanup-eligible only when its Tier-1 content is already integrated into the canonical criterion in its `1-framework/` theme file.

For each cleanup-eligible heading:

- Keep the heading and anchor.
- Replace migrated prose with one `[!INFO] Migrated to ...` callout.
- Delete migrated prose only after comparing it against the current target criterion.
- Preserve content that belongs to a Tier-2 or Tier-3 decision.
- Do not add redirects, move files, or reorganize sections during Step A.4.

When source content is not clearly covered by the target criterion, stop and ask the user to choose one route:

- migrate the content into the relevant `1-framework/` theme file;
- move it to a backup or staging location for later Tier-2/Tier-3 work;
- discard it with explicit approval.

Never delete substantive unintegrated content without that approval.

---

## Workflow per file

1. Read the whole source file.
2. Read each target criterion in its `1-framework/` theme file (the cleanup-target table names the file and anchor).
3. Compare every source paragraph, list, table, example, callout, citation, and cross-reference with the target criterion.
4. Report covered content and flagged content to the user.
5. Apply only approved deletions or migrations.
6. Verify that the source anchor still resolves and that no stale migrated body remains under the cleaned heading.
7. Stop after one file and wait for the next instruction.

---

## Cleanup targets

The four legacy `1-framework/` stub files — `content-adequacy.md`, `epistemic-adequacy.md`, `operational-quality.md`, `structural-quality.md` — were deleted and their inbound links redirected (see Status); those rows are **done** and dropped from this table. The remaining targets:

| File | Cleanup-eligible source | Target or disposition |
| --- | --- | --- |
| `2-architecture/constraints.md` | `^t2-separation-of-concerns` | `^t1-activity-access-rights` in `research-activities-workflows.md` |
| `2-architecture/constraints.md` | `^t2-non-redundancy` | `^t1-non-redundancy` in `modular-content-organization.md` |
| `2-architecture/constraints.md` | `^t2-graph-queryability` | `^t1-relational-queryability` in `modular-content-organization.md` |
| `2-architecture/constraints.md` | `^t2-defeasibility` | `^t1-valid-licensing` in `reasoning-integrity.md` — its warrant-composition facet |
| `2-architecture/constraints.md` | `^t2-snapshot-dag` | `^t1-valid-licensing` in `reasoning-integrity.md` — its no-circular-reasoning facet |
| `2-architecture/constraints.md` | `^t2-mechanical-validation` | split across `^t1-read-side-automation` and `^t1-write-side-automation` in `cost-ergonomics.md` |
| `2-architecture/constraints.md` | `^t2-repr-vs-gen` | retired; concerns absorbed by `^t1-partial-formalization` (`expressive-depth.md`), `^t1-activity-coverage` (`expressive-depth.md`), `^t1-activity-access-rights` (`research-activities-workflows.md`), and `^t1-inquiry-content-and-progression` (`framework-foundations.md`) |
| `2-architecture/constraints.md` | `^t2-revision-semantics` | `^t1-revision-accountability` in `research-activities-workflows.md` |
| `2-architecture/data-formats.md` | `^t2-data-format-criteria` | prose, formulas, and math sub-claim to `^t1-rich-prose-expressivity` in `expressive-depth.md`; other sub-claims redirect to existing cost and automation criteria |
| `3-aspect-specific/arguments-reasoning.md` | — (no longer eligible) | The `## Criteria` section, including `^t3-discharge-accounting`, was removed and rebuilt as a machinery-decision section; nothing remains to clean. See the File 7 note. |
| `_backup/criteria-framework.md` | migrated core-requirements rows | target criteria named by each adjacent callout |
| `_backup/criteria-framework.md` | `Quality constraints` operation list | `^t1-manipulable-reasoning` in `reasoning-integrity.md` |
| `_backup/object-types-ontology/taxo-criteria-ontology.md` | functional criterion paragraph | `^t1-function-driven-typology` in `framework-foundations.md` |
| `_backup/registries-indexes.md` | mandatory drafting gate paragraph | `^t1-staleness-gating` in `research-activities-workflows.md` |
| `_backup/tooling-validation.md` | externality and hard-gate sentence | `^t1-validation-externality` in `research-activities-workflows.md` |
| `_backup/tooling-validation.md` | terminology-enforcement row | `^t1-canonical-terminology` in `modular-content-organization.md` |

Anything not listed here is outside Step A.4 unless the user explicitly expands scope.

---

## File-specific warnings

### `2-architecture/constraints.md`

Only the eight listed subsections are eligible. Leave all other constraints, gaps, and tensions intact. Preserve any cross-reference in a callout when the source body points to a downstream decision that still matters.

### `2-architecture/data-formats.md`

Only `^t2-data-format-criteria` is eligible. The rest of the source-language and grammar decisions remain active.

### `3-aspect-specific/arguments-reasoning.md` — no longer in scope

The Step A.4 plan once treated `^t3-discharge-accounting`'s criterion clause as cleanup-eligible. That is now moot: the file's entire `## Criteria` section was removed and rebuilt as a machinery section of decisions and open questions (each implementing a Tier-1 reasoning-integrity facet). The discharge-accounting content survives as the open question `^t3-assumption-discharge-mechanism`. Nothing in this file remains to clean.

### Backup sources

Clean only the passages listed in the target table. Backup passages destined for later Tier-2 or Tier-3 decisions remain as historical source material.

---

## Report format

After each file, report:

- headings cleaned;
- flagged content and the user's decision for each flag;
- content migrated into a `1-framework/` theme file;
- content moved to backup or staging;
- content discarded with explicit approval;
- classification-table rows updated.

Then stop.
