---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Assessment record
---
# Assessment record

> [!QUESTION] Goal: what does a researcher write in each field of an assessment record, and when is each field required?

The tests whose verdicts this record holds are stated in the [conditions of satisfaction](../epistemology/objects/answer/satisfaction-conditions.md).

The verdicts of the tests and the appraisal are kept outside the answer, in one record per candidate or construct assessed. The record references the object that it assesses, either a candidate answer or a construct that a problem demands, and the question or the problem that fixes its tests. A candidate can then be restated, or a second one added, without rewriting a verdict or an assessment already settled. ^assessment-record

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Assesses — the candidate answer or the construct whose verdicts this record holds | always | the identifier of one [candidate answer](../epistemology/objects/answer/answer-form.md), or of the record of a construct that a problem demands, such as a model | the answer by inhibitory delay | — |
| Against — the record whose specifications fix which tests apply | always | for an answer, the identifier of one question, or the revised question that a reformulating answer names; for a construct, the identifier of its problem | why the network is synchronous rather than asynchronous | [tests drawn from filled specifications](../epistemology/objects/answer/satisfaction-conditions.md#^conditions-satisfaction) |
| Tests: admissibility | for an answer | per criterion of the tests of the core and of the tests of the block of the aim of the question, a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | contrast: pass, by producing the asynchronous state in a simulation; admissible explanans: not-applicable, since the question bounded the answer to no variables | the [admissibility level](../epistemology/objects/answer/satisfaction-conditions.md#^admissibility-per-block) |
| Tests: warrant | for an answer | per criterion of the warrant table, a verdict with the evidence that settles it | robustness: fail, since the claim did not survive at finite network size | the [warrant level](../epistemology/objects/answer/satisfaction-conditions.md#^warrant-through-binding) |
| Tests: constraints | for a construct | per constraint of the problem, its name and a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | a model that reproduces the delay within the tolerance of the problem: pass | the [demand met](../epistemology/objects/problem/epistemic-problem.md#^demand-met) |
| Comparisons — the inputs from which each comparison cited by a verdict is recomputed | when a verdict of fidelity rests on a binding | per comparison, the binding and its version, and the version of the data; the metric and the tolerance are read from the question | version 2 of the binding of the rate model, with version 3 of the recordings | the [computed comparison](../epistemology/objects/answer/model-and-binding.md#^comparison-recomputed) |
| Obligations | when the question states a proof obligation | per obligation, a verdict, pass · fail · pending, or not-applicable for a corrective answer, which holds no aim block, with the derivation or the counterexample that settles it, and the identifier of the [derivation record](derivation.md) when one settles it | the necessary direction: pass, by the derivation of Lemma 2; the sufficient direction: fail, by a counterexample | — |
| Appraisal | when the question marks a virtue [preferred](../epistemology/objects/task/epistemic-pragmatic-virtues.md#^virtue-standing) and no test of admissibility or of warrant fails or stays pending | per virtue, the assessment of this answer, and the candidates over which it is preferred once they have been appraised | intelligibility: the oscillation frequency can be read off the delay, without simulating the network | the [appraisal record](../epistemology/objects/answer/satisfaction-conditions.md#^appraisal-record) |
| Credence | when the assessor states a degree of belief in the answer | a number between 0 and 1, with the evidence and the prior from which it follows | 0.6, after two replications at a larger width | degree of belief, revised by conditionalization [talbott2016] |
| Credence: value | with the credence | a number between 0 and 1 | 0.6 | — |
| Credence: basis | with the credence | the evidence and the prior from which the value follows | two replications at a larger width, from a prior of 0.3 | [credence beside the verdicts](../epistemology/objects/answer/satisfaction-conditions.md#^credence) |

- **The record cannot yet name the version of the question that it read.** Each assessment is made against the version of the specification fixed before it, and a revision of a layer voids the verdicts made under the earlier version, as the [rule on versions of the specification](../epistemology/objects/answer/satisfaction-conditions.md#^tests-fixed-before) states. The field `question` references the question in its present state only, since the records keep no successive versions, as the [versions of records](itinerary.md#^record-versions) state. ^question-version

- **A verdict of `not-applicable` is a *result*.** The record marks a test removed by an empty specification as `not-applicable`, instead of leaving it pending. A reader can then tell an untested candidate from a fully assessed one.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [talbott2016] ◐ [Talbott, "Bayesian epistemology", _SEP_, revised 2016](https://plato.stanford.edu/entries/epistemology-bayesian/), §1 on degrees of belief and conditionalization
