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
| **[Epistemic aim](epistemic-aim.md) $A$** | always: it selects the interrogative word of the question | What knowledge is the inquiry intended to produce? What cognitive achievement is sought? | description/representation, exploration, prediction, explanation, modal knowledge, knowledge of theories or models |  |
| **[Requested relation](requested-relation.md) $R$** | whenever the answer must relate an explanans to the explanandum | What kind of relation must the explanans bear to the explanandum to answer the question? | causal, mechanistic, constitutive, functional, statistical, nomological, mathematical | van Fraassen ("relevance / dependence relation") |
| **[Modal strength](modal-strength.md) $\mu$** | always | How tight the answer must bind the phenomenon | actual, possible, necessary | Verreault-Julien (_how-possibly_ vs _how-actually_) |
| **[Admissible explanans](admissible-explanans.md) $\lambda$** | only to bound the explanans further; left aside, proportionality with the phenomenon selects the level | Which kinds of variables may enter the explanans? | compositional level; substrate dependence | Craver (levels of mechanisms); Batterman (universality) |
| **Required accuracy $\tau$** | always, and `not-applicable` when the answer is matched against no measurement | Which observables of the target must the answer reproduce, which of its structures must correspond, and to what accuracy? | qualitative agreement; order of magnitude; a stated numeric bound; structural correspondence only. Within a tolerance, `answer` names the candidate's value and `target` the observable it reproduces. Each output and each structure carries a justification stating why the question demands that particular correspondence | fidelity criteria (Weisberg); adequacy for purpose (Parker) |
| **Proof obligations** | when the answer must derive a statement rather than match a measurement | Which implication must the answer establish, and in which direction? | per obligation, the antecedent and the consequent, each as expressions over the declared observables; a converse is a second obligation | proof as the satisfaction of a mathematical relation [craver2007] |

> [!HINT] Practical use
> These dimensions are fixed before any candidate exists, and the [fidelity test](satisfaction-conditions.md) checks a candidate against that accuracy.

> [!NOTE]
> Each dimension is developed in its own note, linked in the table. The required accuracy has none yet, because its row holds its whole specification.
