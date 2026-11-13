---
tags:
  - procedure
index: "[Procedures of an inquiry](docs/procedures/inquiry/_index.md)"
aliases:
  - Promoting selected external research
---
# Promoting selected external research

> [!QUESTION] Goal: when does an inquiry turn part of an external source into a Gnomon record, and where does the selected unit belong?

Keep a source external when Gnomon needs only a pointer. Promote only the smallest unit required by the active question or chosen act. A check can also require the internal fields of a source because of an authored identifier, commitment or epistemic aim. ^selective-promotion

Repairing a current record leaves its sources external. When the inquiry requires source structure, select the smallest required content. Classify that content. Then place it in its owning record and retain its immediate source pointer.

## Classify the selected unit

Classify the content rather than its source format. A data set can identify a phenomenon without being that phenomenon. A model file can remain external until the researcher must structure its system. The researcher chooses the class. Ekphrasis presents the fields that the selected record contract admits, and Gnomon validates the saved record. Neither tool chooses the class. ^external-unit-classification

| Decision question | Classification | Gnomon home |
| --- | --- | --- |
| Does the unit delimit the particular system or the class of systems studied? | target system | a [target-system record](../../specification/target-system.md) |
| Does the unit state an unmet demand for a result, together with constraints that a satisfactory result must meet? | problem | a [problem record](../../specification/problem.md) |
| Does the unit ask for a typed answer? | question | a [question record](../../specification/question.md) |
| Does the unit state a behavior of the target system that the question concerns? | phenomenon | a [phenomenon record](../../specification/phenomenon.md) |
| Does the unit state a system studied as a stand-in for the target? | model | a [model record](../../specification/model.md) |
| Does the inquiry admit the unit before seeking the answer, as a dependence among declared target quantities? | admitted law | the `laws` block of a [background record](../../specification/background.md) |
| Does the unit state a dependence among quantities of a stand-in system? | model law | the `laws` block of the owning model record |
| Does the unit state a typed claim that responds to one recorded atomic question? | answer | an [answer record](../../specification/answer.md) |

A unit can have both a content classification and a role among the grounds of an answer. Author the content once and reference its identifier from the answer. In particular, the role `warrant` names a ground that licenses the step to the answer claim, as the [grounds of an answer](../../specification/answer.md#^answer-elements) specify. By contrast, the field `laws[].warrant` states the support mode of a law, as the [background specification](../../specification/background.md) specifies.

Keep a unit external unless a listed class applies or an existing record owns its content.

## Place the classified unit

Place the classified unit according to whether its Gnomon home already exists:

| Selected source unit | Gnomon home | Operation |
| --- | --- | --- |
| a unit classified as a standalone record kind not yet present | the first record of that kind | run *Create instance*, or add its sparse record with the CLI option `--with` |
| a unit classified as a record kind already present | another record of that kind | run *Create instance* with a distinct filename; the post-creation command registers it in the inquiry index |
| a law admitted before the inquiry or proposed by a model | the `laws` block of its background or model record | add the owning record only when it does not yet exist |
| content used as a datum, warrant, condition, assumption, idealization or criterion | the record or nested unit that owns the content | reference that owner from the answer field `grounds` instead of copying the content into the ground |
| a unit already held by a Gnomon record | the existing record | reference its identifier instead of creating a copy |

Fill only the selected content. The number of sources and units imposes no conversion rule. A source can supply several units, and a unit can draw on several sources.

## Retain the source pointer

Record at least one immediate originating source in the field owned by the promoted unit. When a field accepts lists, it may retain multiple origins. A law accepts one `origin`. Its fields `rests_on`, `requires` and `warrant` state support and descent rather than additional origins. ^promoted-source-relations

| Promoted unit | Pointer destination | Boundary |
| --- | --- | --- |
| target system | `identification.pointers` of the target-system record | the source must fix the system or class that the record denotes |
| problem | `sources` of the problem record | the pointer imports no source content |
| question | `sources` of the question record | the pointer imports no source content |
| phenomenon | `identification.pointers` of the phenomenon record | the source must report or fix the behavior that the record denotes |
| model | `sources` of the model record | the pointer names the source of the selected model; `derives_from` records ancestry and `operations[].rests_on` records support |
| admitted law | `laws[].origin` of the background record | the pointer names the immediate source of the law, not its warrant |
| model law | `laws[].origin` of the model record | the pointer names the immediate source of the law, not its warrant |
| answer | `sources` of the answer record | the pointer names the source of the selected answer; `support` and `route.pointer` remain independent fields |

A promoted law may serve as a warrant. An argued binding pair held by a Gnomon record may also serve as one. Then, the answer references its identifier, while the source pointer remains with the owning record. A source placed in `identification.pointers` must fix the referent. Otherwise, keep the source external unless another row applies.
