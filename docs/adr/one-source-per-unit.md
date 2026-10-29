---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - One source per unit
---
# One source per unit of content

> [!QUESTION] Goal: where is a unit of content authored, and in which form does another record or artifact that needs it carry it?

Five decisions each give one source to the content of one grain:

- the fields of one record, under the [single field per fact](single-field-per-fact.md);
- the admitted values of a vocabulary, under the [decision on registries](registries-as-source.md);
- the fields of a record type, under the [decision on record schemas](record-schemas.md);
- the content presented by an exposition, under the [decision on expositions](expositions-as-projections.md);
- the symbols of a notation and the questions of a project, under the [decision on terminology, audience and project specifications](terminology-audience-project-specifications.md).

No decision covered a unit that several records need, such as a law, a model or a claim, nor stated the rule that these five decisions share.

## Decision

Each unit of content has one authored source: the record, or the entry of package data, that declares it. ^one-source

Another record that needs the unit names it by its identifier, in the [dotted form](dotted-identifiers.md), and never restates it. ^reference-not-restate

A copy of a unit is admitted only when a tool generates it from its source. An authored copy is excluded, even when a check holds it equal to its source. ^generated-copies-only

The checks enforce the mechanical part of the rule: each identifier is declared once, and each reference resolves to a declaration. A restatement of a unit in other words escapes every check, so a review of a record searches for restatements of units that other records declare. ^non-redundancy-scope

## Constraints that decide the source

- **Two authored copies drift apart.** An edit to one copy leaves the other stale, and a reader cannot tell which copy holds.
- **Units are reused across records and across problems.** A model grounds several answers, a key serves several bindings, and a concept serves several projects, as the decisions on [answers, models and bindings](answers-models-bindings.md) and on [concepts, glossaries and notations](concepts-glossaries-notations.md) state.
- **No check recognizes one claim under two wordings.** An equality check compares grammatical values only, so it cannot hold a prose restatement equal to its source.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Restate a unit in each record that uses it, and check that the copies agree | Each record reads on its own | The check compares grammatical values only, so a restatement in prose drifts unreported |
| Hold all the content of a problem in one record | No reference crosses records within a problem | A model, a key or a concept used by two problems is still copied, and one file mixes the concerns that the framework separates |
| Copy each unit into every record that uses it by a build step | Each record shows the content that it uses, and the source stays single | Admitted as a generated output only: the copy is a view that no author edits and no check reads, as the [decision on the inputs of checks](checks-read-records.md#^records-are-source) states |
| One authored source per unit, named elsewhere by identifier | Each unit is edited once, and each reference is checked | A reader follows identifiers to reach the content that a record uses |

## Consequences

- A unit that another record must name receives an identifier, as the decision on dotted identifiers requires of idealizations, abstractions and explanans factors.
- A check that compares a generated copy with its source stays admitted, such as the check of templates against their schemas.
- Non-redundancy beyond identifiers rests on review, so the rule holds without a guarantee for prose fields.
