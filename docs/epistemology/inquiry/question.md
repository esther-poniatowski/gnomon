---
tags:
  - theory
  - wip
index: "[Inquiry](docs/epistemology/inquiry/_index.md)"
aliases:
  - Question
  - Question (term)
  - Question schema
  - Level of commitment
  - Linked questions
---
# Question

> [!QUESTION] Goal: what is a question, how far can each slot of a question stay uncommitted, and how do two questions depend on each other?

A **question** is a request whose possible answers form a definite set [hamblin1958].

The fields of a question, and the rules that bind them, are documented in the [question record](../../specification/question.md).

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Question | logic of questions | a request fixed by its possible answers: to know the question is to know the statements that count as its answers; in a formal semantics, a question denotes the set of its possible answers | [hamblin1958]; [hamblin1973] |
| Question | erotetic logic | a subject, presenting the range of alternatives, and a request, fixing how many alternatives an answer must select and how completely | [belnap1976] |
| Why-question | pragmatics of explanation | a triple of a topic, a contrast class and a relevance relation | [vanfraassen1980] |

The why-question of the pragmatic account corresponds to three components of a question of this method. Its topic is the phenomenon $P$, its [contrast class](../subject/contrast.md) is $X$, and its relevance relation is the [requested relation](../epistemic-task/requested-relation.md) $R$.

## Question schema and levels of commitment

A **question schema** is a question in which at least one slot holds a typed placeholder. The type of each slot comes from a closed list: `system | phenomenon | observable | contrast | condition`. Thus, a schema fixes the *type* of each slot before any record fixes its referent. ^question-schema

Each slot of a question carries one of three **levels of commitment**: ^commitment-levels

| Level | The slot holds | Decidable check |
| --- | --- | --- |
| `placeholder` | a type from the closed list, with a description in words | the type belongs to the list |
| `identified` | a record whose referent is fixed by a definite description and by pointers to data, results or literature | the record exists and states its identification |
| `specified` | a record whose formal declarations are written | the required fields are filled, and every symbol resolves |

The level `identified` fixes a referent without stating its formal properties. A definite description can fix the referent of a term without giving its meaning [kripke1980]. *Example*: "the geometry of the fixed points reached by the networks of this benchmark" fixes one object before any kernel is written. The description of an identified slot serves as an *explicandum*, an inexact concept already in use. At the level `specified`, an exact *explicatum* replaces that explicandum [carnap1950_logical].

Commitment is kept apart from three other attributes of records and of their fields:

| Attribute | Content | Values |
| --- | --- | --- |
| Commitment | how far a slot fixes its referent | `placeholder`, `identified`, `specified` |
| Maturity | how far one specification has been revised, graded by its [maturity marker](../subject/subject-of-inquiry.md) | `open`, `provisional`, `stabilized` |
| Record status | the attitude taken toward the whole record | one vocabulary per kind of record, such as `entertained` or `accepted` for an answer |
| Empty value | the state of an unfilled field | a gap when the field is required, and a product of the inquiry when the aim lists the field as produced |

- **Commitment and maturity vary independently.** A slot can be identified and stabilized, when the referent is settled and no formal declaration is sought. A slot can also be specified and provisional, when the declarations are written and still under revision.
- **An empty field is a gap unless the inquiry produces it.** *Example*: an exploratory question leaves the statement and the category of its phenomenon empty, because finding them is the aim of the inquiry. The [epistemic aim](../epistemic-task/epistemic-aim.md) lists the paths produced by the inquiry.

## Linked questions

Two questions are **linked** when the answer to one bears on the other. A link names the other question, one relation from a closed list, and the record shared by the two questions. ^linked-questions

| Relation | This question … |
| --- | --- |
| `subquestion-of` | is answered by a part of an answer to the linked question; each of its answers, with the available premises, narrows the answers of the linked question, which is erotetic implication [wisniewski2013] |
| `explanans-from` | has an explanans factor that is the explanandum of the linked question |
| `presupposes` | has a true answer only if the linked question has a true answer |
| `enables` | has an answer that establishes a condition of answerability of the linked question, without narrowing its answers |

*Example*: a first question describes the [representation geometry](../definitions/representations/representation-and-encoding.md) of the benchmark networks. A second question explains a capacity of readout by that geometry. The second question links to the first with `explanans-from`, through the phenomenon record of the geometry. Therefore, neither question restates the content fixed by the other.

*Example*: the question "how is the dimension of the population activity estimated from finite samples?" links to the question "does the dimension grow with the complexity of the mixture?" with `enables`.

## Distinctions

- **A problem is not a question, and every inquiring question presupposes a problem.** The difference between the two is stated in the note on the [epistemic problem](epistemic-problem.md#^problem-vs-question). A question asked to learn its answer carries at least a [minimal problem](epistemic-problem.md#^minimal-problem), and a problem record makes that problem explicit.
- **The type of a problem bounds the aims of its questions.** The [types of problem](problem-types.md) map each type of result demanded onto the aims, the question forms and the answer forms that it admits.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976; the entry was confirmed through library catalogues, and the division of a question into subject and request was not checked
- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum, explicatum and the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211); the postulate that knowing what counts as an answer is knowing the question, checked through secondary sources
- [hamblin1973] ◐ Hamblin, "Questions in Montague English", *Foundations of Language* 10(1), 41–53, 1973; a question denotes the set of its possible answers, checked through secondary sources
- [kripke1980] ◐ Kripke, *Naming and Necessity*, Harvard University Press, 1980, pp. 54–57; reference fixing by a description, checked through secondary sources
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, the why-question as a triple
- [wisniewski2013] ○ Wiśniewski, *Questions, Inferences, and Scenarios*, College Publications, 2013; erotetic implication
