---
tags:
  - theory
index: "[Epistemic task](docs/epistemology/objects/task/_index.md)"
aliases:
  - Epistemic task
---
# Epistemic task

> [!QUESTION] Goal: along which dimensions does the knowledge that a question requests vary, and what does each dimension decide?

The epistemic task is the layer of the [specification of a question](../question/question-specification.md) that fixes the kind of knowledge sought. A question $Q$ is specified by $\langle\Sigma,T,\mathcal{V}\rangle$: its [subject of inquiry](../subject/subject-of-inquiry.md) $\Sigma$, its epistemic task $T$, and the [virtues](epistemic-pragmatic-virtues.md) $\mathcal{V}$ that it weighs. The task belongs to the question, not to the problem that the question serves: it states which kind of answer the question requests, before any candidate answer is evaluated. The subject and the task fix the possible answers of the question and, among them, its direct answers, as the [answer sets of a question](../question/question.md#^answer-sets) define them. The virtues fix no answer set: they fix the standards by which the admissible answers are narrowed and ranked. The [conditions of satisfaction](../answer/satisfaction-conditions.md) follow from the three layers together. Through its aim, the task also constrains a candidate model, because each epistemic aim imposes its own evidential requirements.

## Sub-layers of specification

> [!IMPORTANT]
> Epistemic aim is the broadest concept of the task: **explanation** is only one aim among others, beside description, exploration, prediction, modal knowledge and knowledge of models, as the [registry of aims](epistemic-aim.md#^aim-registry) lists them.

An epistemic task is described by the tuple:
$$T=\langle A,R,\mu,\lambda,\tau,\omega\rangle $$

where $A$ is the [epistemic aim](epistemic-aim.md), $R$ the [requested relation](requested-relation.md), $\mu$ the [modal strength](modal-strength.md), $\lambda$ the [bound on the explanans](admissible-explanans.md), given by its values on two axes, which delimit the variables that an explanation may appeal to, $\tau$ the [required accuracy](#^required-accuracy) of the answer, and $\omega$ the [proof obligations](#^proof-obligations) that the answer must discharge. The first four dimensions are developed in notes of their own, and the last two below.

The fields that a question record fills for each dimension, with their admitted values, are documented in the [epistemic task of a question](../../../specification/question-task.md).

## Required accuracy

The required accuracy $\tau$ fixes how closely the answer must match the target: the metric and the tolerance within which a value of the answer must agree with an observable of the target, and the outputs or structures of the target to which they apply. The required accuracy applies to an answer whose claim is compared with data of the target, and the [fidelity test](../answer/satisfaction-conditions.md#^warrant-through-binding) reads it through the [comparison computed](../answer/model-and-binding.md#^comparison) from a binding. ^required-accuracy

- **The question owns the tolerance.** A discrepancy between a model and its target has three owners: the structural discrepancy belongs to the binding, the observation error to the data of the phenomenon, and the tolerance to the question, as the [owners of a discrepancy](../answer/model-and-binding.md#^discrepancy-owners) state. A tolerance fixed in the question before any candidate exists cannot be adjusted to the discrepancy that a fidelity test finds.
- **The tolerance follows from the purpose of the question.** A model is adequate for a purpose, not in general [parker2020]. A question that needs only the regime of the target can therefore tolerate a value off by an order of magnitude, whereas a question that must discriminate between two candidate values needs a bound finer than their difference.
- **Accuracy is tested, not weighed.** An answer outside the tolerance fails its fidelity test, so predictive accuracy is not among the [virtues](epistemic-pragmatic-virtues.md) that rank admissible answers.

## Proof obligations

The proof obligations $\omega$ are the statements that the answer must derive. Each obligation is an implication between two statements over the declared quantities, and states its direction. The converse of an obligation is a separate obligation, since a sufficient condition need not be necessary. ^proof-obligations

- **Proof obligations bound a derivation, as the required accuracy bounds a match with data.** Obligations apply when the answer must derive a statement rather than match a measurement: a consequence of a model, an impossibility or a necessity, or a claim about a formal target, whose admitted laws define the system completely. A question that asks for both a match and a derivation states both $\tau$ and $\omega$.
- **Each obligation receives its own verdict.** A consequence names the obligations that it discharges, as the [tests of the aim block](../answer/satisfaction-conditions.md#^admissibility-per-block) require, and a derivation or a counterexample settles each obligation separately. A candidate can thus discharge one direction of an equivalence and fail the other.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the relativity of adequacy to a purpose, as cited.
> - **Proposals:**
> 	- the six dimensions of the task, and the specification of a question by its subject, its task and its virtues;
> 	- the ownership of the tolerance by the question;
> 	- the proof obligations as directed implications, each with its own verdict.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
