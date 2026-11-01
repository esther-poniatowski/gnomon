---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-30
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Admission of a record kind
---
# Admission of a record kind

> [!QUESTION] Goal: when does a proposed construct become a record kind of its own, rather than a unit of an existing record?

The method fixes one record kind per concern of an inquiry. Other constructs arise while records are filled. The model, the binding and the key became records of their own under the [decision on answers, models and bindings](answers-models-bindings.md), and the concept under the [decision on concepts, glossaries and notations](concepts-glossaries-notations.md). A transformation between models stays a block of its destination model, since it has no identity apart from that model and serves no other. Those choices applied a test that no decision of `gnomon` stated. The test was amended in place with two conditions, non-distortion and unitary epistemic role, drawn from the retired design notes.

## Decision

A construct becomes a record kind of its own only if it meets seven conditions: ^admission-conditions

- **independent identity**: the construct is meaningful without the record that would otherwise contain it;
- **reuse**: several records can cite one instance of the construct;
- **local validity**: a check can judge its content without reading the records that cite it;
- **independent editing**: an author can revise it without rewriting the records that cite it;
- **irreducibility**: no tool can generate it from other records;
- **non-distortion**: the construct cannot be stated through an existing kind, field, value, relation or unit without erasing its structure, merging heterogeneous objects, or moving its content into prose;
- **unitary epistemic role**: the instances of the kind license the same reasoning operations.

Irreducibility tests whether a tool can generate the construct, whereas non-distortion tests whether an existing kind can encode it, so an example or an analogy mapping that an existing kind already states now fails the test.

A construct that fails one condition is stated as a field, a value of a closed vocabulary, a relation, a unit of an existing record with an identifier of its own, or a generated view. ^failing-construct

*Examples*: the retired design notes (commit 9e138e2, `docs/design/_backup/object-types-ontology/taxo-criteria-ontology.md`) worked three cases, and each fails non-distortion. A motivation is a field of the object that it motivates. A dependency is a typed relation between two records. A limitation is an attribute of the object that it limits, such as the domain of an answer or the idealizations of a model. An example fails in the same way, since it is a relation [`exemplifies`](../proposals/relation-registry.md#examples-as-relations), from an existing record to a concept or an answer.

The record kinds of the concerns of an inquiry are fixed by the method, and the test governs every other construct. ^scope-of-admission

## Constraints that decide the test

- **Each record kind costs every author.** A kind adds a template, a schema, a check and a specification note, which each author learns, so the set of kinds stays small.
- **A unit of a record is already addressable.** The [dotted identifiers](dotted-identifiers.md) name a unit inside a record, so a construct that is cited, but fails another condition, stays a unit.
- **A generated record has a source.** A record that a tool can generate from others would be a copy, which the [rule of one source](one-source-per-unit.md#^generated-copies-only) admits only as a generated output.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Fix the complete set of record kinds before cases are filled | The set of kinds stays stable | Constructs arise from cases: the audits of the model design found the model, the binding and the key |
| Admit a kind whenever one case, or the literature, names a construct | Each construct has a home of its own | The set grows with each case, as a field admitted for one case would, which the [grounds for a shared field](shared-field-grounds.md) exclude at the grain of a field |
| Keep every construct inside the record of its concern | No kind is added | A model that grounds several answers would be repeated in each of them |
| Let a classifier infer the kind of a record from its properties | No author assigns a kind | The kind of a record is authored, as the [decision against inference at run time](no-run-time-inference.md#^excluded-inference) requires |
| Seven conditions, all required | Each kind has a stated warrant, and the set grows only by constructs that several records cite and that an author edits apart | A construct that only one record cites stays inside that record, and its author edits it there |

## Consequences

- The model passes the seven conditions. Stated through the blocks of its target, a stylized model asserted an identity that a model never has with its target, as the [decision on answers, models and bindings](answers-models-bindings.md) found, and every model licenses the same reasoning operations: a derivation or a simulation runs on it, and a binding, when one exists, carries its results to a target. The transformation fails independent identity, since it has no identity apart from its destination model.
- A decision that admits a record kind states how the kind meets each condition. The new kind also declares the segments of its identifier and its [record schema](record-schemas.md).
- A relation reified as a record of its own passes the same test, under the goal `relation-registry`.
