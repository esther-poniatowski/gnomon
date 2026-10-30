---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-29
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Checks read records
---
# Records as the only input of checks

> [!QUESTION] Goal: which files may a check of `gnomon` read, and which process produces the verdict that a record conforms?

Three kinds of file surround an inquiry: the records that authors write, the package data that declares vocabularies and schemas, and the outputs that tools generate, such as the symbol table of a problem and the record templates. The [decision on registries](registries-as-source.md) already excludes the notes of the documentation from the inputs of a check. Two questions remained open. The first asks whether a check may read a generated output, or a state that a tool holds apart from the files. The second asks whether an author, or a field of a record, may certify that the record conforms.

## Decision

A check reads authored records and package data, and nothing else. The decision on registries admits a single exception: the alignment check, which reads a note against its registry. ^checks-read-records

The records are the source of the research content. A generated output is rebuilt from the records, and no tool holds content that the records lack. ^records-are-source

A verdict on a record is produced by a checker run on that record. No field of a record states that the record conforms, and a correction that an author makes before the checker runs does not replace the verdict. ^external-verdict

## Constraints that decide the inputs

- **A generated output restates its source.** A check that read the symbol table, or a template, would depend on the last run of its generator. A stale output would then pass or fail a record that has not changed.
- **A reader and a checker must read the same object.** A state held by a tool apart from the files diverges from the records that authors edit and that git versions, and a reader of a record cannot inspect it.
- **The process that writes a record shares the assumptions of its author.** An error that the author does not recognize also passes the review of the author. A checker applies the declared rules independently of the assumptions of the author, so its verdict reports that error.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Let a check read the generated outputs as a cache | A check over the symbol table avoids loading every record again | A stale output decides the verdict, so a record passes or fails according to the last run of the generator |
| Hold the corpus in a store operated by the tool, and render the records from it | Queries and checks run on an indexed store | The files that authors edit and that git versions stop being the source, so a reader of a record cannot inspect the content that the tool holds |
| Mark conformance in a field of the record | A reader sees which records were checked | The mark copies a verdict that the next edit invalidates, and an author can set it without running the checker |
| Checks read authored records and package data, and only a checker run produces a verdict | Every verdict is reproduced from files that a reader can open | Each run of a check rebuilds its own view of the records |

## Consequences

- A generated file placed beside the records, such as the table `vocabulary.yml` of a problem, is excluded from the inputs of every check. The count of unused declarations in `src/gnomon/vocabulary.py` already excludes that table.
- A check that needs a derived structure, such as the graph of the [relations between records](closed-typed-relations.md#^relation-graph), builds that structure from the records at each run.
- The decision excludes a field that certifies conformance to the checks. A field that names the agent who drafted or reviewed the content of a record is a separate question: the [decision on the knowledge interchange format](knowledge-interchange-format.md#^trust-fields-open) leaves the trust fields of the Open Knowledge Format to a later decision.
