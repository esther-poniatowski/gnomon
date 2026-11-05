---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - CLI reference
---
# CLI reference

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

**Output:** one line containing the package name, version, operating system, and Python version, such as `gnomon 0.0.0 | Platform: Darwin Python 3.12.4`.

## `init`

A researcher starting a problem needs the record templates in a folder of its own, in the order in which they are filled. The `init` command creates that folder with the itinerary, opened with the problem, and with the templates of the first four stages of the [order of specification](../epistemology/processes/inquiry/specification-order.md): the problem, the question, the target system, the phenomenon, the background and the operators. The index of the folder lists them stage by stage, each with the goal of its record.

```sh
gnomon init <directory> [--with KIND]... [--force]
```

| Argument or option | Description                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `<directory>`      | Folder of the new problem, created when it does not exist.                                                                               |
| `--with`, `-w`     | A further record kind to scaffold: `model`, `key`, `binding`, `answer`, `assessment`, `concept`, `design` or `derivation`; repeat it for several. |
| `--force`          | Overwrite the files that already exist.                                                                                                  |

**Output:** one line per file written, then the next step. The command writes no file and exits with code 1 when one of the files exists and `--force` is not given, or when a kind has no template.

## `validate`

Validate each record against the contract that its field `_schema` names, such as `gnomon:answer@1`. A record whose type has no schema, such as a generated vocabulary, is skipped. The command prints each violation with the path of its field, and exits with a nonzero code when any record breaks its contract.

```sh
gnomon validate <paths...>
```

| Argument   | Description                                  |
| ---------- | -------------------------------------------- |
| `<paths>`  | One or more record files or directories.     |

## `check`

A researcher needs to know, before an answer is assessed, whether the records of a problem hold the specifications that the method requires. The `check` command runs every check of `gnomon` on a directory tree:

- the resolution of each symbol, operator and reference;
- the specifications that each record kind, each aim and each level of commitment require;
- the consistency between records, such as the classification of each operation of a model by a ground of the answer, the binding of an answer whose question names outputs to match, and the pair of each target status;
- the steps of each itinerary;
- the rules of each derivation record, as the [checks of a derivation](../specification/derivation.md#^derivation-checks) state them, and the descent of each law marked derived;
- the dimensional homogeneity of the laws and the conditions of a problem that declares a dimensional formula;
- the presuppositions and the interventions of the claim of each answer.

Each folder that holds records is checked as one problem, and a reference may reach a record of any folder. A generated record, such as a vocabulary, is not checked. A template not yet started, whose identifier is still the placeholder of its template, is listed apart and not checked, so a folder can be checked after each stage of filling.

```sh
gnomon check <directory> [--format text|yaml|sarif] [--output PATH]
```

| Argument or option | Description                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `<directory>`      | Directory of records, read recursively.                                                                             |
| `--format`, `-f`   | `text` (default), `yaml` for a report, or `sarif` for a log in the findings profile of the gate Elenchos. |
| `--output`, `-o`   | File receiving the report instead of standard output; its missing folders are created.                              |

**Output:** in `text`, one line per finding with its file, its record, its rule and its message, then one line counting the records and the findings. The `yaml` report groups the findings by file, holds no date and no absolute path, and sorts its content, so two runs on unchanged records write the same file; a renderer of the workspace, such as Ekphrasis in Obsidian, presents it. Paths are stated relative to `<directory>`. The command exits with code 1 when it reports a finding or cannot read a file, and with code 2 when it cannot write the report.

## `schemas`

Write the contract of each record type and its template, generated from the base schemas in `src/gnomon/data/schemas/` and from the vocabulary registry. With `--check`, the command writes nothing, reports each generated file that differs from its generated form, and exits with a nonzero code when one does.

```sh
gnomon schemas [--check]
```

| Option    | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `--check` | Report the stale generated files instead of writing them.          |

## `status`

A researcher choosing the next act of an inquiry needs the conditions that block each question and the acts that can lift them. The `status` command applies the [choice of the next act](../procedures/inquiry/next-act.md) to the records of a directory tree, question by question and route by route:

- the state of each [condition for obtaining an answer](../epistemology/objects/question/conditions-of-answerability.md#^condition-states), read from the block `answerability` of the question, else from a field that shows it, else `not-established`;
- the open conditions, each with the activities that act on it, and whether each activity is ready, its required inputs held by records of the problem that no failed step impeached;
- the refuted conditions, which call for a revision;
- the steps whose record is stabilized while their verdict is pending, so that their norm is judged anew, and the impeached records;
- for each revision that a step records, the dependents that it flags, by the [kind of the revision](../epistemology/objects/knowledge/grounds-and-dependence.md#^revision-kinds) and the warrant of each dependent, and those that the researcher has not yet reviewed.

```sh
gnomon status <directory> [--format text|yaml] [--output PATH]
```

| Argument or option | Description                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------- |
| `<directory>`      | Directory of records, read recursively; each folder is one problem.                      |
| `--format`, `-f`   | `text` (default), one line per open or refuted condition, or `yaml`, the full diagnosis. |
| `--output`, `-o`   | File receiving the report instead of standard output; its missing folders are created.   |

**Output:** the `yaml` report holds no date and no absolute path, so two runs on unchanged records write the same file. A state that the records do not show stays `not-established` until the researcher asserts it with pointers, so the diagnosis never replaces a judgment. The command exits with code 1 when a file cannot be read, and with code 2 when the report cannot be written.

## `vocabulary`

An author choosing a symbol for a new quantity needs every symbol and operator that the records of one problem already declare. The `vocabulary` command collects them from the filled records of a problem folder into a vocabulary record, with the LaTeX form of each symbol. The record is a YAML view bound to the schema `gnomon:view.vocabulary@1` of the [view schemas](../../src/gnomon/data/views/_index.md), so a renderer displays it as it displays the other views. The command below writes it into the problem folder:

```sh
gnomon vocabulary <directory>
```

| Argument      | Description                                      |
| ------------- | ------------------------------------------------ |
| `<directory>` | Folder holding the filled records of one problem. |

| Option             | Default          | Description                                                                 |
| ------------------ | ---------------- | --------------------------------------------------------------------------- |
| `--output`, `-o`   | `vocabulary.yml` | Name of the vocabulary record written inside the problem folder.           |

**Output:** one line with the number of symbols, the number of operators that the problem declares, and the number of symbols reused across its records. The command exits with an error, before writing any file, when the problem folder does not exist.

## `itinerary`

An author who has filled the itineraries of a problem needs to know whether each step takes the products that its activity requires. The `itinerary` command checks every itinerary record of one problem folder against the registries of activities and of product types, and against the records that its steps name. The conditions of the check are stated in the [itinerary check](../epistemology/processes/activities/epistemic-activities.md#^itinerary-check), and the checks on the fields of an itinerary in the [itinerary record](../specification/itinerary.md#^record-checks).

```sh
gnomon itinerary <directory> [--format text|sarif] [--output PATH] [--root PATH]
```

| Argument or option | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `<directory>`      | Folder holding the filled records of one problem.                                                 |
| `--format`, `-f`   | `text` (default) or `sarif`, a log in the findings profile of the gate Elenchos.                  |
| `--output`, `-o`   | With `sarif`, file receiving the log instead of standard output; its missing folders are created. |
| `--root`, `-r`     | With `sarif`, root against which the log states every path; the current folder by default.        |

**Output:** one line per defect, prefixed with the identifier of its itinerary, then one line with the number of itineraries checked and the number of defects found. The command exits with code 1 when it finds a defect, or when the folder does not exist.

With `--format sarif`, the [findings output](../adr/findings-output.md#^command-output) states the content of the log and the exit statuses. When the log takes standard output, the text lines go to standard error.

## `views`

A researcher who proceeds by local increments needs the global state of the research. The `views` command writes seven views of a directory tree of records, each as a YAML record that a renderer such as Ekphrasis displays as a read-only form:

- the state of each problem: its demand met, its accepted answers and its candidates, and its obstacles, stated and shown;
- the open conditions and the ready acts, the diagnosis of `gnomon status` as tables;
- the exposure of each answer: every revisable unit reached by walking its dependencies back, with its kind and the reason of the exposure;
- the progress of each itinerary: its steps in the order of their dependencies, sound, conditional or impeached, with the edges between them;
- the maturity of each record and of its marked fields;
- the question tree, as nodes and edges;
- the statement of each question, authored and composed from its subject and its aim in the [statement frame](../epistemology/objects/subject/subject-of-inquiry.md#^question-statement), with the slots left unfilled by its fields;
- the LaTeX form of each expression of each record, composed from the notations of its symbols and of the operators of its target system.

```sh
gnomon views <directory> [--output DIR]
```

| Argument or option | Description                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| `<directory>`      | Directory of records, read recursively; each folder is one problem.                  |
| `--output`, `-o`   | Folder receiving the views; the folder `views` of `<directory>` by default.          |

**Output:** one file per view, named after the view, each declaring the schema `gnomon:view.<name>@<version>` of the [view schemas](../../src/gnomon/data/views/_index.md), which the schema registry of the renderer maps to its file. A view holds no date and no absolute path, so two runs on unchanged records write the same files, and `gnomon check` skips the views. The command exits with code 1 when a file cannot be read, and with code 2 when a view cannot be written.

## `tree`

A researcher reading a project needs its questions and their answers at a glance. The `tree` command prints the question tree of a directory, read recursively, from its problems to the assessments of its answers.

```sh
gnomon tree <directory>
```

**Output:** one indented line per record, with its kind, its identifier, its title and its status. A file that cannot be read is reported on standard error, and the command exits with code 1 only when the folder does not exist.
