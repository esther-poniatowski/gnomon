---
tags:
  - handoff
index: "[Design documentation](_index.md)"
aliases:
  - Design refactor handoff
---
# Refactor handoff — design folder

This handoff owns the Step A-D refactor state. It does not repeat the project brief in [main handoff](_handoff.md) or the Step A.4 file-by-file mechanics in [cleanup handoff](_handoff-cleanup.md).

The Step A–D sequence and the batch order within Step C are the **default** order, not a hard barrier. Under explicit user direction, any step may bring forward work the sequence assigns to a later step — see [Opportunistic scope](_handoff#^opportunistic-scope) in the main handoff. The "Brought-forward C/D work" callout below is the standing record of what has already been brought forward; whoever extends scope further adds to it and records the [deferred synchronization debt](_handoff#^deferred-synchronization-debt).

---

## Status

- **Step A.1–A.3 complete.** [The classification table](_classification-table.md) records active criteria and decisions; selected backup decisions are integrated. The canonical Tier-1 criteria are the [per-theme framework files](1-framework/_index.md).
- **Step A.4 nearly done.** The framework tier, the former architectural-constraints file, [data formats](2-architecture/data-formats.md), the former criteria-framework backup, the former tooling-validation backup, and the former registries-indexes backup are cleaned. The constraints file, the criteria-framework backup, the tooling-validation backup, and the registries-indexes backup have since been **deleted** — their inbound references were swept to the live anchors (a Step-C action brought forward, with user ratification). One backup source remains — a named-passage check, no migrated bodies to strip; see the [cleanup handoff](_handoff-cleanup.md).
- **Step A.5 largely done.** See the [residue](#^step-a5) below for the open items.
- **Step B blocked.** [The migration table](_migration-table.md) is only a header; Step A.5's residue should settle first.
- **Step C blocked on Step B** — but partly brought forward, see "Brought-forward C/D work" below.
- **Step D blocked on Step C — done for Tier 1, partly brought forward for Tier 2.**

> [!IMPORTANT] Brought-forward C/D work — the table is now ahead of the step sequence
> Several migrations the step sequence assigns to C and D were executed early, with user ratification. Whoever runs Steps B–D must treat these as **already done** and not re-plan them:
> - Every cross-cutting Tier-2 criterion has been promoted to Tier 1, moved to a theme-local `## Criteria` section, folded into a theme decision/open question, or retired. The former `constraints.md` migration index has been **deleted**: its inbound references were swept to the live anchors. [object-kinds.md](2-architecture/object-kinds.md) and [layering.md](2-architecture/layering.md) now have `## Criteria` sections (the Step-D shape); the other Tier-2 files do not yet.
> - The irreducible tensions and known gaps live in [tensions.md](1-framework/_tensions.md) (framework-level) and [gaps.md](2-architecture/_gaps.md) (architecture-level).
> - The snapshot-acyclicity property has its Step-C home: [snapshot acyclicity](2-architecture/relations-graph#^t2-snapshot-dag-property) on the relational-graph representation.
> - Inbound references to every retired anchor were swept across all theme files.
> - The tooling-validation backup cleanup brought forward further Step-C/D work, all ratified: the validator catalogue migrated to [t2-validator-catalogue](2-architecture/validation-views#^t2-validator-catalogue); a schema-specification meta-rule created as the open question [t2-schema-specification](2-architecture/object-kinds#^t2-schema-specification); the staleness/transition material staged as a candidate under [t3-status-transition-propagation](3-aspect-specific/status-vocabulary#^t3-status-transition-propagation); the staging-area `Ir` repair executed and the anchor renamed to [t3-registry-updates](3-aspect-specific/registries-indexes#^t3-registry-updates); and [t2-epistemic-status](2-architecture/object-kinds#^t2-epistemic-status) plus [t3-per-kind-status-enums](3-aspect-specific/status-vocabulary#^t3-per-kind-status-enums) **reopened** on the per-kind-vs-uniform enum grain. The classification-table rows these leave stale are itemised in the [Step A.5 residue](#^step-a5).
> - The registries-indexes backup cleanup brought forward a substantial Step-C/D execution, all ratified per paragraph:
>   - New Tier-3 decisions in [3-aspect-specific/registries-indexes.md](3-aspect-specific/registries-indexes.md): [typed references](3-aspect-specific/registries-indexes#^t3-typed-references) (object-transposed, replacing the placeholder `^t3-typed-imports`); [registry-component taxonomy](3-aspect-specific/registries-indexes#^t3-registry-component-taxonomy) (an 11-component closed catalogue grouped by query class, with the version-graph component dropped against [no version history](1-framework/framework-foundations#^t1-no-version-history)); [open-questions index schema](3-aspect-specific/registries-indexes#^t3-open-questions-index); [terminology-index schema](3-aspect-specific/registries-indexes#^t3-terminology-index-schema).
>   - New Tier-3 open questions: [registry scope per vault scale](3-aspect-specific/registries-indexes#^t3-registry-scope-per-scale), [registry serialization format](3-aspect-specific/registries-indexes#^t3-registry-serialization-format), [dependency-graph artifact maintenance](3-aspect-specific/registries-indexes#^t3-dependency-graph-artifact).
>   - New Tier-2 open question [drafting gate on import readiness](2-architecture/validity-revision#^t2-drafting-gate) in [validity-revision.md](2-architecture/validity-revision.md), agent-neutral, executing the former `^bk-drafting-gate` plan as an open question rather than a settled decision.
>   - Three-family edge-type proposal (semantic / justificatory / inquiry relevance) folded into the open question [t2-dependency-graph-layers](2-architecture/relations-graph#^t2-dependency-graph-layers) as a distinct candidate partition alongside the existing four-layer proposal.
>   - "Typed exports" added as a required aspect of the [schema-specification meta-rule](2-architecture/object-kinds#^t2-schema-specification).
>   - "Reasoning or argument map" framing folded into [relational graph representation](2-architecture/relations-graph#^t2-relational-graph-representation).
>   - Discards: the `^admissible-import-kinds` / `^admissible-output-types` / `^admissible-statement-roles` enumerations (frozen enums premature against the unfixed ontology); the per-note `notes`-array schema (stale note-centric draft, registry will be drafted fresh); the dependencies-registry schema (fully covered by the canonical object store, dependency graph, and reverse-dependency index components of the catalogue).
>   - Two `_backup/rendering/formal-contracts.md` cross-repo links repointed to the new [typed references](3-aspect-specific/registries-indexes#^t3-typed-references) decision.
>   - The [registry cluster](_alias-table#^cluster-registry) in [_alias-table.md](_alias-table.md) was rewritten to record the executed migrations and discards.
>   - The classification-table rows this leaves stale (rows 440, 442, 443, 447, 448, 449, 480) are itemised in the [Step A.5 residue](#^step-a5).
> - [The classification table](_classification-table.md) records the earlier brought-forward migrations with an "executed" marker on the relevant row.
> - **Formal-expression Tier-1 addition (ratified).** A new framework-tier criterion [t1-formal-expression](1-framework/framework-foundations#^t1-formal-expression) was added as a sub-criterion of [language-tooling integration](1-framework/framework-foundations#^t1-language-tooling-integration): expressivity is achieved exclusively by formalization; every semantic field is grammar-bound; free prose is confined to strictly unessential fields that no operation, validator, relation, or query reads. The consistent Tier-1 edits were applied in the same pass: [rich content expressivity](1-framework/expressive-depth#^t1-rich-prose-expressivity) (formerly *rich prose expressivity*) was rewritten so its expressivity targets are met by formal grammars rather than prose; [partial formalization tolerance](1-framework/expressive-depth#^t1-partial-formalization) was clarified so that partial means *annotations absent*, never sub-formal content; a new tension [t2-x5](1-framework/_tensions#^t2-x5) records the formal-expression vs. authoring-cost tradeoff; the reasoning-field-grammars open question was staged as [fleeting-reasoning-field-grammars](_fleeting-ideas#^fleeting-reasoning-field-grammars). Tier-2/Tier-3 sweep is **not** done in this pass; the debt below itemises what remains.
>
> Step B must extract migration rows only for content **not** already migrated; Step D must bring the remaining Tier-2 files (and all Tier-3 files) into the per-theme layout that `object-kinds.md` and `layering.md` already have.

<!-- end callout -->

> [!IMPORTANT] Synchronization debt from the formal-expression addition
> The Tier-1 formal-expression pass was scoped to framework-tier criteria only. The following items remain to be settled in a separate pass; each is *recalled, not silently carried*:
>
> - **Inbound-reference sweep.** Thirteen files cite [t1-rich-prose-expressivity](1-framework/expressive-depth#^t1-rich-prose-expressivity) — `1-framework/framework-foundations.md`, `1-framework/modular-content-organization.md`, `1-framework/expressive-depth.md`, `1-framework/research-activities-workflows.md`, `2-architecture/data-formats.md`, `2-architecture/validity-revision.md`, `2-architecture/relations-graph.md`, `2-architecture/validation-views.md`, `3-aspect-specific/ontology.md`, `3-aspect-specific/rendering-views.md`, `3-aspect-specific/reasoning-fields.md`, `3-aspect-specific/arguments-reasoning.md`, `3-aspect-specific/revision-vocabulary.md`. Each citation must be audited: citations of the retained residue (formulas / derivations / diagrams as rich content) stay; citations that lean on prose-as-semantic-content redirect to [t1-formal-expression](1-framework/framework-foundations#^t1-formal-expression).
> - **Tier-2 field-typing edit.** [t2-field-typing](2-architecture/object-kinds#^t2-field-typing) must be rewritten to partition fields into *semantic* (grammar-bound, mandatory grammar) and *unessential* (free-prose, framework-opaque). The check that no operation, validator, relation, or query reads an unessential field is the discriminator and should be stated explicitly.
> - **Tier-2 admission-test edit.** [t2-object-kind-admission](2-architecture/object-kinds#^t2-object-kind-admission) must drop any admission path for kinds whose canonical content is prose.
> - **Data-formats rewrite.** [data-formats.md](2-architecture/data-formats.md) lines 10, 18, and 244–249 still describe Markdown-with-prose as a substantive field shape; the line-10 `[!INFO]` migration note about the prose sub-claim is now misleading and needs updating to reflect the new partition.
> - **Reasoning-fields rewrite.** [reasoning-fields.md](3-aspect-specific/reasoning-fields.md) currently proposes prose defaults for strategic rationale, explanatory gain, route selection, and rejected-alternative records (lines 24, 26–27, 29, 31, 35, 43, 45). These directly violate the new criterion. Grammars are not designed here — the question is staged at [fleeting-reasoning-field-grammars](_fleeting-ideas#^fleeting-reasoning-field-grammars). Until grammars are chosen, this file is inconsistent with the framework tier; that inconsistency is recorded, not hidden.
> - **Validator obligation.** A new validator entry — *no semantic field contains ungrammatical content* — must be added to [t2-validator-catalogue](2-architecture/validation-views#^t2-validator-catalogue).
> - **Classification table.** A new row for [t1-formal-expression](1-framework/framework-foundations#^t1-formal-expression); revised rows wherever a decision was classified assuming prose-as-content (notably the reasoning-fields cells and data-formats); the 6 existing rows that match `rich-prose-expressivity` / `free-form` should be re-audited against the rewritten downstream consequences. Folds into the [Step A.5 residue](#^step-a5) "add rows" item and the Step B re-read.
> - **Other Tier-3 audits.** [ontology.md](3-aspect-specific/ontology.md), [rendering-views.md](3-aspect-specific/rendering-views.md), [arguments-reasoning.md](3-aspect-specific/arguments-reasoning.md), [revision-vocabulary.md](3-aspect-specific/revision-vocabulary.md) all reference prose; each citation needs the same retained-residue-vs-removed-claim audit as the Tier-1 sweep.

The rest of Tier 2 and all of Tier 3 still use the flat layout. Do not reorganize those files until Step D.

---

## Step A.4 boundary

Step A.4 only removes duplicate Tier-1 source bodies that have already moved into a canonical criterion in its [framework theme file](1-framework/_index.md). It does not migrate Tier-2 or Tier-3 decisions, does not redirect references, and does not retire files wholesale except where the [cleanup handoff](_handoff-cleanup.md) says a file becomes a stub.

The cleanup must preserve anchors so inbound links keep resolving until Step C — except where the cleanup handoff records that a file's redirect sweep was already brought forward.

---

## Step A.5 scope ^step-a5

Step A.5 brings [the classification table](_classification-table.md) current after Step A.4. It is authored classification work, not a mechanical extraction, so it belongs before Step B.

**Largely done.** The post-A.3 restructures are reconciled into the table: the Reasoning-integrity restructure, the [arguments and reasoning](3-aspect-specific/arguments-reasoning.md) machinery rebuild, the [framework tier](1-framework/_index.md) theme split, the `^t1-activity-separation` → `^t1-activity-access-rights` rename, and the Functional-separation merge (`^t1-stable-boundaries` + `^t1-function-driven-typology` → `^t1-functional-separation`). Every retired anchor now appears only as a historical-record mention; no live row targets one.

**What remains:**

- **Re-tally the numeric class counts.** The Summary-by-class table carries a `[!WARNING]`: its counts predate the restructures and are stale; only the numbers need a recount. The brought-forward C/D work changed several class assignments, so the counts are now further out of date. This can fold into Step B, which re-reads every row anyway.
- **Add rows for the post-A.3 tier-file anchors** not yet in the table: `^t3-epistemic-gap-subtypes`, `^t3-concept-type-taxonomy`, `^t3-definition-normal-form`, `^t3-reasoning-schemes`, `^t3-attack-target`, `^t3-undischarged-commitments`, `^t2-interpretive-hazard-lint`, `^t2-relation-reification`, and `^t2-schema-specification` (the schema-specification meta-rule open question minted during the tooling-validation backup cleanup). The registries-indexes backup cleanup minted further anchors that need rows: `^t3-typed-references` (replacing the placeholder `^t3-typed-imports`, which is retired), `^t3-registry-component-taxonomy`, `^t3-open-questions-index`, `^t3-terminology-index-schema`, `^t3-registry-scope-per-scale`, `^t3-registry-serialization-format`, `^t3-dependency-graph-artifact`, and the Tier-2 open question `^t2-drafting-gate`. (The post-A.4 pass added rows for the anchors it created — `^t2-dependency-graph-layers`, `^t2-validator-catalogue`, `^t2-relational-graph-representation`, and the Tier-1 `^t1-component-set-adequacy` minted during the criteria-framework backup cleanup — and for the theme-local criteria from the brought-forward C/D work.)
- **Reconcile the reopened status anchors.** `^t2-epistemic-status` and `^t3-per-kind-status-enums` were reopened during the tooling-validation cleanup: the per-kind-vs-uniform enum grain is now an open question. Classification rows 595 (`^t2-epistemic-status` — `D — Keep`) and 683 (`^t3-per-kind-status-enums` — `D — Keep`) still record them as settled decisions and must be updated. Row 477 (`^bk-status-transition-rules`, planned BK decision) is superseded — the transition table became a candidate under `^t3-status-transition-propagation`. Row 476 (`^bk-schema-enforcement-policy`, planned decision) is superseded — its content became the open question `^t2-schema-specification`.
- **Reconcile the registries-indexes BK plans now executed or superseded.** The registries-indexes backup cleanup left several planned BK rows out of date. Row 442 (`^bk-drafting-gate`, planned D in `validity-revision.md`) is superseded — the mechanism became the open question `^t2-drafting-gate`, agent-neutral. Row 440 (`^bk-registry-scale-layering`, planned D) is superseded — the scale stratification became the open question `^t3-registry-scope-per-scale`. Row 447 (`^bk-registry-component-taxonomy`, planned D) is executed — it is now `^t3-registry-component-taxonomy`, with the version-graph component dropped against `^t1-no-version-history` and the open-questions-index added as the 11th component. Row 448 (`^bk-open-questions-registry`, planned D) is executed — it is now `^t3-open-questions-index`. Row 449 (`^bk-dependencies-registry`, planned D) is superseded as discarded — its content is fully covered by the canonical object store, the dependency-graph component, and the reverse-dependency-index component of the taxonomy. Row 443 (`^bk-dependency-graph-artifact`, planned D for maintenance policy) is executed as the open question `^t3-dependency-graph-artifact`. Row 480 (`^bk-terminology-enforcement`, planned D in `validation-views.md`) still stands — the terminology-index schema executed as `^t3-terminology-index-schema`, but the linter realisation remains to be drafted at the validation work; the row needs a "still-pending" marker but no retirement.
- **Add provisional rows for unresolved candidates** in [the fleeting-ideas catalogue](_fleeting-ideas.md) under `## Candidates`. Exclude `## Principled rejections`, `## Triage log`, explanatory preambles, and already-propagated references that merely point to an active tier anchor. These rows mark staged candidates only; they do not produce Step-B migration rows unless a candidate has become a real decision.
- **Record the Step-D disposition** for [the fleeting-ideas catalogue](_fleeting-ideas.md) and [the worked-examples suite](_worked-examples.md). Current assumption: both stay outside the theme reorganization as staging and reference files.

The relation-reification question is settled: `^t2-relation-reification` now exists as an open question in [the relations graph](2-architecture/relations-graph.md); only its classification-table row is outstanding, folded into the "add rows" item above.

Step A.5 is complete when every active Tier-2/Tier-3 anchor and every staged candidate either appears in [the classification table](_classification-table.md) or is explicitly marked outside refactor scope, the table reflects the current Tier-1 labels and theme placements, and the class counts are re-tallied.

---

## Step B

Build [the migration table](_migration-table.md) from [the classification table](_classification-table.md), one row per final-state bullet that describes migratable content.

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

Use [the migration table](_migration-table.md) as the redirect source of truth. Run batches in this order: ^step-c

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
| `F` | Keep or create a Tier-1 criterion in its [framework theme file](1-framework/_index.md). |
| `A` | Keep or create a theme-local criterion. |
| `D` | Keep, move, copy, or create a decision or open question. |
| `P` | Fold into the named host decision. |
| `T` | Keep as cross-criterion metadata. |

After each batch, sweep inbound links and repair broken anchors before starting the next batch.

---

## Step D

After Step C, reorganize the design folder by theme. **Tier 1 is done; [object-kinds.md](2-architecture/object-kinds.md) and [layering.md](2-architecture/layering.md) already carry the `## Criteria` structure** from the brought-forward C/D work. Step D applies to the **remaining Tier 2 files and all of Tier 3**, bringing them into the same per-theme layout. The target theme files use this structure:

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
