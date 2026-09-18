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
$$\operatorname{Adequate}(M\mid Q,C)$$
where $Q$ is the specified epistemic problem and $C$ contains *relevant methodological and pragmatic circumstances*.

These desiderata provide additional constrains that shape the form of an adequate answer (e.g. the types of variables, the nature of equations). Several answers or models may provide an equally admissible explanation but not provide the same practical and cognitive effects.

*Examples*: 

- a derivation may include irrelevant, uneconomical detours,
- a fully expanded formula may fail to capture the high-level load-bearing structural properties, 
- an dynamical equation may fail to reveal qualitative regimes, imposing computationally extensive simulations,
- an expression may be exact but uncomputable in practice,
- a mechanism might apply in a narrow setting although it could be generalized under relaxing a few assumptions.

| Virtue                                  | Operational question                                                                          | Main epistemic benefit                                              | Representative account                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Unification**                         | Does the account explain many phenomena through a small number of common principles/patterns? | scope; systematic integration                                       | Friedman; Kitcher                                                                     |
| **Generality / scope**                  | Does the same explanatory structure extend across cases or parameter regimes?                 | transfer and reuse                                                  | closely related to unification, but without requiring a common explanatory derivation |
| **Robustness**                          | Do the relevant conclusions survive changes in parameters, assumptions, or representation?    | identifies which conclusions depend on incidental modelling choices | robustness-analysis literature                                                        |
| **Intelligibility / qualitative grasp** | Can characteristic consequences be recognized without carrying out the full calculation?      | understanding; qualitative anticipation                             | de Regt                                                                               |
| **Structural transparency**             | Does the representation make the important components, relations, and dependencies salient?   | grasp of organization / dependence                                  | accounts of scientific understanding; Grimm/Kvanvig                                   |
| **Economy / simplicity**                | Does it achieve its purpose without unnecessary representational or computational complexity? | cognitive and methodological efficiency                             | traditional theoretical virtues; modelling literature                                 |
| **Tractability**                        | Can the model actually be analyzed, computed, manipulated, or used under available resources? | practical usability                                                 | modelling / adequacy-for-purpose literature, Parker                                   |

> [!ERROR] Virtues should restate requirements for the epistemic task.
> Include here only properties that improve an already admissible answer without defining what makes it an answer of the requested kind. In particular:
> - *predictive accuracy* should not be considered as an additional virtue when prediction is the task itself: it is then a constitutive success condition;
> - difference-making (Strevens) should not be listed as a generic virtue if it is being used to characterize what makes an explanation explanatory; that would duplicate the task's constitutive requirements.

> [!CHECK] Support from the literature
> Parker's adequacy-for-purpose framework argues that the adequacy of a model depends on what they are being used to accomplish and on the *broader circumstances of use*.
> The philosophy of models supports the general idea that representational accuracy and explanatory adequacy should not be equated. Idealized models may omit or distort features while preserving what matters for the intended epistemic function.