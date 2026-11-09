---
tags:
  - decision
status: accepted
created: 2026-11-09
revised: 2026-11-09
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Research export
---
# Research export

> [!QUESTION] Goal: which units and which relations does `gnomon` publish for an exposition, and how does it map them onto the classes of the contract that `ekthesis` publishes?

The [decision on the scope of gnomon](research-scope.md) moves exposition to `ekthesis`, which reads research units through the export of their source. `ekthesis` publishes the contract of that export, `ekthesis:export@1`. Its fields are stated in the [contract of a research export](https://github.com/esther-poniatowski/ekthesis/blob/main/docs/adr/export-contract.md). The [relation registry](relation-registry.md) declares the class of each relation in that contract. Until now, no code read that class, and no command wrote an export.

## Decision

The command `gnomon export` writes the export of a directory of records into one file, `export.yml` by default, with the type `export`. The export is generated, committed beside the records, and never edited. Its type is a generated kind, so no check and no view reads it, as the [decision on the inputs of checks](checks-read-records.md) requires. The repository is named by `repository.id` in the nearest `repository.yml`, and the command fails when no such file names it. ^export-command

**Units.** The registry `registries/export.yml` declares the exported units: ^export-units

- per record kind, the kind of its unit in the contract and the path of its statement: problems, questions, answers, concepts, phenomena, target systems, models, backgrounds, derivations and designs;
- per record kind, the lists of units inside a record: the operations, laws, organization and assumptions of a model, the laws and organization of a background, the consequences of a derivation, the presuppositions of a claim, the presuppositions and the excluded parts of a question, and the feature pairs of a binding.

A binding is not exported as a unit, but its feature pairs are, since a ground with the role `warrant` names an argued pair. An itinerary, an assessment and a key are not exported, since no check of `ekthesis` reads them. A question carries its version, and an answer the answers that revise it, computed from `revises`.

**Relations.** The export reads the edges of each record, and keeps each edge whose declaration in the relation registry names a class: ^export-relations

| Relation | Class | Direction in the export |
| --- | --- | --- |
| `supports` | support | from the supporting answer to the supported one |
| a ground of role `assumption`, `warrant` or `datum` | support | from the ground to the answer, with the role as its use |
| a ground of role `condition` | condition | from the ground to the answer |
| `incompatible-with` | incompatibility | the sorted members of the set, the holder included |
| `contrasts-with` | contrast | the two answers in sorted order, once |
| `subquestion-of` | elaboration, form whole and part | from the subquestion to the question |
| `broader` | elaboration, form generalization and specific | from the narrower concept to the broader one |
| `exemplifies` | instance | from the answer to the concept or the more general answer |
| `answers` | solutionhood | from the question to the answer |

A ground with the role `idealization` or `criterion` maps onto no class: an idealization is false of the target, and a criterion is a standard of the question. `defeats` maps onto no class, since an undermining or an undercutting defeater leaves the two claims jointly possible, whereas an antithesis requires their incompatibility. Every other relation is omitted, and `revises` survives as the supersession of a unit.

**Identity and closure.** A relation lifted from a ground takes the dotted identifier of that ground. Every other relation takes a key built from its name and its ends. A relation is exported only when each of its ends is an exported unit; the command lists every relation that it drops. ^export-closure

**Determinism.** The units are sorted by identifier, and the relations by class, first end, second end, name and identifier. The export holds no date, no revision and no absolute path, so two runs on unchanged records write the same bytes. The option `--check` compares the committed export with a fresh generation, and writes nothing. ^export-determinism

**Failing records.** The command refuses to write while `gnomon check` reports an error. The option `--allow-findings` writes the export anyway, and the export records it under `findings_overridden`. ^export-findings

## Constraints that decide the export

- **The export is a copy generated from its sources**, which the [rule of one source](one-source-per-unit.md#^generated-copies-only) admits. Therefore, the export changes the relations of the records only by the mapping onto classes and by the closure. A `supports` that restates a ground is reported by the check `relation/restated-ground`, not removed.
- **`ekthesis` reads classes only.** The names of the relations of `gnomon` and the uses of their entries are carried for provenance, and stay opaque to the reader.
- **A relation needs both of its ends.** An exposition resolves each end of a relation in the export, so an end missing from the export would leave the relation unverifiable.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Support from `supports` alone | One source of support | Support resting on a law or a datum would never be verifiable, since the grounds state it |
| `defeats` mapped onto incompatibility | Every attack licenses an antithesis | A defeat that denies a ground leaves both claims possible, so the class would overstate it |
| `exemplifies` with five uses | Each use of a case is named | Four uses restate `tests`, `defeats`, `incompatible-with` and the grounds of an answer, and no reader reads them |
| Symbols and formulas in the export | A renamer reads the symbols of a project | No rule of `ekthesis` reads them, and a formula is parsed only by `gnomon` |
| The binding records as units | Every record named by a ground is a unit | A ground names an argued pair, not the binding as a whole |
| A relation kept with an end that is no unit | No relation is lost | An exposition could not resolve that end |
| Dropping a `supports` that restates a ground | No duplicate support in the export | The export would no longer be a function of the records alone |

## Consequences

- The `export` property of the relation registry gains a reader.
- The answer gains the relation `exemplifies`, and the note on [relations between research units](../epistemology/objects/knowledge/relations-between-units.md#^instance) defines it.
- Each edge of the graph of claims runs from the unit that depends on the other, so a support stated beside the ground that it restates forms no cycle.
- `gnomon` declares a schema dependency on `ekthesis:export@1` through `kleisis`, pinned at a commit of `ekthesis` in the [schema resources](../../specs/schema-resources.yml). The tests validate the export of each worked example against the materialized schema, and check that every class and form of the relation registry belongs to the contract.
