---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Filling the records of an inquiry
---
# Filling the records of an inquiry

Leads a researcher from a research problem to a folder of records that the checks of `gnomon` accept, one record per concern of the inquiry.

> [!IMPORTANT] Prerequisites
> The package is installed, as the [installation guide](installation.md) states, and the researcher has one research problem in view.

## Create the folder of a problem

The records of one research problem share one folder. The following command creates that folder with a sparse problem and itinerary. The command also creates an index that lists both records:

```sh
gnomon init ./my-problem
```

The option `--with` adds a sparse record kind when required for the current inquiry. For example, the argument `--with question` adds the first question. The arguments `--with answer --with assessment` add the records needed to state and assess a candidate. In an existing folder, the command writes only missing records, and the index registers each one under its stage. Optional branches remain absent, so Ekphrasis places them behind *+ Add a field*. For source-based authoring, `--full-template` writes the [complete commented templates](../../src/gnomon/data/templates/_index.md). A problem may hold one file per target system, phenomenon or candidate answer. To create another record of the same kind, copy its complete template to the problem folder and register it in the index.

## Distinguish editable records

Inquiry records are the only files that hold authored research. Researchers create inquiry records with `gnomon init` or Ekphrasis. Alternatively, researchers can copy a canonical template. Researchers may edit these records in Ekphrasis or in a source editor. By contrast, every other file belongs to one of three non-editable classes:

- The files under `.gnomon/schemas` and the schema registry are package resources. Leave them unchanged and rerun `gnomon setup` when the installed contracts change.
- The views written by `gnomon views` or `gnomon vocabulary` are generated results. Ekphrasis presents these views as read-only. Regenerate them after an authored record changes.
- The canonical templates in the Gnomon package or repository define the copies created by `gnomon init`. The option `--full-template` places an editable copy inside the inquiry folder.

## Fill the records stage by stage

The records are filled in the five stages of the [order of specification](../epistemology/processes/inquiry/specification-order.md), which the index of the folder lists:

1. the problem, with its demand, its constraints and its explicanda;
2. the question schema: each question that serves the problem, typed before its terms are identified, with a placeholder in place of a target system or a phenomenon not yet recorded;
3. the identified subject: the target system and the phenomenon at the commitment `identified`, each fixed by a definite description and pointers, as the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) define it;
4. the background and the specified subject: the admitted laws, and the formal declarations of a record raised to the commitment `specified` when an open condition of a question requires them;
5. the candidate answers, with the models, the keys and the bindings on which they rest, the derivations that establish their derived laws, and the assessment of each answer.

Each stage takes the records of the earlier stages as given, and a change to an earlier record is made as a revision. A problem that uses dimensional analysis declares the dimensional formula of its quantities and index sets, with the base scales of its operator record. Its laws and conditions are then checked for homogeneity, as the [decision on the dimensional formula](../adr/dimensional-formula.md) states. The itinerary records each act of the inquiry as a step, from the statement of the problem on. A record not yet started keeps the placeholder identifier projected from its template, such as `quest.TOPIC.NAME`; the command `gnomon check` lists it apart and checks only the records already started, so the folder can be checked after each stage. In a started full template, a field still holding its placeholder, or a block left as the template wrote it, is read as empty. The check reports each such leftover once, under the rule `completeness/template-leftover`, to be filled or deleted.

## Name each record

Records reference one another by their identifiers, so an identifier is chosen once and kept. A record identifier opens on the prefix of its type, already written by its template, such as `quest` in `quest.TOPIC.NAME`. The placeholders after the prefix are replaced by segments of lowercase words joined by hyphens:

- the first segment, the topic, is shared by the records of the problem, such as `grokking` in `prob.grokking.delayed-generalization` and `ans.grokking.slow-structured-representation`;
- a target system takes a topic of its own, such as `system.delayed-generalization-networks`;
- a background record or an operator record takes the topic of the target system named in its field `describes` or `target_system`, such as `bg.delayed-generalization-networks.training-specification`;
- the second segment names the record within its topic, and the prefixes `system` and `ops` take no second segment.

A field of another record names a unit of this record in two parts. The identifier of the record comes first, followed by the symbol of the unit, or by its `id` when the unit has no symbol, as in `phen.grokking.delayed-generalization.tgen`. The [decision on dotted identifiers](../adr/dotted-identifiers.md#^identifier-form) states the form, and `gnomon check` reports a malformed identifier and a topic foreign to the problem.

## Keep the field `_schema`

The field `_schema`, at the top of each template, names the contract followed by the record, such as `gnomon:question@3`: the type of the record and the version of its contract. The template writes it, and the researcher leaves it as written. The command `gnomon validate` checks each record against that contract, and Ekphrasis opens the record as a form through it, as the [decision on record schemas](../adr/record-schemas.md) states.

## Mark the maturity of a field

A field may be filled before the inquiry fixes it. The block `maturity` of a record marks such a field: its key is the path of the field, and its value is `open`, `provisional` or `stabilized`. For a field of one entry of a list, the path names the entry by its symbol or its `id`, as the [form of a key](../specification/maturity.md#^maturity-keys) states. A marker `open` carries a comment naming one of the [three reasons for an open specification](../epistemology/objects/status/statuses-and-acceptance.md#^open-reasons): a result that the inquiry seeks, a decision of the author, or a value outside the type language. In the tipping-cascades inquiry, the phenomenon marks the value set of its observable `Z` in this way:

```yaml
maturity:
  observables.Z.values: open  # outside the type language: a marked sequence of transitions
```

A field left unmarked takes the maturity that the status of its record implies, as the [maturity of a field](../specification/maturity.md) states. The command `gnomon views` lists the maturity of each marked field.

## Find what a commitment and an aim require

Some specifications are required only at a level of commitment or for an epistemic aim. The [requirement registry](../../src/gnomon/data/requirements.yml) lists them in two sections:

- under `by_commitment`, the fields required of a target system or a phenomenon at the commitment `identified`, and in addition at `specified`;
- under `by_aim`, the paths required by each aim of a question, and the paths produced by the inquiry itself, allowed to stay empty.

For instance, the aim `explanation` requires the requested relation of the question, and a target system at the commitment `specified` declares its variables. The check reports a field missing at a commitment under the rule `completeness/unmet-commitment`, and a path missing for an aim under the rule `completeness/unmet-aim`. The specification notes state the same requirements in their column *When it is required*.

## Read the specification of each field

The [specification](../specification/_index.md) documents each record kind in one note. Its tables state, row by row, the content of a field, the condition under which the field is required, and its admitted values. The question record is documented in four notes, all listed in the header of its template.

Completed records can be consulted in the [worked inquiries](../../examples/_index.md). For each worked inquiry, an issues note states what its records could not express.

## Check the records

The following command runs every check of `gnomon` on the folder, and prints one line per finding with its file, its record and its rule:

```sh
gnomon check ./my-problem
```

A template not yet started is counted among the templates not yet filled, and that count falls as the records are filled. A line marked `warning:` reports a specification usually stated in the case shown, such as the domain of an answer whose route runs on a model; a warning fails no check. A stable report, which can be kept beside the records and compared between two runs, is written in YAML:

```sh
gnomon check ./my-problem --format yaml --output ./my-problem/reports/check.yml
```

## Collect the symbols

The symbols of a problem are declared in its records, under the rules of [symbols and expressions](../specification/expressions.md). Before a new quantity is named, the following command collects the symbols already declared, with their LaTeX forms, and writes the vocabulary record of the problem into the folder, a YAML view that a renderer displays:

```sh
gnomon vocabulary ./my-problem
```

## Check the itinerary

The steps taken in the inquiry are recorded in an [itinerary](../specification/itinerary.md), each step as an instance of a registered activity. The [choice of the next act](../procedures/inquiry/next-act.md) guides the step to take. The following command checks each step against the registries and against the records that the step names:

```sh
gnomon itinerary ./my-problem
```

Each line of the output names one defect and the itinerary that holds it, and the command exits with an error when it finds a defect. The command `gnomon check` runs the same check together with the others. The options and the outputs of every command are listed in the [command reference](cli-reference.md).
