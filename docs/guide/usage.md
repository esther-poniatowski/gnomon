# Usage

Gnomon organizes mathematical research into a traceable graph of results,
dependencies, and open questions.

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

The following commands exist in the CLI but are not yet functional. Each prints
a stub message and exits.

### `init` — Scaffold a Research Workspace

```sh
gnomon init --target ./my-research
```

Intended behavior: create a structured workspace directory from the standard
template, mirroring the hierarchical organization of projects and modules.

### `validate` — Validate Registry Files

```sh
gnomon validate registries/
```

Intended behavior: check YAML registry files against their JSON schemas
(reasoning graph, open questions, dependencies, terminology).

### `status` — Report Inferential Position

```sh
gnomon status --target ./my-research
```

Intended behavior: summarize established results, open questions, in-progress
notes, and blocked entries within a workspace.

## Data Templates

The package ships template files under `src/gnomon/data/`, accessible at
runtime via `gnomon.data_path()`. Five subdirectories provide starter content
for consuming projects:

| Directory      | Contents                                                    |
| -------------- | ----------------------------------------------------------- |
| `contracts/`   | Per-note-type contract templates (pre-draft and post-draft) |
| `registries/`  | YAML templates for reasoning graphs, questions, terms, deps |
| `schemas/`     | JSON schemas for validating registry files                  |
| `specs/`       | Note type specifications (sections, strategies, scope)      |
| `workflow/`    | Staged pipeline definitions and the audit protocol          |
