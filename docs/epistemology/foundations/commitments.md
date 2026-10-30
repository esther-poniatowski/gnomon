---
tags:
  - theory
index: "[Foundations](docs/epistemology/foundations/_index.md)"
aliases:
  - Commitments of the method
  - Performed, recorded and judged acts
---
# Commitments of the method

> [!QUESTION] Goal: which commitments does the method of `gnomon` make about the objects and the processes of an inquiry, on which grounds, and which acts does its tool perform rather than record or leave to the researcher?

A **commitment** of the method is a choice that binds every record and every process of an inquiry. Each commitment below is stated with its grounds, and links the note that develops it. The commitments form the third part of the answer to the [root question](overview.md#^root-question) of the theory.

## Access, claims and existence

1. **Mediated access.** An object is known only through a description, which is itself a representation. *Grounds*: phenomena are inferred from data, a measurement outcome is inferred from a reading through a model of the instrument, and a target is specified by the modeller, as the [mediated access](existence-and-access.md#^mediated-access) states. Measurement and observation are therefore model-based inferences. The registry of activities still gives them the mode `non-inferential`, pending a change of the registry. ^commitment-access
2. **Literal claims, adequate declarations.** A claim is read literally and can be false of its target, whereas a declaration makes no claim and is assessed for its adequacy. *Grounds*: a law statement, a bridge law or a binding asserts a relation that can fail of its target, whereas a declaration only introduces a quantity, as the [stance of the method](existence-and-access.md#^method-stance) and the [adequacy of a declaration](things-and-constructs.md#^declaration-adequacy) state. ^commitment-literal
3. **Neutrality on existence.** No record states whether its object exists independently of any description. *Grounds*: a realist reading and an empiricist reading use the same records, the same checks and the same tests, since each test compares a claim with recorded data or with admitted laws, as the [stance of the method](existence-and-access.md#^method-stance) and the [decision on neutral records](../../adr/neutral-records-on-existence.md) state. ^commitment-neutrality

## Questions and tests

4. **The subject and the task fix the possible answers of a question.** The virtues fix the standards of the answers: a constitutive virtue narrows the admissible answers, and a preferred virtue ranks them. *Grounds*: a question is a request whose possible answers form a definite set, and a preferred virtue ranks only answers that are already admissible, so it changes no set of answers, as the [sets of answers of a question](../objects/question/question.md#^answer-sets) state. ^commitment-answers
5. **Tests fixed before evaluation, under iteration.** Each assessment is made against the version of the specification fixed before it. A revision of a layer voids the verdicts made under the earlier version and records its trigger. *Grounds*: a test fixed after a candidate is seen can be fitted to that candidate, and the [controlled iteration](../processes/inquiry/specification-order.md#^controlled-iteration) revises earlier choices after an evaluation, so each verdict must name the version that it tests, as the [conditions of satisfaction](../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) state. ^commitment-tests
6. **Three layers, with the answer as a product.** The subject, the task and the virtues specify a question. The answer type and the conditions of satisfaction follow from them, and the answer is a product of the inquiry, never part of the specification of its question. *Grounds*: the [specification of a question](../objects/question/question-specification.md) derives every requirement on an answer from the three layers. ^commitment-layers

## Evidence and representation

7. **Pluralism on evidence and on representation.** Severity governs the verdict of a test, and a credence, when stated, is Bayesian and complements the verdict. A binding records the surrogative inferences that its asserter licenses, the inferences from a feature of the model to a claim about the target, and states them in the vocabulary of the DEKI account, denotation, exemplification, keying-up and imputation, as a choice of the method. The neutrality of the binding among the accounts of representation bears on the grounds that make the inferences sound, not on the vocabulary. *Grounds*: a verdict and a credence answer two questions about one answer, as the [credence of an assessment](../objects/answer/satisfaction-conditions.md#^credence) states, and the [model and its binding](../objects/answer/model-and-binding.md) state why a binding records inferences. ^commitment-pluralism
8. **Warrant as provenance, not a degree.** The warrant of a law is its provenance, `derived`, `posited`, `fitted` or `measured`, and these values are not ordered. A result reports the set of laws whose warrant it is exposed to, never a degree. *Grounds*: the [warrant of a law](../objects/knowledge/background.md#^law-warrant) records the provenance of the law, and the [exposure rule](../objects/knowledge/grounds-and-dependence.md#^weakest-link) departs from a weakest-link rule, which needs ordered degrees. ^commitment-warrant

## Knowledge and its revision

9. **Base revision.** The accepted knowledge is a belief base, and its revision follows the norm of base revision. *Grounds*: a claim enters the [accepted knowledge](inquiry-and-state.md#^state) only by an act of acceptance, and the [revision](../processes/activities/revision.md) activities state the norm. ^commitment-base
10. **No inference at run time.** A tool never adds a claim, a relation or a record kind that no record states, never decides whether an answer is accepted, and reports the dependents of a revision without relabelling them. *Grounds*: a derived claim would have no author and no trace of revision, as the [decision against inference at run time](../../adr/no-run-time-inference.md#^excluded-inference) states. [Acceptance](../objects/status/statuses-and-acceptance.md#^acceptance-act) and [propagation](../objects/knowledge/grounds-and-dependence.md#^propagation) apply the commitment. ^commitment-no-inference
11. **Fallibilism.** Every specification of a record carries a maturity, every revision records its trigger, and the controlled iteration keeps that revision non-circular. *Grounds*: the [maturity](../objects/status/statuses-and-acceptance.md#^maturity) expects revision, and the [decision on revision accountability](../../adr/revision-accountability.md#^traceable-revision) traces each revision to its origin. ^commitment-fallibilism
12. **Least commitment.** A choice is deferred until a condition requires it. *Grounds*: fewer choices then need revision, as the devices of the [order of specification](../processes/inquiry/specification-order.md) state. ^commitment-least

## Records and their expression

13. **One source per unit.** Each research unit has one authored source, and another record names it by its identifier, never restates it. *Grounds*: a restated unit can diverge from its source without any check noticing, as the [rule of one source](../../adr/one-source-per-unit.md#^one-source) states. ^commitment-one-source
14. **A role fixed by place.** The epistemic role of a research unit is fixed by the kind of object that holds it and by its place in that object, never by a label. *Grounds*: a unit then cannot blend a definition and a result, as the [roles of the research units](../objects/status/epistemic-objects.md#^role-by-place) state. ^commitment-role
15. **An exposition adds no content.** An exposition selects and orders research units for an audience, and every statement that carries content presents a research unit. *Grounds*: content has one source, and an exposition stands to the records as a view stands to its store, as the [rule against added content](../expression/exposition.md#^adds-no-content) states. ^commitment-exposition

## Performed, recorded and judged

The commitments against inference at run time and for one source divide each process of an inquiry into three parts: the computations and the checks that the tool performs by a declared rule, the authored contents that the records only hold, and the judgments that the researcher makes. ^performed-recorded-judged

| Process | Performed by the tool | Held by the records only | Judged by the researcher |
| --- | --- | --- | --- |
| comparing a model with data | computes the [comparison](../objects/answer/model-and-binding.md#^comparison) from a binding, a version of the data, a metric and a tolerance | the inputs of the comparison, cited by the assessment | the binding, with its declared discrepancy |
| assessing an answer | reads the [disposition](../objects/answer/satisfaction-conditions.md#^disposition) from the verdicts; checks an authored verdict against the [rules on the reports](../objects/answer/satisfaction-conditions.md#^fidelity-reads-reports) of a comparison | the verdict of each test, the appraisal, the credence and the ranking | whether a test was severe, and the verdict of each warrant test |
| accepting an answer | reports an acceptance whose assessment is `not-satisfied`, under a proposal of the method | the record of the acceptance | the act of acceptance or of withdrawal |
| revising | reports every record that rests on a revised unit, and the laws to which a result is exposed | the revision, with its trigger | whether each dependent holds, is adjusted or is retracted, and which exposed law is the weakest |
| diagnosing answerability | computes the open conditions of a question | the asserted state of each condition, with the records that support it | whether a condition is `established` or `refuted` |
| performing an act | runs the [itinerary check](../processes/activities/epistemic-activities.md#^itinerary-check) | the step, with the verdict of its norm | the verdict of each norm, and the assignment of the inputs of an act |

The [choices left to the researcher](../processes/inquiry/choice-of-act.md#^researcher-choices) when the next act is chosen extend the last column.

---
## Sources

> [!NOTE] Status of the claims
> - **Proposals:** the list of commitments, the grouping of the commitments, and the division of each process into the acts that the tool performs, the contents that the records hold and the judgments of the researcher. The grounds of each commitment are established or proposed in the note that it links.
