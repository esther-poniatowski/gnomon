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

The records of one research problem share one folder. The [record templates](../../src/gnomon/data/templates/_index.md) supply one file per record kind. The header of each template names its method note and states how many files of its kind a problem holds: for instance, one file per target system, per phenomenon or per candidate answer. Each record is filled in a copy of its template, kept in the folder of the problem.

## Fill the records in order

The index of the templates numbers the record kinds in the order of filling, from the problem to the assessment. The [order of specification](../epistemology/inquiry/specification-order.md) states why each stage takes the earlier stages as given, and how a change to an earlier record is made as a revision. A target system and a phenomenon can first be recorded at the commitment `identified`, before their quantities are declared, as the [levels of commitment](../epistemology/inquiry/question.md#^commitment-levels) define it.

## Read the method note of each field

The table of a method note states, row by row, the content of a slot, the condition under which the slot is required, and its admitted values. The question record draws on several notes, all listed in the header of its template.

Completed records can be consulted in the [worked inquiries](../../examples/_index.md). For each worked inquiry, an issues note states what its records could not express.

## Collect the symbols

The symbols of a problem are declared in its records, under the rules of [symbols and expressions](../epistemology/language/symbols-and-expressions.md). Before a new quantity is named, the following command collects the symbols already declared, and writes a vocabulary record and a Markdown table into the folder:

```sh
gnomon vocabulary ./my-problem --markdown
```

## Check the itinerary

The steps taken in the inquiry are recorded in an [itinerary](../epistemology/inquiry/itinerary.md), each step as an instance of a registered activity. The [choice of the next act](../epistemology/inquiry/next-act.md) guides the step to take. The following command checks each step against the registries and against the records that the step names:

```sh
gnomon itinerary ./my-problem
```

Each line of the output names one defect and the itinerary that holds it, and the command exits with an error when it finds a defect. The options and the outputs of both commands are listed in the [command reference](cli-reference.md).
