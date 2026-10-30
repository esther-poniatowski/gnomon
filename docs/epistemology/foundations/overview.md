---
tags:
  - theory
index: "[Foundations](docs/epistemology/foundations/_index.md)"
aliases:
  - Overview of the theory
  - Root question of the theory
  - Reading path of the theory
---
# Overview of the theory

> [!QUESTION] Goal: which question does the theory of `gnomon` answer, and which epistemic objects, processes and commitments does its answer comprise?

## The question that the theory answers

The [README](../../../README.md#motivation) names five failures of a research project kept in prose: hidden dependencies, a diluted argument, drift toward side questions, mixed epistemic roles, and content held only in exposition. The five failures share one cause: prose serves both to store the content and to access it. The theory of `gnomon` therefore answers one root question: ^root-question

> How can a research inquiry be represented so that its content, the dependencies among its results, the warrant and the maturity of each result, and the next act that it calls for can be stated, checked and revised without any exposition, and then projected into expositions that add no content?

The theory answers the root question in three parts: the **epistemic objects** that an inquiry states, the **epistemic processes** by which it advances, and the **commitments** that the method makes about both. Each part is stated below in short accounts, and each account points to the note that holds its detail.

The theory covers concepts, distinctions, criteria stated over concepts, and the grounds of each choice in the literature. The theory does not cover the fields of the records, which the [specification](../../specification/_index.md) documents, nor the procedures that apply the theory, which the [procedures](../../procedures/_index.md) state. The [test that separates theory from specification](../../../CONTRIBUTING.md#theory-and-specification) decides the tier of each content.

## Epistemic objects

An inquiry states the following objects. The first item frames the others, and each later item uses only the items listed before it:

1. **Inquiry and state.** An [inquiry](inquiry-and-state.md#^inquiry) is a course of epistemic acts directed at problems, and its [state](inquiry-and-state.md#^state) at a given time holds the accepted knowledge $K$, the proposed candidates $H$, the open questions and the admitted background of each target.
2. **Problem.** A [problem](../objects/problem/epistemic-problem.md) is a demand for a result that $K$ does not yet deliver, with the constraints on that result. Its [obstacles](../objects/problem/problem-types.md) explain why the demand is unmet.
3. **Question and its specification.** A [question](../objects/question/question.md) is a request whose possible answers form a definite set. Its [specification](../objects/question/question-specification.md) $\langle\Sigma,T,\mathcal{V}\rangle$ fixes that set through three layers: the subject $\Sigma$, the epistemic task $T$ and the virtues $\mathcal{V}$.
4. **Subject.** The [subject of inquiry](../objects/subject/subject-of-inquiry.md) $\Sigma$ names the target system, the phenomenon, the contrast and the conditions held fixed.
5. **Admitted background and accepted knowledge.** The [background](../objects/knowledge/background.md) of a target holds the laws admitted about it before any answer is sought. Those laws are [admitted, not necessarily accepted](inquiry-and-state.md#^admitted-accepted) into $K$.
6. **Task.** The [epistemic task](../objects/task/epistemic-task.md) $T$ fixes the kind of knowledge that an answer must deliver: its aim, its requested relation, its modal strength, its bound on the explanans, its required accuracy and its proof obligations.
7. **Virtues.** The [virtues](../objects/task/epistemic-pragmatic-virtues.md) $\mathcal{V}$ are the qualities by which a question compares admissible answers, each marked constitutive or preferred.
8. **Answer and its grounds.** An [answer](../objects/answer/answer-form.md) is a typed claim, a product of the inquiry and never part of the specification of its question. The answer rests on [grounds](../objects/knowledge/grounds-and-dependence.md#^ground), each with a role.
9. **Model system and binding.** When the route of an answer runs on a stand-in, the answer rests on a [model system](../objects/answer/model-and-binding.md), and a binding relates that model to the phenomenon.
10. **Assessment.** An [assessment](../objects/answer/satisfaction-conditions.md) tests an answer for admissibility, warrant and appraisal, against conditions fixed before the answer is evaluated.
11. **Itinerary.** An itinerary records each act of the inquiry as a step typed by its [epistemic activity](../processes/activities/epistemic-activities.md#^itinerary-check), so that its inputs and its output can be checked.
12. **Concept.** A [concept](../expression/concepts-and-names.md) is a unit of meaning, kept apart from the names and symbols that express it.

## Epistemic processes

An inquiry advances by the following processes, which the method performs or records:

1. **Posing.** The [problem-posing](../processes/activities/problem-posing.md) activities turn a source into a problem, and a problem into the questions that serve it.
2. **Specifying in order.** The [order of specification](../processes/inquiry/specification-order.md) fixes the order in which a question is specified, and revises an earlier choice without circularity.
3. **Diagnosing answerability.** The [conditions of answerability](../processes/inquiry/conditions-of-answerability.md) state the conditions that must hold before an answer can be obtained, and the order in which they can be established.
4. **Decomposing.** The [decomposition of a question](../processes/inquiry/question-decomposition.md) yields the questions that serve it, as the inquiry proceeds.
5. **Performing typed epistemic activities.** Each act instantiates one [epistemic activity](../processes/activities/epistemic-activities.md), typed by its inputs, its output and its norm.
6. **Assessing.** The [conditions of satisfaction](../objects/answer/satisfaction-conditions.md) return a verdict per test, from which the disposition of the assessment is read.
7. **Accepting.** [Accepting](inquiry-and-state.md#^acceptance-act) an answer into $K$ is an act of the researcher, informed by the assessment and never computed from it.
8. **Revising.** The [revision](../processes/activities/revision.md) activities change the attitude toward existing claims or the frameworks that pose them, and every revision is [reported to the claims that depend on it](../objects/knowledge/grounds-and-dependence.md#^propagation).
9. **Choosing the next act.** The [choice of the next act](../processes/inquiry/choice-of-act.md) addresses an open or a refuted condition with an act that is ready, and ranks the ready acts. The [procedure of the next act](../../procedures/inquiry/next-act.md) applies these criteria to a state, outside the theory tier.

## Expression

The content that the objects state and the processes advance is expressed for a reader without being changed. The [concepts and names](../expression/concepts-and-names.md) keep a meaning apart from the names and symbols that express it, and an [exposition](../expression/exposition.md) selects and orders research units for an audience, adding no content. Projecting into an exposition is therefore not an epistemic process: it changes how the content is presented, never what the inquiry has established.

## Commitments

The method makes ten commitments:

1. **Mediated access.** An object is known only through a description, which is itself a representation, as the [mediated access](existence-and-access.md#^mediated-access) states.
2. **Literal claims.** A claim is read literally and can be false of its target, as the [commitments of the method](existence-and-access.md#^method-stance) state.
3. **Neutrality on existence.** No record states whether its object exists independently of any description, as the same commitments and the [decision on neutral records](../../adr/neutral-records-on-existence.md) state.
4. **Questions determined by their answers.** A question is fixed by its set of possible answers, as the [definition of a question](../objects/question/question.md) states.
5. **Tests fixed before evaluation.** The tests that an answer must pass are stated before any candidate is evaluated, as the [conditions of satisfaction](../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) state.
6. **Three layers, with the answer as a product.** The subject, the task and the virtues specify a question. The answer type and the conditions of satisfaction follow from them, and the answer is a product of the inquiry, as the [specification of a question](../objects/question/question-specification.md) states.
7. **Pluralism on evidence and on representation.** Severity governs the verdict of a test, and a credence, when stated, is Bayesian and complements the verdict, as the [evaluation](../processes/activities/evaluation.md) activities state. The binding stays neutral among the accounts of scientific representation, and adopts the inferential vocabulary as a choice of the method, as the note on the [model and its binding](../objects/answer/model-and-binding.md) states.
8. **Base revision.** The accepted knowledge is a [belief base](inquiry-and-state.md#^state), and its revision follows the norm of base revision stated with the [revision](../processes/activities/revision.md) activities.
9. **Least commitment.** A choice is deferred until a condition requires it, as the devices of the [order of specification](../processes/inquiry/specification-order.md) state.
10. **Fallibilism.** Every object carries a [maturity](inquiry-and-state.md#^maturity), every revision records its trigger, and the [controlled iteration](../processes/inquiry/specification-order.md#^controlled-iteration) keeps that revision non-circular.

## Words that change sense across the theory

Several words of the theory name different objects in different notes. The table separates them, and a note whose context does not fix the sense names it as the table does. ^senses-table

| Word | Sense | Note that owns it |
| --- | --- | --- |
| model | **target description**: the target specification with its background, which represents the target with no stand-in | [model](../vocabulary/representations/model.md#^target-description-is-a-model) |
| model | **model system**: an object studied in place of the target | [model](../vocabulary/representations/model.md) |
| model | **model record**: the record that declares a model system | [model record](../../specification/model.md) |
| model | **mechanistic model**: a model whose form represents a mechanism | [mechanism and mechanistic model](../vocabulary/regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test) |
| model | **semantic-view model**: a structure that satisfies the predicate defining a theory | [theory](../vocabulary/representations/theory.md) |
| target | **target**: the system, or the class of systems, that an inquiry is about | [two senses of target](things-and-constructs.md#^target-senses) |
| target | **target specification**: the record that delimits the target | [two senses of target](things-and-constructs.md#^target-senses) |
| background | **background**: the laws admitted about one target | [background](../objects/knowledge/background.md) |
| — | **accepted knowledge** $K$: the claims accepted by the inquiry, never called a background | [state of an inquiry](inquiry-and-state.md#^state) |
| — | **conditions held fixed** $D$: the causal field of a question, never called a background | [domain of conditions](../objects/subject/domain.md) |
| law | **law of a record**: any admitted general claim about declared quantities, with a role | [background](../objects/knowledge/background.md#^laws) |
| law | **law statement**: a general claim that meets a criterion of lawhood | [law](../vocabulary/regularities/law.md#^lawhood) |
| phenomenon | **phenomenon**: the behavior of the target that a question concerns | [phenomenon](../objects/subject/phenomenon.md) |
| explanandum | **explanandum**: the role of the phenomenon when the aim is explanation | [pattern and phenomenon](../vocabulary/regularities/pattern-and-phenomenon.md) |
| adequacy | **adequacy for purpose**: a model serves the purpose of a question | [model and binding](../objects/answer/model-and-binding.md#^adequacy-for-purpose) |
| adequacy | **adequacy to use**: a model has the property that its declared use requires | [warrant through the binding](../objects/answer/satisfaction-conditions.md#^warrant-through-binding) |
| adequacy | **adequacy of an explication**: an explicatum meets the requirements on replacing its explicandum | [concepts and names](../expression/concepts-and-names.md#^concept) |
| adequacy | **adequacy of a declaration**: a declared quantity represents a property of the target | [things and constructs](things-and-constructs.md#^declaration-adequacy) |
| appraisal | **appraisal**: the tier of an assessment that compares admissible answers by the virtues, never called adequacy | [conditions of satisfaction](../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) |
| warrant | **warrant tier**: the tier of an assessment that tests the evidence for an answer | [conditions of satisfaction](../objects/answer/satisfaction-conditions.md#^warrant-through-binding) |
| warrant | **warrant of a law**: the provenance of a law, `derived`, `posited`, `fitted` or `measured` | [background](../objects/knowledge/background.md#^law-warrant) |
| warrant | **ground role `warrant`**: a law that licenses the step from the other grounds to the claim | [grounds and dependence](../objects/knowledge/grounds-and-dependence.md#^ground-roles) |
| — | **burdens of justification**: the kinds of justification that a claim sought requires, never called warrants | [question decomposition](../processes/inquiry/question-decomposition.md) |
| hypothesis | **attitude** `hypothesized`: a claim held provisionally while it is tested | [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| hypothesis | **ampliative output**: a claim whose content exceeds that of its premises | [ampliative inference](../processes/activities/ampliative-inference.md) |
| hypothesis | **claim about a target**, as opposed to a consequence that holds of a model | [product types](../processes/activities/epistemic-activities.md#^product-types) |
| hypothesis | **theoretical hypothesis**: the claim that a model is similar to a target in stated respects | [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md) |
| — | **resistance hypothesis** $\eta$: the obstacle that generates a serving question, never written with $H$ | [question decomposition](../processes/inquiry/question-decomposition.md) |
| established | **evidential status** `established` of a phenomenon, and **condition state** `established` of a condition of answerability | [two axes of "established"](inquiry-and-state.md#^two-established) |
| question | **question**: a request whose possible answers form a definite set; a **research question** composed of atomic questions is its decomposition; a **question schema** is a question form, not yet a question | [question](../objects/question/question.md) |
| activity | **epistemic activity**: an act of inquiry, typed by its output and its norm; **mechanistic activity**: a producer of change in a mechanism | [epistemic activities](../processes/activities/epistemic-activities.md); [mechanistic activity](../vocabulary/change/mechanistic-activity.md) |
| $\lambda$ | **bound on the explanans**, along two axes, never called the level | [admissible explanans](../objects/task/admissible-explanans.md) |

## Reading path

The notes are read in the following order, in which each note uses only terms defined before it:

1. **Foundations.** This overview, then [inquiry and its state](inquiry-and-state.md), [existence and access](existence-and-access.md) and [things and constructs](things-and-constructs.md).
2. **Core vocabulary.** [Model](../vocabulary/representations/model.md), [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md), [law](../vocabulary/regularities/law.md) and [pattern and phenomenon](../vocabulary/regularities/pattern-and-phenomenon.md). The other notes of the [vocabulary](../vocabulary/_index.md) serve for lookup, and the [notation](../vocabulary/notation/notation.md) is consulted throughout.
3. **Problem.** The [epistemic problem](../objects/problem/epistemic-problem.md), then the [types of problem](../objects/problem/problem-types.md).
4. **Question.** The [question](../objects/question/question.md), then its [specification](../objects/question/question-specification.md).
5. **Subject.** The notes of the [subject of inquiry](../objects/subject/_index.md), in the order of their index.
6. **Admitted background.** The [background](../objects/knowledge/background.md).
7. **Task and virtues.** The notes of the [epistemic task](../objects/task/_index.md), in the order of their index.
8. **Answer and assessment.** The notes of the [answer and its assessment](../objects/answer/_index.md), in the order of their index, then [grounds and dependence](../objects/knowledge/grounds-and-dependence.md).
9. **Expression.** [Concepts and names](../expression/concepts-and-names.md), then [exposition](../expression/exposition.md).
10. **Activities.** The [epistemic activities](../processes/activities/epistemic-activities.md), then their families in the order of their [index](../processes/activities/_index.md).
11. **Course of an inquiry.** The [order of specification](../processes/inquiry/specification-order.md), the [conditions of answerability](../processes/inquiry/conditions-of-answerability.md) the [decomposition of a question](../processes/inquiry/question-decomposition.md) and the [choice of the next act](../processes/inquiry/choice-of-act.md), then the procedure of the [next act](../../procedures/inquiry/next-act.md).
