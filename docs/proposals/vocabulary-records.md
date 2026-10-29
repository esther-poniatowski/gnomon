---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the vocabulary records
---
# Proposals for the vocabulary records

The goal [`vocabulary-records`](../../TODO.md) provides the mechanisms of notations, glossaries, audiences and project specifications, and defines the concept record.

## Concept as class and concept as object

A concept is both a category, a class of things, and an object of inquiry, which carries a definition, a history, sources, variants and critiques. "Representation" is at once a class and an object about that class. The discipline keeps both readings explicit: a concept object that `denotesClass` a category. The concept record already holds both: its broader concept states an inclusion between the classes that two concepts denote, whereas its source note and its confusions describe the concept as an object of inquiry. The candidate requires the schema of the record to mark which fields bear on the class and which on the object, so that no check reads one as the other.

**Literature.** Metamodeling in Description Logics.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record, and `definitions-framework`.

## Kind, confusions and boundary of a concept

Three parts of the concept record admit a closed form:

- **The kind of a concept** takes one of four values: a system, a subtype or class, a property, which may have an antagonist, and a process. The values are aligned with the definitions of [system, constituent and environment](../epistemology/definitions/systems/system-constituent-environment.md), [kind, class and population](../epistemology/definitions/systems/kind-class-population.md), [property, attribute and predicate](../epistemology/definitions/systems/property-attribute-predicate.md), and [process, event and history](../epistemology/definitions/change/process-event-history.md).
- **A confusion with another concept** names the other concept, the axis along which the two differ, the feature that blocks their interchange, the source of the risk of conflating them, and the consequence of that conflation.
- **The boundary criterion** separates a concept from a claim: content that fixes a meaning without asserting belongs to the concept, and content that asserts, denies, defines or evaluates belongs to a claim or a definition.

**Literature.** None cited.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record.

**Retired source.** `docs/design/3-aspect-specific/ontology.md`, `docs/design/_backup/object-types-ontology/obj-distinction.md` and `docs/design/_backup/object-types-ontology/taxo-boundaries.md`, at commit 9e138e2.
