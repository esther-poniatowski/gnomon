# Contributing to "gnomon"

> [!IMPORTANT]
> To contribute effectively, please conform to those guidelines and use the provided templates.

## Submitting issues

To submit a new issue:

1. In the repository page, navigate to the "Issues" tab and click on "New Issue".
2. Select and fill the issue template.
3. Add relevant labels, assignees, and milestone if applicable.

## Developing the code

Contributions to the codebase should be developed in a local clone of the repository. Follow these steps to set up a development environment:

### Installation

1. Initialize a local copy of the repository:

   ```sh
   cd /path/to/local/directory
   git clone git@github.com:esther-poniatowski/gnomon.git
   ```

2. Create a virtual environment containing the development dependencies:

   ```sh
   cd  gnomon
   conda env create -f environment.yml
   ```

   By default, the environment will be named `gnomon`, as specified in the `environment.yml` file. This name can be modified by passing the `-n` option.

3. Register the packages in "editable mode":

   ```sh
   conda activate gnomon
   pip install -e /src/gnomon
   ```

### Using the commit message template

1. Edit the commit template (`.gitmessage`, at the root of the repository) to specify the name and email address of the committer.

2. Configure `git` to use this file as a commit template:

   ```sh
   git config commit.template .gitmessage
   ```

3. Verify the configuration:

   ```sh
   git config --get commit.template
   ```

### Commit message format

> [!NOTE]
> To write a commit message with this template, adhere to the following format:

- Capitalize the subject, do not add a period at the end
- Limit the subject line to 50 characters
- Use the imperative mood in the subject line
- Separate subject from body with a blank line
- Wrap the body at 72 characters per line
- Use the body to explain what and why (not how)
- Add references to issues or other commits using [GitHub keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests)

### Verifying a change

A change is verified by the narrowest checks that exercise it. A change to a shared template reaches every dependent fixture and every downstream template, so those fixtures and templates are checked in the same pass.

- **Alignment of notes and templates:** each row of a method table resolves to one key, in the same order, and every key of a template is documented.
- **Symbol resolution:** each symbol is unique within its record, and every reference and every identifier of a formula resolves to a declaration. Each rule carries a planted negative case that fails for the intended reason.
- **YAML integrity:** every template and every fixture parses, keeps its `id` and its `type`, and holds no uppercase placeholder.
- **Reference integrity:** each identifier pointing to another record, and each Markdown link, resolves to one existing target.
- **Downstream consistency:** a change to a requirement of the epistemic task updates every field of an answer or an assessment that reads that requirement.

## Owner of each contract

Each contract of the framework has one owning file. A contributor reads that file before editing any file that depends on the contract.

- The [expression language](docs/epistemology/symbols-and-expressions.md) fixes the syntax of symbols, expressions and signatures.
- The [specification method](docs/epistemology/_index.md) fixes the meaning of every inquiry field and the options that the field admits.
- The [record templates](src/gnomon/data/templates/_index.md) fix the machine-readable shape of each record and the order of its keys.
- The tests of [template alignment](tests/test_gnomon/test_template_alignment.py) and of [symbol resolution](tests/test_gnomon/test_symbol_resolution.py) enforce that each method table aligns with its template, and that every symbol and every reference resolves.

## Writing documentation

Every Markdown file under `docs/` is a note: it declares its metadata in a YAML frontmatter block, and it is registered in the index of the folder holding it. A file that satisfies neither is invisible to a reader navigating by index, and is effectively lost while appearing to exist.

### Frontmatter block

Three keys open every note, in this order:

```yaml
---
tags:
  - criteria
index: "[Framework-level criteria](docs/design/1-framework/_index.md)"
aliases:
  - Cost and Ergonomics (criteria)
---
```

- `tags` names the kind of the note, drawn from the vocabulary below.
- `index` links the entry point of the folder holding the note, as a Markdown link whose path starts at the repository root. An `_index.md` points one level up instead, at the index of its parent folder; the documentation root has no parent and omits the key.
- `aliases` fixes the name under which the note is cited. Each alias is unique across `docs/`.

The order is fixed, so that a divergence shows up in a diff.

| Tag                | Kind of note                                      |
|--------------------|---------------------------------------------------|
| `index`            | Folder entry point                                |
| `overview`         | Statement of what the project is for              |
| `tasks`            | Open work on the design                           |
| `guide`            | Operation of the installed tool                   |
| `criteria`         | Framework-level criteria (Tier 1)                 |
| `tensions`         | Tensions holding between framework criteria       |
| `architecture`     | Architectural commitment (Tier 2)                 |
| `gaps`             | Architectural gaps not yet operationalized        |
| `aspect`           | Aspect-specific decisions (Tier 3)                |
| `handoff`          | State a new contributor resumes from              |
| `table`            | Registry consulted during a migration             |
| `examples`         | Expressivity test cases and their resolutions     |
| `ideas`            | Material awaiting triage                          |
| `reference`        | External work, stated on its own terms            |
| `backup`           | Superseded proposal, carried alongside a kind tag |
| `object-candidate` | One candidate object kind                         |

### Registering a note

Each folder carries an `_index.md` registering every file it holds, images included. Register a new file in the same edit that creates it: a later pass answers a different concern and leaves orphans behind.

An entry names the note and states what a reader obtains from it, so that a reader chooses one file rather than opening several.

### Cross-references

A cross-reference is a relative Markdown link carrying the `.md` extension, so that it resolves both in an editor and on the repository page:

```markdown
the [conditions on a canonical object](../2-architecture/object-kinds.md)
```

A finer reference appends a block anchor, declared at the end of the target line:

```markdown
[object-kind set smallness](../2-architecture/object-kinds.md#^t2-ontology-small)
```

Link text names the result, the object, or the message found at the target, never the file name and never a bare category word.

Renaming a note, an anchor or an identifier requires updating every inbound reference in the same change, so that no link is left dangling.

### Source entries

A note cites a work by a key of the form `authYYYY`, placed as a tail tag after the claim it supports. The "Sources" section of the note lists every cited key once, in alphabetical order, in the following form:

```markdown
- [craver2007] ◐ [Craver, *Explaining the Brain*, Oxford University Press, 2007](https://philpapers.org/rec/CRAETB-2)
```

The mark after the key states how the entry was checked, so that a reader can judge how far to rely on it: ✓ the text was read in full · ◐ the entry was checked through an abstract, the publisher page, or a secondary summary · ○ the entry is cited from standard knowledge without a check. ^reading-marks

## Configuration file organization

This project separates configuration concerns between two locations:

### `pyproject.toml` — Project management

Contains only build system, package metadata, dependencies, entry points, and tool configurations that **must** reside in `pyproject.toml` (because the tool does not support external config paths):

- `[build-system]` — Build backend (setuptools)
- `[project]` — Name, version, authors, license, description, keywords, classifiers, URLs
- `[project.dependencies]` — Runtime dependencies
- `[project.optional-dependencies]` — Optional dependency groups
- `[project.scripts]` — CLI entry points
- `[tool.setuptools]` — Package discovery and source layout
- `[tool.pytest.ini_options]` — Pytest settings (pytest does not support custom config paths)

### `config/tools/` — Tool-specific settings

Contains dedicated configuration files for each development tool. This achieves modular, tool-specific settings that are decoupled from the main project file:

| File                  | Tool                   | Purpose                           |
|-----------------------|------------------------|-----------------------------------|
| `black.toml`          | Black                  | Code formatting rules             |
| `mypy.ini`            | MyPy                   | Static type checking rules        |
| `pylintrc.ini`        | Pylint                 | Linting rules (main code)         |
| `pylintrc_tests.ini`  | Pylint                 | Linting rules (test code)         |
| `pyrightconfig.json`  | Pyright                | Static type analysis overrides    |
| `releaserc.toml`      | Python Semantic Release| Versioning and changelog           |

### `config/dictionaries/` — Spell checking

Custom word lists for CSpell (VS Code spell checker):

| File          | Contents                    |
|---------------|-----------------------------|
| `project.txt` | Project-specific terms      |
| `python.txt`  | Python language terms       |
| `tools.txt`   | Development tool names      |

### Rationale

- **Modularity**: Each tool's configuration is self-contained and independently editable.
- **Clarity**: `pyproject.toml` stays concise and focused on project identity.
- **Discoverability**: Tool configs are grouped in a single directory, easy to locate.
- **Flexibility**: Tools with complex configs (Pylint, MyPy) benefit from dedicated files with inline comments explaining each setting.
