---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - CLI reference
---
# CLI reference

All commands are invoked through the `gnomon` entry point. Validation, checks, diagnoses and authored verdict fields use the [interface result classes](../adr/findings-output.md#^interface-result-classes). These classes distinguish software conformance and computed diagnosis from researcher-authored judgment.

## Global Options

| Option            | Description                          |
| ----------------- | ------------------------------------ |
| `--version`, `-v` | Print the package version and exit.  |
| `--help`          | Print the help message and exit.     |

## `info`

Print version and platform diagnostics. ^cli-info

```sh
gnomon info
```

**Arguments:** none.

**Output:** one line containing the package name, version, operating system, and Python version, such as `gnomon 0.0.0 | Platform: Darwin Python 3.12.4`.

## `setup`

Install the complete Gnomon schema closure in an existing Obsidian vault. The command copies the current record contracts, view contracts and referenced base schemas from the installed package. It writes a registry whose paths start from the vault root, so the vault does not need to contain the Gnomon checkout. ^cli-setup

```sh
gnomon setup <vault> [--registry PATH] [--schema-directory DIRECTORY] [--force]
```

| Argument or option | Description |
| ------------------ | ----------- |
| `<vault>` | Existing Obsidian vault that receives the registry and schema resources. |
| `--registry` | Vault-relative registry path; `.gnomon/schema-registry.yml` by default. |
| `--schema-directory` | Vault-relative resource directory; `.gnomon/schemas` by default. |
| `--force` | Replace a generated target whose current content differs from the installed package. |

The registry and resource directory are independent settings. Neither path may be absolute or leave the vault. A repeated command retains identical files. A changed target stops the operation before any file is written unless `--force` is present.

**Output:** one line counts the schema files, written files and unchanged files. The final line gives the exact vault-relative path to enter under **Schema registry** in the Ekphrasis settings. The command exits with code 1 for a missing vault, an unsafe path, an incomplete installed package, a conflicting target or a write failure.

## `init`

To start an inquiry, a researcher selects the active problem or question. The `init` command creates that sparse record, a sparse itinerary and an index. A sparse record includes its designation and the fields required at its first operational stage, while optional branches remain absent. A new folder defaults to `problem`; the option `--start-with question` begins the [adoption route](adopting-existing-research.md) from one active question. When the command later adds records to a folder that holds a question but no problem, omission of `--start-with` preserves the question-led route. ^cli-init

```sh
gnomon init <directory> [--start-with problem|question] [--with KIND]... [--full-template] [--force] [--dry-run] [--yes]
```

| Argument or option | Description                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `<directory>`      | Inquiry folder, created when it does not exist.                                                                                           |
| `--start-with`     | Starting record kind. A new folder defaults to `problem`; a question-only folder retains `question` when this option is omitted.          |
| `--with`, `-w`     | A further record kind to scaffold, including `question`, `target-system`, `phenomenon`, `background`, `operators`, `model`, `key`, `binding`, `answer`, `assessment`, `concept`, `design` or `derivation`; repeat it for several. |
| `--full-template`  | Write the complete commented templates instead of sparse records.                                                                         |
| `--force`          | Preserve and replace records and the index that already exist.                                                                            |
| `--dry-run`        | List every file that would be written or backed up without changing the folder.                                                           |
| `--yes`, `-y`      | Proceed without asking before files are backed up and replaced.                                                                           |

In a folder that already holds records, the command writes only the missing records. The command registers each new record in the existing index and keeps every other line of that index. With the force option `--force`, the command copies each existing target under `.gnomon-backup` before replacing it. The command asks before replacing files unless the yes option `--yes` is present. An existing backup stops the command.

**Output:** the command reports each file written or backed up. The output also states the index state `written`, `updated` or `kept`, the number of existing files kept and the next step. A dry run reports the complete write set without writing. The command exits with code 1 when a kind has no template or the command cannot create a safe backup.

## `register`

Add an existing Gnomon YAML record to the `_index.md` in its folder. The command reads the record's published `_schema` contract and derives the entry label, purpose and stage from Gnomon's template index. A caller therefore supplies no Gnomon ordering or Markdown rules. ^cli-register

```sh
gnomon register <record>
```

| Argument | Description |
| -------- | ----------- |
| `<record>` | Existing `.yml` or `.yaml` Gnomon record in an inquiry folder that already contains `_index.md`. |

The command preserves every existing line and inserts the new entry under its canonical stage. It encodes spaces and punctuation in the selected filename. A repeated call keeps the index unchanged. A malformed record, an unpublished or foreign contract, a missing sibling index, or a concurrent change stops the command without replacing the current index.

**Output:** one line names the index and reports `updated` or `kept`. Ekphrasis can use this idempotent command as its configured post-creation command:

```json
["-m", "gnomon", "register", "{vault}/{path}"]
```

## `validate`

Validate each record against the contract that its field `_schema` names, such as `gnomon:answer@3`. A record whose type has no schema, such as a generated vocabulary, is skipped, and a template not yet started, whose identifier still holds its placeholder, is counted apart. The command prints each violation with the path of its field, then one line counting the records checked, the errors found and the templates not yet filled. The command exits with a nonzero code when any record breaks its contract. ^cli-validate

Each schema defect has the result class `contract validation`. A clean result establishes only that the record follows its schema. The validation establishes no truth or warrant for the claims.

```sh
gnomon validate <paths...>
```

| Argument   | Description                                  |
| ---------- | -------------------------------------------- |
| `<paths>`  | One or more record files or directories.     |

## `check`

A researcher needs to know, before an answer is assessed, whether the records of a problem hold the specifications that the method requires. The `check` command runs every check of `gnomon` on a directory tree: ^cli-check

- the contract that each record names in its field `_schema`: the type of each field, the fields admitted, and their forms, each violation stated with its repair;
- the resolution of each symbol, operator and reference;
- the specifications that each record kind, each aim and each level of commitment require;
- the consistency between records, such as the classification of each operation of a model by a ground of the answer, the binding of an answer whose question names outputs to match, and the pair of each target status;
- the steps of each itinerary;
- the rules of each derivation record, as the [checks of a derivation](../specification/derivation.md#^derivation-checks) state them, and the descent of each law marked derived;
- the dimensional homogeneity of the laws and the conditions of a problem that declares a dimensional formula;
- the presuppositions and the interventions of the claim of each answer.

Each folder that holds records is checked as one problem, and a reference may reach a record of any folder. A generated record, such as a vocabulary, is not checked. A template not yet started, whose identifier is still the placeholder of its template, is listed apart and not checked, so a folder can be checked after each stage of filling. In a started record, every command reads a field that still holds its placeholder, or a block left as the template wrote it, as empty, and the check reports each such leftover once.

Schema defects have the result class `contract validation`. The other reported defects have the class `method-conformance finding`. A clean check establishes only that the records follow the encoded contract and method rules. The check establishes no truth or acceptance for a claim.

```sh
gnomon check <directory> [--scope SCOPE] [--format text|yaml|sarif] [--output PATH]
```

| Argument or option | Description                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `<directory>`      | Directory of records, read recursively.                                                                             |
| `--scope`          | [Named completion target](../specification/validation-scopes.md#^ordered-validation-scopes) used to classify missing content as current or future work. |
| `--format`, `-f`   | `text` (default), `yaml` for a report, or `sarif` for a log in the findings profile of the gate Elenchos. |
| `--output`, `-o`   | File receiving the report instead of standard output; its missing folders are created.                              |

**Output:** text output prints one line per finding with its file, record, rule and message. A selected scope adds one line per future item. The final line always counts records and unfilled templates, with separate totals for findings and warnings. With `--scope`, that line also counts future work. A rule of level `warning`, such as `completeness/unstated-domain`, marks its line with `warning:`. Such a rule reports content usually expected for the case shown without requiring it.

With `--scope`, missing content due now produces a method-conformance finding. Missing content due at a subsequent scope produces a computed inquiry diagnosis. The `yaml` report separates these results under `files` and `future_work`. The `sarif` log contains current findings only, and its run context names the selected completion target for interfaces such as Ekphrasis. Future work leaves the exit status unchanged. Without `--scope`, the command retains the previous behavior. The command computes future work only when a scope is selected. The [validation scopes](../specification/validation-scopes.md#^scope-requirement-sets) state the requirements and current experimental boundary.

A complete SARIF run without an error or warning also carries a clean-result context for interfaces such as Ekphrasis. The context states that the records satisfy the checked structural and method rules. It also states that the check establishes no truth, warrant or acceptance for the research claims.

The `yaml` report groups findings by file, holds no date or absolute path and sorts its content. A renderer such as Ekphrasis presents this report in Obsidian. Paths are relative to `<directory>`. The command exits with code 1 for an error finding or an unreadable file, and code 2 for an unknown scope or an unwritable report. A warning leaves the exit code at 0.

Under the rule `check/failed`, a finding means that a read or checker error stopped part of the check. Its explanation identifies the failing input or checker. Correct the reported error. Then, rerun the command. The finding remains until the check completes over the named record. ^cli-check-recovery

## `explain`

A researcher who reads a finding needs to know what its rule requires and where the method states that requirement. The `explain` command takes one rule identifier copied from a finding and prints the entry that the catalogue of rules holds for it. Every finding of that rule carries the same entry: ^cli-explain

- the identifier of the rule;
- its level, `error` or `warning`;
- the meaning of a finding of that rule;
- the repair condition, the record content that resolves the finding;
- the documentation target, the path of the note that states the requirement within the Gnomon repository, optionally followed by a block anchor.

```sh
gnomon explain <rule-id>
gnomon explain --list
```

| Argument or option | Description                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `<rule-id>`        | Rule identifier as a finding prints it, such as `itinerary/cycle`. The text output of `check` and `itinerary`, the YAML report and every SARIF log carry it. |
| `--list`           | Print every rule identifier, one per line in sorted order, instead of one explanation.                                                    |

**Output:** five lines, labelled `rule:`, `level:`, `meaning:`, `repair:` and `documentation:` in this order. The repair condition and the documentation target are those that the `yaml` report and the `sarif` log attach to each finding of the rule. For an unknown identifier, standard error names the identifier, suggests the closest rule when one is similar, and points to `--list`. The command exits with code 2 when the identifier is unknown, and when neither or both of an identifier and `--list` are given.

## `schemas`

Write the contract of each record type and its template, generated from the base schemas in `src/gnomon/data/schemas/` and from the vocabulary registry. In a checkout of the repository, the command also writes the [field index](field-index.md) of the user guide, from the same schemas and the specification notes. With `--check`, the command writes nothing, reports each generated file that differs from its generated form, and exits with a nonzero code when one does.

```sh
gnomon schemas [--check]
```

| Option    | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `--check` | Report the stale generated files instead of writing them.          |

## `migrate`

To update authored records without losing their prior bytes, select one explicit migration mode. The check mode previews the complete plan without writing. The apply mode displays the same plan before asking the researcher to approve it. ^cli-migrate

```sh
gnomon migrate <directory> --check
gnomon migrate <directory> --apply
```

| Input | Description |
| ----- | ----------- |
| `<directory>` | Directory of authored records, read recursively. |
| `--check` | Preview every proposed change without writing. |
| `--apply` | Display every safe change, preserve the sources and apply the approved plan. |
| `--yes`, `-y` | With apply mode, confirm the displayed changes without prompting. |

First, the command checks each record against the newest contract of its type. A passing record needs only a new value for the field `_schema`. Then, the plan shows the old and new field values in a unified diff. By contrast, the plan lists every blocking field of a failing record. Missing research values block the complete plan. The researcher must supply them. Each view command regenerates its own views. Therefore, the command ignores generated views, hidden directories and foreign YAML files.

Apply mode accepts only plans with zero blocked and zero unreadable records. For a clean plan, the command prints every diff. Then, the researcher approves or declines the plan.

An approved plan runs in this order:

1. The command copies the exact source bytes to `.gnomon-backup/migrations/<former-contract>/<relative-record-path>`.
2. The command verifies every source against the reviewed bytes.
3. The command writes the new value of `_schema` only to matching sources.

Two unsafe states stop the command: an existing recovery file and altered source bytes.

**Output:**

- Exit code `0` reports that every applicable record is current or that every approved change was applied. After the command changes the records, it names each source and its recovery file.
- Exit code `1` in check mode reports pending work and confirms that zero files were written. In apply mode, this code reports that the researcher declined or that the command could not complete the reviewed write safely. If the command changes some records before failing, the output names every recovery file and changed record.
- Exit code `2` reports a missing or ambiguous mode. The yes option `--yes` also produces this code outside apply mode.

## `status`

A researcher choosing the next act of an inquiry needs the conditions that block each question and the acts that can lift them. The `status` command applies the [choice of the next act](../procedures/inquiry/next-act.md) to the records of a directory tree, question by question and route by route: ^cli-status

- the state of each [condition for obtaining an answer](../epistemology/objects/question/conditions-of-answerability.md#^condition-states), read from the block `answerability` of the question, else from a field that shows it, else `not-established`;
- the open conditions, each with every registered activity mapped to it; each activity states its required inputs, output type, possible storage locations and waiting activities that it may unblock;
- the refuted conditions, which call for a revision;
- the steps whose record is stabilized while their verdict is pending, so that their norm is judged anew, and the impeached records;
- for each revision that a step records, the dependents that it flags, by the [kind of the revision](../epistemology/objects/knowledge/grounds-and-dependence.md#^revision-kinds) and the warrant of each dependent, and those that the researcher has not yet reviewed.

```sh
gnomon status <directory> [--format text|yaml] [--output PATH]
```

| Argument or option | Description                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------- |
| `<directory>`      | Directory of records, read recursively; each folder is one problem.                      |
| `--format`, `-f`   | `text` (default), per open condition its ready acts and the acts waiting for an input, and per refuted condition its revisions; or `yaml`, the full diagnosis. |
| `--output`, `-o`   | File receiving the report instead of standard output; its missing folders are created.   |

**Output:** the `yaml` report has the result class `computed inquiry diagnosis`. The report holds no date and no absolute path, so two runs on unchanged records write the same file. A state that the records do not show stays `not-established` until the researcher asserts it with pointers. Therefore, only the researcher can replace that state with an established judgment. The command exits with code 1 when a file cannot be read, and with code 2 when the report cannot be written.

## `vocabulary`

An author choosing a symbol for a new quantity needs every symbol and operator that the records of one problem already declare. The `vocabulary` command collects them from the filled records of a problem folder into a vocabulary record, with the LaTeX form of each symbol. The record is a YAML view bound to the schema `gnomon:view.vocabulary@3` of the [view schemas](../../src/gnomon/data/schemas/views/_index.md), so a renderer displays it as it displays the other views. Its `source_state` identifies the authored records from which it was generated. The command below writes it into the problem folder: ^cli-vocabulary

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

An author who has filled the itineraries of a problem needs to know whether each step takes the products that its activity requires. The `itinerary` command checks every itinerary record of one problem folder against the registries of activities and of product types, and against the records that its steps name. The conditions of the check are stated in the [itinerary check](../epistemology/processes/activities/epistemic-activities.md#^itinerary-check), and the checks on the fields of an itinerary in the [itinerary record](../specification/itinerary.md#^record-checks). ^cli-itinerary

```sh
gnomon itinerary <directory> [--format text|sarif] [--output PATH] [--root PATH]
```

| Argument or option | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `<directory>`      | Folder holding the filled records of one problem.                                                 |
| `--format`, `-f`   | `text` (default) or `sarif`, a log in the findings profile of the gate Elenchos.                  |
| `--output`, `-o`   | With `sarif`, file receiving the log instead of standard output; its missing folders are created. |
| `--root`, `-r`     | With `sarif`, root against which the log states every path; the current folder by default.        |

**Output:** each defect occupies one line. The line states the itinerary identifier, rule identifier and message. A warning inserts the mark `warning:` before the rule identifier. The rule identifier can be passed to the `explain` command. The final line gives the number of itineraries checked and defects found. The command exits with code 1 when it finds a defect, or when the folder does not exist.

With `--format sarif`, the [findings output](../adr/findings-output.md#^command-output) states the content of the log and the exit statuses. When the log takes standard output, the text lines go to standard error.

## `source-state`

The command supplies the identifier of the current authored records. A presentation tool can compare this identifier with the one stored in a generated view to determine whether that view is current. This command is the integration boundary for record selection, template cleanup and canonical serialization; a consumer must not reproduce that algorithm. ^cli-source-state

```sh
gnomon source-state <directory>
```

**Output:** one `sha256:` identifier on standard output. The command exits with code 1 without printing an identifier when the directory does not exist or a record cannot be read.

## `views`

A researcher who proceeds by local increments needs the global state of the research. The `views` command writes nine views of a directory tree of records, each as a YAML record that a renderer such as Ekphrasis displays as a read-only form: ^cli-views

- the state of each problem: its demand met, its accepted answers and its candidates, and its obstacles, stated and shown;
- the open conditions, with separate tables for required predecessors and unranked ready acts, followed by comparisons that show each supplied input and relation derived through ordinal dominance;
- the exposure of each answer: every revisable unit reached by walking its dependencies back, with its kind and the reason of the exposure;
- the assembly of each level, a problem or a decomposed question: its components, the parts of its answer and the parts settled, the citations between its questions, its gaps, its limits of validity and the parts that it leaves out;
- the progress of each itinerary: the itinerary-derived state of each named output, with dependencies formed when one step names another step's output;
- the maturity of each record and of its marked fields;
- the operational inquiry graph: typed activity nodes connect the products that they consume and produce, while typed inquiry relations connect each starting problem to its questions, answers and assessments;
- the statement of each question, authored and composed from its subject and its aim in the [statement frame](../epistemology/objects/subject/subject-of-inquiry.md#^question-statement), with the slots left unfilled by its fields;
- the LaTeX form of each expression of each record, composed from the notations of its symbols and of the operators of its target system.

```sh
gnomon views <directory> [--scope SCOPE] [--output DIR] [--result text|json]
```

| Argument or option | Description                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| `<directory>`      | Directory of records, read recursively; each folder is one problem.                  |
| `--scope`          | Named completion target whose primary view is written.                               |
| `--output`, `-o`   | Folder receiving the views; the folder `views` of `<directory>` by default.          |
| `--result`         | `text` (default), or one JSON object naming the selected file; JSON requires `--scope`. |

Each named completion target selects one view for a specific research task:

| Completion target     | Primary view    | Research task                                                             |
| --------------------- | --------------- | ------------------------------------------------------------------------ |
| `problem-posed`       | `problem-state` | Inspect the demand, obstacles and closure state of each problem.          |
| `question-typed`      | `next-act`      | Inspect open conditions and the acts that can address them.               |
| `subject-identified`  | `next-act`      | Inspect the conditions that remain open after identifying the subject.    |
| `subject-specified`   | `next-act`      | Inspect the remaining open conditions and the acts that are ready.        |
| `candidate-proposed`  | `exposure`      | Inspect the revisable units of the candidate and their dependencies.      |
| `candidate-assessed`  | `problem-state` | Inspect whether the demand is met and whether each problem may close.     |

The scope option `--scope` selects the view but does not check that the inquiry meets the corresponding completion target. Without this option, the command continues to write every view.

Each selected view begins with a coverage block. The first coverage table lists every started authored record read by Gnomon. The second table lists each absent record kind required after the selected target, with its due target and expected file. The scoped `check` command reports missing fields within existing records.

**Output:** the command writes one file per selected view and names the file after the view. Each file declares a schema of the form `gnomon:view.<name>@<version>` from the [view schemas](../../src/gnomon/data/schemas/views/_index.md). The schema registry of the renderer maps that identity to its schema file. Each view carries a `source_state` digest of the authored records used to generate it. A view holds no date and no absolute path. Therefore, two runs on unchanged records write the same files. The command `gnomon check` skips generated views. With `--result json`, standard output holds the path, target and purpose of the selected view. This result lets an interface open the file without reproducing the scope-to-view route. The command exits with code 1 when a scope is unknown or a file cannot be read, and with code 2 when a view cannot be written.

## `tree`

A researcher reading a project needs its questions and their answers at a glance. The `tree` command prints the question tree of a directory, read recursively, from its problems to the assessments of its answers. ^cli-tree

```sh
gnomon tree <directory>
```

**Output:** one indented line per record, with its kind, its identifier, its title and its status. A file that cannot be read is reported on standard error, and the command exits with code 1 only when the folder does not exist.
