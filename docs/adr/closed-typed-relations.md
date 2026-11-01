---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-29
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Closed typed relations
---
# Closed typed relations

> [!QUESTION] Goal: which relations may link two records, what does each relation declare, and how are the relations queried?

Records of `gnomon` are linked in three ways. An answer carries `relations` to other answers, whose types the [decision on answers, models and bindings](answers-models-bindings.md) fixes. A question carries `links` to other questions, typed by the [links between questions](../epistemology/objects/question/question.md#^linked-questions). Several fields name a record by identifier, such as the target system of a phenomenon. The types of relations and links are closed vocabularies of the [registry of vocabularies](../../src/gnomon/data/vocabularies.yml), under the [decision on registries](registries-as-source.md). Three questions had no decision: whether a relation may fall outside every vocabulary, which properties a relation type declares, and how a reader finds the units that depend on a unit.

## Decision

Every relation between records takes its type from a closed vocabulary declared in package data. No record states a relation whose type the vocabulary lacks, whatever the commitment or the maturity of the record. ^closed-relations

Each relation type declares the record types that its source and its target may take. A check reports a relation whose ends take other types. ^typed-ends

A relation is authored once, on its source record. A tool builds the graph of relations from the records at each run, and every query reads that graph: the units on which a unit depends, the units that rest on it, the units that no relation reaches, and the cycles that a relation forms. ^relation-graph

The registry that gathers the relation types of every family of records, with their warrant kinds and the relations that transmit a revision, is decided under the goal `relation-registry` of the [project goals](../../TODO.md). ^relation-registry-open

## Constraints that decide the vocabulary

- **A relation read by a tool needs a grammar.** A relation whose type is stated in prose conforms to no grammar, so the [decision on grammatical fields](grammatical-fields-and-readings.md#^grammar-for-read-fields) excludes it from every query.
- **The types of the ends fix the sense of a relation.** The retired design notes (commit 9e138e2) record that one phrase, "is a stronger version of", names an implication between two theorems and a specialization between two concepts. A relation type that declares its ends keeps one sense.
- **Dependence must be found without reading prose.** A researcher facing a new question must find the records that bear on it, which the [motivation of the README](../../README.md#motivation) names as the first failure of an organization built on documents. Typed nodes linked by typed relations are the structure of issue-based information systems [kunz1970].

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Untyped links, with the type stated in prose | Any relation is recorded at once | No query reads the type, as the [decision on the knowledge interchange format](knowledge-interchange-format.md#^no-okf-source) finds for the links of the Open Knowledge Format |
| Free linking phrases that harden into types as the inquiry matures, as in concept maps | A relation is recorded before its type exists | One field holds values of two kinds. A relation without a declared type is stated in a reading until the registry admits its type, so the progression runs through the registry |
| A vocabulary that each problem extends with relations of its own | Each problem names the relations that it needs | Two problems name one relation differently, so a query across problems misses one of them |
| A store of relations outside the records, such as relational tables or a triple store | A standard query language over an indexed store | The store holds a second copy of each relation, which the [decision on the inputs of checks](checks-read-records.md#^records-are-source) excludes |
| A record of its own for each relation, carrying its context and its status | A relation carries its own warrant and status | Deferred to the goal `relation-registry`, together with the warrant kinds, and subject to the [admission of a record kind](record-kind-admission.md#^admission-conditions) |
| A closed vocabulary with typed ends, and a graph built from the records | Every relation is checked, and every query reads one structure | A relation outside the vocabulary waits for a change of the registry |

## Consequences

- A new relation type enters the registry first, with the types of its source and its target.
- Today the ends of each relation are fixed by the field that holds it: the `relations` of an answer link two answers, and the `links` of a question link two questions. The check of the itinerary is the only tool that builds a graph, the graph of its steps.
- The result of a query is a report, never a relation that a record asserts, as the [decision against inference at run time](no-run-time-inference.md#^admitted-computation) requires.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the bibliographic record.

- [kunz1970] ◐ Kunz & Rittel, *Issues as Elements of Information Systems*, Working Paper 131, Institute of Urban and Regional Development, University of California, Berkeley, 1970
