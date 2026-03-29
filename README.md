# Gnomon

[![Maintenance](https://img.shields.io/maintenance/yes/2026)]()
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/gnomon)](https://github.com/esther-poniatowski/gnomon/commits/main)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.12-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Organizes mathematical research into a traceable graph of results, dependencies, and open questions.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Overview

### Motivation

Mathematical research produces many interconnected results, definitions, and open
questions. As a project grows, it becomes difficult to track what has been established,
what depends on what, and where gaps remain. Without formal structure, notes accumulate
without clear inferential relationships, leading to redundant derivations and lost context.

### Advantages

Gnomon treats a research workspace as a directed graph of inferential dependencies
rather than a flat collection of documents:

- **Typed notes**: Each note serves a precise role (problem, result, definition, tool,
  synthesis, comparison, frontier) with structural constraints that prevent scope drift.
- **Formal contracts**: Every note begins with a binding specification that fixes its
  scope, dependencies, and expected contribution before drafting begins.
- **Machine-readable registries**: Reasoning graphs, dependency maps, open questions,
  and terminology are maintained as structured YAML files that both humans and tools
  can query.
- **Hierarchical workspace**: Research is organized at workspace, project, and module
  scales, each with its own governance, registries, and frontier tracking.

---

## Features

- [ ] Scaffold a structured research workspace from a standard template.
- [ ] Validate registry files against schemas.
- [ ] Report the inferential position of a workspace: established results, open
  questions, in-progress notes, and blocked entries.
- [ ] Track upstream revisions and propagate instability warnings to downstream
  consumers.

---

## Installation

### Using pip

Install from the GitHub repository:

```bash
pip install git+https://github.com/esther-poniatowski/gnomon.git
```

### From Source

1. Clone the repository:

      ```bash
      git clone https://github.com/esther-poniatowski/gnomon.git
      ```

2. Install in editable mode:

      ```bash
      cd gnomon
      pip install -e ".[dev]"
      ```

---

## Usage

### Command Line Interface (CLI)

Scaffold a research workspace:

```sh
gnomon init --target ./my-research
```

Validate registry files against their schemas:

```sh
gnomon validate registries/
```

Report the current inferential position of the workspace:

```sh
gnomon status
```

Display version and platform diagnostics:

```sh
gnomon info
```

---

## Documentation

Design documents are maintained in [`docs/design/`](docs/design/):

- [Workspace architecture](docs/design/methods/workspace-architecture.md) --- Directory
  layout and hierarchical organization.
- [Formal contracts](docs/design/methods/formal-contracts.md) --- Per-note inferential
  specifications.
- [Note types](docs/design/methods/note-types.md) --- Structural constraints for each
  note type.
- [Registries](docs/design/methods/registries.md) --- Machine-readable project state
  and reasoning graphs.
- [Procedural workflows](docs/design/methods/procedural-workflows.md) --- Staged
  pipelines and pass model.
- [Quality criteria](docs/design/quality-criteria/) --- Reasoning principles and
  decision rules.

Writing-quality rules are maintained in
[hermeneia](https://github.com/esther-poniatowski/hermeneia). Note-governance
audits and workflow gates are maintained in gnomon.

---

## Contributing

Please refer to the [contribution guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).
