# Source-file cleanup handoff — Step A.4

This handoff owns only Step A.4: removing source bodies whose Tier-1 content has already moved into the canonical framework criteria. For the broader refactor sequence, use the [refactor handoff](_handoff-refactor.md).

> [!IMPORTANT] The canonical Tier-1 criteria are the [framework theme files](1-framework/_index.md)
> Wherever this handoff says "the target criterion", it means the criterion in its [framework theme file](1-framework/_index.md). The cleanup-target table below names the theme file and anchor for each source.

---

## Status

- **The framework-tier and [data formats](2-architecture/data-formats.md) portions of Step A.4 are complete.** The legacy framework stub files were deleted and their inbound links swept; `data-formats.md` had every cleanup-eligible body replaced with a `[!INFO]` callout.
- **The architectural-constraints file, the criteria-framework backup, the tooling-validation backup, and the registries-indexes backup are done and have since been deleted.** Each was reduced to migrated/folded/repaired content, then retired: inbound references were swept to the live anchors (a Step-C action brought forward, with user ratification). The registries-indexes deletion executed a substantial brought-forward Step-C/D sweep, recorded in the [refactor handoff](_handoff-refactor.md)'s brought-forward-work callout.
- **One backup source remains pending.** The remaining file in the target table below needs only the named-passage check — it carries no migrated bodies under `[!INFO]` callouts.

---

## Cleanup rule

A heading is cleanup-eligible only when its Tier-1 content is already integrated into the canonical criterion in its [framework theme file](1-framework/_index.md).

For each cleanup-eligible heading:

- Keep the heading and anchor.
- Replace migrated prose with one `[!INFO] Migrated to ...` callout.
- Delete migrated prose only after comparing it against the current target criterion.
- Preserve content that belongs to a Tier-2 or Tier-3 decision.
- By default, do not add redirects, move files, or reorganize sections during Step A.4 — these belong to later steps. **But the user may explicitly direct such extended actions**, per [Opportunistic scope](_handoff#^opportunistic-scope) in the main handoff: under explicit user direction, the cleanup may redirect references, delete files, create or rename entries and anchors. When it does, it records the [deferred synchronization debt](_handoff#^deferred-synchronization-debt) and surfaces it at the next stopping point.

When source content is not clearly covered by the target criterion, stop and ask the user to choose one route:

- migrate the content into the relevant [framework theme file](1-framework/_index.md);
- move it to a backup or staging location for later Tier-2/Tier-3 work;
- discard it with explicit approval.

Never delete substantive unintegrated content without that approval.

---

## Workflow per file

1. Read the whole source file.
2. Read each target criterion in its theme file (the cleanup-target table names the file and anchor).
3. Compare every source paragraph, list, table, example, callout, citation, and cross-reference with the target criterion.
4. Report covered content and flagged content to the user.
5. Apply only approved deletions or migrations.
6. Verify that the source anchor still resolves and that no stale migrated body remains under the cleaned heading.
7. Stop after one file and wait for the next instruction.

---

## Cleanup targets

The framework-tier stub files, [data formats](2-architecture/data-formats.md), the now-deleted architectural-constraints file, the now-deleted criteria-framework backup, the now-deleted tooling-validation backup, and the now-deleted registries-indexes backup are done (see Status) and dropped from this table. The remaining target is one backup source:

| File                                                                                | Cleanup-eligible source              | Target or disposition                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ontology-criteria backup](_backup/object-types-ontology/taxo-criteria-ontology.md) | functional criterion paragraph       | `^t1-functional-separation` in [framework foundations](1-framework/framework-foundations.md)                                                                                                                                                                                                                                                                                |

This backup file carries no migrated bodies under `[!INFO] Migrated to ...` callouts and may need only the named-passage check. Anything not listed here is outside Step A.4 unless the user explicitly expands scope.

---

## File-specific warning

### Backup sources

Clean only the passages listed in the target table. Backup passages destined for later Tier-2 or Tier-3 decisions remain as historical source material.

---

## Report format

After each file, report:

- headings cleaned;
- flagged content and the user's decision for each flag;
- content migrated into a [framework theme file](1-framework/_index.md);
- content moved to backup or staging;
- content discarded with explicit approval;
- classification-table rows updated.

Then stop.
