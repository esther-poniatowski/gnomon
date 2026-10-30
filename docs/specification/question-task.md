---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Epistemic task of a question
---
# Epistemic task of a question

> [!QUESTION] Goal: what does a researcher write in each field of the `task` block of a question, and when is each field required?

The dimensions that these fields fix, and the grounds of each dimension, are stated in the theory of the [epistemic task](../epistemology/epistemic-task/epistemic-task.md).

| Dimension | When it is required | Role | Typical options | Canonical tradition |
| --------- | ------------------- | ---- | --------------- | ------------------- |
| **[Epistemic aim](../epistemology/epistemic-task/epistemic-aim.md) $A$** | always: it selects the interrogative word of the question | What knowledge is the inquiry intended to produce? What cognitive achievement is sought? | description/representation, exploration, prediction, explanation, modal knowledge, knowledge of theories or models |  |
| **[Requested relation](../epistemology/epistemic-task/requested-relation.md) $R$** | whenever the answer must relate an explanans to the explanandum | What kind of relation must the explanans bear to the explanandum to answer the question? | causal, mechanistic, constitutive, functional, statistical, nomological, mathematical | relevance / dependence relation [vanfraassen1980] |
| **Function sense** | when the requested relation is functional | Which sense of function must the answer establish? | causal role (the contribution of a part to a capacity of the system); etiological (the effects for which the part was selected) | [senses of function](../epistemology/epistemic-task/requested-relation.md#^function-sense) |
| **[Modal strength](../epistemology/epistemic-task/modal-strength.md) $\mu$** | always | How tightly must the answer bind the phenomenon? | actual, possible, necessary | _how-possibly_ vs _how-actually_ [verreaultjulien2019] |
| **[Admissible explanans](../epistemology/epistemic-task/admissible-explanans.md) $\lambda$** | only to bound the explanans further, because proportionality with the phenomenon selects the level when $\lambda$ is left unset | Which kinds of variables may enter the explanans? | compositional level; substrate dependence | levels of mechanisms [craver2007]; universality [batterman2000] |
| **Required accuracy $\tau$** | always, and `not-applicable` when the answer is matched against no measurement | Which observables of the target must the answer reproduce, which of its structures must correspond, and to what accuracy? | qualitative agreement; order of magnitude; a stated numeric bound; structural correspondence only. Within a tolerance, `answer` names the candidate's value and `target` the observable that it reproduces. Each output and each structure carries a justification stating why the question demands that particular correspondence. | fidelity criteria [weisberg2013]; adequacy for purpose [parker2020] |
| **Proof obligations $\omega$** | when the answer must derive a statement rather than match a measurement | Which implication must the answer establish, and in which direction? | Per obligation: the antecedent and the consequent, each as expressions over the declared observables. A converse counts as a separate obligation. | explanation by mathematical proof [lange2017] |

> [!HINT] Practical use
> Once a candidate exists, it is checked against the required accuracy by the [fidelity test](../epistemology/answer/satisfaction-conditions.md).

> [!NOTE]
> Each dimension is developed in its own note, linked from its row. The required accuracy and the proof obligations have no note yet, because each row holds its whole specification.

## Specifications each aim requires

Because an aim fixes the product that an answer must deliver, the aim also determines the specifications that the inquiry cannot leave empty. Each aim adds specifications to those every inquiry fixes. Under some aims, the inquiry itself produces some general specifications: an aim that produces a phenomenon cannot require the question to state it in advance. Therefore, the third column lists the specifications that a note marks as required in general but that the inquiry itself produces. On those paths alone, an empty field is admitted. A dash marks an aim that neither adds nor produces a specification. Each dash is attested by a filled inquiry that pursues the aim and fixes nothing beyond the general requirements. Each entry names a field path. Each row documents the entry for one aim in the registry of [required fields](../../src/gnomon/data/requirements.yml), the authoritative source of the table. ^required-by-aim

| Aim | Additionally required | Produced by the inquiry, although required in general |
| --- | --- | --- |
| `description` | — | — |
| `exploration` | `phenomenon.detection_criterion` | `phenomenon.statement`, `phenomenon.category`, `phenomenon.occurrence`, `phenomenon.evidential_status` |
| `prediction` | `phenomenon.manifestations`, `question.task.required_accuracy.outputs_to_match` | — |
| `explanation` | `question.subject.contrast.foil_set`, `question.task.requested_relation` | — |
| `modal-knowledge` | `question.task.modal_strength`, `question.task.proof_obligations` | — |
| `model-knowledge` | — | — |

- **An exploratory inquiry fixes no phenomenon in advance, so it must fix the criterion that would establish one.** The exploratory inquiry produces the statement, the category, the occurrence class and the evidential status, although every other aim fixes these four specifications. In their place, the detection criterion states the test that a candidate pattern must pass. Exploration illustrates a general division: a general requirement lists the fields of a complete record, and an aim marks the fields that the inquiry itself fills.

- **Only prediction compares an output against a measurement in every inquiry**, so the field `outputs_to_match` is required for this aim alone. An aim that seeks a proof, by contrast, requires no output to match, so an absent accuracy is *correct* for that aim.

## Admissible explanans

Two independent axes supply the options for the level $\lambda$. In addition, a justification records why the answer is bound to the options chosen: ^level-axes

| Specification | When it is required | Varied feature | Options | Examples | Source |
| ------------- | ------------------- | -------------- | ------- | -------- | ------ |
| Compositional level | when the question restricts the parts whose activities may explain the phenomenon | the constituent kinds or index sets whose parts may enter the explanans | the [constituents of the target system](../epistemology/subject/target-system.md) · their sub-parts · aggregates of them | channel · neuron · circuit · population | [craver2007] |
| Substrate dependence | when the question binds the answer to one realization of the system, or explicitly declines to do so | whether the explanans variables are specific to one realization of the system | substrate-specific (variables of the particular parts) · substrate-independent (variables shared by every realization: functional roles, universality classes) · mapping (how substrate-specific variables realize substrate-independent ones) | membrane potentials of identified neurons (specific) · an error signal on any carrier, or the universality class of a phase transition (independent) · how a circuit implements context-dependent gating (mapping) | [batterman2000]; [marr1982]; [bechtel2015] |
| Justification | whenever an axis is stated | why the research program binds the answer to these variables, and which content is lost when the explanans uses other variables | one clause that carries no commitment already held by the axes | "the forecast names when each subsystem transitions, so the explanans must resolve each of them individually" | — |

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [batterman2000] ◐ [Batterman, "Multiple realizability and universality", *British Journal for the Philosophy of Science* 51(1), 2000](https://philpapers.org/rec/BATMRA)
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [lange2017] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2017](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [marr1982] ○ Marr, *Vision*, Freeman, 1982
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", _Philosophy of Science_ 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [verreaultjulien2019] ◐ [Verreault-Julien, "How could models possibly provide how-possibly explanations?", _Studies in History and Philosophy of Science Part A_ 73, 2019](https://philpapers.org/rec/VERHCM)
- [weisberg2013] ◐ [Weisberg, _Simulation and Similarity_, OUP, 2013](https://academic.oup.com/book/3141/chapter/143989335)
