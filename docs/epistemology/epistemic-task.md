---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying an epistemic task
tags: []
source:
---
#  Specifying an epistemic task

> [!QUESTION] Goal: what must be fixed to specify an epistemic task?

This [layer of inquiry](inquiry-specification.md) specifies the **epistemic problem before any candidate answer is evaluated**. Different aims impose different evidential requirements on a model.

## Sub-levels of specification

> [!IMPORTANT]
> Epistemic aim is the broadest concept. **Explanation is only one epistemic aim among others**. The philosophy-of-modeling literature explicitly distinguishes explaining and understanding from other cognitive functions of models.

An epistemic task can be described by:
$$T=\langle A,R,\mu,\lambda,\tau\rangle $$

| Dimension | When it is required | Role | Typical options | Canonical tradition |
| --------- | ------------------- | ---- | --------------- | ------------------- |
| **[Epistemic aim](epistemic-aim.md) $A$** | always: it selects the interrogative word of the question | What knowledge is the inquiry intended to produce? What cognitive achievement is sought? | description/representation, prediction, explanation, understanding, exploration, possibility proof, theory/model testing |  |
| **[Requested relation](requested-relation.md) $R$** | whenever the answer must relate an explanans to the explanandum | What kind of relation must the explanans bear to the explanandum to answer the question? | causal, mechanistic, constitutive, functional, statistical, nomological, mathematical | van Fraassen ("relevance / dependence relation") |
| **[Modal strength](modal-strength.md) $\mu$** | always | How tight the answer must bind the phenomenon | actual, possible, necessary | Verreault-Julien (_how-possibly_ vs _how-actually_) |
| **[Level of the explanans](explanans-level.md) $\lambda$** | only to bound the explanans further; left aside, proportionality with the phenomenon selects the level | Which kinds of variables may enter the explanans? | compositional level; substrate dependence | Craver (levels of mechanisms); Batterman (universality) |
| **Required accuracy $\tau$** | when the answer must be matched against measurements | Which outputs of the model must match which observables of the target, which structures of the model must match which structures of the target, and to what accuracy? | qualitative agreement; order of magnitude; a stated numeric bound; structural correspondence only | fidelity criteria (Weisberg); adequacy for purpose (Parker) |

> [!HINT] Practical use
> This dimensions are fixed before any candidate exists, and the [fidelity test](satisfaction-conditions.md) checks whether a candidate against that accuracy.

> [!NOTE]
> Each dimension is developed in its own note, linked in the table. The required accuracy has none yet, because its row holds its whole specification.
