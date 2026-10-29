---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Usage
---
# Usage

Gnomon organizes mathematical research into a traceable graph of results, dependencies, and open questions.

## Diagnostics

The `info` command prints the package version and platform details:

```sh
gnomon info
```

Example output:

```text
gnomon 0.0.0 | Platform: Darwin Python 3.12.4
```

The `--version` / `-v` flag prints only the version string:

```sh
gnomon --version
```

## Planned Commands

The following commands exist in the CLI but are not yet functional. Each prints a stub message and exits.

### `init` — Scaffold a Research Workspace

```sh
gnomon init --target ./my-research
```

Intended behavior: create a structured workspace directory from the standard template, mirroring the hierarchical organization of projects and modules.

### `validate` — Validate Records

```sh
gnomon validate ./my-research
```

Intended behavior: check each record against the schema of its type.

### `status` — Report Inferential Position

```sh
gnomon status --target ./my-research
```

Intended behavior: summarize established results, open questions, in-progress notes, and blocked entries within a workspace.

## Data Templates

The package ships its data under `src/gnomon/data/`, accessible at runtime via `gnomon.data_path()`. The subdirectories below hold the content that consuming projects use:

| Directory      | Contents                                                          |
| -------------- | ----------------------------------------------------------------- |
| `registries/`  | Registries of the epistemic activities and of the product types   |
| `schemas/`     | JSON Schemas of the record types, planned under `record-schemas`  |
| `templates/`   | Record templates, one per concern of an inquiry                   |
