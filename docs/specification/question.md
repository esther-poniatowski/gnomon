---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Question record
---
# Question record

> [!QUESTION] Goal: what does a researcher write in the top-level fields of a question record, and how does the commitment of its slots fix the type of the record?

The question record names the [problem](problem.md) that it addresses and the questions to which it is linked. The relations of a link are defined with the [linked questions](../epistemology/objects/question/question.md#^linked-questions).

| Field | When it is required | Content | Example |
| ----- | ------------------- | ------- | ------- |
| Title | always | a short name of the question, as a label | delay before generalization |
| Statement | always | the question in words, restating its fields in the [statement frame](../epistemology/objects/subject/subject-of-inquiry.md#^question-statement) | "in overparameterized networks trained to fit their data, what produces the delay before generalization?" |
| Status | always | posed · refined · answered · abandoned | `posed`, for a question not yet refined |
| Addresses | when a problem record states the problem that the question serves | the identifier of one problem record | the problem of the delay before generalization |
| Links | when the answer to another question bears on this one | per link, the other question, the relation, and the record shared by the two questions | — |
| Links: question | with every link | the identifier of the other question record | the question that describes the representation geometry of a network |
| Links: relation | with every link | subquestion-of · explanans-from · presupposes · enables | `explanans-from`, for a question that explains a readout capacity by that geometry |
| Links: via | when the two questions share a record | the identifier of the shared record, such as a phenomenon | the phenomenon record of the geometry |

- **A problem is recorded in its own record.** Its fields, and the field by which a question names its problem, are specified in the [problem record](problem.md).
- **The steps that answer a question are recorded in an itinerary.** An [itinerary](itinerary.md) lists the activities that lead from a problem to its questions, and from a question to its answers and their assessments. The itinerary check verifies that each step takes the types of product required by its activity.

The commitment of a slot takes one of the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) defined for a question. Each level is decided by one check over the records: ^commitment-checks

| Level | Check |
| --- | --- |
| `placeholder` | the type of the placeholder belongs to the [admitted types](question-subject.md#^placeholder-slots) |
| `identified` | the record exists and states its identification |
| `specified` | the required fields are filled, and every symbol resolves |

- **The slots of a question admit a placeholder.** The rule is stated under [placeholders before records](question-subject.md#^placeholder-slots).
- **The type of a question record follows the commitment of its slots.** When any slot holds a placeholder, the record is a `question-schema`. When every slot is `identified` or `specified`, the record is a `question`. The two take the same fields.
