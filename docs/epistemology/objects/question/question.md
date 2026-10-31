---
tags:
  - theory
  - wip
index: "[Question](docs/epistemology/objects/question/_index.md)"
aliases:
  - Question
  - Question (term)
  - Question schema
  - Level of commitment
  - Linked questions
---
# Question

> [!QUESTION] Goal: what is a question, which sets of answers does it delimit, how far can each slot of a question form stay uncommitted, and how do two questions depend on each other?

A **question** is a request whose answers form a definite set: to know the question is to know the statements that count as its answers [hamblin1958]. The [specification of a question](question-specification.md) states it in three layers, beside which stands its [request](question-specification.md#^question-request). The possible answers are fixed by the subject $\Sigma$ of the question and by its epistemic task $T$, and the direct answers by these two layers together with the request of the question. The virtues $\mathcal{V}$ that it weighs fix the standards by which its answers are judged.

A research question is usually composed of several atomic questions, joined by the [links between questions](#^linked-questions). That composition is the [decomposition](../../processes/inquiry/question-decomposition.md#^decomposition-graph) of the research question, not its definition: each atomic question is a question in the sense above, and each candidate answer answers one atomic question.

The fields of a question, and the rules that bind them, are documented in the [question record](../../../specification/question.md).

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Question | logic of questions | a request whose answers are statements forming an exhaustive set of mutually exclusive possibilities: to know the question is to know the statements that count as its answers | [hamblin1958] |
| Question | formal semantics | the set of the propositions that count as its possible answers, among which the question sets up a choice; these propositions can be true together | [hamblin1973] |
| Question | erotetic logic | a subject, presenting the range of alternatives, and a request, fixing how many alternatives an answer must select and how completely | [belnap1976] |
| Why-question | pragmatics of explanation | a triple of a topic, a contrast class and a relevance relation | [vanfraassen1980] |

The why-question of the pragmatic account corresponds to three components of a question of this method. Its topic is the phenomenon $P$, its [contrast class](../subject/contrast.md) is $X$, and its relevance relation is the [requested relation](../task/requested-relation.md) $R$.

## Answers of a question

A question delimits five sets of answers. The possible answers are the material of the others. The direct and the partial answers are the two kinds of answer that the possible answers compose, and the admissible and the satisfying answers are filtered from those two kinds by tests: ^answer-sets

| Set | Its members | Fixed by | Source |
| --- | --- | --- | --- |
| **Possible answers** | the alternatives that the subject presents, such as the candidate mechanisms of a which-question; two possible answers can be true together | the subject $\Sigma$ and the task $T$ | [hamblin1973] |
| **Direct answers** | the statements that settle the request: each selects as many possible answers as the request demands, and as completely. Under a request that claims completeness, such as `all`, the direct answers exclude each other and jointly cover every possibility in which the presuppositions of the question hold, as the answers of Hamblin's postulates do | the subject $\Sigma$ and the task $T$, with the request of the question | [belnap1976]; [hamblin1958] |
| **Partial answers** | the statements that exclude at least one direct answer, are compatible with at least one, and entail none, so that they narrow the direct answers without settling the request | the direct answers | proposal of this method |
| **Admissible answers** | the direct or partial answers that pass the admissibility tests, the constitutive virtues included | the standards of the question: the tests derived from $\Sigma$ and $T$, and the constitutive virtues of $\mathcal{V}$ | proposal of this method |
| **Satisfying answers** | the admissible answers that also pass the warrant tests | the warrant tests of the question | proposal of this method |

The sets are ordered in two ways. The satisfying answers form a subset of the admissible answers, and the admissible answers a subset of the direct and the partial answers together. A direct answer is built from possible answers, and it is itself a possible answer only under a request that selects one alternative without a claim of completeness, such as `one`, or in a whether-question. A partial answer can pass its tests and still leave the question open, since only a direct answer settles the request.

A **corrective answer** denies a presupposition of the question [belnap1976]. A corrective answer is neither a direct nor a partial answer, so it lies outside these sets, and the [erotetic routing](../answer/satisfaction-conditions.md#^erotetic-routing) of an assessment states which tests apply to it.

The admissibility tests and the warrant tests are stated among the [conditions of satisfaction](../answer/satisfaction-conditions.md#^conditions-satisfaction), which the answer notes define. The preferred virtues fix no set: a preferred virtue ranks the admissible answers, as the [standing of a virtue](../task/epistemic-pragmatic-virtues.md#^virtue-standing) states. Therefore, the virtues of a question fix only the standards by which its answers are judged. A question is individuated by its direct answers [belnap1976]. *Example*: "which mechanism produces the delay?" asked under the request `one` and under the request `all` has the same possible answers but different direct answers, so the two are different questions.

The **presuppositions** of a question are the statements entailed by every direct answer [belnap1976]. A question has a true direct answer only if its presuppositions are true. The presuppositions are stated over the direct answers, not over the admissible ones. The admissible answers differ from the direct answers in two ways, so the statements that all of them entail can differ from the presuppositions. First, they omit the direct answers that fail a test, which can add a claim that the question does not presuppose, such as a claim shared by the answers that a constitutive virtue admits and by none of the other direct answers. Second, they include partial answers, which can remove a presupposition, since a partial answer can be true when a presupposition is false. ^presupposition

## Question schema and levels of commitment

A **question schema** is a question form, not yet a question: at least one of its slots holds a typed placeholder instead of a referent. The type of each slot comes from a closed list, which the [placeholders of the subject](../../../specification/question-subject.md#^placeholder-slots) enumerate. Thus, a schema fixes the *type* of each slot before any record fixes its referent. A schema becomes a question once each of its slots reaches the level `identified` and its request is fixed: the identified slots make its possible answers a definite set, and the request then fixes its direct answers. ^question-schema

Each slot of a question or of a question schema carries one of three **levels of commitment**: ^commitment-levels

| Level | The slot holds |
| --- | --- |
| `placeholder` | a type from the closed list, with a description in words |
| `identified` | a record whose referent is fixed by a definite description and by pointers to data, results or literature |
| `specified` | a record whose formal declarations are written |

The checks that decide the level of a slot are documented with the [question record](../../../specification/question.md#^commitment-checks).

The level `identified` fixes a referent without stating its formal properties. A definite description can fix the referent of a term without giving its meaning [kripke1980]. *Example*: "the geometry of the fixed points reached by the networks of a stated class" fixes one object before any kernel is written. The description of an identified slot serves as an *explicandum*, an inexact concept already in use. At the level `specified`, an exact *explicatum* replaces that explicandum [carnap1950_logical].

Commitment is kept apart from three other attributes of records and of their fields: ^record-attributes

| Attribute | Content | Values |
| --- | --- | --- |
| Commitment | how far a slot fixes its referent | `placeholder`, `identified`, `specified` |
| Maturity | how far one specification has been revised, as the [maturity of a specification](../status/statuses-and-acceptance.md#^maturity) defines it | `open`, `provisional`, `stabilized` |
| Record status | the attitude taken toward the whole record; for an answer, the record status is the attitude toward its claim | one vocabulary per kind of record, such as `entertained` or `accepted` for an answer |
| Empty value | the state of an unfilled field | a gap when the field is required, and a product of the inquiry when the aim lists the field as produced |

- **Commitment and maturity vary independently.** A slot can be identified and stabilized, when the referent is settled and no formal declaration is sought. A slot can also be specified and provisional, when the declarations are written and still under revision.
- **An empty field is a gap unless the inquiry produces it.** *Example*: an exploratory question leaves the statement and the category of its phenomenon empty, because finding them is the aim of the inquiry. The [epistemic aim](../task/epistemic-aim.md) lists the paths produced by the inquiry.

## Linked questions

Two questions are **linked** when the answer to one bears on the other. A link names the other question, one relation from a closed list, and the record shared by the two questions. ^linked-questions

| Relation | This question … |
| --- | --- |
| `subquestion-of` | is answered by a part of an answer to the linked question; each of its answers, with the available premises, narrows the answers of the linked question, which is the second clause of erotetic implication [wisniewski2013] |
| `explanans-from` | has an explanans factor that is the phenomenon of the linked question |
| `presupposes` | has a true direct answer only if the linked question has a true direct answer |
| `enables` | has an answer that establishes a condition of answerability of the linked question, without narrowing its answers |

*Example*: a first question describes the [representation geometry](../../vocabulary/representations/representation-and-encoding.md) of a class of networks. A second question explains a capacity of readout by that geometry. The second question links to the first with `explanans-from`, through the phenomenon record of the geometry. Therefore, neither question restates the content fixed by the other.

*Example*: the question "how is the dimension of the population activity estimated from finite samples?" links to the question "does the dimension grow with the complexity of the mixture?" with `enables`.

## Distinctions

- **A problem is not a question, and every inquiring question presupposes a problem.** The difference between the two is stated in the note on the [epistemic problem](../problem/epistemic-problem.md#^problem-vs-question). A question asked to learn its answer carries at least a [minimal problem](../problem/epistemic-problem.md#^minimal-problem), and a problem record makes that problem explicit.
- **The link `presupposes` does not point to a question about a presupposition.** A whether-question about the presupposition of another question, such as "does the delay of generalization occur?", has a true direct answer, positive or negative: its presupposition is trivially true, so no question presupposes it in the sense of the link. A positive answer to it establishes the [soundness](conditions-of-answerability.md#^eight-conditions) of the other question, the condition that its presuppositions are true, so the two questions are linked by `enables`. The link `presupposes` joins two questions when the presupposition of the first entails the presupposition of the second, and the second is not trivially true. *Example*: "which mechanism produces the delay?" presupposes "how long is the delay?", since the first presupposes that a delay exists and is produced by a mechanism, and the second presupposes only that a delay exists.
- **The link `presupposes` between questions is not the relation of the same name between answers.** Between two questions, the link states that one question has a true direct answer only if the other has one. Between two [answers](../answer/answer-form.md#^answer-relations), the relation states that one answer is admissible only if the other answer is true.
- **The type of a problem bounds the aims of its questions.** The [types of problem](../problem/problem-types.md) map each type of result demanded onto the aims, the question forms and the answer forms that it admits.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); a question modeled by its direct answers, a presupposition as a statement entailed by every direct answer, a corrective answer as the denial of a presupposition, and the division of a question into subject and request, checked through the [SEP entry on questions](https://plato.stanford.edu/entries/questions/) and Wiśniewski's summaries of the book
- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum, explicatum and the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211); the postulates that an answer is a statement, that knowing what counts as an answer is knowing the question, and that the possible answers form an exhaustive set of mutually exclusive possibilities, checked through secondary sources
- [hamblin1973] ◐ Hamblin, "Questions in Montague English", *Foundations of Language* 10(1), 41–53, 1973; a question denotes the set of its possible answers, among which it sets up a choice, checked through the [SEP entry on questions](https://plato.stanford.edu/entries/questions/) and secondary sources
- [kripke1980] ◐ Kripke, *Naming and Necessity*, Harvard University Press, 1980; pp. 54–56 and 135; reference fixing by a description, checked through the [SEP entry on rigid designators](https://plato.stanford.edu/entries/rigid-designators/)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, the why-question as a triple
- [wisniewski2013] ◐ [Wiśniewski, *Questions, Inferences, and Scenarios*, Studies in Logic 46, College Publications, 2013](https://philpapers.org/rec/WINQIA); erotetic implication
