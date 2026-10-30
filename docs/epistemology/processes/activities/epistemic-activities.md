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
> The taxonomy is a synthesis proposed by this method. Each family note cites the sources of its activities one by one. The notes are the source of the content: the [registry of activities](../../../../src/gnomon/data/registries/activities.yml) and the [registry of product types](../../../../src/gnomon/data/registries/product-types.yml) transcribe them. Therefore, a change must start in the notes. A note that states a change not yet transcribed says that the change is pending a change of the registry.

## Criterion of an epistemic activity

An operation of an inquiry counts as epistemic when its output is an **epistemic object**, as the [criterion of an epistemic object](../../objects/status/epistemic-objects.md#^epistemic-object-criterion) defines it. ^epistemic-criterion

The [product types](#^product-types) classify the epistemic objects that activities take or produce, from the problem that opens an inquiry to the change of attitude that closes one of its cycles. The [inventory of epistemic objects](../../objects/status/epistemic-objects.md#^inventory) also holds objects that no activity produces, such as the parts of a question and the computed objects. The criterion tests only the output of an activity, not the record kinds available today. Therefore, when the output of an activity has no record kind yet, the activity is still epistemic, and its output type is marked as a gap.

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
- a type followed by a qualifier, such as `model` (source), `verdict` (several) or `model` (optional), states the role, the number or the optionality of its records, and leaves the type unchanged;
- types joined by `|`, such as `hypothesis | model`, take one record of either type.

Three attributes take their values from closed lists: ^attribute-vocabularies

| Attribute | Values | Assigned to |
| --- | --- | --- |
| Verdict of the norm | `pass`, `fail`, `pending` | each step of an itinerary |
| Mode | `deductive`, `inductive`, `abductive`, `analogical`, `non-inferential` | each activity type |
| Context | `discovery`, `justification`, `both` | each activity type |

- **The norm is a named test.** Each activity has one norm, and each step of an itinerary carries the verdict of that norm: `pending` before the norm is judged, then `pass` or `fail`. The identifier under which a record names the norm of an activity is stated with the [itinerary record](../../../specification/itinerary.md).
- **The verdict of a norm differs from the product type `verdict`.** The verdict of a norm judges one step of an itinerary. The product type `verdict` is the output of an evaluation activity: the outcome of a test of a claim or of a model, which an assessment records as the verdict of a test. The [axes of the statuses](../../objects/status/statuses-and-acceptance.md#^status-axes) place each verdict on its bearer.
- **The mode `non-inferential` covers operations that draw no inference.** Formalization and idealization are examples. Observation and measurement are not, since each infers an outcome through a model of its instrument, as the [modes of the empirical activities](empirical-activities.md#^modes-pending) state.
- **The context is assigned to each activity type.** A family does not fix it: model-building holds activities of discovery, such as idealization, and of justification, such as fitting. An activity of discovery outputs a candidate, and an activity of justification judges or warrants one [reichenbach1938]. The division is contested: the reasoning that generates hypotheses follows patterns that can be analyzed [hanson1958] [simon1973]. The value `both` marks an activity whose norm serves either context, such as classification.

## Choice of the taxonomy

Three candidate taxonomies were compared on one requirement: every activity of an inquiry must receive exactly one place.

| Candidate | Primary criterion | Coverage | Decision |
| --- | --- | --- | --- |
| By stage of inquiry | the position of the activity in a cycle of inquiry [dewey1938] | fails: stages recur, and concept formation and measurement belong to no single stage | rejected as primary; kept as the relation of iteration |
| By mode of inference | abduction, deduction and induction [peirce1934] | fails: the criterion covers inferential acts only, and leaves out non-inferential activities, such as intervention, explication, formalization and framework revision | rejected as primary; kept, extended by analogy, as the attribute *mode* |
| By signature | the [signature](#^activity-criterion), with families defined by output type | succeeds: every activity has exactly one output type, non-inferential activities included | chosen |

## Families

Each family groups the activities whose output types belong to one class of product types. Each product type is the output of at most one family, so the output type of an activity fixes its family. Within one family, when two activities share an output type, they differ by their norm. ^families

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

Three types are the output of no registered activity. The type `source` is an exception by design, since a source enters an inquiry from outside it. The type `key` is a gap of the taxonomy: a key is written during an inquiry, yet no activity types the act of writing it. The type `binding` is the output of the binding activity stated below, which the registry does not yet transcribe. Conversely, a type may be the input of no activity. Such a type is a final product of an inquiry (e.g. `classification`, `inter-theory-relation`).

The partition by output type has two consequences for borderline activities. First, when the output of an activity is a model, the activity belongs to model-building, regardless of its mode and its context. Second, revision outputs only changes of attitude or of status across existing records, so a new model is never the output of a revision.

### Binding and transfer to the target

Two operations carry a model to its target, and the registry of activities types neither of them yet: ^binding-step

- **The binding activity** takes a `model`, a `phenomenon` and a `key`, and outputs a `binding`. Its norm passes when the binding denotes the phenomenon, and each of its feature pairs states the feature that the model exemplifies, the feature imputed to the target, and the key that carries the feature of the model onto the feature of the target, as the note on the [model and its binding](../../objects/answer/model-and-binding.md) states a binding. An argued pair cites its argument. The norm judges how the binding is stated, not its fidelity, which [validation](evaluation.md) judges through the comparison computed from the binding.
- **The transfer to the target** takes a `consequence` and a `binding`, and outputs a `hypothesis`: it carries a consequence of the model, through a feature pair of the binding, to a claim about the target. Its norm passes when the consequence bears on a feature that a pair of the binding carries onto the target, and the hypothesis states the imputed feature that the key of that pair yields. The step differs from the activity `transfer` of [model-building](model-building.md), which carries laws from another class of systems to the target.

The two names are kept apart. A *theoretical hypothesis*, in the sense of Giere, is a claim that relates a model to a real system [giere1988], and a binding records such claims. The *transfer to the target* names the step that uses such a claim. By the partition of the families, the transfer to the target joins ampliative inference, since its output is a `hypothesis`; the family of the binding activity is fixed when the registry transcribes it.

> [!WARNING] Pending a change of the registry
> The binding activity and the transfer to the target, with their signatures and their norms, are proposals of this method. Adding them is pending a change of the [registry of activities](../../../../src/gnomon/data/registries/activities.yml). Until that change, an itinerary cannot type the writing of a binding, and a prediction or an explanation about a target that rests on a model cannot be checked as a composition of typed steps.

## Product types

The product types form a closed list. Each type classifies the epistemic objects taken or produced by activities. The column *Output of* names the family whose activities produce the type. The taxonomy is the authority for the list: a type that no record kind holds yet is a gap of the records, which must be extended to match the taxonomy. ^product-types

> [!NOTE] Implementation coverage
> The *Status* column is not a content of the theory. That column transcribes from the [registry of product types](../../../../src/gnomon/data/registries/product-types.yml) how far the records of `gnomon` cover each type today, as the [itinerary record](../../../specification/itinerary.md#^type-coverage) documents. The column stays in this note only because a test of the project reads it, and moving that test to the registry is pending an item of the [project goals](../../../../TODO.md).

| Type | Epistemic object | Output of | Status |
| --- | --- | --- | --- |
| `source` | a document, a dataset or a result external to the inquiry | no activity, by design | exists |
| `problem` | a demand for a solution under constraints, defined in the note on the [epistemic problem](../../objects/problem/epistemic-problem.md) | problem-posing | exists |
| `question-schema` | a [question schema](../../objects/question/question.md#^question-schema): a question form whose slots are typed placeholders, not yet a question | problem-posing | exists |
| `identified-subject` | the system and the phenomenon of a question, at the [level of commitment](../../objects/question/question.md#^commitment-levels) `identified` or above | problem-posing | exists |
| `question` | a question, each of whose slots names its referent at the level `identified` or above | problem-posing | exists |
| `concept` | a term with its definition or its explication | conceptual activities | to-create |
| `measurement-procedure` | a procedure that assigns values to a quantity on a stated [scale](../../vocabulary/quantities/scale-and-level.md) | conceptual activities | partial |
| `classification` | a partition of systems into [classes](../../vocabulary/systems/kind-class-population.md) | conceptual activities | exists |
| `design` | a plan of observations, interventions or simulation runs, with their conditions | empirical activities | to-create |
| `data` | the recorded [values](../../vocabulary/quantities/variable-value-observable.md) of observables | empirical activities | partial |
| `phenomenon` | the behavior of a target that a question concerns, detected from data; only a phenomenon of the category *regularity* must be stable, as the note on [phenomena](../../vocabulary/regularities/pattern-and-phenomenon.md) states | empirical activities | exists |
| `target-specification` | the declared constituents and quantities of a [target](../../foundations/things-and-constructs.md) | model-building | exists |
| `background-model` | the laws admitted about a target, with their closure and organization, as the [background](../../objects/knowledge/background.md) states them | model-building | exists |
| `model` | a candidate [model](../../vocabulary/representations/model.md) of the target | model-building | exists |
| `binding` | the relation of a model to a phenomenon, stated as the inferences from the model to the target that its asserter licenses | the [binding activity](#^binding-step), pending a change of the registry | exists |
| `key` | a shared, versioned map between the side of a model and the side of its target | no activity yet: a gap | exists |
| `consequence` | a statement derived from a model, or from the admitted laws of a target; it becomes a claim about the target only through the [transfer to the target](#^binding-step), or when the admitted laws define the target completely | model analysis | partial |
| `hypothesis` | a [claim](../../vocabulary/representations/claim-and-hypothesis.md) about the target, held with the attitude `hypothesized` | ampliative inference | exists |
| `verdict` | the outcome of a test of a claim or of a model | evaluation | exists |
| `credence` | a degree of belief in a claim | evaluation | exists |
| `ranking` | an order over rival candidates | evaluation | exists |
| `explanation` | the claim that an explanans explains a phenomenon under the requested relation | explanation and integration | exists |
| `inter-theory-relation` | a relation of unification, reduction or integration between [theories](../../vocabulary/representations/theory.md) | explanation and integration | to-create |
| `knowledge-state-change` | a change of the attitude or of the status of existing records | revision | partial |

The word *hypothesis* has several senses, which the note on [claims and hypotheses](../../vocabulary/representations/claim-and-hypothesis.md) separates. The product type `hypothesis` combines two of them: a claim about the target, as opposed to a consequence that holds of a model, held under the attitude `hypothesized`. The excess of content over the premises is a property of the ampliative inference that produces a hypothesis, not of the type. Two consequences follow. ^hypothesis-type

First, an answer whose attitude is `entertained`, `accepted` or `retracted` has no product type of its own, since the attitude of a claim is an attribute of the claim, not a type: a type for an answer claim with any attitude is a gap of the list. Second, a statement that holds of a model is a `consequence`, so the activity of prediction outputs a `consequence`, whereas an inquiry with the aim of prediction requires a `hypothesis` about the target. The [transfer to the target](#^binding-step) carries the first to the second.

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

## Itinerary

> [!NOTE] The itinerary and its check are proposals of this method

An **itinerary** is the course of acts of one inquiry toward one problem or one question, written as a set of steps. Each step instantiates one activity type, assigns each input of that type to an epistemic object or to the output of an earlier step, and carries the verdict of the norm of the activity. The research records hold the contents that the acts produce, whereas the itinerary holds the acts themselves, as the [definition of an inquiry](../../foundations/inquiry-and-state.md#^inquiry) states. No activity outputs an itinerary, so it has no product type, and its place among the epistemic objects is stated in the [inventory of epistemic objects](../../objects/status/epistemic-objects.md#^inventory). ^itinerary

An itinerary is **well formed** when its steps compose by type, which four conditions state: ^itinerary-check

- each step instantiates one activity type of the taxonomy;
- the input types and the output type of each step equal those of the signature of its activity;
- each input of a step is an existing epistemic object of the declared type, or the output of an earlier step of that type;
- the steps, linked by their inputs, form a directed acyclic graph.

The itinerary check tests these conditions on the itinerary record, together with conditions on the fields of that record, as the [record checks of an itinerary](../../../specification/itinerary.md#^record-checks) state. When [subject identification](problem-posing.md) raises the slots of a question schema to the level `identified`, the schema becomes a question, so that change needs no activity of its own.

The conditions match types only, so an itinerary that meets them is well formed. The success of each step is decided separately, by the verdict of its norm. Each step has the form of an action schema in [classical planning](../../../references/ai-planning-pddl.md): the input types play the part of preconditions, and the output type plays the part of an effect. A step can decompose into sub-steps, as a compound task does in [hierarchical task network planning](../../../references/hierarchical-task-network-planning.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [alchourron1985] ◐ [Alchourrón, Gärdenfors & Makinson, "On the logic of theory change: partial meet contraction and revision functions", *Journal of Symbolic Logic* 50(2), 510–530, 1985](https://doi.org/10.2307/2274239)
- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001)
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987)
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html); theoretical hypotheses assert a similarity between a model and a real system
- [hanson1958] ◐ [Hanson, *Patterns of Discovery: An Inquiry into the Conceptual Foundations of Science*, Cambridge University Press, 1958](https://ci.nii.ac.jp/ncid/BA0361033X)
- [michalski1993] ◐ [Michalski, "Inferential theory of learning as a conceptual basis for multistrategy learning", *Machine Learning* 11(2–3), 111–151, 1993](https://doi.org/10.1007/BF00993074); the four pairs of transmutations are listed in the abstract
- [peirce1934] ◐ Peirce, *Collected Papers of Charles Sanders Peirce*, vol. 5, *Pragmatism and Pragmaticism*, Hartshorne & Weiss (eds.), Harvard University Press, 1934; checked through the [SEP supplement on Peirce on abduction](https://plato.stanford.edu/entries/abduction/peirce.html)
- [reichenbach1938] ◐ [Reichenbach, *Experience and Prediction: An Analysis of the Foundations and the Structure of Knowledge*, University of Chicago Press, 1938](https://catalogo.biblio.unc.edu.ar/Record/ffyh.39329)
- [simon1973] ◐ [Simon, "Does scientific discovery have a logic?", *Philosophy of Science* 40(4), 471–480, 1973](https://doi.org/10.1086/288559)
