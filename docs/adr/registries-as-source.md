---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Registries as source
tags: []
source:
---
# Registries for vocabularies and requirements

> [!QUESTION] Goal: which file declares the vocabularies and the requirements that a checker enforces, and which file documents them?

A filled inquiry draws on three vocabularies, and each vocabulary has a single author and a single reach.

| Vocabulary | Author | Reach | Where it is declared |
| ---------- | ------ | ----- | -------------------- |
| Fields and their option lists | Designer | Every problem | Package data, documented by the method notes and the templates |
| Symbols of one problem | Author of that problem | The records of that problem | The records themselves, collected into one generated table per problem |
| Operators | Designer for the canonical set, author for the rest | The canonical set in every problem, the rest in one problem | Package data for the canonical set, and one file per problem for its [local operators](../epistemology/symbols-and-expressions.md#^local-operators) |

## Decision

Package data declares every closed vocabulary, every requirement of an epistemic aim and every canonical operator. The method notes document those declarations, and the alignment check reads a note against its registry.

## Constraints that decide the source

- **A checker must not parse prose.** A checker that reads a document couples the logic of the framework to the formatting of that document, and it makes the package depend on a workspace that holds `docs/`. Only the alignment check has reason to read a note.
- **One constant serves one purpose.** A single constant had named both the record kinds that the checkers read and the blocks that declare symbols, so adding a kind that declares no symbol excluded that kind from every check without any report.
- **A sentinel carries one meaning.** Every closed field accepts `open` for a value that an inquiry has not settled, so no vocabulary lists it, and the first state of a question is `posed`.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Declare each vocabulary in the method note that explains it | One source serves the reader and the checker alike, and a note can never drift from the rule that it documents | The checker then parses prose, so a heading, a table format or a wording change alters the behavior of the framework, and the package requires the documentation workspace at run time |
| Declare each vocabulary in the checking code | The declaration sits beside the logic that reads it | A designer extending a vocabulary edits a module, and a reader of the framework cannot inspect the admitted values without reading code |
| Declare each vocabulary in package data, and document it in the notes | The checker reads data, the reader reads prose, and the alignment check reports a note that drifts | Each admitted value is written twice, in the registry and in the note, so the alignment check becomes the only guarantee that the two copies agree |

## Consequences

- A value outside its vocabulary is reported, and so is a template comment whose option list drifts from the registry.
- An epistemic aim requires a specification to be filled and never a value that the specification takes. The inquiry judges which value is correct, and a rule reaching inside a field is a consistency between fields.
- The notes document the registries and own no vocabulary, so a designer who adds an option edits the registry first and the note in the same change.
