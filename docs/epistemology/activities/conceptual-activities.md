---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/activities/_index.md)"
aliases:
  - Conceptual activities
  - Definition and explication
  - Operationalization
  - Classification (activity)
  - Concept revision
---
# Conceptual activities

> [!QUESTION] Goal: which activities introduce, revise or operationalize a concept, and by which norm is each judged?

The activities of this family output a concept, a measurement procedure that applies a concept, or a classification. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `explicit-definition` | `concept` | `concept` | deductive | both |
| `explication` | `concept` | `concept` | non-inferential | discovery |
| `operationalization` | `concept` | `measurement-procedure` | non-inferential | both |
| `classification` | `concept`, `data` | `classification` | inductive | both |
| `concept-revision` | `concept`, `phenomenon` | `concept` | abductive | discovery |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `explicit-definition` | state necessary and sufficient conditions for a new term in terms already available | eliminability: the new term can be replaced by its definition in every formula; non-creativity: the definition yields no new theorem stated in the old terms [suppes1957] |
| `explication` | replace a concept of ordinary or prescientific use by a precise concept | the explicatum is similar to the explicandum, exact, fruitful and simple [carnap1950_logical] |
| `operationalization` | tie a concept to the operations that apply it, possibly under test conditions only | the procedure assigns values on a stated [scale](../definitions/quantities/scale-and-level.md) [bridgman1927] [carnap1936] [hempel1952] |
| `classification` | group systems or observations by shared attributes into classes, following the [method of classification](../../procedures/classification/_index.md) | the criterion of the partition is stated, and the projectibility of the classes is claimed or tested [goodman1955] [boyd1991] |
| `concept-revision` | restructure a concept that fails to cover a phenomenon, through models and analogies | the revised concept covers the anomalous phenomenon and keeps the prior successes of the concept [nersessian2008] [thagard1992] |

## Distinctions

- **Explicit definition and explication differ in their norm.** A definition must be eliminable, so it adds no content. An explication may depart from the explicandum, as long as the explicatum is similar enough to serve the same uses and is more fruitful [carnap1950_logical].
- **The strict and the partial form of operationalization fix a meaning to different extents.** The strict form identifies a concept with one set of operations, so two procedures define two concepts [bridgman1927]. The partial form fixes how the concept applies under test conditions only, and leaves its meaning open elsewhere [carnap1936].
- **Operationalization outputs a procedure, and measurement outputs data.** Operationalization is judged before any value is recorded, by the scale stated by its procedure. [Measurement](empirical-activities.md) executes that procedure on a target.

## Consequences for a record

- **A derived term of an answer is introduced by an explicit definition.** The [derived terms of a model](../answer/model-and-binding.md#^derived-terms) can be eliminated by substituting their definitions, so the norm of explicit definition applies to them.
- **An explanandum variable operationalizes a phenomenon.** The [specification of the phenomenon](../subject/phenomenon.md) restates a behavior through observables, each on a stated scale. A phenomenon first stated by a qualitative label may be operationalized later, when its manifestation gains features that parametrize it. For a phenomenon of category *capacity*, the operationalization is the [criterion of performance](../definitions/regularities/capacity-and-disposition.md) that tests the conditional of the capacity.
- **The reference class of a target records a classification.** The [specification of the target system](../subject/target-system.md) states the class of admissible systems, and records whether its projectibility is assumed, tested or not claimed.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [boyd1991] ◐ [Boyd, "Realism, anti-foundationalism and the enthusiasm for natural kinds", *Philosophical Studies* 61(1–2), 127–148, 1991](https://doi.org/10.1007/BF00385837); defends homeostatic property cluster kinds, introduced in earlier papers of the author
- [bridgman1927] ◐ [Bridgman, *The Logic of Modern Physics*, Macmillan, 1927](https://www.gutenberg.org/ebooks/70620)
- [carnap1936] ◐ [Carnap, "Testability and meaning", *Philosophy of Science* 3(4), 419–471, 1936](https://doi.org/10.1086/286432), continued in [*Philosophy of Science* 4(1), 1–40, 1937](https://doi.org/10.1086/286443)
- [carnap1950_logical] ◐ [Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950](https://archive.org/details/logicalfoundatio00carn_0); ch. I, §3, "Requirements for an Explicatum"
- [goodman1955] ◐ [Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955](https://plato.stanford.edu/entries/goodman/)
- [hempel1952] ◐ [Hempel, *Fundamentals of Concept Formation in Empirical Science*, International Encyclopedia of Unified Science II.7, University of Chicago Press, 1952](https://openlibrary.org/works/OL85621W)
- [nersessian2008] ◐ [Nersessian, *Creating Scientific Concepts*, MIT Press, 2008](https://philpapers.org/rec/NERCSC)
- [suppes1957] ◐ [Suppes, *Introduction to Logic*, Van Nostrand, 1957](https://archive.org/details/introductiontolo0000supp); ch. 8, "Theory of Definition"; the criteria of eliminability and non-creativity are named from the general literature on definition, not confirmed at the page
- [thagard1992] ◐ [Thagard, *Conceptual Revolutions*, Princeton University Press, 1992](https://wellcomecollection.org/works/cja3cv87)
