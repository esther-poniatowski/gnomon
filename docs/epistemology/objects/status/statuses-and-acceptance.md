---
tags:
  - theory
index: "[Statuses of epistemic objects](docs/epistemology/objects/status/_index.md)"
aliases:
  - Statuses and acceptance
  - Axes of the statuses
  - Maturity of a specification
  - Acceptance of an answer
---
# Statuses and acceptance

> [!QUESTION] Goal: which bearer and which axis does each status of an inquiry qualify, what does the maturity of a specification state, and how does an answer enter the accepted knowledge?

Each item of the [state of an inquiry](../../foundations/inquiry-and-state.md#^state) carries statuses. The statuses come from every object of the inquiry, from the problem to the assessment of its answers.

## Statuses, their bearers and their axes

Each status of the state qualifies one bearer along one axis. An axis is the question that the status answers about its bearer. ^status-axes

| Bearer | Axis | The status measures | Values | Note that owns it |
| --- | --- | --- | --- | --- |
| claim of an answer | attitude | the stance of the inquiry toward the claim | `entertained`, `hypothesized`, `accepted`, `retracted` | [claim and hypothesis](../../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| claim of an answer | support | the kind of grounds that the claim has, independently of the attitude | `unsupported`, `informal`, `formally-proven`, `empirically-supported` | [claim and hypothesis](../../vocabulary/representations/claim-and-hypothesis.md#^attitude-support) |
| law of a record | warrant of a law | the provenance of the law | `derived`, `posited`, `fitted`, `measured` | [background](../knowledge/background.md#^law-warrant) |
| specification of a record | maturity | how far the specification has been revised, and whether further revision is expected | `open`, `provisional`, `stabilized` | [maturity](#^maturity) |
| slot of a question | commitment | how far the slot fixes its referent | `placeholder`, `identified`, `specified` | [levels of commitment](../question/question.md#^commitment-levels) |
| phenomenon | evidential status | the kind of evidence that the behavior occurs | `established`, `reported`, `predicted`, `derived` | [phenomenon](../subject/phenomenon.md) |
| condition of answerability | state of a condition | whether the records show that the condition holds | `established`, `not established`, `refuted` | [states of a condition](../question/conditions-of-answerability.md#^condition-states) |
| step of an itinerary | verdict of a norm | whether the output of the act meets the norm of its activity | `pass`, `fail`, `pending` | [attributes of an activity](../../processes/activities/epistemic-activities.md#^attribute-vocabularies) |
| test of an assessment | verdict of a test | whether the answer passes one test | `pass`, `fail`, `pending`, `not-applicable` | [conditions of satisfaction](../answer/satisfaction-conditions.md#^conditions-satisfaction) |
| assessment | disposition | the outcome read from the verdicts of admissibility and warrant | `satisfied`, `not-satisfied`, `withheld`, `corrective` | [disposition](../answer/satisfaction-conditions.md#^disposition) |
| assessment | credence | the strength of belief of the assessor in the answer, given all verdicts and the prior evidence | a degree, optional | [credence](../answer/satisfaction-conditions.md#^credence) |
| problem | outcome | whether and how the problem ended | solved, dissolved, abandoned | [outcomes of a problem](../problem/epistemic-problem.md#^problem-outcomes) |
| record | record status | the attitude taken toward the whole record; the record status of an answer is the attitude of its claim | one vocabulary per kind of record | [question](../question/question.md#^commitment-levels) |

Three groups of statuses are often merged:

- **Attitude, support and warrant of a law answer three questions.** The attitude states how the inquiry holds a claim, the support states the kind of grounds that the claim has, and the warrant of a law states where one law comes from. A claim can be accepted with informal support while it rests on a measured law.
- **Verdict, disposition and acceptance follow one another, and only the first two are read from the records.** Each test returns a verdict, the disposition is read from the verdicts, and [acceptance](#^acceptance-act) is a further act.
- **Maturity and commitment vary independently**, as the note on the [levels of commitment](../question/question.md#^commitment-levels) states.

**"Established" names a value on two axes.** The evidential status `established` qualifies a phenomenon: the behavior has been shown across data sets or methods. The condition state `established` qualifies a condition of answerability of one question: the records show that the condition holds. The two meet at one point only. When a question presupposes that its phenomenon occurs, the evidential status `established` of that phenomenon is one record that shows that the condition of soundness of the question holds, as the [states of a condition](../question/conditions-of-answerability.md#^condition-states) admit. A condition can also be established without any phenomenon, for instance by an accepted proof that a result of the demanded type exists. ^two-established

## Maturity

The **maturity** of a specification states how far it has been revised and whether the inquiry expects to revise it again. A specification is `open` while it is not fixed, `provisional` while it is written and still under revision, and `stabilized` once the inquiry expects no further revision in its current state. The marker belongs to each specification of a record, as the [maturity of a field](../../../specification/maturity.md) documents. ^maturity

- **Maturity records the fallibilism of the method.** An inquiry improves its knowledge through successive corrections that start from an initially affirmed system [chang2004]. The [controlled iteration](../../processes/inquiry/specification-order.md#^controlled-iteration) of the method therefore requires every specification of a record to carry a maturity, so that a revision can be expected and traced.
- **Maturity is not a degree of confirmation.** A stabilized specification can still be false, or inadequate when it is a declaration. Maturity states only that no revision is expected, whereas the attitude and the support state the stance toward the claim and the kind of its grounds.
- **The maturity of a result combines several statuses.** The README asks for each result with its maturity. A result, in the sense of the [role](epistemic-objects.md#^unit-roles), is an answer accepted into $K$, such as the [solving claim](../problem/epistemic-problem.md#^solution-claim) of a problem. Its maturity is therefore read from the attitude and the support of that answer, from the maturity of the specifications on which the answer rests and of the records that hold a demanded construct, and from the warrant of the laws among its grounds. No single status measures it.

## Acceptance

**Accepting** an answer is an act of the researcher, or of the group that owns the inquiry, which moves the answer from the proposed candidates $H$ into the accepted knowledge $K$. The assessment informs that act through its verdicts, its disposition and its credence, and never decides it. No tool computes an acceptance, as the [decision against inference at run time](../../../adr/no-run-time-inference.md#^excluded-inference) fixes. Acceptance applies only to [claims](epistemic-objects.md#^accepted-objects): a construct, such as a model or a concept, is never accepted. The record of an acceptance would name the corpus revised, its owner, the answer accepted, and the assessment, with the verdicts, the credence or the ranking, on which the act rests. No record kind holds an acceptance yet, so the records read $K$ from the answers whose attitude is `accepted`, pending that record kind. ^acceptance-act

Three reasons exclude a rule that would compute acceptance from the assessment:

- **Sufficient evidence depends on the cost of an error.** No hypothesis is ever completely verified, so accepting one requires a decision that the evidence is strong enough, and that decision depends on how serious a mistake would be [rudner1953]. No test of the assessment fixes that seriousness.
- **A threshold on credence yields an inconsistent corpus.** If every claim whose credence exceeds a fixed threshold were accepted, a large set of claims, each above the threshold, would be accepted together with the claim that one of them is false [kyburg1961].
- **Several answers can be satisfied at once.** The disposition reads only the tests of admissibility and warrant, so two rival answers to one question can both be `satisfied`. Appraisal ranks them, and choosing one of them is a decision.

The act of acceptance is typed by the activity [`belief-revision`](../../processes/activities/revision.md), whose mode is non-inferential: the act is a decision of the researcher, not a deduction from the verdicts. The registry of activities still types that activity `deductive`, pending a change of the registry. Withdrawing an answer from $K$ is an act of the same kind, performed by the same family, and its record names the answer withdrawn instead of the answer accepted. Under a proposal of this method, a check may report an acceptance whose own assessment has the disposition `not-satisfied`. The report leaves the decision to the researcher.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** epistemic iteration, the dependence of acceptance on the cost of error, and the lottery paradox, as cited.
> - **Proposals:**
> 	- one bearer and one axis for each status;
> 	- the reading of the three values of maturity;
> 	- the non-inferential mode of the act of acceptance;
> 	- the report of an acceptance that contradicts its own assessment.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001); epistemic iteration from an initially affirmed system
- [kyburg1961] ◐ Kyburg, *Probability and the Logic of Rational Belief*, Wesleyan University Press, 1961; the lottery paradox
- [rudner1953] ◐ [Rudner, "The scientist qua scientist makes value judgments", *Philosophy of Science* 20(1), 1–6, 1953](https://doi.org/10.1086/287231); checked through secondary summaries
