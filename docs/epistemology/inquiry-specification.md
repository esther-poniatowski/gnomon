---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying an inquity
tags: []
source:
---
# Specifying an inquiry

> [!QUESTION] Goal: what must be fixed to specify a research objective?

> [!DANGER] Philosophy of science offers no single canonical decomposition of an inquiry: the layers of specification combine several traditions.

## Layers of specification

A research objective is specified in four layers, each with a **distinct logical role**:

| Layer of specification                                                   | Question                                                                   | Typical concepts                                                                                                                                                                                           |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. [Subject of inquiry](subject-of-inquiry.md)**                       | What objects is the inquiry about?                                         | target system $S$, phenomenon/explanandum $P$, contrast class $X$, domain of conditions $D$                                                                                                                |
| **2. [Epistemic task](epistemic-task.md)**                               | What *kind* of knowledge or *achievement* is sought?                       | epistemic aim $A$ (description vs prediction vs explanation vs exploration)<br>relevance relations $R$ (causal vs mechanistic vs mathematical)<br>modal status $\mu$ (how-actually vs how-possibly)<br>admissible explanans $\lambda$<br>required accuracy $\tau$ |
| **3. [Epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md)** | What must the answer accomplish to be practically or cognitively *useful*? | unification, economy, pragmatic use, robustness, intelligibility / qualitative grasp, tractability, etc                                                                                                    |
| **4. [Answer form](answer-form.md) and [conditions of satisfaction](satisfaction-conditions.md)** | What form must the answer take, and which tests must it pass?      | constituents $C$, terms $V$, laws or structural relations $L$, organization $O$, idealizations $I$, explanans $E$<br>admissibility, warrant and appraisal                                                                     |

The components of each layer are denoted by letters, each with one meaning fixed across the notes by a shared [notation registry](notation.md).

**Subject (1) versus Task (2)**. A research question combines the [subject of inquiry](subject-of-inquiry.md) $\Sigma$ with an [epistemic task](epistemic-task.md) $T$: 
$$Q=\langle \Sigma,T\rangle$$
The task is fixed separately because the same subject can admit several types of answer. In particular, the epistemic aim selects the interrogative word.

*Example.* One subject yields a different question under each epistemic aim:

- explanation: "In system $S$ under conditions $D$, why/how does $P$ occur rather than $X$?"
- description: "In system $S$ under conditions $D$, what features does $P$ have?"
- prediction: "In system $S$ under conditions $D$, does $P$ occur when one element of $D$ changes?"

Three results of the literature support separating the subject from the task:

- In erotetic logic, a question divides into a *subject*, presenting the alternatives, and a *request*, specifying which of them the answer must select [belnap1976].
- A why-question separates its topic, namely its *explanandum* and its *contrast class*, from the sort of information that it requests. The context of the question fixes that sort of information through a *relevance relation* [vanfraassen1980].
- More broadly, an epistemic achievement, such as explanation or understanding, is distinguished from the objects that it bears on.

**Task (2) versus Answer form and conditions of satisfaction (4)**. Two results of the literature support separating the task from the tests of an answer:

- A model is evaluated for a purpose in two steps. First, the purpose and its criterion of success are fixed. Second, the model is assessed for its reliability in meeting that criterion [parker2020].
- An explanatory question is specified separately from the rules that evaluate its candidate answers [vanfraassen1980].

## Goals of the specification

The specification of an inquiry serves four goals. ^specification-goals

| Goal                           | Effect of the specification                                                                                                                                  | Support                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Transparency**               | The inquiry commits to explicit objectives, so that its claims can be checked and its analyses reproduced.                                                   | predictions stated before data collection separate tests from post hoc accounts [nosek2018]                                                 |
| **Operationalization**         | Once the system is specified, it can be partly formalized as a repertoire of variables and relations that later analyses use.                                         | a formal model forces the modeler to specify intuitions that otherwise stay unexamined [guest2021]                                          |
| **Success conditions**         | The specification fixes the [conditions of satisfaction](satisfaction-conditions.md#^conditions-satisfaction): the tests that each candidate answer must pass. These tests decide which candidates are admissible and which are adequate. | a question is determined by the set of its possible answers [hamblin1958], and a model is evaluated by its adequacy for a purpose [parker2020] |
| **Guidance towards an answer** | Once analyzed, the question yields the research actions that answer it and serve the other goals.                                                  | a question can be answered through the auxiliary questions that it generates [wisniewski2013]                                               |

---

## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ Belnap & Steel, _The Logic of Questions and Answers_, Yale UP, 1976, via [SEP, Questions](https://plato.stanford.edu/entries/questions/). The subject/request distinction was checked only through a summary returned by a search engine.
- [guest2021] ◐ [Guest & Martin, "How computational modeling can force theory building in psychological science", _Perspectives on Psychological Science_ 16(4), 789–802, 2021](https://journals.sagepub.com/doi/abs/10.1177/1745691620970585)
- [hamblin1958] ◐ [Hamblin, "Questions", _Australasian Journal of Philosophy_ 36(3), 1958](https://www.tandfonline.com/doi/abs/10.1080/00048405885200211)
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", _Philosophy of Science_ 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, ch. 5, read in [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [wisniewski2013] ◐ [Wiśniewski, *Questions, Inferences, and Scenarios*, College Publications, 2013](https://philpapers.org/rec/WINQIA)
