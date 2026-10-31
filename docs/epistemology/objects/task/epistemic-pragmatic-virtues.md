---
tags:
  - theory
index: "[Epistemic task](docs/epistemology/objects/task/_index.md)"
aliases:
  - Epistemic and pragmatic virtues
---
# Epistemic and pragmatic virtues

> [!QUESTION] Goal: which qualities can a question select for its answers beyond its epistemic task, and how does each bear on the assessment of answers?

The virtues, written $\mathcal{V}$, form the third layer of the [specification of a question](../question/question-specification.md), beside its subject and its [epistemic task](epistemic-task.md). A virtue is a quality that the question selects for its answers, beyond the kind of knowledge that the task fixes. The question marks each selected virtue either **constitutive**, a condition that every admissible answer meets, or **preferred**, a ground for ranking the answers that are already admissible, as the [standing of a virtue](#^virtue-standing) states. The virtues fix none of the possible or direct answers of the question, which its subject and its task fix: they fix its standards, since a constitutive virtue narrows the [admissible answers](../question/question.md#^answer-sets) and a preferred virtue ranks them. The virtues typically bear on practical and cognitive effects that the task does not require: they make an answer more useful, more intelligible, or more reusable.

The virtues are kept apart from the [adequacy for purpose](../answer/model-and-binding.md#^adequacy-for-purpose) of a model, which the note on the model and its binding owns.

The virtues constrain an answer beyond the requirements of its task: some bear on the range of its claims, and the others on the *form* of its representation (e.g. the types of variables, the nature of equations). These constraints are needed because several answers or models may be equally admissible and still differ in their practical and cognitive effects.

> [!ERROR] A listed virtue never restates a requirement of the epistemic task

*Examples* of admissible answers that lack a virtue:

- a derivation may include irrelevant, uneconomical steps;
- a fully expanded formula may fail to capture the structural properties, stated at a higher level, on which the result rests;
- a dynamical equation may fail to reveal qualitative regimes, and so impose computationally extensive simulations;
- an expression may be exact but uncomputable in practice;
- a mechanism may be stated for a narrow setting, although relaxing a few assumptions would widen its scope.

Each virtue below is stated with the operational question that tests it, and the fields by which a question weighs it are documented in the [virtues of a question](../../../specification/question-virtues.md).

| Virtue                                  | Operational question                                                                          | Main epistemic benefit                                              | Representative account                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Unification** | Does the account explain many phenomena through a small number of common principles or patterns? | scope; systematic integration                                       | [friedman1974]; [kitcher1981]                                                                     |
| **Generality / scope** | Does the same explanatory structure extend across cases or parameter regimes?                 | transfer and reuse                                                  | closely related to unification, but without requiring a common explanatory derivation |
| **Robustness** | Do the relevant conclusions survive changes in parameters, assumptions, or representation?    | identifies which conclusions depend on incidental modelling choices | robustness analysis [weisberg2006]                                                    |
| **Intelligibility / qualitative grasp** | Can characteristic consequences be recognized without carrying out the full calculation?      | understanding; qualitative anticipation                             | contextual approach to understanding [deregt2005]                                     |
| **Structural transparency** | Does the representation make the important components, relations, and dependencies salient?   | grasp of organization and dependence                                | accounts of scientific understanding [grimm2010]; [kvanvig2003]                                   |
| **Economy / simplicity** | Does the account achieve its purpose without unnecessary representational or computational complexity? | cognitive and methodological efficiency                             | the theoretical virtues of theory choice [kuhn1977]                                   |
| **Tractability** | Can the model be analyzed, computed, manipulated, or used with the available resources? | practical usability                                                 | proposal of this method |

- **Each virtue entry states its standing, independently of the aim.** A virtue bears on an answer in one of two ways. A **constitutive** virtue is a condition of the product: its absence makes an answer inadmissible however accurate. Such a virtue is applied by the product test, one of the [levels of evaluation](../answer/satisfaction-conditions.md#^conditions-satisfaction) of a candidate answer. A **preferred** virtue ranks answers that are already admissible, and is applied by appraisal. The same virtue takes either standing in different inquiries. For example, in one inquiry, intelligibility may be required of any answer regardless of the product sought. In another, the same virtue only decides between two admissible accounts. The question therefore states the standing on each entry. Each virtue is then applied by exactly one tier. ^virtue-standing

- **Robustness names a virtue and a test, at two tiers.** The [robustness test](../answer/satisfaction-conditions.md#^warrant-through-binding) of warrant checks that the claim survives each idealization declared among its grounds, and an answer that fails it is not warranted. The virtue of robustness ranks answers that already pass, by the breadth of the changes in parameters, assumptions or representation that their conclusions survive beyond those idealizations [weisberg2006]. ^robustness-two-tiers

- **Predictive accuracy is not among the virtues.** Predictive accuracy is the product of the predictive aim itself, fixed by the required accuracy $\tau$, and is therefore tested, not weighed.

- **The virtues divide in two by the aspect of the answer that they bear on.** Unification, generality and robustness bear on the *content* of an answer: its claims and their range. When held constitutive, these three virtues subject the explanatory structure to the [scope criterion](../answer/satisfaction-conditions.md#^conditions-satisfaction) that already governs the claim: the whole reference class under the domain must be reached. Intelligibility, structural transparency, economy and tractability bear instead on the *form* in which that content is presented. No other test checks these four virtues, because every other criterion bears only on the *assertions* of an answer. An inquiry seeking understanding therefore adds nothing to its subject or its task, and states all its specific demands among the virtues. This placement holds because intelligibility is a property of a theory as scientists use it, not a product beside explanation [deregt2005]. ^virtue-kinds

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [friedman1974] ◐ [Friedman, "Explanation and scientific understanding", _The Journal of Philosophy_ 71(1), 5–19, 1974](https://philpapers.org/rec/FRIEAS)
- [grimm2010] ◐ [Grimm, "The goal of explanation", _Studies in History and Philosophy of Science_ 41(4), 337–344, 2010](https://philpapers.org/rec/GRITGO-12)
- [kitcher1981] ◐ [Kitcher, "Explanatory unification", _Philosophy of Science_ 48(4), 507–531, 1981](https://philpapers.org/rec/KITEU)
- [kuhn1977] ◐ Kuhn, "Objectivity, value judgment, and theory choice", in *The Essential Tension: Selected Studies in Scientific Tradition and Change*, University of Chicago Press, 320–339, 1977; accuracy, consistency, scope, simplicity and fruitfulness as criteria of theory choice
- [kvanvig2003] ◐ [Kvanvig, *The Value of Knowledge and the Pursuit of Understanding*, Cambridge UP, 2003](https://philpapers.org/rec/KVATVO-8)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006](https://doi.org/10.1086/518628)
