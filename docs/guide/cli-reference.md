---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - CLI reference
---
# CLI Reference

All commands are invoked through the `gnomon` entry point.

## Global Options

| Option            | Description                          |
| ----------------- | ------------------------------------ |
| `--version`, `-v` | Print the package version and exit.  |
| `--help`          | Print the help message and exit.     |

## `info`

Print version and platform diagnostics.

```sh
gnomon info
```

**Arguments:** none.

**Output:** one line containing the package name, version, operating system, and Python version.

## `init`

> Stub — prints "Research workspace scaffolding is not yet implemented."

Scaffold a research workspace into a target directory.

```sh
gnomon init --target <dir>
```

| Option           | Default | Description                  |
| ---------------- | ------- | ---------------------------- |
| `--target`, `-t` | `.`     | Target workspace directory.  |

## `validate`

> Stub — prints "Registry validation is not yet implemented."

Validate registry files against their JSON schemas.

```sh
gnomon validate <paths...>
```

| Argument   | Description                                  |
| ---------- | -------------------------------------------- |
| `<paths>`  | One or more registry files or directories.   |

## `status`

> Stub — prints "Workspace status reporting is not yet implemented."

Report the inferential position of a research workspace: established results, open questions, in-progress notes, and blocked entries.

```sh
gnomon status --target <dir>
```

| Option           | Default | Description                      |
| ---------------- | ------- | -------------------------------- |
| `--target`, `-t` | `.`     | Research workspace directory.    |

## `vocabulary`

An author choosing a symbol for a new quantity needs every symbol and operator that the records of one problem already declare. The `vocabulary` command collects them from the filled records of a problem folder into a vocabulary record, and optionally into a Markdown table beside it. Running it from the workspace root writes both files into the problem folder:

```sh
gnomon vocabulary <directory> --markdown
```

| Argument      | Description                                      |
| ------------- | ------------------------------------------------ |
| `<directory>` | Folder holding the filled records of one problem. |

| Option             | Default          | Description                                                                 |
| ------------------ | ---------------- | --------------------------------------------------------------------------- |
| `--output`, `-o`   | `vocabulary.yml` | Name of the vocabulary record written inside the problem folder.           |
| `--markdown`, `-m` | off              | Also write the Markdown table, named after the record.                     |
| `--root`, `-r`     | `.`              | Workspace root from which the table links the index of the problem folder. |

**Output:** one line with the number of symbols, the number of operators that the problem declares, and the number of symbols reused across its records. The command exits with an error, before writing any file, when the problem folder lies outside the workspace root.
