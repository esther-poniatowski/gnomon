---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying an epistemic task
tags: []
source:
---
# Specifying an epistemic task

> [!QUESTION] Goal: what must be fixed to specify an epistemic task?

The epistemic task is the layer of an [inquiry specification](inquiry-specification.md) that fixes the kind of knowledge sought. The task states the **epistemic problem** before any candidate answer is evaluated. Through its aim, the task also constrains a candidate model, because each epistemic aim imposes its own evidential requirements.

## Sub-layers of specification

> [!IMPORTANT]
> Epistemic aim is the broadest concept of the task: **explanation** is only one aim among others. The philosophy of modeling supports this breadth: it explicitly distinguishes explaining and understanding from the other cognitive functions of models.

An epistemic task is described by the tuple:
$$T=\langle A,R,\mu,\lambda,\tau,\omega\rangle $$

| Dimension | When it is required | Role | Typical options | Canonical tradition |
| --------- | ------------------- | ---- | --------------- | ------------------- |
| **[Epistemic aim](epistemic-aim.md) $A$** | always: it selects the interrogative word of the question | What knowledge is the inquiry intended to produce? What cognitive achievement is sought? | description/representation, exploration, prediction, explanation, modal knowledge, knowledge of theories or models |  |
| **[Requested relation](requested-relation.md) $R$** | whenever the answer must relate an explanans to the explanandum | What kind of relation must the explanans bear to the explanandum to answer the question? | causal, mechanistic, constitutive, functional, statistical, nomological, mathematical | relevance / dependence relation [vanfraassen1980] |
| **[Modal strength](modal-strength.md) $\mu$** | always | How tightly must the answer bind the phenomenon? | actual, possible, necessary | _how-possibly_ vs _how-actually_ [verreaultjulien2019] |
| **[Admissible explanans](admissible-explanans.md) $\lambda$** | only to bound the explanans further, because proportionality with the phenomenon selects the level when $\lambda$ is left unset | Which kinds of variables may enter the explanans? | compositional level; substrate dependence | levels of mechanisms [craver2007]; universality [batterman2000] |
| **Required accuracy $\tau$** | always, and `not-applicable` when the answer is matched against no measurement | Which observables of the target must the answer reproduce, which of its structures must correspond, and to what accuracy? | qualitative agreement; order of magnitude; a stated numeric bound; structural correspondence only. Within a tolerance, `answer` names the candidate's value and `target` the observable that it reproduces. Each output and each structure carries a justification stating why the question demands that particular correspondence. | fidelity criteria [weisberg2013]; adequacy for purpose [parker2020] |
| **Proof obligations $\omega$** | when the answer must derive a statement rather than match a measurement | Which implication must the answer establish, and in which direction? | Per obligation: the antecedent and the consequent, each as expressions over the declared observables. A converse counts as a separate obligation. | explanation by mathematical proof [lange2016] |

> [!HINT] Practical use
> Once a candidate exists, it is checked against the required accuracy by the [fidelity test](satisfaction-conditions.md).

> [!NOTE]
> Each dimension is developed in its own note, linked from its row. The required accuracy and the proof obligations have no note yet, because each row holds its whole specification.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [batterman2000] ◐ [Batterman, "Multiple realizability and universality", *British Journal for the Philosophy of Science* 51(1), 2000](https://philpapers.org/rec/BATMRA)
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [lange2016] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2016](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", _Philosophy of Science_ 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [verreaultjulien2019] ◐ [Verreault-Julien, "How could models possibly provide how-possibly explanations?", _Studies in History and Philosophy of Science Part A_ 73, 2019](https://philpapers.org/rec/VERHCM)
- [weisberg2013] ◐ [Weisberg, _Simulation and Similarity_, OUP, 2013](https://academic.oup.com/book/3141/chapter/143989335)
