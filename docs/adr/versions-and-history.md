---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Versions and history
---
# Versions and history

> [!QUESTION] Goal: which records carry a version, and which records rely on the history of the repository alone?

The records of `gnomon` are files under git, which keeps every earlier state of each record. Some references must nevertheless fix the state of their target. Bindings and keys carry versions under the [decision on answers, models and bindings](answers-models-bindings.md), and a record names its schema at a version under the [decision on record schemas](record-schemas.md). The retired design notes (commit 9e138e2) forbade both a store of past versions and every reference fixed to a past state, so the versions now in use contradicted them.

## Decision

`gnomon` keeps no store of past versions of its records. The history of the repository, kept by git, holds every earlier state. ^git-keeps-history

A record carries a version only if a reference must fix the state of that record, so that the referring record stays valid once the record is revised. ^version-where-pinned

Three references fix a state of their target: ^pinned-references

- a reference to a binding or to a key, which names its [version](../epistemology/model-and-binding.md#^binding-version);
- the root property `_schema` of a record, which names its schema at a version;
- a step of an itinerary, which is planned to name the state of each record that it used, by `as_of`, under the goal `inquiry-records-round-2` of the [project goals](../../TODO.md). The goal also decides the form of `as_of`: a version of the record, or a revision of the repository.

Every other reference names its target at its current state. ^current-by-default

## Constraints that decide the versions

- **Git already records every state.** A store of past versions inside the records would restate that history, which the [rule of one source](one-source-per-unit.md#^one-source) excludes.
- **A computed result must stay reproducible.** A comparison is [recomputed from a binding at one version](../epistemology/model-and-binding.md#^comparison-recomputed), so a binding without versions would change the result of every earlier comparison once revised.
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
- The check of the itinerary resolves `as_of` once the goal `inquiry-records-round-2` adds it.
- A new reference that must fix a state is added to the list of references that fix a state, with the reason that the referring record must stay valid.
