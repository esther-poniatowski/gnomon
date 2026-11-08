---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-11-08
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Versions and history
---
# Versions and history

> [!QUESTION] Goal: which records carry a version, and which records rely on the history of the repository alone?

The records of `gnomon` are files under git, which keeps every earlier state of each record. Some references must nevertheless fix the state of their target. Bindings and keys carry versions under the [decision on answers, models and bindings](answers-models-bindings.md), and a record names its schema at a version under the [decision on record schemas](record-schemas.md). The retired design notes (commit 9e138e2) forbade both a store of past versions and every reference fixed to a past state, so the versions now in use contradicted them.

## Decision

`gnomon` keeps no store of past versions of its records. The history of the repository, kept by git, holds every earlier state. ^git-keeps-history

A record carries a version only if a reference must fix the state of that record, so that the referring record stays valid, or is reported void, once the record is revised. ^version-where-pinned

Four references fix a state of their target: ^pinned-references

- a reference to a binding or to a key, which names its [version](../specification/binding.md#^binding-version);
- the root property `_schema` of a record, which names its schema at a version;
- an assessment of an answer, which names by `against_version` the [version of the question](../specification/question.md#^question-version) against which its verdicts were made, so that a revision of the question reports those verdicts void, as the [rule on tests fixed before evaluation](../epistemology/objects/answer/satisfaction-conditions.md#^tests-fixed-before) requires. A revision of the repository was the other form weighed. It is discarded on three grounds. First, the file of a question also changes when its status or its answerability is updated, and marking a question `answered` follows a satisfied assessment, so a comparison of revisions would void the assessment that answers the question. Second, a revision is unreadable after a move of the file, a rewriting of the history or an export of the record, and on a clone without history. Third, two revisions cannot be compared without git, whereas two versions are compared by equality. A declared version leaves to the researcher the judgment that a change revises the specification, which the theory requires of a revision;
- a step of an itinerary, which names the state of each record that it used, by `as_of`, a revision of the repository. A version of the record was the other form weighed. That form is discarded because a step may use a record of any kind, so it would require a version on every record, the option that the table below discards.

Every other reference names its target at its current state. ^current-by-default

A version and a revision serve two purposes. A version names a state of a record that a reference must find current, and a check compares two versions by equality. A revision of the repository locates the content of a state in the history, so that a check can read the content that a step used. The step that revises a question joins the two: its input names, by `as_of`, the revision at which the earlier version was read. ^version-and-revision

## Constraints that decide the versions

- **Git already records every state.** A store of past versions inside the records would restate that history, which the [rule of one source](one-source-per-unit.md#^one-source) excludes.
- **A computed result must stay reproducible.** A comparison is [recomputed from a binding at one version](../epistemology/objects/answer/model-and-binding.md#^comparison-recomputed), so a binding without versions would change the result of every earlier comparison once revised.
- **A step stays valid once it has run.** A step that names a record at its current state becomes invalid at the next revision of that record, although the step ran correctly.
- **A version on every reference fragments the records.** Each revision would require an update of every referring record, or would leave the records spread over past states.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep past versions in the records, or in an archive of earlier records | Each earlier state is read without git | The store restates the history of git, and the two histories can disagree |
| Forbid every reference fixed to a past state, as the retired design notes did | Every record shares one current state | A revised binding changes every earlier comparison, and a step of an itinerary becomes invalid once its record is revised |
| Version every record, and fix the state of every reference | Every reference is reproducible | Each revision forces an update of every referring record, or leaves the records spread over past states |
| Versions only on records whose state a reference must fix | Git keeps the history, and each reproducible result keeps its inputs | A check must resolve a reference at a stated version, not only at the current state |

## Consequences

- The decision replaces the criterion of the retired design notes that excluded any version history, including its prohibition of references fixed to a past state.
- The check of the itinerary reads a record named with `as_of` from the history of the repository, at that revision. A revision so named must be reachable from the default branch, since a squash or a rebase of a branch removes its commits.
- The check of an assessment compares its `against_version` with the version of its question, and reports the assessment void when they differ.
- A new reference that must fix a state is added to the list of references that fix a state, with the reason that the referring record must stay valid.
