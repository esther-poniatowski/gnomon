---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Shared field grounds
tags: []
source:
---
# Grounds for a shared field

> [!QUESTION] Goal: which evidence admits a field to the schema that every inquiry record fills?

A field of the shared schema binds every record, so a field added for one problem reaches inquiries that never use it. Three kinds of evidence are available when a field is proposed:

- a limitation met while filling one case;
- the presence or the absence of a construction across the filled cases;
- the statements that the design of the framework requires an inquiry to make.

## Decision

A typed distinction earns a field only when it recurs across cases or when it changes the admissible answers. The design of the framework justifies a field on its own, and the absence of a construction from the filled cases refutes none.

## Constraints that decide the grounds

- **A complication local to one case must not expand every record.** A limitation met once is repaired within its own case whenever that case can express the repair, because a field admitted to the shared schema reaches every author of every later inquiry.
- **A count over the cases measures the corpus.** The seven filled problems request no causal relation, although inquiries seeking a causal relation are ordinary, so the absence of a construction among them refutes no requirement.
- **A declaration already written carries typed content.** In three cases the purpose of an unused declaration could be stated, and a field of the record now connects it (four microbial coefficients, for instance, type the interaction specification).

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Admit a field whenever one case requires it | Each case states every specification that its inquiry needs | A complication specific to one case then expands every record, and each later author meets a field that the inquiry leaves empty |
| Admit a field only where the filled cases exhibit it | The evidence is countable, and every admitted field has an instance | The corpus holds seven problems, and ordinary constructions are missing from it, so the count reports the reach of the corpus |
| Declare per aim the fields that must stay empty | An aim would bound its record from both sides, and an irrelevant field would be reported | Three counterexamples refute such a list: a formal model class appears with three matched outputs, with two, and with none. Neither the aim, the target type nor the requested relation decides the exclusion |
| Admit a typed distinction that recurs or changes the admissible answers | The schema grows by the distinctions that inquiries draw, and each admitted field has a stated warrant | Two proposals can be separated only by judgement, since neither recurrence nor a change of admissible answers is counted mechanically |

## Consequences

- An unused declaration is kept wherever its purpose can be stated, and a field of the record then connects it. Deleting it would discard the typed content and hide the law that the record has not yet written.
- No list names, per aim, the fields that a record must leave empty. An empty field is read as a choice of the inquiry, and a consistency between two fields is checked where one exists.
- A fixture demonstrates that the schema can express one inquiry, and the corpus therefore measures expressivity.
