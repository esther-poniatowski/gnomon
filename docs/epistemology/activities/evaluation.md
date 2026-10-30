---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/activities/_index.md)"
aliases:
  - Evaluative activities
  - Testing and confirmation
  - Model validation
  - Model selection
  - Inference to the best explanation
  - Critique (activity)
---
# Evaluation

> [!QUESTION] Goal: which activities judge, weigh or rank candidate hypotheses and models, and by which norm is each judged?

The activities of this family output a **verdict**, a **credence** or a **ranking** about a hypothesis or a model. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `testing` | `hypothesis`, `consequence`, `data` | `verdict` | deductive | justification |
| `confirmation` | `hypothesis`, `data` | `credence` | inductive | justification |
| `validation` | `model`, `binding`, `question` | `verdict` | non-inferential | justification |
| `model-selection` | `model` (several), `data` | `ranking` | inductive | justification |
| `inference-to-the-best-explanation` | `hypothesis` (several), `data` | `verdict` | abductive | justification |
| `critique` | `hypothesis \| model` | `verdict` | non-inferential | justification |
| `admissibility-check` | `hypothesis \| model`, `question` | `verdict` | non-inferential | justification |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `testing` | compare with data a consequence derived from the hypothesis and its auxiliary assumptions | the test is severe: it would probably have detected an error, had the hypothesis been false [mayo1996] [mayo2018] |
| `confirmation` | update the credence in a hypothesis on the evidence | the posterior credence follows from the prior credence by conditionalization on the evidence [howson2006] |
| `validation` | judge whether a model is adequate for the purpose stated by the question | the model is adequate for that purpose [parker2020] |
| `model-selection` | rank models by their expected accuracy in predicting new data | the ranking follows predictive accuracy, penalized for complexity [forster1994] |
| `inference-to-the-best-explanation` | accept the hypothesis that would, if true, best explain the data | the best of the rival explanations is also good enough, so that it is not merely the best of a bad lot [harman1965] [lipton2004] |
| `critique` | expose a hypothesis or a model to criticism from other perspectives | each objection is named with its ground [longino1990] |
| `admissibility-check` | apply the admissibility tests of the [conditions of satisfaction](../answer/satisfaction-conditions.md) to a candidate, mostly before any evidence is weighed | each admissibility test is applied to the declared specifications, with its evidence |

A test never bears on a hypothesis alone: the prediction follows from the hypothesis together with auxiliary assumptions. Consequently, a failed prediction refutes the conjunction without locating the error, a difficulty known as the Duhem–Quine problem.

## Distinctions

- **Admissibility and testing differ in their norm.** An admissibility check asks whether a candidate is an answer of the kind that the question requests, by its form and its declarations. Testing asks whether a hypothesis is true of its target, under a severe test. The first check is meant to precede the second, since an answer that is not admissible cannot satisfy the question, whatever its warrant.
- **Testing and validation differ in their object.** Testing asks whether a hypothesis is true of its target. Validation asks whether a model is adequate for a purpose, and a model known to be false can be adequate [parker2020].
- **Testing and confirmation differ in their output.** Testing returns a verdict. Confirmation returns a degree of credence. Evidence changes that degree whenever its probability differs under the hypothesis and under its negation [howson2006].
- **Testing and inference to the best explanation both return a verdict, under different norms.** Testing judges one hypothesis by the severity of the test. Inference to the best explanation compares rival hypotheses by how well each would explain the data, if true [lipton2004].
- **The norm of critique checks the trace of a social process.** Criticism is transformative only when the community meets social conditions, such as public venues, shared standards and a tempered equality of intellectual authority [longino1990]. A record can hold only the trace of that process: each objection with its ground.

## Consequences for a record

- **The conditions of satisfaction fix the evaluation before it runs.** The [conditions of satisfaction](../answer/satisfaction-conditions.md) state the tests that decide whether a candidate succeeds. The required accuracy of the [epistemic task](../epistemic-task/epistemic-task.md) states the purpose to be served by a validated model.
- **Model selection uses the virtues of the method.** The [epistemic and pragmatic virtues](../epistemic-task/epistemic-pragmatic-virtues.md) state the qualities used to compare admissible answers. Penalized accuracy is one instance of these qualities.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [forster1994] ◐ [Forster & Sober, "How to tell when simpler, more unified, or less ad hoc theories will provide more accurate predictions", *British Journal for the Philosophy of Science* 45(1), 1–35, 1994](https://doi.org/10.1093/bjps/45.1.1)
- [harman1965] ◐ [Harman, "The inference to the best explanation", *Philosophical Review* 74(1), 88–95, 1965](https://doi.org/10.2307/2183532)
- [howson2006] ◐ [Howson & Urbach, *Scientific Reasoning: The Bayesian Approach*, 3rd ed., Open Court, 2006](https://eprints.lse.ac.uk/12474)
- [lipton2004] ◐ [Lipton, *Inference to the Best Explanation*, 2nd ed., Routledge, 2004](https://www.routledge.com/Inference-to-the-Best-Explanation/Lipton/p/book/9780415242028); "loveliness is a guide to likeliness", p. 61; the requirement that the best explanation be good enough, in reply to the objection of the bad lot, checked through secondary sources, page not confirmed
- [longino1990] ◐ [Longino, *Science as Social Knowledge: Values and Objectivity in Scientific Inquiry*, Princeton University Press, 1990](https://search.worldcat.org/oclc/19811327); ch. 4, conditions of transformative criticism; from standard knowledge, not checked at the page
- [mayo1996] ◐ [Mayo, *Error and the Growth of Experimental Knowledge*, University of Chicago Press, 1996](https://www.press.uchicago.edu/ucp/books/book/chicago/E/bo3637756.html)
- [mayo2018] ◐ [Mayo, *Statistical Inference as Severe Testing: How to Get beyond the Statistics Wars*, Cambridge University Press, 2018](https://doi.org/10.1017/9781107286184)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
