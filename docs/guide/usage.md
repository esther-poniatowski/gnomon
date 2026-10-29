---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Usage
---
# Usage

The purpose of `gnomon` is stated in the [overview of the README](../../README.md#overview). This page shows the commands of the installed tool on the records of one problem. Their arguments and options are listed in the [command reference](cli-reference.md).

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

## Checks on the records of a problem

Two commands read the filled records of one problem folder.

The `vocabulary` command collects the symbols and the operators that the records declare, so that an author can choose the symbol of a new quantity. The command writes a vocabulary record into the folder, and a Markdown table beside it with the option `--markdown`:

```sh
gnomon vocabulary ./my-research/my-problem --markdown
```

The `itinerary` command checks every itinerary of the problem against the registries of activities and of product types, and against the records that its steps name. The command prints one line per defect and a summary line, and it exits with an error when it finds a defect:

```sh
gnomon itinerary ./my-research/my-problem
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
