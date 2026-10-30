---
tags:
  - method
  - wip
index: "[Epistemic activities](docs/epistemology/activities/_index.md)"
aliases:
  - Ampliative inference
  - Abduction
  - Induction
  - Causal inference
---
# Ampliative inference

> [!QUESTION] Goal: which inferences reach a hypothesis beyond their premises, and by which norm is each judged?

The activities of this family output a [hypothesis](../definitions/representations/claim-and-hypothesis.md): a claim whose content exceeds that of the premises, held for testing. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `abduction` | `phenomenon` | `hypothesis` | abductive | discovery |
| `induction` | `data` | `hypothesis` | inductive | discovery |
| `analogical-inference` | `model` (source), `phenomenon` | `hypothesis` | analogical | discovery |
| `causal-inference` | `data`, `model` | `hypothesis` | inductive | both |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `abduction` | propose a hypothesis on the schema: "The surprising fact, C, is observed. But if A were true, C would be a matter of course. Hence, there is reason to suspect that A is true." | the hypothesis is worth pursuing: it deserves testing, and its truth is not claimed [peirce1934] |
| `induction` | extend a regularity from observed instances to unobserved instances, possibly guided by heuristics that search the space of candidate laws | the predicates of the generalization are projectible [goodman1955] [langley1987] |
| `analogical-inference` | carry a property of a source model over to the target along a mapping | the similarities are relevant to the transferred property, and the known differences are not [bartha2010] |
| `causal-inference` | infer a causal structure or the size of an effect from data and causal assumptions | the effect is identifiable: the stated assumptions and the data determine the target quantity uniquely [pearl2009] [spirtes2000] |

On the account of its originator, abduction is the only logical operation that introduces a new idea [peirce1934].

## Distinctions

- **Abduction outputs a candidate, and inference to the best explanation outputs a verdict.** Abduction generates a hypothesis and licenses its pursuit. [Inference to the best explanation](evaluation.md) selects among rival hypotheses and licenses acceptance, so it belongs to evaluation.
- **Induction and causal inference differ in their assumptions.** Induction extends a regularity. Causal inference also requires assumptions about the causal structure, such as the assumption that no hidden common cause exists. Only under these assumptions does a causal conclusion follow from correlations [pearl2009] [spirtes2000].

## Consequences for a record

- **A hypothesis enters the records as a candidate answer.** The [answer form](../answer/answer-form.md) holds a candidate with the attitude `hypothesized` before any test. The [conditions of satisfaction](../answer/satisfaction-conditions.md) state the tests required to accept it.
- **Causal inference must state its assumptions as part of the answer.** The identifiability of a causal effect depends on assumptions untested by the data, so these assumptions belong to the answer, beside its idealizations.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [bartha2010] ◐ [Bartha, *By Parallel Reasoning: The Construction and Evaluation of Analogical Arguments*, Oxford University Press, 2010](https://doi.org/10.1093/acprof:oso/9780195325539.001.0001)
- [goodman1955] ◐ [Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955](https://plato.stanford.edu/entries/goodman/)
- [langley1987] ◐ [Langley, Simon, Bradshaw & Zytkow, *Scientific Discovery: Computational Explorations of the Creative Processes*, MIT Press, 1987](https://www.cambridge.org/core/journals/philosophy-of-science/article/pat-langley-herbert-a-simon-gary-l-bradshaw-and-jan-m-zytkow-scientific-discovery-computational-explorations-of-the-creative-process-cambridge-mass-the-mit-press-1987-357-pp-995-paper/F388006F966310BCB42A23318458F553); checked through a published review
- [pearl2009] ◐ [Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009](https://doi.org/10.1017/CBO9780511803161)
- [peirce1934] ◐ [Peirce, *Collected Papers of Charles Sanders Peirce*, vol. 5, *Pragmatism and Pragmaticism*, Hartshorne & Weiss (eds.), Harvard University Press, 1934](https://plato.stanford.edu/entries/abduction/peirce.html); CP 5.189 for the schema, punctuation as in the SEP supplement; CP 5.171 or 5.172 for the claim on new ideas, the paragraph number differing between secondary sources
- [spirtes2000] ◐ [Spirtes, Glymour & Scheines, *Causation, Prediction, and Search*, 2nd ed., MIT Press, 2000](https://doi.org/10.7551/mitpress/1754.001.0001)
