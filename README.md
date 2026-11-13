# Gnomon

![Maintenance](https://img.shields.io/maintenance/yes/2026)
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/gnomon)](https://github.com/esther-poniatowski/gnomon/commits/main)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.12-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Specifies a research inquiry as typed records, from the problem that it addresses to the assessment of its answers, checks those records against the method that they follow, and exports them for the tools that present research to readers.

Gnomon serves domain-competent researchers who are new to Gnomon and its epistemic vocabulary. A new inquiry begins with the [greenfield tutorial](docs/guide/first-inquiry.md). An active part of existing research begins with the [adoption guide](docs/guide/adopting-existing-research.md). Both routes use the same records and checks. The [capability-status guide](docs/guide/capabilities.md) states the current boundary of each route.

---

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Overview

### Motivation

A theoretical research project typically holds many definitions, derivations and arguments, linked by dependencies. When such a project is kept in prose documents, five failures appear as it grows, and each aggravates the others:

- **Hidden dependencies.** The results that bear on a new question can be found only by reading the prose again.
- **Diluted argument.** Each restatement across notes, summaries and drafts is locally reasonable, and together they bury the main argument.
- **Drift toward side questions.** Without a record of the questions that the target requires, the work expands while the target does not advance.
- **Mixed epistemic roles.** A note blends a definition, a result, an assumption, a motivation, a proof sketch and an example, so the work cannot be read as a graph of distinct contributions.
- **Content held only in exposition.** The text written for a reader becomes the only form of the content, so revising the content requires rewriting the text.

These failures follow from one organization: prose serves both to store the content and to access it, and dependencies, roles and revisions stay implicit in the writing. Therefore, `gnomon` aims to:

- represent the state of knowledge of an inquiry, each result with its maturity;
- record the logic of the inquiry, that is, the dependencies through which results compose into answers;
- guide the inquiry, by listing the open conditions addressable now, each with its ready acts, and leaving the choice to the researcher;
- export the content of the inquiry, so that a presentation to a reader references the records instead of restating them.

### Advantages

`gnomon` replaces the documents by **records**. Each record holds one concern of an inquiry, under a stable identifier, and the records are linked by relations of closed and typed kinds. A presentation of that content to a reader, specified in [`ekthesis`](https://github.com/esther-poniatowski/ekthesis), references the records through their export, so the records stay the only source of the content. Three principles govern this design, each stated in an architecture decision:

- [separation of concerns](docs/adr/research-scope.md) between research, which `gnomon` specifies, and its presentation to readers, which `ekthesis` specifies;
- [one source](docs/adr/one-source-per-unit.md) for each unit of content;
- [explicit dependencies](docs/adr/closed-typed-relations.md), through typed relations that form a graph.

The **method** specifies an inquiry in [ordered stages](docs/epistemology/processes/inquiry/specification-order.md), from the problem to the questions that serve it, their subject, and the candidate answers, each a typed claim resting on models bound to the phenomenon. An assessment tests each answer against conditions of satisfaction fixed before the answer is evaluated, and an itinerary records each act of the inquiry. The stages, the tests and the choice of the next act rest on results from the philosophy of science, collected in the [epistemology of inquiry](docs/epistemology/_index.md).

The **vocabulary records** of a project separate the meaning of a term from its symbols, as the [decision on concepts, glossaries and notations](docs/adr/concepts-glossaries-notations.md) states. A concept record holds the meaning of a concept, which stays the same across projects. A notation composes each symbol from declared bases, modifiers and index sets. Glossaries and audiences serve readers, so `ekthesis` specifies them, as the [decision on the scope of gnomon](docs/adr/research-scope.md) states.

The **views** of a project are generated from its records. The operational inquiry graph connects each research product to the activities that consume or produce it. Typed inquiry relations also connect each problem to its questions, answers and assessments. The separate command `gnomon tree` retains a textual question hierarchy for explicit hierarchy inspection.

The [Gnomon–Ekphrasis boundary](docs/adr/research-scope.md#^ekphrasis-boundary) assigns the meanings, checks and generated view data to Gnomon. Ekphrasis owns form interaction and the rendering of generated views. The [interface result classes](docs/adr/findings-output.md#^interface-result-classes) distinguish software conformance, computed diagnosis and researcher-authored judgment.

The **language** states the content of each record. Every declared quantity carries a symbol, and each record declares its symbols in one table. A formula names only declared symbols, those of its own record or, by reference, those of another record of the same problem. Two consequences follow. A researcher writing a law must name quantities that a record already declares. A reader can find every declaration in one table.

The vocabulary of the method is declared in [registries](src/gnomon/data/_index.md), written by hand and stored in package data. Each declaration is documented in a specification note, and a value whose meaning the theory defines is owned by its theory note, as the [decision on registries](docs/adr/registries-as-source.md) states.

The language and the registries together serve one design goal: a record is **machine-checkable**. A check reports these classes of defect:

- a reference resolving to no declaration;
- a field left empty although the epistemic aim requires a value;
- a claim ranging beyond the members bearing it;
- a step of an itinerary whose inputs or output do not match its activity;
- a derivation whose units, orientations, segments, kernel or consequences break its rules;
- a law or a condition that is not dimensionally homogeneous;
- a presupposition or an intervention of a claim that names no admissible record.

Seven worked inquiries, from as many domains, exercise the method, and each records the limits of the method that it exposed.

---

## Features

The [capability-status guide](docs/guide/capabilities.md) is the canonical inventory of published outcomes. Each outcome is `supported`, `experimental`, `planned` or `deprecated`. These labels describe the current release. The pre-alpha package may change its interfaces before a later release.

---

## Quick start

To specify a research problem, a researcher fills one record per concern in a folder of its own. The [guide to filling the records of an inquiry](docs/guide/filling-records.md) leads through the records in order, the [record templates](src/gnomon/data/templates/_index.md) provide the complete source-authoring form, and completed records can be consulted in the [worked inquiries](examples/_index.md).

The initialization command creates the folder with a sparse starting problem, a sparse itinerary and an index in the order of filling. Optional branches stay absent for progressive disclosure in a form. The option `--with` adds another sparse record when the inquiry requires it, while `--full-template` writes the complete commented templates for source-based authoring. Then, the check command tests the filled records. The vocabulary command also collects their declared symbols and operators:

```sh
gnomon init ./my-problem
gnomon check ./my-problem
gnomon vocabulary ./my-problem
```

The [tutorial starting an inquiry from an empty folder](docs/guide/first-inquiry.md) applies these commands to a first inquiry, record by record. Every command is specified in the [CLI reference](docs/guide/cli-reference.md).

---

## Documentation

Five parts of the documentation serve the first tasks of a reader:

- [Filling the records of an inquiry](docs/guide/filling-records.md): leads a researcher from a research problem to a folder of records that the checks accept
- [Specification](docs/specification/_index.md): documents the fields of each record, when each is required and the values that it admits
- [Epistemology](docs/epistemology/_index.md): states the theory of inquiry behind the records, and its grounds in the philosophy of science
- [User guide](docs/guide/_index.md): installs the tool and looks up its commands
- [Architecture decisions](docs/adr/_index.md): finds the constraint behind a settled decision, and the change of constraint that would reopen it

The remaining parts are registered in the [documentation index](docs/_index.md).

Writing-quality rules are maintained in [hermeneia](https://github.com/esther-poniatowski/hermeneia).

Open goals, the open design decisions included, are recorded in the [project goals](TODO.md).

---

## Contributing

For setting up an environment, verifying a change or registering a new note, consult the [contribution guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the terms of the
[GNU General Public License v3.0](LICENSE).
