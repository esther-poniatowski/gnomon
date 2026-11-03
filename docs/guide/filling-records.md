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

The records of one research problem share one folder. The following command creates that folder with the [record templates](../../src/gnomon/data/templates/_index.md) of the problem, its subject, its question and its operators, and with an index listing them in the order of filling:

```sh
gnomon init ./my-problem
```

A later record kind is added to the folder with the option `--with`, such as `--with answer --with assessment` once a candidate answer is in view. The header of each template names its specification note and states how many files of its kind a problem holds: for instance, one file per target system, per phenomenon or per candidate answer. A second file of one kind is a copy of its template, kept in the folder of the problem.

## Fill the records stage by stage

The records are filled in the five stages of the [order of specification](../epistemology/processes/inquiry/specification-order.md), which the index of the folder lists:

1. the problem, with its demand, its constraints and its explicanda;
2. the question schema: each question that serves the problem, typed before its terms are identified, with a placeholder in place of a target system or a phenomenon not yet recorded;
3. the identified subject: the target system and the phenomenon at the commitment `identified`, each fixed by a definite description and pointers, as the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) define it;
4. the background and the specified subject: the admitted laws, and the formal declarations of a record raised to the commitment `specified` when an open condition of a question requires them;
5. the candidate answers, with the models, the keys and the bindings on which they rest, and the assessment of each answer.

Each stage takes the records of the earlier stages as given, and a change to an earlier record is made as a revision. The itinerary records each act of the inquiry as a step, from the statement of the problem on. A template not yet started keeps the placeholder identifier of its template, such as `quest.TOPIC.NAME`; the command `gnomon check` lists it apart and checks only the records already started, so the folder can be checked after each stage.

## Read the specification of each field

The [specification](../specification/_index.md) documents each record kind in one note. Its tables state, row by row, the content of a field, the condition under which the field is required, and its admitted values. The question record is documented in four notes, all listed in the header of its template.

Completed records can be consulted in the [worked inquiries](../../examples/_index.md). For each worked inquiry, an issues note states what its records could not express.

## Check the records

The following command runs every check of `gnomon` on the folder, and prints one line per finding with its file, its record and its rule:

```sh
gnomon check ./my-problem
```

A template left unfilled reports one finding per placeholder, so the count falls as the records are filled. A stable report, which can be kept beside the records and compared between two runs, is written in YAML:

```sh
gnomon check ./my-problem --format yaml --output ./my-problem/reports/check.yml
```

## Collect the symbols

The symbols of a problem are declared in its records, under the rules of [symbols and expressions](../specification/expressions.md). Before a new quantity is named, the following command collects the symbols already declared, and writes a vocabulary record and a Markdown table into the folder:

```sh
gnomon vocabulary ./my-problem --markdown
```

## Check the itinerary

The steps taken in the inquiry are recorded in an [itinerary](../specification/itinerary.md), each step as an instance of a registered activity. The [choice of the next act](../procedures/inquiry/next-act.md) guides the step to take. The following command checks each step against the registries and against the records that the step names:

```sh
gnomon itinerary ./my-problem
```

Each line of the output names one defect and the itinerary that holds it, and the command exits with an error when it finds a defect. The command `gnomon check` runs the same check together with the others. The options and the outputs of every command are listed in the [command reference](cli-reference.md).
