---
tags:
  - theory
index: "[Statuses of epistemic objects](docs/epistemology/objects/status/_index.md)"
aliases:
  - Epistemic objects
  - Inventory of epistemic objects
  - Unit of content
  - Epistemic role of a unit
---
# Epistemic objects

> [!QUESTION] Goal: what counts as an epistemic object of an inquiry, and which epistemic role, product type and record kind does each object take?

An **epistemic object** is a representation whose content bears on the questions, the knowledge or the warrants of an inquiry. ^epistemic-object-criterion

The criterion tests the content of an object, not the way in which the object comes about. The objects that pass it come about in four ways, and the [inventory](#^inventory) names one way for each object:

- **an output of an activity**: the object falls under one of the [product types](../../processes/activities/epistemic-activities.md#^product-types), the closed list of the inputs and outputs of the epistemic activities. An activity is epistemic exactly when its output is an epistemic object, as the [criterion of an epistemic activity](../../processes/activities/epistemic-activities.md#^epistemic-criterion) states, but an epistemic object need not be the output of an activity;
- **a part of a question**: the object is fixed when the question is specified, and no activity outputs it alone;
- **a computed object**: a tool computes the object from authored records by a declared rule, so the object has no author, as the [boundary of computation](../../../adr/no-run-time-inference.md#^admitted-computation) states;
- **a collection**: the object gathers other objects, each of which comes about in one of the three ways above.

## Units of content and their epistemic roles

A research unit, the grain of content defined with the [records of an inquiry](../../foundations/inquiry-and-state.md#^record), bears an **epistemic role**: the kind of reasoning that the unit licenses. A definition licenses substitution, a result licenses citation as a ground, and an assumption licenses a derivation under its scope. Two units have the same role when they license the same reasoning operations, which is the criterion of a [unitary epistemic role](../../../adr/record-kind-admission.md#^five-conditions). ^unit-roles

The method fixes the role of a unit by the kind of object that holds it and by the place of the unit in that object, never by a label attached to free text. This rule answers the failure of mixed roles named in the [README](../../../../README.md#motivation): a unit cannot blend a definition and a result, because each role has its own place. ^role-by-place

| Role | Object that carries it | Note that states it |
| --- | --- | --- |
| Problem | a demand with its constraints, relative to $K$ | [epistemic problem](../problem/epistemic-problem.md) |
| Question | a request whose possible answers form a definite set | [question](../question/question.md) |
| Definition | a concept with its gloss, a declaration of a quantity, or a key, each assessed for its adequacy rather than its truth | [concept](../concept/concept.md); [adequacy of a declaration](../../foundations/things-and-constructs.md#^declaration-adequacy) |
| Assumption | a ground of an answer with the role `assumption` or `idealization`, a law admitted in a background, the laws of a model, or a binding | [grounds and dependence](../knowledge/grounds-and-dependence.md#^ground-roles) |
| Datum | a phenomenon, its data, or a ground with the role `datum` | [phenomenon](../subject/phenomenon.md) |
| Candidate | an answer whose attitude is `entertained` or `hypothesized` | [claim and hypothesis](../../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| Result | an answer accepted into $K$ | [acceptance](statuses-and-acceptance.md#^acceptance-act) |
| Verdict | the outcome of a test of an answer, or of the norm of an act | [conditions of satisfaction](../answer/satisfaction-conditions.md) |
| Motivation | a field, or a unit with an identifier of its own, of the record that it motivates; never a record of its own | [admission of a record kind](../../../adr/record-kind-admission.md#^failing-construct) |

A role belongs to an authored unit, so a computed object bears no role of its own: a comparison or a disposition informs the verdict that cites it. An example and a proof have no settled place yet. The decision on record kinds treats an example as a relation from a record to a concept or an answer, and the formalization of a derivation is an open goal of the [README](../../../../README.md#features).

## Inventory

The table lists every epistemic object of an inquiry, in the order of the reading path. The column *Product type* gives the type under which an activity outputs the object, or states why no type applies. The column *Record kind* gives the kind of record that holds the object, and the column *Owner* links the note that defines it. ^inventory

| Object | Epistemic role | Product type | Record kind | Owner |
| --- | --- | --- | --- | --- |
| accepted knowledge $K$ | Result, for each member | none: a collection of accepted claims | none: the accepted research units | [state of an inquiry](../../foundations/inquiry-and-state.md#^state) |
| proposed candidates $H$ | Candidate, for each member | none: a collection of answers | none: the answers not yet accepted | [state of an inquiry](../../foundations/inquiry-and-state.md#^state) |
| source | the role of the unit that cites it | `source` | none: an external pointer | [product types](../../processes/activities/epistemic-activities.md#^product-types) |
| problem | Problem | `problem` | `problem` | [epistemic problem](../problem/epistemic-problem.md) |
| question schema | Question | `question-schema` | `question`, with a slot at the level `placeholder` | [question schema](../question/question.md#^question-schema) |
| question | Question | `question` | `question` | [question](../question/question.md) |
| subject $\Sigma$ | none of its own: part of a question | none: part of a question; its system and phenomenon, once identified, form an `identified-subject` | `question` | [subject of inquiry](../subject/subject-of-inquiry.md) |
| target specification | Definition | `target-specification` | `target-system` | [target system](../subject/target-system.md) |
| measurement procedure | Definition | `measurement-procedure` | `target-system`, in part | [conceptual activities](../../processes/activities/conceptual-activities.md) |
| classification | Definition | `classification` | `target-system` | [conceptual activities](../../processes/activities/conceptual-activities.md) |
| design | none yet: a plan of acts, a gap of the role table | `design` | none yet | [empirical activities](../../processes/activities/empirical-activities.md) |
| data | Datum | `data` | `phenomenon`, in part | [empirical activities](../../processes/activities/empirical-activities.md) |
| phenomenon | Datum | `phenomenon` | `phenomenon` | [phenomenon](../subject/phenomenon.md) |
| admitted background | Assumption | `background-model` | `background` | [background](../knowledge/background.md) |
| task $T$ | none of its own: part of a question | none: part of a question | `question` | [epistemic task](../task/epistemic-task.md) |
| virtues $\mathcal{V}$ | none of its own: part of a question | none: part of a question | `question` | [virtues](../task/epistemic-pragmatic-virtues.md) |
| candidate answer | Candidate | `hypothesis` when its attitude is `hypothesized`; for any other attitude, a gap of the list | `answer` | [answer form](../answer/answer-form.md) |
| result | Result | none: an accepted answer, a gap of the list | `answer` | [acceptance](statuses-and-acceptance.md#^acceptance-act) |
| ground | the role fixed by its ground role, such as Assumption or Datum | none: a unit of an answer | `answer` | [grounds and dependence](../knowledge/grounds-and-dependence.md#^ground) |
| explanation | Candidate or Result, by the attitude of its answer | `explanation` | `answer` | [answer form](../answer/answer-form.md) |
| consequence | Candidate or Result, by the attitude of the answer that states it | `consequence` | `answer` or `assessment`, in part | [model analysis](../../processes/activities/model-analysis.md) |
| model system | Assumption | `model` | `model` | [model and binding](../answer/model-and-binding.md) |
| binding | Assumption | `binding` | `binding` | [model and binding](../answer/model-and-binding.md#^map-versus-binding) |
| key | Definition | `key`; no activity outputs it yet | `key` | [model and binding](../answer/model-and-binding.md) |
| comparison | none: computed | none: computed | none: recomputed from the inputs that an assessment cites | [computed comparison](../answer/model-and-binding.md#^comparison) |
| assessment | Verdict | `verdict`, `credence` and `ranking`, for its parts | `assessment` | [assessment](../answer/satisfaction-conditions.md#^assessment) |
| disposition | none: computed | none: computed | none: read from the verdicts of an assessment | [disposition](../answer/satisfaction-conditions.md#^disposition) |
| inter-theory relation | Candidate or Result, by its attitude | `inter-theory-relation` | none yet | [explanation and integration](../../processes/activities/explanation-and-integration.md) |
| knowledge-state change | none of its own: it changes the attitude or the status of other units | `knowledge-state-change` | none of its own: the statuses of the records that it changes | [revision](../../processes/activities/revision.md) |
| itinerary | none: it records acts, not content | none: a record of acts | `itinerary` | [itinerary](../../processes/activities/epistemic-activities.md#^itinerary) |
| concept | Definition | `concept` | `concept` | [concept](../concept/concept.md) |

The binding is the output of the binding activity, which takes a model, a phenomenon and a key, pending a change of the registry of activities that adds it.

## Objects outside the inventory

Four kinds of content in the records fail the criterion, or bear on it only through another object:

- **An inquiry is a course of acts, not a representation.** Its [status](../../foundations/things-and-constructs.md#^layer-test) is ontological, and the itinerary represents it.
- **An exposition adds no content.** Each exposition presents research units to an audience, as the [rule against added content](../../expression/exposition.md#^adds-no-content) states.
- **A glossary and a notation hold forms, not meanings.** Each maps concepts or quantities to the forms that express them, as the note on the [glossary and the notation](../../expression/names-and-symbols.md) states.
- **A condition of answerability is a requirement on a question.** Its state is a status of that question, placed on the [axes of the statuses](statuses-and-acceptance.md#^status-axes).

## Distinctions

- **A product type differs from an object.** The product types classify the inputs and the outputs of the activities, whereas the inventory classifies the contents of the state of an inquiry. An answer has a product type only under the attitude `hypothesized`, and the task, the virtues, the comparison and the itinerary have none.
- **An epistemic role differs from a product type.** The role states the reasoning that a unit licenses, whereas the type states which activity outputs it. A `hypothesis` and an `explanation` share the role Candidate while they are not accepted.

---
## Sources

> [!NOTE] Status of the claims
> - **Proposals:**
> 	- the criterion of an epistemic object stated over content, and its four ways of coming about;
> 	- the epistemic role of a unit fixed by the object and the place that hold it;
> 	- the roles assigned to the laws of a model, to a binding and to a key;
> 	- the inventory, and the objects excluded from it.
