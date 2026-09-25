---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying epistemic and pragmatic virtues
tags: []
source:
---
# Specifying epistemic and pragmatic virtues

> [!QUESTION] Goal: what must be fixed to specify the epistemic and pragmatic virtues of an answer or model?

The virtues form a [layer of the inquiry specification](inquiry-specification.md): they name properties that increase the **value** of an answer once it already satisfies the epistemic task. These properties typically bear on practical and cognitive effects that are not already *constitutive* of the specified epistemic task. Such effects make an admissible answer more useful, more intelligible, or more reusable.

Adequacy is **relational and evaluative**:
$$\operatorname{Adequate}(M\mid Q,\Gamma)$$
where $Q$ is the specified epistemic problem and $\Gamma$ contains *relevant methodological and pragmatic circumstances*. Both symbols follow the [notation registry shared across the framework](notation.md).

The virtues constrain an adequate answer beyond its admissibility: some bear on the range of its claims, and the others on the *form* in which it presents them (e.g. the types of variables, the nature of equations). These constraints are needed because several answers or models may provide equally admissible explanations and still differ in their practical and cognitive effects.

> [!ERROR] A listed virtue never restates a requirement of the epistemic task

*Examples* of admissible answers that lack a virtue:

- a derivation may include irrelevant, uneconomical steps;
- a fully expanded formula may fail to capture the structural properties, stated at a higher level, on which the result rests;
- a dynamical equation may fail to reveal qualitative regimes, and so impose computationally extensive simulations;
- an expression may be exact but uncomputable in practice;
- a mechanism may be stated for a narrow setting, although relaxing a few assumptions would widen its scope.

| Virtue                                  | Operational question                                                                          | Main epistemic benefit                                              | Representative account                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Unification** | Does the account explain many phenomena through a small number of common principles or patterns? | scope; systematic integration                                       | [friedman1974]; [kitcher1981]                                                                     |
| **Generality / scope** | Does the same explanatory structure extend across cases or parameter regimes?                 | transfer and reuse                                                  | closely related to unification, but without requiring a common explanatory derivation |
| **Robustness** | Do the relevant conclusions survive changes in parameters, assumptions, or representation?    | identifies which conclusions depend on incidental modelling choices | robustness analysis [weisberg2006]                                                    |
| **Intelligibility / qualitative grasp** | Can characteristic consequences be recognized without carrying out the full calculation?      | understanding; qualitative anticipation                             | contextual approach to understanding [deregt2005]                                     |
| **Structural transparency** | Does the representation make the important components, relations, and dependencies salient?   | grasp of organization and dependence                                | accounts of scientific understanding [grimm2010]; [kvanvig2003]                                   |
| **Economy / simplicity** | Does the account achieve its purpose without unnecessary representational or computational complexity? | cognitive and methodological efficiency                             | traditional theoretical virtues; modelling literature                                 |
| **Tractability** | Can the model be analyzed, computed, manipulated, or used with the available resources? | practical usability                                                 | adequacy for purpose [parker2020]; modelling literature                               |

- **Each virtue entry states its standing, independently of the aim.** A virtue bears on an answer in one of two ways. A **constitutive** virtue is a condition of the product: its absence makes an answer inadmissible however accurate. Such a virtue is applied by the product test, [one of the levels at which a candidate answer is evaluated](satisfaction-conditions.md#^conditions-satisfaction). A **preferred** virtue ranks answers that are already admissible, and is applied by appraisal. The same virtue takes either standing in different inquiries. For example, in one inquiry, intelligibility may be required of any answer regardless of the product sought. In another, the same virtue only decides between two adequate accounts. The question therefore states the standing on each entry. Each virtue is then applied by exactly one tier. ^virtue-standing

- **Predictive accuracy is not among the virtues.** Predictive accuracy is the product of the predictive aim itself, fixed by the required accuracy $\tau$, and is therefore tested, not weighed.

- **The virtues divide in two by the aspect of the answer that they bear on.** Unification, generality and robustness bear on the *content* of an answer: its claims and their range. When held constitutive, these three virtues subject the explanatory structure to the scope criterion that already governs the claim: [the whole reference class under the domain must be reached](satisfaction-conditions.md#^conditions-satisfaction). Intelligibility, structural transparency, economy and tractability bear instead on the *form* in which that content is presented. No other test checks these four virtues, because every other criterion bears only on the *assertions* of an answer. An inquiry seeking understanding therefore adds nothing to its subject or its task, and states all its specific demands among the virtues. This placement holds because intelligibility is a property of a theory as scientists use it, not a product beside explanation [deregt2005]. ^virtue-kinds

> [!CHECK] Support from the literature
> The adequacy of a model depends on the purpose that it serves and on the *broader circumstances of use* [parker2020].
> Representational accuracy differs from explanatory adequacy (philosophy of models). An idealized model, for instance, may omit or distort some features yet preserve the features that its intended epistemic function requires.

---
## Sources

Marks follow [the legend that states how each entry was checked](../../CONTRIBUTING.md#^reading-marks).

- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", _Philosophy of Science_ 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [friedman1974] ◐ [Friedman, "Explanation and scientific understanding", _The Journal of Philosophy_ 71(1), 5–19, 1974](https://philpapers.org/rec/FRIEAS)
- [kitcher1981] ◐ [Kitcher, "Explanatory unification", _Philosophy of Science_ 48(4), 507–531, 1981](https://philpapers.org/rec/KITEU)
- [grimm2010] ◐ [Grimm, "The goal of explanation", _Studies in History and Philosophy of Science_ 41(4), 337–344, 2010](https://philpapers.org/rec/GRITGO-12)
- [kvanvig2003] ◐ [Kvanvig, *The Value of Knowledge and the Pursuit of Understanding*, Cambridge UP, 2003](https://philpapers.org/rec/KVATVO-8)
