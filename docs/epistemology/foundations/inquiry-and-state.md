---
tags:
  - theory
index: "[Foundations](docs/epistemology/foundations/_index.md)"
aliases:
  - Inquiry and its state
  - Inquiry
  - State of an inquiry
  - Admitted and accepted
  - Acceptance of an answer
---
# Inquiry and its state

> [!QUESTION] Goal: what is an inquiry, what does its state hold at a given time, and which bearer and which axis does each status of that state qualify?

An **inquiry** is a course of epistemic acts directed at one or several problems. An inquiry starts from a body of accepted knowledge, poses the questions that serve its problems, and changes that knowledge by proposing, assessing and accepting answers to those questions. ^inquiry

Three accounts of inquiry ground this definition, each for one of its parts:

- **An inquiry starts from a problem.** Dewey defines inquiry as the transformation of an indeterminate situation into a determinate one, and a situation becomes a problem once an inquiry states it [dewey1938]. The note on the [epistemic problem](../objects/problem/epistemic-problem.md) states a problem relative to the accepted knowledge, so that its existence and its solution can be checked.
- **An inquiry changes a corpus of accepted knowledge.** The corpus of an inquirer is the standard of serious possibility, and inquiry revises it by expansion and contraction [levi1980].
- **An inquiry proceeds by questions.** In the interrogative model, an inquiry alternates questions put to sources with deductions from the knowledge already held [hintikka2007]. The [question](../objects/question/question.md) is the unit of that course.

The definition adds one element that the records require: each act of an inquiry is typed by the [epistemic activity](../processes/activities/epistemic-activities.md) that it performs, so that the course can be checked step by step.

- **An inquiry is not a question.** One problem motivates one or several questions, and one question serves one or several problems, as the [comparison of a problem and a question](../objects/problem/epistemic-problem.md#^problem-vs-question) states. A question is therefore a part of an inquiry. A research project, in the sense of the [README](../../../README.md#motivation), holds one or several inquiries.
- **An inquiry is a course of acts, and its records represent it.** The acts are performed by inquirers, whether or not a record describes them, as the [status of an epistemic activity](things-and-constructs.md#^layer-test) states. The research records hold the content that the acts produce, and the itinerary records the acts themselves.

## The state of an inquiry

The **state** of an inquiry at a given time holds four components: ^state

- the **accepted knowledge** $K$: the finite set of claims accepted by the inquiry, together with the claims of the publications that its records cite, as the [formal statement of a problem](../objects/problem/epistemic-problem.md#^problem-triple) delimits it;
- the **proposed candidates** $H$: the answers put forward and not yet accepted, as the note on the [epistemic problem](../objects/problem/epistemic-problem.md#^candidates) defines them;
- the **open questions**: the questions posed whose problems still exist, each with the state of its [conditions of answerability](../objects/question/conditions-of-answerability.md#^condition-states);
- the **admitted background** of each target: the laws admitted about that target before any answer is sought, as the note on the [background](../objects/knowledge/background.md) states.

Each item of these components carries the statuses placed in the [table of statuses](#^status-axes). The itinerary is not a component of the state. The itinerary records the acts through which each item entered the state, and the [readiness of an act](../processes/inquiry/choice-of-act.md#^ready-act) reads it.

**The accepted knowledge is a belief base.** A belief base is a set of claims that is not closed under logical consequence, so a consequence of its members belongs to it only once it is itself accepted [hansson1999]. Two features of the method make $K$ a base. First, a claim counts as obtained only once the available means have yielded it and an assessment has accepted it, as the [reading of obtained claims](../objects/problem/epistemic-problem.md#^problem-triple) states. Second, no tool of `gnomon` derives a claim that no record states, as the [decision against inference at run time](../../adr/no-run-time-inference.md#^no-inference) fixes. The revision of $K$ therefore follows the norm of base revision, stated with the activity [`belief-revision`](../processes/activities/revision.md).

## Admitted and accepted

Two relations hold between a claim and an inquiry, and they vary independently: ^admitted-accepted

- a claim is **admitted** when the inquiry takes it as a premise, with a stated warrant, whether or not the claim is accepted as known;
- a claim is **accepted** when it is a member of $K$.

| Claim | Admitted | Accepted |
| --- | --- | --- |
| a law posited as a working assumption in the background of a target | yes | no |
| a provisional answer adopted for a dependency between two questions | yes | no |
| an accepted answer cited as a ground of another answer | yes | yes |
| an accepted claim of a cited publication, used by no answer | no | yes |
| a candidate of $H$, neither adopted nor accepted | no | no |

The second row comes from the rule on [provisional answers](../objects/question/conditions-of-answerability.md#^condition-dependencies): a result that rests on an adopted answer stays conditional on it. Every result that rests on an admitted claim that is not accepted stays conditional on that claim in the same way, as the note on [grounds and dependence](../objects/knowledge/grounds-and-dependence.md#^propagation) states.

> [!WARNING] Two uses of "acceptance" in the literature
> Cohen defines the acceptance of a proposition as a voluntary policy of taking it as a premise, distinct from believing it [cohen1992]. That sense corresponds to *admitted* in this method. The acceptance into a corpus, in the sense of Levi [levi1980], corresponds to *accepted*.

## Units of content and their epistemic roles

A **unit of content** is a research record, or a unit of such a record with an identifier of its own, as the [decision on expositions](../../adr/expositions-as-projections.md) defines a research unit. Its **epistemic role** is the kind of reasoning that it licenses: a definition licenses substitution, a result licenses citation as a ground, an assumption licenses a derivation under its scope. Two units have the same role when they license the same reasoning operations, which is the criterion of a [unitary epistemic role](../../adr/record-kind-admission.md#^five-conditions). ^unit-roles

The method fixes the role of a unit by the kind of object that holds it and by the place of the unit in that object, never by a label attached to free text. This rule answers the failure of mixed roles named in the [README](../../../README.md#motivation): a unit cannot blend a definition and a result, because each role has its own place.

| Role | Object that carries it | Note that states it |
| --- | --- | --- |
| Problem | a demand with its constraints, relative to $K$ | [epistemic problem](../objects/problem/epistemic-problem.md) |
| Question | a request whose possible answers form a definite set | [question](../objects/question/question.md) |
| Definition | a concept with its gloss, or a declaration of a quantity, which is assessed for its adequacy rather than its truth | [concepts and names](../expression/names-and-symbols.md); [adequacy of a declaration](things-and-constructs.md#^layer-test) |
| Assumption | a ground of an answer with the role `assumption` or `idealization`, or a law admitted in a background | [grounds and dependence](../objects/knowledge/grounds-and-dependence.md#^ground-roles) |
| Datum | a phenomenon, or a ground with the role `datum` | [phenomenon](../objects/subject/phenomenon.md) |
| Candidate | an answer whose attitude is `entertained` or `hypothesized` | [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| Result | an answer accepted into $K$ | [acceptance](#^acceptance-act) |
| Verdict | the outcome of a test of an answer, or of the norm of an act | [conditions of satisfaction](../objects/answer/satisfaction-conditions.md) |
| Motivation | a field of the object that it motivates, never a unit of its own | [admission of a record kind](../../adr/record-kind-admission.md#^failing-construct) |

An example and a proof have no settled place yet. The decision on record kinds treats an example as a relation from a record to a concept or an answer, and the formalization of a derivation is an open goal of the [README](../../../README.md#features).

## Statuses, their bearers and their axes

Each status of the state qualifies one bearer along one axis. An axis is the question that the status answers about its bearer. ^status-axes

| Bearer | Axis | The status measures | Values | Note that owns it |
| --- | --- | --- | --- | --- |
| claim of an answer | attitude | the stance of the inquiry toward the claim | `entertained`, `hypothesized`, `accepted`, `retracted` | [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| claim of an answer | support | the kind of grounds that the claim has, independently of the attitude | `unsupported`, `informal`, `formally-proven`, `empirically-supported` | [claim and hypothesis](../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| law of a record | warrant of a law | the provenance of the law | `derived`, `posited`, `fitted`, `measured` | [background](../objects/knowledge/background.md#^law-warrant) |
| specification of a record | maturity | how far the specification has been revised, and whether further revision is expected | `open`, `provisional`, `stabilized` | [maturity](#^maturity) |
| slot of a question | commitment | how far the slot fixes its referent | `placeholder`, `identified`, `specified` | [levels of commitment](../objects/question/question.md#^commitment-levels) |
| phenomenon | evidential status | the kind of evidence that the behavior occurs | `established`, `reported`, `predicted`, `derived` | [phenomenon](../objects/subject/phenomenon.md) |
| condition of answerability | state of a condition | whether the records show that the condition holds | `established`, `not established`, `refuted` | [states of a condition](../objects/question/conditions-of-answerability.md#^condition-states) |
| step of an itinerary | verdict of a norm | whether the output of the act meets the norm of its activity | `pass`, `fail`, `pending` | [attributes of an activity](../processes/activities/epistemic-activities.md#^attribute-vocabularies) |
| test of an assessment | verdict of a test | whether the answer passes one test | `pass`, `fail`, `pending`, `not-applicable` | [conditions of satisfaction](../objects/answer/satisfaction-conditions.md#^conditions-satisfaction) |
| assessment | disposition | the outcome read from the verdicts of admissibility and warrant | `satisfied`, `not-satisfied`, `withheld`, `corrective` | [disposition](../objects/answer/satisfaction-conditions.md#^disposition) |
| assessment | credence | the strength of belief of the assessor in the answer, given all verdicts and the prior evidence | a degree, optional | [credence](../objects/answer/satisfaction-conditions.md#^credence) |
| problem | outcome | whether and how the problem ended | solved, dissolved, abandoned | [outcomes of a problem](../objects/problem/epistemic-problem.md#^problem-outcomes) |
| record | record status | the attitude taken toward the whole record | one vocabulary per kind of record | [question](../objects/question/question.md#^commitment-levels) |

Three groups of statuses are often merged:

- **Attitude, support and warrant of a law answer three questions.** The attitude states how the inquiry holds a claim, the support states the kind of grounds that the claim has, and the warrant of a law states where one law comes from. A claim can be accepted with informal support while it rests on a measured law.
- **Verdict, disposition and acceptance follow one another, and only the first two are read from the records.** Each test returns a verdict, the disposition is read from the verdicts, and [acceptance](#^acceptance-act) is a further act.
- **Maturity and commitment vary independently**, as the note on the [levels of commitment](../objects/question/question.md#^commitment-levels) states.

**"Established" names a value on two axes.** The evidential status `established` qualifies a phenomenon: the behavior has been shown across data sets or methods. The condition state `established` qualifies a condition of answerability of one question: the records show that the condition holds. The two meet at one point only. When a question presupposes that its phenomenon occurs, the evidential status `established` of that phenomenon is one record that shows that the condition of soundness of the question holds, as the [states of a condition](../objects/question/conditions-of-answerability.md#^condition-states) admit. A condition can also be established without any phenomenon, for instance by an accepted proof that a result of the demanded type exists. ^two-established

## Maturity

The **maturity** of a specification states how far it has been revised and whether the inquiry expects to revise it again. A specification is `open` while it is not fixed, `provisional` while it is written and still under revision, and `stabilized` once the inquiry expects no further revision in its current state. The marker belongs to each specification of a record, as the [maturity of a field](../../specification/maturity.md) documents. ^maturity

- **Maturity records the fallibilism of the method.** An inquiry improves its knowledge through successive corrections that start from an initially affirmed system [chang2004]. The [controlled iteration](../processes/inquiry/specification-order.md#^controlled-iteration) of the method therefore requires every object to carry a maturity, so that a revision can be expected and traced.
- **Maturity is not a degree of confirmation.** A stabilized specification can still be false, or inadequate when it is a declaration. Maturity states only that no revision is expected, whereas the attitude and the support state the stance toward the claim and the kind of its grounds.
- **The maturity of a result combines several statuses.** The README asks for each result with its maturity. A result is an accepted answer, so its maturity is read from the attitude and the support of its claim, from the maturity of the specifications on which it rests, and from the warrant of the laws among its grounds. No single status measures it.

## Acceptance

**Accepting** an answer is an act of the researcher, or of the group that owns the inquiry, which moves the answer from $H$ into $K$. The assessment informs that act through its verdicts, its disposition and its credence, and never decides it. No tool computes an acceptance, as the [decision against inference at run time](../../adr/no-run-time-inference.md#^excluded-inference) fixes. The record of an acceptance names the corpus revised, its owner, the answer accepted and the verdicts, credence or ranking on which the act rests, as the [acceptance of an answer](../objects/task/epistemic-aim.md#^acceptance) states. ^acceptance-act

Three reasons exclude a rule that would compute acceptance from the assessment:

- **Sufficient evidence depends on the cost of an error.** No hypothesis is ever completely verified, so accepting one requires a decision that the evidence is strong enough, and that decision depends on how serious a mistake would be [rudner1953]. No test of the assessment fixes that seriousness.
- **A threshold on credence yields an inconsistent corpus.** If every claim whose credence exceeds a fixed threshold were accepted, a large set of claims, each above the threshold, would be accepted together with the claim that one of them is false [kyburg1961].
- **Several answers can be satisfied at once.** The disposition reads only the tests of admissibility and warrant, so two rival answers to one question can both be `satisfied`. Appraisal ranks them, and choosing one of them is a decision.

Withdrawing an answer from $K$ is an act of the same kind, performed by the [revision](../processes/activities/revision.md) family. Under a proposal of this method, a check may report an acceptance whose own assessment has the disposition `not-satisfied`. The report leaves the decision to the researcher.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the accounts of inquiry, belief bases, the two senses of acceptance, the dependence of acceptance on the cost of error, and the lottery paradox, as cited.
> - **Proposals:**
> 	- the definition of an inquiry, which combines the three accounts with typed acts;
> 	- the four components of the state, and the separation of admitted from accepted claims;
> 	- the epistemic role of a unit fixed by the object and the place that hold it;
> 	- the reading of the three values of maturity;
> 	- the report of an acceptance that contradicts its own assessment.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001); epistemic iteration from an initially affirmed system
- [cohen1992] ◐ Cohen, *An Essay on Belief and Acceptance*, Clarendon Press, 1992; acceptance as premising, distinct from belief, checked through secondary sources
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987); ch. 6; checked through secondary sources
- [hansson1999] ◐ [Hansson, *A Textbook of Belief Dynamics: Theory Change and Database Updating*, Kluwer, 1999](https://doi.org/10.1007/978-94-007-0814-3); belief bases, as opposed to belief sets closed under consequence
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); interrogative and deductive moves
- [kyburg1961] ◐ Kyburg, *Probability and the Logic of Rational Belief*, Wesleyan University Press, 1961; the lottery paradox
- [levi1980] ◐ Levi, *The Enterprise of Knowledge: An Essay on Knowledge, Credal Probability, and Chance*, MIT Press, 1980; the corpus of knowledge, revised by expansion and contraction
- [rudner1953] ◐ [Rudner, "The scientist qua scientist makes value judgments", *Philosophy of Science* 20(1), 1–6, 1953](https://doi.org/10.1086/287231); checked through secondary summaries
