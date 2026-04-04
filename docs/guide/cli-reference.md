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

**Output:** one line containing the package name, version, operating system,
and Python version.

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

Report the inferential position of a research workspace: established results,
open questions, in-progress notes, and blocked entries.

```sh
gnomon status --target <dir>
```

| Option           | Default | Description                      |
| ---------------- | ------- | -------------------------------- |
| `--target`, `-t` | `.`     | Research workspace directory.    |
