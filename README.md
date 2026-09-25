# Gnomon

![Maintenance](https://img.shields.io/maintenance/yes/2026)
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/gnomon)](https://github.com/esther-poniatowski/gnomon/commits/main)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.12-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Organizes a rigorous research project, by fixing the concerns that specify a research problem and by supplying a language for stating their content.

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

A theoretical research project typically holds many definitions, derivations and arguments, linked by dependencies. Two limitations are commonly observed as such a project grows. First, retrieving the results that bear on a question requires reading the prose again. Second, checking a candidate answer against the demands of its question relies on the memory of the reader. Both limitations belong to five failure modes of a [document-centric organization](docs/project-overview.md), each answered by one architectural response.

### Advantages

For specifying a research problem, `gnomon` supplies a framework and a language.

The **framework** separates that specification into four concerns, settled in this order:

- the system under study, and its observed behavior;
- the question asked about that behavior;
- the answer proposed;
- the assessment of that answer.

The order is a rule of the framework: a concern is settled only in terms that the preceding concerns have fixed. Therefore, an answer cannot be stated before the question that it answers. The specifications of each concern rest on results from the philosophy of science, collected in the [epistemology of inquiry](docs/epistemology/_index.md).

The **language** states the content of each concern. Every declared quantity carries a symbol, and each formula uses symbols that its own record declares. Two consequences follow. A researcher writing a law must name quantities that the record already declares. A reader can find every declaration in one table.

The vocabulary of the framework is declared in **registries**, written by hand and stored in package data:

- the admitted values of each closed field;
- the requirements of each epistemic aim;
- the canonical operators.

Each declaration is documented in the method notes.

The language and the registries together serve one design goal: a record is **machine-checkable**. Three classes of defect are reported:

- a reference resolving to no declaration;
- a field left open although the epistemic aim requires a value;
- a claim ranging beyond the members bearing it.

The framework has been validated against seven real research problems, each filled as a complete specification.

---

## Features

- [x] Supplies a documented template for each concern of a research problem.
- [x] Resolves every symbol, reference and formula of a research problem, and reports each identifier that resolves to no declaration.
- [x] Checks each filled record against the requirements of its epistemic aim, and each closed field against its registry.
- [x] Collects the symbols and the operators of a research problem into one table.
- [ ] Scaffolds a research workspace from a standard template.
- [ ] Validates registry files against schemas.
- [ ] Reports the inferential position of a workspace: established results, open questions, blocked entries.
- [ ] Formalizes a definition.
- [ ] Formalizes the decomposition of a question into subquestions.
- [ ] Formalizes the derivation yielding an answer.
- [ ] Names the atomic research actions of a workspace.

The capabilities not yet available are recorded in the [project goals](TODO.md).

---

## Quick start

To specify a research problem, a researcher fills one record per concern, in a directory of its own. The fields to fill are stated in the [record templates](src/gnomon/data/templates/_index.md), each with its admitted values. Completed records can be consulted in the seven [worked examples](test/_index.md).

Once the records declare their quantities, the symbols and the operators of the research problem are collected automatically, by running the following command:

```sh
gnomon vocabulary ./my-problem --markdown
```

The table is written beside the records. Three counts are reported:

- the symbols collected;
- the operators that the research problem declares;
- the symbols shared across its records.

---

## Documentation

To start using the framework, consult three parts of the documentation:

- [Epistemology](docs/epistemology/_index.md): to reach the specifications that each concern fixes, and their grounds in the philosophy of science.
- [Record templates](src/gnomon/data/templates/_index.md): to fill each record, field by field.
- [Architecture decisions](docs/adr/_index.md): to find the constraint behind a settled decision, and the change of constraint reopening the question.

The remaining parts are registered in the [documentation index](docs/_index.md).

Writing-quality rules are maintained in [hermeneia](https://github.com/esther-poniatowski/hermeneia).

Open design decisions are recorded in the [design task list](docs/TODO.md).

---

## Contributing

For setting up an environment, verifying a change or registering a new note, consult the [contribution guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the terms of the
[GNU General Public License v3.0](LICENSE).
