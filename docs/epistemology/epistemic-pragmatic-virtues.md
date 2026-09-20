---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying epistemic and pragmatic virtues
tags: []
source:
---
#  Specifying an epistemic and pragmatic virtues

> [!QUESTION] Goal: what must be fixed to specify epistemic and pragmatic virtues of an answer or model?

This [layer of inquiry](inquiry-specification.md) names additional properties of the answer that **increase its value beyond minimally satisfying the epistemic task**. These properties typically characterize practical and cognitive effects that are _not already constitutive of the specified epistemic task_, but make an admissible answer more useful, illuminating, or reusable. They separate answers that are merely valid from answers that are actually useful.

Adequacy is **relational and evaluative**:
$$\operatorname{Adequate}(M\mid Q,\Gamma)$$
where $Q$ is the specified epistemic problem and $\Gamma$ contains *relevant methodological and pragmatic circumstances*, following the [notation registry](notation.md).

These desiderata provide additional constrains that shape the form of an adequate answer (e.g. the types of variables, the nature of equations). Indeed, several answers or models may provide an equally admissible explanation but not yield the same practical and cognitive effects.

> [!ERROR] Listed virtues do not restate requirements for the epistemic task

*Examples*: 

- a derivation may include irrelevant, uneconomical detours,
- a fully expanded formula may fail to capture the high-level load-bearing structural properties, 
- an dynamical equation may fail to reveal qualitative regimes, imposing computationally extensive simulations,
- an expression may be exact but uncomputable in practice,
- a mechanism might apply in a narrow setting although it could be generalized under relaxing a few assumptions.

| Virtue                                  | Operational question                                                                          | Main epistemic benefit                                              | Representative account                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Unification** | Does the account explain many phenomena through a small number of common principles/patterns? | scope; systematic integration                                       | Friedman; Kitcher                                                                     |
| **Generality / scope** | Does the same explanatory structure extend across cases or parameter regimes?                 | transfer and reuse                                                  | closely related to unification, but without requiring a common explanatory derivation |
| **Robustness** | Do the relevant conclusions survive changes in parameters, assumptions, or representation?    | identifies which conclusions depend on incidental modelling choices | robustness-analysis literature                                                        |
| **Intelligibility / qualitative grasp** | Can characteristic consequences be recognized without carrying out the full calculation?      | understanding; qualitative anticipation                             | de Regt                                                                               |
| **Structural transparency** | Does the representation make the important components, relations, and dependencies salient?   | grasp of organization / dependence                                  | accounts of scientific understanding; Grimm/Kvanvig                                   |
| **Economy / simplicity** | Does it achieve its purpose without unnecessary representational or computational complexity? | cognitive and methodological efficiency                             | traditional theoretical virtues; modelling literature                                 |
| **Tractability** | Can the model actually be analyzed, computed, manipulated, or used under available resources? | practical usability                                                 | modelling / adequacy-for-purpose literature, Parker                                   |

- **Some aims force the selection of virtues.** When the product of the aim is itself a cognitive state, the properties that constitute that state are *selected with the aim*, instead of being added to it. ^entailed-virtues

| Epistemic aim                                                                   | Virtues that the aim forces to select                                                                                                                               |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Understanding**                                                               | intelligibility / qualitative grasp, and structural transparency                                                                                                    |
| **Prediction**                                                                  | none of the listed virtues: *predictive accuracy* is not considered as an additional virtue, since it is the product itself, fixed by the required accuracy $\tau$, |
| **Description, exploration, explanation, modal knowledge, knowledge of models** | none by default: these virtues bear on the answer only if the question selects them                                                                                 |

- **A forced virtue is constitutive, not merely preferred.** Once the aim forces a virtue, the [product test](satisfaction-conditions.md) applies it as a success condition, and the appraisal no longer counts it a second time.

> [!CHECK] Support from the literature
> Parker's adequacy-for-purpose framework argues that the adequacy of a model depends on what they are being used to accomplish and on the *broader circumstances of use*.
> The philosophy of models supports the general idea that representational accuracy and explanatory adequacy should not be equated. Idealized models may omit or distort features while preserving what matters for the intended epistemic function.