---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/activities/_index.md)"
aliases:
  - Model-building activities
  - Delimitation of a target system
  - Background appraisal
  - Transfer of laws
  - De-idealization
  - Decomposition and localization
  - Formalization
  - Fitting
---
# Model-building

> [!QUESTION] Goal: which activities specify a target, admit its background laws and construct a model of it, and by which norm is each judged?

The activities of this family output a target specification, a background model or a [model](../definitions/representations/model.md). Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `delimitation` | `question`, `identified-subject` | `target-specification` | non-inferential | discovery |
| `background-appraisal` | `source` | `background-model` | inductive | justification |
| `transfer` | `background-model` (other class), `target-specification` | `background-model` | analogical | justification |
| `abstraction` | `model` | `model` | non-inferential | discovery |
| `idealization` | `model` | `model` | non-inferential | discovery |
| `de-idealization` | `model` | `model` | deductive | justification |
| `decomposition-localization` | `phenomenon`, `target-specification` | `model` | abductive | discovery |
| `model-analogy` | `model` (source) | `model` | analogical | discovery |
| `formalization` | `model` | `model` | non-inferential | both |
| `fitting` | `model`, `data` | `model` | inductive | justification |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `delimitation` | declare the [constituents, environment and structure](../definitions/systems/system-constituent-environment.md) of the system that a question concerns | every declared constituent and every shared variable occurs in at least one admissible answer type of the question, a member of the answer set over its typed slots [hamblin1958] |
| `background-appraisal` | admit laws about the target from sources | each admitted law carries a warrant, an origin and a range |
| `transfer` | carry laws established for another class of systems over to the target | structural similarity licenses the extrapolation: the mechanism that supports each law in the source class operates in the target, undisrupted at the stages where the two classes may differ [steel2008] |
| `abstraction` | omit factors of the target from the model | the omitted factors are named, and no claim of the answer bears on them [jones2005] [cartwright1989] |
| `idealization` | introduce a deliberate distortion into the model | the motive is stated, and the condition of its kind holds: a Galilean idealization can be removed; a minimalist idealization omits only factors that make no difference to the phenomenon [mcmullin1985] [weisberg2007] |
| `de-idealization` | remove an idealization from the model, or correct for it | a correction to the idealized result is known, so the idealization is `controlled`, and each conclusion is shown to be stable under that correction or is corrected [mcmullin1985] [knuuttila2019] |
| `decomposition-localization` | divide the behavior of the target into activities, and assign each activity to a part | each component of the model maps onto a constituent of the target or onto a declared admissible part, as the [explanatory mapping](../definitions/regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test) requires [bechtel1993] [craver2006] |
| `model-analogy` | carry the structure of a source model over to the domain of the target | the mapping preserves the relations relevant to the phenomenon, and no known difference defeats the transfer [hesse1966] [bartha2010] |
| `formalization` | state each term and relation of a verbal model as a quantity, a set or an equation | every symbol resolves to a declaration, under the [expression language](../../specification/expressions.md) |
| `fitting` | estimate the parameters of a model from data | the estimator and the uncertainty of each estimate are stated, and each fitted parameter carries the warrant `fitted` [kennedy2001] |

## Distinctions

- **The norm of delimitation ranges over answer types.** Candidate answers are produced after delimitation, so a norm stated over them cannot be checked when the target is specified. The answer types of a question exist as soon as its slots are typed.
- **Background appraisal and transfer share their output and differ in their norm.** Appraisal admits laws established for the class of the target, each with its warrant. Transfer admits laws established for another class, and its norm requires evidence that the supporting mechanism is shared [steel2008].
- **Abstraction and idealization differ by the truth of their products.** The [truth test](../definitions/representations/idealization-and-abstraction.md#^truth-test) decides between them.
- **De-idealization outputs a model, so it belongs to this family.** A revision changes the attitude toward existing records, whereas de-idealization builds a new model. Removing an idealization often reformulates the model, instead of simply reversing the earlier distortion [knuuttila2019].
- **Decomposition and localization build a model, and explanation judges it.** Decomposition outputs a model, and its norm checks that each component corresponds to a part of the target. The norm of [explanation](explanation-and-integration.md) judges whether that model explains the phenomenon.
- **Decomposition of a system differs from decomposition of a question.** Decomposition and localization divide a behavior among the parts of a system [bechtel1993]. The decomposition of a question in [problem-posing](problem-posing.md) divides a question into subquestions, under the norm of erotetic implication.
- **Analogy as model-building differs from analogical inference.** Model-building by analogy produces a candidate model. [Analogical inference](ampliative-inference.md) concludes that the target has a property, so its output is a hypothesis, judged by the relevance of the similarities.

## Relations to the method

- **Decomposition relates each component to the target.** A component of a [mechanistic model](../definitions/regularities/mechanism-and-mechanistic-model.md) is either defined by a map from the declared constituents of the target, as the [perspective of a model](../answer/model-and-binding.md#^perspective) requires, or kept as a unit of the model alone, related to the target only through a [pair of type `component`](../answer/model-and-binding.md#^component-pairs) of a binding.

The fields filled by delimitation, by background appraisal and transfer, and by abstraction and idealization are documented in the [target-system record](../../specification/target-system.md), in the [background record](../../specification/background.md), in the [model record](../../specification/model.md) and in the [answer record](../../specification/answer.md).

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [bartha2010] ◐ [Bartha, *By Parallel Reasoning: The Construction and Evaluation of Analogical Arguments*, Oxford University Press, 2010](https://doi.org/10.1093/acprof:oso/9780195325539.001.0001)
- [bechtel1993] ◐ [Bechtel & Richardson, *Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research*, Princeton University Press, 1993](https://philpapers.org/rec/BECDC); reissued MIT Press, 2010
- [cartwright1989] ◐ [Cartwright, *Nature's Capacities and Their Measurement*, Clarendon Press, 1989](https://doi.org/10.1093/0198235070.001.0001)
- [craver2006] ◐ [Craver, "When mechanistic models explain", *Synthese* 153(3), 355–376, 2006](https://doi.org/10.1007/s11229-006-9097-x); checked through the abstract
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://philpapers.org/rec/HAMQ); the possible answers form an exhaustive set of mutually exclusive possibilities, checked through secondary summaries
- [hesse1966] ◐ [Hesse, *Models and Analogies in Science*, University of Notre Dame Press, 1966](https://philpapers.org/rec/REMAA); revised edition of the Sheed and Ward edition, London, 1963
- [jones2005] ◐ [Jones, "Idealization and abstraction: a framework", in Jones & Cartwright (eds.), *Idealization XII: Correcting the Model. Idealization and Abstraction in the Sciences*, Poznań Studies in the Philosophy of the Sciences and the Humanities 86, Rodopi, 173–217, 2005](https://philportal.de/records/kug/EBP9789401202732)
- [kennedy2001] ◐ [Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society, Series B* 63(3), 425–464, 2001](https://doi.org/10.1111/1467-9868.00294); calibration fits the parameters of a model to observed data, and carries the uncertainty of the fitted parameters into predictions; checked through the abstract
- [knuuttila2019] ◐ [Knuuttila & Morgan, "Deidealization: no easy reversals", *Philosophy of Science* 86(4), 641–661, 2019](https://doi.org/10.1086/704975); checked through the abstract
- [mcmullin1985] ◐ [McMullin, "Galilean idealization", *Studies in History and Philosophy of Science* 16(3), 247–273, 1985](https://doi.org/10.1016/0039-3681(85)90003-2)
- [steel2008] ◐ [Steel, *Across the Boundaries: Extrapolation in Biology and Social Science*, Oxford University Press, 2008](https://doi.org/10.1093/acprof:oso/9780195331448.001.0001); the publisher lists the print edition on 1 October 2007; extrapolation by comparative process tracing, checked through the publisher abstract and secondary summaries
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", *Journal of Philosophy* 104(12), 639–659, 2007](https://doi.org/10.5840/jphil20071041240)
