# Gnomon

![Maintenance](https://img.shields.io/maintenance/yes/2026)
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/gnomon)](https://github.com/esther-poniatowski/gnomon/commits/main)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.12-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Specifies a research inquiry as typed records, from the problem that it addresses to the assessment of its answers, checks those records against the method that they follow, and projects them into expositions for declared audiences.

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
- guide the inquiry, by naming the next act that the current state and the target question call for;
- project the inquiry into expositions for an audience, which add only announcements, connectors and syntheses.

### Advantages

`gnomon` replaces the documents by **records**. Each record holds one concern of an inquiry, under a stable identifier, and the records are linked by relations of closed and typed kinds. Expositions are generated from the records and never edited, so the records stay the only source of the content. Three principles govern this design, each stated in an architecture decision:

- [separation of concerns](docs/adr/expositions-as-projections.md) between research content and its exposition;
- [one source](docs/adr/one-source-per-unit.md) for each unit of content;
- [explicit dependencies](docs/adr/closed-typed-relations.md), through typed relations that form a graph.

The **method** specifies an inquiry in [ordered stages](docs/epistemology/inquiry/specification-order.md), from the problem to the questions that serve it, their subject, and the candidate answers, each a typed claim resting on models bound to the phenomenon. An assessment tests each answer against conditions of satisfaction fixed before the answer is evaluated, and an itinerary records each act of the inquiry. The stages, the tests and the choice of the next act rest on results from the philosophy of science, collected in the [epistemology of inquiry](docs/epistemology/_index.md).

The **vocabulary records** of a project separate the meaning of a term from its names, as the [decision on concepts, glossaries and notations](docs/adr/concepts-glossaries-notations.md) states. A concept record holds the meaning of a concept, which stays the same across projects. A glossary holds the names of the concepts of a project, with the forms forbidden for given audiences. A notation composes each symbol from declared bases, modifiers and index sets. An audience specification records the knowledge and the register of a readership, and a project specification binds one glossary, one notation and the audiences of a project to its inquiry, as the [decision on terminology, audience and project specifications](docs/adr/terminology-audience-project-specifications.md) states.

**Expositions** form a second family of records, beside the research records. An exposition selects research units, orders them for an audience, and adds only announcements, connectors and syntheses, so that every statement carrying content traces to a research record, as the [decision on expositions](docs/adr/expositions-as-projections.md) states. The terms of an exposition are checked against its glossary and against the audiences that its design brief cites.

The **language** states the content of each record. Every declared quantity carries a symbol, and each record declares its symbols in one table. A formula names only declared symbols, those of its own record or, by reference, those of another record of the same problem. Two consequences follow. A researcher writing a law must name quantities that a record already declares. A reader can find every declaration in one table.

The vocabulary of the method is declared in [registries](src/gnomon/data/_index.md), written by hand and stored in package data, and each declaration is documented in a specification note.

The language and the registries together serve one design goal: a record is **machine-checkable**. Four classes of defect are reported:

- a reference resolving to no declaration;
- a field left empty although the epistemic aim requires a value;
- a claim ranging beyond the members bearing it;
- a step of an itinerary whose inputs or output do not match its activity.

Seven worked inquiries, from as many domains, exercise the method, and each records the limits of the method that it exposed.

---

## Features

- [x] Supplies a documented template for each record of an inquiry.
- [x] Resolves every symbol, reference and formula of a research problem, and reports each identifier that resolves to no declaration.
- [x] Checks each filled record against the requirements of its epistemic aim, and each closed field against its registry.
- [x] Collects the symbols and the operators of a research problem into one table.
- [x] Checks each step of an itinerary of inquiry against the registry of epistemic activities.
- [x] Formalizes the decomposition of a question into subquestions.
- [ ] Scaffolds a research workspace from a standard template.
- [ ] Validates each record against the schema of its type.
- [ ] Reports the open conditions of each question, and the acts ready to perform.
- [ ] Computes the comparison of a model with the data through its binding.
- [ ] Records each concept of a project with one meaning, and its names in a glossary.
- [ ] Composes the symbols of a notation from declared bases, modifiers and index sets, and generates the LaTeX macros of an exposition.
- [ ] Specifies the audiences of a project, and the project specification that binds its glossary, its notation and its audiences.
- [ ] Specifies expositions that select and order research units for an audience, and renders them without adding content.
- [ ] Checks the terms of an exposition against its glossary and the forms forbidden for its audiences.
- [ ] Formalizes a definition.
- [ ] Formalizes the derivation yielding an answer.
- [ ] Derives the epistemic activities from a smaller set of primitive actions.

The capabilities not yet available are recorded in the [project goals](TODO.md).

---

## Quick start

To specify a research problem, a researcher fills one record per concern in a folder of its own, from the [record templates](src/gnomon/data/templates/_index.md). The [guide to filling the records of an inquiry](docs/guide/filling-records.md) leads through the records in order, and completed records can be consulted in the [worked inquiries](examples/_index.md).

The two commands below check a filled folder. The first collects the symbols and the operators that its records declare, and the second checks each step of its itineraries against the registry of epistemic activities:

```sh
gnomon vocabulary ./my-problem --markdown
gnomon itinerary ./my-problem
```

Every command is specified in the [CLI reference](docs/guide/cli-reference.md).

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
