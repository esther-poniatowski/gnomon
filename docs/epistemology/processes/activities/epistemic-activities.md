---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/processes/activities/_index.md)"
aliases:
  - Epistemic activities
  - Taxonomy of epistemic activities
  - Activity record
  - Product types
  - Itinerary check
---
# Epistemic activities

> [!QUESTION] Goal: which operations of an inquiry count as epistemic, and how is each typed so that a research itinerary can be checked as a composition of typed steps?

Each **epistemic activity** of an inquiry is typed by its inputs, its output and its norm. These types serve one purpose: a research itinerary can be checked step by step.

> [!IMPORTANT] Notes and registries
> The taxonomy is a synthesis proposed by this method. Each family note cites the sources of its activities one by one. The notes are the source of the content: the [registry of activities](../../../../src/gnomon/data/registries/activities.yml) and the [registry of product types](../../../../src/gnomon/data/registries/product-types.yml) transcribe them. Therefore, a change must start in the notes.

## Criterion of an epistemic activity

An operation of an inquiry counts as epistemic when its output is an **epistemic object**: a representation whose content bears on the questions, the knowledge or the warrants of an inquiry. ^epistemic-criterion

The [product types](#^product-types) enumerate these objects, from the problem that opens an inquiry to the change of attitude that closes one of its cycles. The criterion tests only the output of an activity, not the record kinds available today. Therefore, when the output of an activity has no record kind yet, the activity is still epistemic, and its output type is marked as a gap.

Three borderline operations receive no activity type of their own:

- **Communication is excluded by the criterion.** A paper, a talk or a figure carries the content of existing epistemic objects into another medium. Therefore, the output of communication adds no content to the questions, the knowledge or the warrants of the inquiry.
- **Curation is a method of observation.** Curation assembles a dataset from existing recordings, so its output is data. Its success is judged as that of an [observation](empirical-activities.md): by the reliability of the procedures that produced the recordings.
- **Replication is part of the norm of phenomenon detection.** A replication repeats a procedure on an independent setup, so its output is data, a type already listed. The norm of [phenomenon detection](empirical-activities.md) requires such independent procedures.

## Signature of an activity type

An activity type is specified by its **signature**: ^activity-criterion

- the types of its **inputs**, drawn from the [product types](#^product-types);
- the type of its **output**, exactly one, drawn from the same list;
- the **operation** that turns the inputs into the output;
- the **norm**, a named test stating when the output is correct or adequate;
- the **mode** of inference performed by the operation;
- the **context** of the activity: discovery or justification.

Two activity types are distinct when they differ in their output type or in their norm. When two procedures share both, they are two methods for one activity type, such as two estimators implementing [fitting](model-building.md).

The family notes write the inputs of an activity in three forms:

- a type alone, such as `data`, takes one record of that type;
- a type followed by a qualifier, such as `model` (source) or `verdict` (several), states the role or the number of its records, and leaves the type unchanged;
- types joined by `|`, such as `hypothesis | model`, take one record of either type.

Three attributes take their values from closed lists: ^attribute-vocabularies

| Attribute | Values | Assigned to |
| --- | --- | --- |
| Verdict of the norm | `pass`, `fail`, `pending` | each step of an itinerary |
| Mode | `deductive`, `inductive`, `abductive`, `analogical`, `non-inferential` | each activity type |
| Context | `discovery`, `justification`, `both` | each activity type |

- **The norm is a named test.** The test of an activity takes the id `norm.<activity-id>`, such as `norm.fitting`. Each step of an itinerary records the verdict of that test: `pending` before the test runs, then `pass` or `fail`.
- **The mode `non-inferential` covers operations that draw no inference.** Observation and formalization are examples.
- **The context is assigned to each activity type.** A family does not fix it: model-building holds activities of discovery, such as idealization, and of justification, such as fitting. An activity of discovery outputs a candidate, and an activity of justification judges or warrants one [reichenbach1938]. The division is contested: the reasoning that generates hypotheses follows patterns that can be analyzed [hanson1958] [simon1973]. The value `both` marks an activity whose norm serves either context, such as classification.

## Choice of the taxonomy

Three candidate taxonomies were compared on one requirement: every activity of an inquiry must receive exactly one place.

| Candidate | Primary criterion | Coverage | Decision |
| --- | --- | --- | --- |
| By stage of inquiry | the position of the activity in a cycle of inquiry [dewey1938] | fails: stages recur, and concept formation and measurement belong to no single stage | rejected as primary; kept as the relation of iteration |
| By mode of inference | abduction, deduction and induction [peirce1934] | fails: the criterion covers inferential acts only, and leaves out non-inferential activities, such as measurement, intervention, explication and framework revision | rejected as primary; kept, extended by analogy, as the attribute *mode* |
| By signature | the [signature](#^activity-criterion), with families defined by output type | succeeds: every activity has exactly one output type, non-inferential activities included | chosen |

## Families

Each family groups the activities whose output types belong to one class of product types. Each product type is the output of one family only, so the output type of an activity fixes its family. Within one family, when two activities share an output type, they differ by their norm. ^families

| Family | Output types |
| --- | --- |
| [Problem-posing](problem-posing.md) | `problem`, `question-schema`, `identified-subject`, `question` |
| [Conceptual activities](conceptual-activities.md) | `concept`, `measurement-procedure`, `classification` |
| [Empirical activities](empirical-activities.md) | `design`, `data`, `phenomenon` |
| [Model-building](model-building.md) | `target-specification`, `background-model`, `model` |
| [Model analysis](model-analysis.md) | `consequence` |
| [Ampliative inference](ampliative-inference.md) | `hypothesis` |
| [Evaluation](evaluation.md) | `verdict`, `credence`, `ranking` |
| [Explanation and integration](explanation-and-integration.md) | `explanation`, `inter-theory-relation` |
| [Revision](revision.md) | `knowledge-state-change` |

The type `source` is the output of no activity, since a source enters an inquiry from outside it. Conversely, a type may be the input of no activity. Such a type is a final product of an inquiry (e.g. `classification`, `inter-theory-relation`).

The partition by output type has two consequences for borderline activities. First, when the output of an activity is a model, the activity belongs to model-building, regardless of its mode and its context. Second, revision outputs only changes of attitude or of status across existing records, so a new model is never the output of a revision.

## Product types

The product types form a closed list. Each type classifies the epistemic objects taken or produced by activities. Each type also maps onto the record kind of gnomon that holds its objects. When no record kind holds a type, the type is a gap marked `to-create`. In that case, the records must be extended to match the taxonomy. ^product-types

| Type | Epistemic object | Record | Status |
| --- | --- | --- | --- |
| `source` | a document, a dataset or a result external to the inquiry | external pointer, held by the `sources` of a problem and the `pointers` of an identification | exists |
| `problem` | a demand for a solution under constraints, defined in the note on the [epistemic problem](../../objects/problem/epistemic-problem.md) | `problem` | exists |
| `question-schema` | a [question schema](../../objects/question/question.md#^question-schema), whose slots are typed placeholders | `question`, with placeholder slots | exists |
| `identified-subject` | the system and the phenomenon of a question, at the [level of commitment](../../objects/question/question.md#^commitment-levels) `identified` or above | `target-system` and `phenomenon` at commitment `identified` or above | exists |
| `question` | a question whose slots refer to records | `question`, with every slot at commitment `identified` or above | exists |
| `concept` | a term with its definition or its explication | `to-create` | to-create |
| `measurement-procedure` | a procedure that assigns values to a quantity on a stated [scale](../../vocabulary/quantities/scale-and-level.md) | `variables[].scale` and `variables[].expression` | partial |
| `classification` | a partition of systems into [classes](../../vocabulary/systems/kind-class-population.md) | `target-system.reference_class` | exists |
| `design` | a plan of observations, interventions or simulation runs, with their conditions | `to-create` | to-create |
| `data` | the recorded [values](../../vocabulary/quantities/variable-value-observable.md) of observables | `phenomenon.data` | partial |
| `phenomenon` | a stable feature of a target, detected from data, as defined in the note on [phenomena](../../vocabulary/regularities/pattern-and-phenomenon.md) | `phenomenon` | exists |
| `target-specification` | the declared constituents and quantities of a [target](../../foundations/things-and-constructs.md) | `target-system` at commitment `specified` | exists |
| `background-model` | the laws admitted about a target, with their closure and organization | [`background`](../../objects/knowledge/background.md) | exists |
| `model` | a candidate [model](../../vocabulary/representations/model.md) of the target | [`model`](../../../specification/model.md#^model-record) | exists |
| `binding` | the relation of a model to a phenomenon, stated as the inferences from the model to the target that its asserter licenses | [`binding`](../../../specification/binding.md#^binding-record) | exists |
| `key` | a shared, versioned map between the side of a model and the side of its target | [`key`](../../../specification/key.md#^key-record) | exists |
| `consequence` | a statement true of a model, possibly false of the target | the block of model knowledge of an `answer`, and `assessment.obligations` | partial |
| `hypothesis` | a [claim](../../vocabulary/representations/claim-and-hypothesis.md) with the attitude `hypothesized` | `answer` with status `hypothesized` | exists |
| `verdict` | the outcome of a test of a claim or of a model | `assessment.tests` | exists |
| `credence` | a degree of belief in a claim | `assessment.credence` | exists |
| `ranking` | an order over rival candidates | `assessment.appraisal.preferred_over` | exists |
| `explanation` | the claim that an explanans explains a phenomenon under the requested relation | the block of an explanation of an `answer` | exists |
| `inter-theory-relation` | a relation of unification, reduction or integration between [theories](../../vocabulary/representations/theory.md) | `to-create` | to-create |
| `knowledge-state-change` | a change of the attitude or of the status of existing records | changes of the record `status`; a revision log is to create | partial |

A theory enters an activity as a `model`, read as a class of models. A framework changes only through the verdicts that motivate the change, so no product type names a framework.

## Distinctions

Four terms describing an inquiry are often used for one another:

| Term | Definition | Question that the term answers | Example | Owning note |
| --- | --- | --- | --- | --- |
| Aim | the cognitive achievement sought by an inquiry | which knowledge is sought? | explanation of a gamma oscillation | [epistemic aim](../../objects/task/epistemic-aim.md) |
| Activity | a typed operation, specified by its [signature](#^activity-criterion) | which object is produced from which objects, under which norm? | model selection | this folder |
| Mode of inference | the type of inference performed by an activity | by which type of inference? | induction | this note |
| Method | a concrete procedure that implements an activity | by which procedure? | Markov chain Monte Carlo, implementing confirmation; the Akaike information criterion, implementing model selection | this note |

The word *explanation* names three objects, each owned by one note: ^explanation-senses

- the **activity** of explanation shows that an explanans bears the requested relation to a phenomenon, as typed in the note on [explanation and integration](explanation-and-integration.md);
- the **product** is a claim, defined in the note on [claims](../../vocabulary/representations/claim-and-hypothesis.md) and held by the product type `explanation`;
- the **aim** of explanation is the achievement sought by an inquiry that asks why or how, fixed by the [epistemic aim](../../objects/task/epistemic-aim.md).

## Relations among activities

Two relations hold among activities across the families:

- **Inverse pairs**: several activities undo or mirror one another. On one theory of learning, four pairs of inverse operations organize learning as a search through a space of knowledge: generalization and specialization, abstraction and concretion, explanation and prediction, similization and dissimilization [michalski1993]. Two further pairs concern the activities of this folder: decomposition and composition, and the expansion and contraction of a belief state [alchourron1985].
- **Iteration**: an activity, or a cycle of activities, may take its own earlier output as input. For example, successive standards of temperature were each used to refine the next, so that the iteration improved a measurement without a fixed foundation [chang2004]. The discovery of mechanisms likewise cycles through characterizing the phenomenon, constructing a schema, evaluating it and revising it [craver2013].

## Activity record and itinerary check

> [!NOTE] The activity record and the itinerary check are proposals of this method

A step of a research itinerary instantiates one activity type. The [itinerary record](../../../specification/itinerary.md) states each step by its activity and its signature, with the verdict of its norm.

An itinerary passes the **itinerary check** when five conditions hold: ^itinerary-check

- every step names an activity listed in the registry of activities;
- the input types and the output type of each step equal those of its activity;
- each input of a step refers to an existing record of the declared type, or to the output of an earlier step of that type;
- the steps, linked by their input references, form a directed acyclic graph;
- every verdict is `pass`, `fail` or `pending`.

The itinerary record adds checks of its own fields, such as unique step identifiers, stated with the [record checks of an itinerary](../../../specification/itinerary.md#^record-checks).

The type of a referenced record follows from its state, as the [record column of the product types](#^product-types) states. For a question record, the state is the commitment of its slots. With a placeholder slot, the record has type `question-schema`. With every slot at commitment `identified` or above, the record has type `question`. Therefore, a schema becomes a question when [subject identification](problem-posing.md) raises its slots, and no activity of its own is needed.

The check matches types only, so an itinerary that passes it is well formed. The success of each step is decided separately, by the verdict of its norm. Each step has the form of an action schema in [classical planning](../../../references/ai-planning-pddl.md): the input types play the part of preconditions, and the output type plays the part of an effect. A step can decompose into sub-steps, as a compound task does in [hierarchical task network planning](../../../references/hierarchical-task-network-planning.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [alchourron1985] ◐ [Alchourrón, Gärdenfors & Makinson, "On the logic of theory change: partial meet contraction and revision functions", *Journal of Symbolic Logic* 50(2), 510–530, 1985](https://doi.org/10.2307/2274239)
- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001)
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987)
- [hanson1958] ◐ [Hanson, *Patterns of Discovery: An Inquiry into the Conceptual Foundations of Science*, Cambridge University Press, 1958](https://ci.nii.ac.jp/ncid/BA0361033X)
- [michalski1993] ◐ [Michalski, "Inferential theory of learning as a conceptual basis for multistrategy learning", *Machine Learning* 11(2–3), 111–151, 1993](https://doi.org/10.1007/BF00993074); the four pairs of transmutations are listed in the abstract
- [peirce1934] ◐ [Peirce, *Collected Papers of Charles Sanders Peirce*, vol. 5, *Pragmatism and Pragmaticism*, Hartshorne & Weiss (eds.), Harvard University Press, 1934](https://plato.stanford.edu/entries/abduction/peirce.html)
- [reichenbach1938] ◐ [Reichenbach, *Experience and Prediction: An Analysis of the Foundations and the Structure of Knowledge*, University of Chicago Press, 1938](https://catalogo.biblio.unc.edu.ar/Record/ffyh.39329)
- [simon1973] ◐ [Simon, "Does scientific discovery have a logic?", *Philosophy of Science* 40(4), 471–480, 1973](https://doi.org/10.1086/288559)
