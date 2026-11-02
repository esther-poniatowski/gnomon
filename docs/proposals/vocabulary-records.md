---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the vocabulary records
---
# Proposals for the vocabulary records

The goal [`vocabulary-records`](../../TODO.md) provides the mechanism of the notation, and defines the concept record, as the [decision on the scope of gnomon](../adr/research-scope.md) states.

## Concept as class and concept as object

A concept is both a category, a class of things, and an object of inquiry, which carries a definition, a history, sources, variants and critiques. "Representation" is at once a class and an object about that class. The discipline keeps both readings explicit: a concept object that `denotesClass` a category. The concept record already holds both: its broader concept states an inclusion between the classes that two concepts denote, whereas its source note and its confusions describe the concept as an object of inquiry. The candidate requires the schema of the record to mark which fields bear on the class and which on the object, so that no check reads one as the other.

**Literature.** Metamodeling in Description Logics.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record, and `definitions-framework`.
