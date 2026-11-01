---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/processes/activities/_index.md)"
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
| `testing` | `target-claim` (hypothesized), `consequence`, `data` | `verdict` | error-statistical | justification |
| `confirmation` | `target-claim` (hypothesized), `data` | `credence` | inductive | justification |
| `validation` | `model`, `binding`, `question` | `verdict` | non-inferential | justification |
| `model-selection` | `model` (several), `data` | `ranking` | inductive | justification |
| `inference-to-the-best-explanation` | `target-claim` (several, hypothesized), `data` | `verdict` | abductive | justification |
| `critique` | `target-claim \| model` (hypothesized) | `verdict` | non-inferential | justification |
| `admissibility-check` | `target-claim \| model` (hypothesized), `question` | `verdict` | non-inferential | justification |

## Norms

| Activity | Operation | The norm passes when |
| --- | --- | --- |
| `testing` | compare with data a consequence derived from the hypothesis and its auxiliary assumptions | the test is severe: it would probably have detected an error, had the hypothesis been false [mayo1996] [mayo2018] |
| `confirmation` | update the credence in a hypothesis on the evidence | the posterior credence follows from the prior credence by conditionalization on the evidence: the new credence in the hypothesis equals the old credence in it given the evidence [howson2006] |
| `validation` | judge whether a model is adequate for the purpose stated by the question | the model is adequate for that purpose [parker2020] |
| `model-selection` | rank models by their expected accuracy in predicting new data | the ranking follows predictive accuracy, penalized for complexity [forster1994] |
| `inference-to-the-best-explanation` | select the hypothesis that would, if true, best explain the data | the best of the rival explanations is also good enough, so that it is not merely the best of a bad lot [harman1965] [lipton2004] |
| `critique` | expose a hypothesis or a model to criticism from other perspectives | each objection is named with its ground [longino1990] |
| `admissibility-check` | apply the admissibility tests of the [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md) to a candidate, mostly before any evidence is weighed | each admissibility test is applied to the declared specifications, with its evidence |

A test never bears on a hypothesis alone: the prediction follows from the hypothesis together with auxiliary assumptions. Consequently, a failed prediction refutes the conjunction without locating the error, a difficulty known as the Duhem–Quine problem [duhem1906] [quine1951].

## Distinctions

- **Admissibility and testing differ in their norm.** An admissibility check asks whether a candidate is an answer of the kind that the question requests: it checks the candidate against the specification of the question, mostly before any evidence. Testing asks whether a hypothesis is true of its target, under a severe test. The first check is meant to precede the second, since an answer that is not admissible cannot satisfy the question, whatever its warrant.
- **Testing and validation differ in their object.** Testing asks whether a hypothesis is true of its target. Validation asks whether a model is adequate for a purpose, and a model known to be false can be adequate [parker2020].
- **Testing and confirmation differ in their output.** Testing returns a verdict. Confirmation returns a degree of credence. Evidence changes that degree whenever its probability differs under the hypothesis and under its negation [howson2006].
- **Testing and confirmation serve two norms of evidence.** Testing outputs the verdict of a test, and confirmation outputs a credence. The norms of evidence that govern the verdicts and the credence of an assessment, and the relation between them, are stated with the [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md#^credence). Acceptance into the accepted knowledge stays an [act of the researcher](../../objects/status/statuses-and-acceptance.md#^acceptance-act), informed by both outputs.
- **The mode of testing is error-statistical.** Testing derives a prediction from the hypothesis and its auxiliary assumptions, and that derivation is deductive. The verdict is then reached from the agreement or the disagreement of the prediction with the data, judged by severity, which is an error-statistical criterion, not a deductive one [mayo1996]. The verdict rests on that criterion, so the mode `error-statistical` names the inference of testing.
- **Testing and inference to the best explanation both return a verdict, under different norms.** Testing judges one hypothesis by the severity of the test. Inference to the best explanation compares rival hypotheses by how well each would explain the data, if true [lipton2004].
- **The norm of critique checks the trace of a social process.** Criticism is transformative only when the community meets social conditions, such as public venues, shared standards and a tempered equality of intellectual authority [longino1990]. A record can hold only the trace of that process: each objection with its ground.

## Relations to the method

- **The conditions of satisfaction fix the evaluation before it runs.** The [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md) state the tests that decide whether a candidate succeeds. The required accuracy of the [epistemic task](../../objects/task/epistemic-task.md) states the purpose to be served by a validated model.
- **Model selection uses the virtues of the method.** The [epistemic and pragmatic virtues](../../objects/task/epistemic-pragmatic-virtues.md) state the qualities used to compare admissible answers. Penalized accuracy is one instance of these qualities.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [duhem1906] ◐ Duhem, *La théorie physique : son objet et sa structure*, Chevalier et Rivière, 1906; 2nd ed., Marcel Rivière, 1914, translated as *The Aim and Structure of Physical Theory*, Princeton University Press, 1954; a hypothesis is tested only together with auxiliary hypotheses; p. 187 of the translation, checked through the [SEP entry on underdetermination](https://plato.stanford.edu/entries/scientific-underdetermination/)
- [forster1994] ◐ [Forster & Sober, "How to tell when simpler, more unified, or less ad hoc theories will provide more accurate predictions", *British Journal for the Philosophy of Science* 45(1), 1–35, 1994](https://doi.org/10.1093/bjps/45.1.1)
- [harman1965] ◐ [Harman, "The inference to the best explanation", *Philosophical Review* 74(1), 88–95, 1965](https://doi.org/10.2307/2183532)
- [howson2006] ◐ [Howson & Urbach, *Scientific Reasoning: The Bayesian Approach*, 3rd ed., Open Court, 2006](https://researchonline.lse.ac.uk/id/eprint/12474/); conditionalization checked through the publisher record; the change of credence whenever the likelihoods differ follows from Bayes' rule and was not located in the book
- [lipton2004] ◐ [Lipton, *Inference to the Best Explanation*, 2nd ed., Routledge, 2004](https://doi.org/10.4324/9780203470855); "loveliness is a guide to likeliness", p. 61; the requirement that the best explanation be good enough, in reply to the objection of the bad lot, checked through secondary sources, page not confirmed
- [longino1990] ◐ [Longino, *Science as Social Knowledge: Values and Objectivity in Scientific Inquiry*, Princeton University Press, 1990](https://search.worldcat.org/oclc/19811327); ch. 4, conditions of transformative criticism; from standard knowledge, not checked at the page
- [mayo1996] ◐ [Mayo, *Error and the Growth of Experimental Knowledge*, University of Chicago Press, 1996](https://www.press.uchicago.edu/ucp/books/book/chicago/E/bo3637756.html)
- [mayo2018] ◐ [Mayo, *Statistical Inference as Severe Testing: How to Get beyond the Statistics Wars*, Cambridge University Press, 2018](https://doi.org/10.1017/9781107286184)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [quine1951] ◐ [Quine, "Two dogmas of empiricism", *Philosophical Review* 60(1), 20–43, 1951](https://doi.org/10.2307/2181906); statements face the tribunal of experience as a body, not one by one
