---
tags:
  - decision
status: accepted
created: 2026-09-25
revised: 2026-10-31
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Registries as source
---
# Registries for vocabularies and requirements

> [!QUESTION] Goal: which file declares the vocabularies and the requirements that a checker enforces, and which file documents them?

A filled inquiry draws on three vocabularies, and each vocabulary has a single author and a single reach.

| Vocabulary | Author | Reach | Where it is declared |
| ---------- | ------ | ----- | -------------------- |
| Fields and their option lists | Designer, after the theory note for a value whose meaning the theory defines | Every problem | Package data, documented by the specification notes and the templates |
| Symbols of one problem | Author of that problem | The records of that problem | The records themselves, collected into one generated table per problem |
| Operators | Designer for the canonical set, author for the rest | The canonical set in every problem, the rest in one problem | Package data for the canonical set, and one file per problem for its [local operators](../specification/operators.md#^local-operators) |

## Decision

Package data declares every closed vocabulary, every requirement of an epistemic aim and every canonical operator. The specification notes document those declarations, and the alignment check reads a note against its registry.

A value whose meaning a theory note defines is owned, as to that meaning, by that note: an epistemic aim with its category and its answer conditions, an epistemic activity with its signature and its norm, a product type, or a value of a status of the state. Such meaning would hold under any format of the records, so it belongs to the theory by the [test that separates theory from specification](../../CONTRIBUTING.md#theory-and-specification). A registry declares the identifier of the value, and the token fields that a check compares with the theory, such as the category of an aim. A registry holds no prose copy of the theory, by the [rule of one source](one-source-per-unit.md#^generated-copies-only). The prose answer conditions of the aims, which package data still holds, are therefore to be removed, and the tests that compare them adapted, as the goal `theory-code-alignment` of the [project goals](../../TODO.md) records. ^concept-ownership

## Constraints that decide the source

- **A checker must not parse prose.** A checker that reads a document couples the logic of the framework to the formatting of that document, and it makes the package depend on a workspace that holds `docs/`. Only the alignment check has reason to read a note.
- **One constant serves one purpose.** A single constant had named both the record kinds that the checkers read and the blocks that declare symbols, so adding a kind that declares no symbol excluded that kind from every check without any report.
- **An empty value states only that the field is not filled.** Every word stays free for the vocabularies: a vocabulary may admit `open` as an ordinary value. The requirements registry tells whether an empty field is a gap or a value produced by the inquiry, and a question starts in the state `posed`.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Declare each vocabulary in the specification note that explains it | One source serves the reader and the checker alike, and a note can never drift from the rule that it documents | The checker then parses prose, so a heading, a table format or a wording change alters the behavior of the framework, and the package requires the documentation workspace at run time |
| Declare each vocabulary in the checking code | The declaration sits beside the logic that reads it | A designer extending a vocabulary edits a module, and a reader of the framework cannot inspect the admitted values without reading code |
| Let the registries own the concepts as well, and the theory notes document them | One owner for every value that a checker reads | An answer condition or a norm would hold under any format of the records, so it belongs to the theory, and a registry that owned it would hold the only statement of a theoretical content outside the theory |
| Declare each vocabulary in package data, and document it in the notes | The checker reads data, the reader reads prose, and the alignment check reports a note that drifts | Each admitted value is written twice, in the registry and in the note, so the alignment check becomes the only guarantee that the two copies agree |

## Consequences

- A value outside its vocabulary is reported, and so is a template comment whose option list drifts from the registry.
- An epistemic aim requires a specification to be filled and never a value that the specification takes. The inquiry judges which value is correct, and a rule reaching inside a field is a consistency between fields.
- The specification notes document the registries and own no vocabulary, so a designer who adds an option edits the registry and the note in the same change.
- A change to a value whose meaning the theory defines, such as a new aim or a new activity, starts in its theory note, and the registry declares it in the same change. The tests of template alignment and of itineraries report a drift of the identifiers and of the token fields in either direction.
