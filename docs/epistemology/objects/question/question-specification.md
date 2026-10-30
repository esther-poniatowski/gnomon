---
tags:
  - theory
index: "[Question](docs/epistemology/objects/question/_index.md)"
aliases:
  - Specification of a question
---
# Specification of a question

> [!QUESTION] Goal: which layers of decision specify a question, what does each layer decide about its answers, and what follows from those decisions?

> [!DANGER] Philosophy of science offers no single canonical decomposition of a question: the layers of specification combine several traditions.

## Layers of specification

A [question](question.md) $Q$ is specified by three layers, each with a **distinct logical role**: ^three-layers

$$Q\ \text{specified by}\ \langle\Sigma,\ T,\ \mathcal{V}\rangle .$$

| Layer of specification | Question that the layer answers | Components |
| --- | --- | --- |
| **1. [Subject of inquiry](../subject/subject-of-inquiry.md)** $\Sigma$ | Which objects does the question concern? | target system $S$, phenomenon $P$, contrast $X$, domain of conditions $D$ |
| **2. [Epistemic task](../task/epistemic-task.md)** $T$ | Which *kind* of knowledge does the question seek? | [epistemic aim](../task/epistemic-aim.md) $A$, such as description, exploration, prediction, explanation, modal knowledge or model knowledge<br>[requested relation](../task/requested-relation.md) $R$, one of seven, from causal dependence under interventions to mathematical derivation<br>[modal strength](../task/modal-strength.md) $\mu$: actual, possible or necessary<br>[bound on the explanans](../task/admissible-explanans.md) $\lambda$<br>required accuracy $\tau$: the metric and the tolerance within which a value of the answer must match the target<br>proof obligations $\omega$: the statements that the answer must derive |
| **3. [Epistemic and pragmatic virtues](../task/epistemic-pragmatic-virtues.md)** $\mathcal{V}$ | Which qualities does the question weigh among its answers? | the virtues weighed, such as unification, robustness, intelligibility or tractability, each with its [standing](../task/epistemic-pragmatic-virtues.md#^virtue-standing): constitutive or preferred |

The symbols of the layers, each with one meaning across the notes, are registered in the [notation](../../vocabulary/notation/notation.md).

**Subject (1) versus task (2).** A question combines its subject $\Sigma$ with an epistemic task $T$. The task is fixed separately because the same subject can admit several types of answer. In particular, the epistemic aim selects the interrogative word.

*Example.* One subject yields a different question under each epistemic aim:

- explanation: "In system $S$ under conditions $D$, why/how does $P$ occur rather than $X$?"
- description: "In system $S$ under conditions $D$, what features does $P$ have?"
- prediction: "In system $S$ under conditions $D$, does $P$ occur when one element of $D$ changes?"

Three results of the literature support separating the subject from the task:

- In erotetic logic, a question divides into a *subject*, presenting the alternatives, and a *request*, specifying which of them the answer must select [belnap1976]. The subject $\Sigma$ of this method corresponds to that subject by analogy only: $\Sigma$ names the objects studied, and the alternatives are fixed by $\Sigma$ and $T$ together.
- A why-question separates its topic, namely its *explanandum* and its *contrast class*, from the sort of information that it requests. The context of the question fixes that sort of information through a *relevance relation*, which corresponds to the requested relation of this method [vanfraassen1980].
- More broadly, an epistemic achievement, such as explanation or understanding, is distinguished from the objects that it bears on. Understanding, however, is not an [aim](../task/epistemic-aim.md#^understanding) of the task, since it bears on a product of the inquiry without fixing the type of its answers.

**Subject and task (1, 2) versus virtues (3).** The subject and the task fix which statements answer the question: its possible answers and its direct answers, as the [answers of a question](question.md#^answer-sets) define them. The virtues fix no answer: they fix the **standards** by which the answers are judged, and weigh qualities that the task does not demand. A virtue marked constitutive adds a condition of admissibility, so it narrows the admissible answers. A virtue marked preferred ranks only the answers that are already admissible.

## What follows from the layers

Two properties of the answers follow from the three layers, so neither is a fourth layer of decision: ^layer-consequences

- **The answer type.** The aim, together with the other components of the task and with the subject, fixes the type of the direct answers, as the [answer form](../answer/answer-form.md#^question-fixes-type) states.
- **The conditions of satisfaction.** The tests that a candidate answer must pass are derived from the layers: admissibility and warrant from the subject and the task, together with the constitutive virtues, and appraisal from the preferred virtues. The [conditions of satisfaction](../answer/satisfaction-conditions.md#^conditions-satisfaction) state these tests.

The candidate answer, by contrast, is a **product** of the inquiry: its claim is sought, not specified. The specification fixes the type that the answer must take and the tests that it must pass, and the inquiry then produces candidates of that type.

Two results of the literature support separating the specification of a question from the assessment of its answers:

- A model is evaluated for a purpose in two steps. First, the purpose and its criterion of success are fixed. Second, the model is assessed for its reliability in meeting that criterion [parker2020].
- An explanatory question is specified separately from the rules that evaluate its candidate answers [vanfraassen1980].

## Problems and linked questions

A question rarely stands alone. A question typically serves a research problem. Its answer may supply the explanans of another question or presuppose the answer of a third.

The fields by which a question names its problem and its linked questions are documented in the [question record](../../../specification/question.md).

## Goals of the specification

The specification of a question serves four goals. ^specification-goals

| Goal                           | Effect of the specification                                                                                                                                  | Support                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Transparency**               | The inquiry commits to explicit objectives, so that its claims can be checked and its analyses reproduced.                                                   | predictions stated before data collection separate tests from post hoc accounts [nosek2018]                                                 |
| **Operationalization**         | Once the system is specified, it can be partly formalized as a repertoire of variables and relations that later analyses use.                                         | a formal model forces the modeler to specify intuitions that otherwise stay unexamined [guest2021]                                          |
| **Success conditions**         | The layers fix the [conditions of satisfaction](../answer/satisfaction-conditions.md#^conditions-satisfaction): the tests that each candidate answer must pass. These tests decide which candidates satisfy the question, and how the answers that satisfy it are appraised. | knowing a question is knowing what counts as its answers [hamblin1958], and a model is evaluated by its adequacy for a purpose [parker2020] |
| **Guidance towards an answer** | Once analyzed, the question yields the research actions that answer it and serve the other goals.                                                  | a question can be answered through the auxiliary questions that it generates [wisniewski2013]                                               |

---

## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); presupposition and corrective answers checked through the [SEP entry on questions](https://plato.stanford.edu/entries/questions/); the division of a question into subject and request checked through Wiśniewski's summaries of the book
- [guest2021] ◐ [Guest & Martin, "How computational modeling can force theory building in psychological science", _Perspectives on Psychological Science_ 16(4), 789–802, 2021](https://journals.sagepub.com/doi/abs/10.1177/1745691620970585)
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211)
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
- [wisniewski2013] ◐ [Wiśniewski, *Questions, Inferences, and Scenarios*, Studies in Logic 46, College Publications, 2013](https://philpapers.org/rec/WINQIA)
