---
tags:
  - definition
  - wip
index: "[Epistemic activities](docs/epistemology/definitions/activities/_index.md)"
aliases:
  - Model analysis
  - Derivational activities
  - Simulation
  - Robustness analysis
  - Prediction (activity)
---
# Model analysis

> [!QUESTION] Goal: which activities draw consequences from a model, and by which norm is each judged?

The activities of this family output a **consequence**: a statement true of a model. A consequence may be false of the target. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `derivation` | `model \| background-model` | `consequence` | deductive | justification |
| `simulation` | `model`, `design` | `consequence` | deductive | justification |
| `robustness-analysis` | `model` (family) | `consequence` | deductive | justification |
| `thought-experiment` | `model` | `consequence` | deductive | discovery |
| `prediction` | `model`, `target-specification` | `consequence` | deductive | justification |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `derivation` | deduce a statement from the laws and assumptions of a model, or from the admitted background laws | each deductive step is valid |
| `simulation` | compute the trajectories of the model numerically, under the conditions fixed by the design | verification holds: the code solves the equations of the model [winsberg2010] |
| `robustness-analysis` | derive one result from several models that share a core and differ in their auxiliary assumptions | the result holds across models whose auxiliary assumptions are independent [levins1966] [weisberg2006] |
| `thought-experiment` | reason about an imagined scenario that is not carried out | the conclusion follows by an argument from the premises of the scenario [norton1996] |
| `prediction` | derive the values assigned by the model to observables under the conditions of a target | the values are derived from the model under the stated conditions of the target |

## Distinctions

- **Verification belongs to simulation, and validation to evaluation.** Verification compares two [levels of a computation](../change/computation.md), the algorithm of the code and the function fixed by the model, without reference to the target. Therefore, verification stays within this family. [Validation](evaluation.md) asks whether the model is adequate to its target for a purpose.
- **The norm of a thought experiment is contested.** On the argument view adopted here, a thought experiment can be reconstructed as an argument from the premises of its scenario [norton1996]. On a rival account, some scenarios give access to a law without such an argument [brown1991].
- **Prediction as an activity differs from prediction as an aim.** The activity derives expected values from a model. The activity serves inquiries of every aim, for instance to test an explanation. The [aim of prediction](../../epistemic-aim.md) makes a warranted expectation the product required of the whole inquiry.
- **Every output of this family holds of the model only.** A consequence becomes a claim about the target only through a [theoretical hypothesis](../representations/claim-and-hypothesis.md) that links model and target.

## Consequences for a record

- **Derivation discharges the proof obligations of a question.** The proof obligations $\omega$ of the [epistemic task](../../epistemic-task.md) state the implications to be derived by an answer.
- **Robustness analysis runs the robustness test of satisfaction.** The robustness test of the [conditions of satisfaction](../../satisfaction-conditions.md) checks whether a conclusion survives the idealizations of the answer.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [brown1991] ◐ [Brown, *The Laboratory of the Mind: Thought Experiments in the Natural Sciences*, Routledge, 1991](https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/james-robert-brown-the-laboratory-of-the-mind-thought-experiments-in-the-natural-sciences-new-york-routledge-1991-xi-175-pp-4995-cloth/0A84321B5BCDAE346E84A3B9B27B57D6); checked through a published review
- [levins1966] ◐ [Levins, "The strategy of model building in population biology", *American Scientist* 54(4), 421–431, 1966](https://www.zoology.ubc.ca/let/pdfs/Levins1966.pdf); robust theorems, p. 423
- [norton1996] ◐ [Norton, "Are thought experiments just what you thought?", *Canadian Journal of Philosophy* 26(3), 333–366, 1996](https://doi.org/10.1080/00455091.1996.10717457)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006](https://doi.org/10.1086/518628)
- [winsberg2010] ◐ [Winsberg, *Science in the Age of Computer Simulation*, University of Chicago Press, 2010](https://doi.org/10.7208/9780226902050)
