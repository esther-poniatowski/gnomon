---
tags:
  - criteria
index: "[[_index|Framework-level criteria]]"
aliases:
  - Cost and Ergonomics (criteria)
---
# Cost and Ergonomics — Framework-level criteria

This cluster of criteria forms a 2×2 grid:

|              | **Read cost**                                 | **Write cost**                                    |
| ------------ | --------------------------------------------- | ------------------------------------------------- |
| **Human**    | [Human read cost](#^t1-human-read-cost)       | [Human action cost](#^t1-human-action-cost)       |
| **Machine**  | [Read-side automation](#^t1-read-side-automation) | [Write-side automation](#^t1-write-side-automation) |

Plus [system scale](#^t1-system-scale) bounding the four costs as project size grows.

## Human read cost ^t1-human-read-cost

Per-read cost is **bounded**: a human reader reaches the content they need without parsing more material than the question requires. Legibility, navigation, and the local density of cross-references all contribute.

**Failure mode prevented.** A representation that requires traversing several layers of indirection to answer a simple question exhausts the reader's attention before the content is reached, and the framework ceases to be consulted.

**Upstream dependencies.**

- None (cost-axis root).

**Downstream consequences.**

- [System scale](#^t1-system-scale) (sub-criterion): bounds per-read cost as the corpus grows.

## Human action cost ^t1-human-action-cost

Per-action cost is **bounded**: each authoring action — adding an object, recording a relation, updating a field, validating a draft — costs the author a small bounded amount.

**Failure mode prevented.** A representation that imposes a high per-action overhead — many mandatory fields per object, redundant manipulations, multiple validation passes per draft — is technically expressive but operationally unusable, and researchers cease to use it.

**Upstream dependencies.**

- None (cost-axis root).

**Downstream consequences.**

- [Object-kind smallness](object-kinds#^t2-ontology-small) (theme-local criterion): more kinds raise per-action cost.
- [System scale](#^t1-system-scale) (sub-criterion): bounds per-action cost as the corpus grows.
- [Justification levels](reasoning-integrity#^t1-justification-levels) (tension per `^t2-x2`): deeper annotation lowers ambiguity at the cost of more per-action work.

## Read-side automation ^t1-read-side-automation

The system supports **automated reading**: query, search, navigation, comparison, and dependency analysis are mechanizable without human inference. Tools can answer specific questions (e.g. "what depends on X?" or "find all objects of kind K with property P") by deterministic computation over canonical state.

**Failure mode prevented.** A representation whose only reader is a human cannot scale: cross-corpus queries, refactoring impact, and integrity audits all become manual sweeps.

**Upstream dependencies.**

- None (cost-axis root).
- [Human read cost](#^t1-human-read-cost) (peer sub-criterion): mirrored on the machine side of the read column in the cost-axis grid.

**Downstream consequences.**

- [Relational queryability](modular-content-organization#^t1-relational-queryability) (sub-criterion): one consumer of automated reading.
- [System scale](#^t1-system-scale) (sub-criterion): bounds automated-reading cost as the corpus grows.

## Write-side automation ^t1-write-side-automation

The system supports **automated writing**: validation, build, registry update, orphan detection, and derived-artefact regeneration are mechanizable without human judgment. The author writes canonical content; the build derives indexes, registries, and rendered views.

**Failure mode prevented.** When derived artefacts must be edited manually, every canonical edit creates an implicit obligation to update each derived artefact. Drift accumulates and the system loses consistency.

**Upstream dependencies.**

- None (cost-axis root).
- [Human action cost](#^t1-human-action-cost) (peer sub-criterion): mirrored on the machine side of the write column in the cost-axis grid.

**Downstream consequences.**

- No-manual-edit policy on derived artefacts (sub-criterion): once the build can regenerate any derived artefact, manual edits become unnecessary and unsafe.
- [Validation externality](research-activities-workflows#^t1-validation-externality) (cross-group sub-criterion in *Research activities and workflows*): externalised validators are the standard consumer of automated writing.
- [System scale](#^t1-system-scale) (sub-criterion): bounds automated-writing cost as the corpus grows.

## System scale ^t1-system-scale

The four cost axes above remain **bounded as project size grows**. The framework handles wide projects — many objects, many contributors, many versions — without storage, query, or build degradation.

**Failure mode prevented.** A representation whose per-read cost grows linearly with corpus size, or whose build time grows quadratically with relation count, fails at research scale even when individual costs are reasonable on a small example.

**Upstream dependencies.**

- [Human read cost](#^t1-human-read-cost), [human action cost](#^t1-human-action-cost), [read-side automation](#^t1-read-side-automation), [write-side automation](#^t1-write-side-automation) (peer sub-criteria): system scale bounds the four per-action costs as the project grows.

**Downstream consequences.**

- [Object-kind smallness](object-kinds#^t2-ontology-small) (theme-local criterion): kind proliferation degrades scaling.