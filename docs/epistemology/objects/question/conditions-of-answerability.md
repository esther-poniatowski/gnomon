---
tags:
  - theory
  - revision
index: "[Question](docs/epistemology/objects/question/_index.md)"
aliases:
  - Conditions of answerability
  - Answerability
  - Route to an answer
---
# Conditions of answerability

> [!QUESTION] Goal: which conditions must hold before an answer to a question can be obtained, how do these conditions depend on each other, and how do they differ from the evaluation of an answer once obtained?

A question is **answerable** at a given time when an admissible answer can be obtained and justified with the means available at that time. Two stages separate the work on an answer:

- the **conditions for obtaining an answer**, which can be checked before any answer exists;
- the **evaluation of an obtained answer**, which the warrant tests of the [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md) perform.

## Two routes to an answer

An answer is reached along one of two routes: ^routes

- **Selection.** Candidates are proposed, a quantity takes different values under them, and the value obtained selects one candidate. *Example*: two rival accounts of gamma oscillations, separated by the effect of blocking the excitatory input to the interneurons.
- **Construction.** A procedure is named that would yield a direct answer once it is developed or run, and no rival candidates need to be separated. *Example*: an algorithm that enumerates the fixed points of a network at each gain.

A construction route is compatible with the [existence of a problem](../../objects/problem/epistemic-problem.md#^problem-existence), which holds while its [demand is not met](../../objects/problem/epistemic-problem.md#^demand-met). A procedure that has not been run has obtained no answer, and a result obtained but not yet accepted is a proposed candidate. Access along this route holds when a procedure of the available means applies to the demanded result, which means that the procedure is designed for that result and that its inputs exist. Establishing access therefore does not end the problem.

The conditions of one route are jointly necessary for that route. Alternatives arise at two levels: between the two routes, and between procedures that meet one condition, such as an analytic derivation and a simulation that both give access to a quantity. The [decomposition graph](../../processes/inquiry/question-decomposition.md#^decomposition-graph) records such alternatives as disjunctive relations between serving questions.

## The eight conditions for obtaining an answer

Each condition is stated for one question. ^eight-conditions

| Condition | Holds when | Route | Typical serving question |
| --- | --- | --- | --- |
| Definiteness of a term | the term has a definition or an operational criterion adequate to its use | both | what counts as a disentangled representation, and how is it measured? |
| Answer type | each component of the type of the direct answers is fixed: the components of the [epistemic task](../../objects/task/epistemic-task.md), the grain of the explanandum, the extent over the reference class and the conditions held fixed, and the contrast | both | at which grain, over which class, and to which accuracy must the answer hold? |
| Soundness | the presuppositions of the question are true: its existence presupposition, and its topic presupposition when it has one | both | does the phenomenon occur robustly? does a result of the demanded type exist? |
| Candidates | at least one proposed candidate passes the admissibility tests | selection | which mechanisms could produce the effect? |
| Discrimination | a quantity with an operational criterion takes different values under the admissible candidates and their alternatives | selection | which observable separates mechanism A from mechanism B? |
| Access | a procedure of the available means applies to the quantity: the discriminating quantity under selection, the demanded result under construction | both | how can the observable be computed or measured? |
| Bridging | an inference stated before the quantity is obtained links the quantity to the answer: a measurement model, an auxiliary hypothesis, a lemma | both | does the observable index the property under the assumptions made? |
| Representation | when access is exercised on a model of the target, that model represents the target to the required accuracy over the reference class | both, when access uses a model of the target other than a model that grounds the answer | does the linear model represent the nonlinear network to the required accuracy over the class? |

- **A candidate is opposed to its alternatives.** Discrimination opposes the admissible candidates to each other and to their alternatives. The alternatives of a candidate are the foils of the contrast, when the question names a contrast; otherwise the members of a declared space of hypotheses, named but not yet proposed; otherwise the negation of the candidate. Discrimination therefore stays defined when a single candidate is proposed.
- **Definiteness holds term by term.** A term can be definite while another term of the same question is not, so the state of definiteness is the state of each term, and a condition that depends on definiteness depends on the terms that it names. For a slot of a question, the level `specified` of the [levels of commitment](../../objects/question/question.md#^commitment-levels) is necessary for definiteness: it writes the formal declarations of the slot. Whether these declarations are adequate to their use is judged separately. The level `identified` fixes the referent of the slot without a criterion.
- **The explicandum of a question of explication is not a slot.** A question that asks which criterion should define a term demands the definiteness of that term as its answer. The explicandum enters the question through its anchored use, as an explicandum of the [problem record](../../../specification/problem.md) does, not as a typed slot. Therefore, definiteness of that term is not a condition of the question, and a dependency on it is void.
- **The answer type supplies two standards.** The epistemic task fixes the proof obligations and the required accuracy of the answer. Bridging must discharge the proof obligations when the answer has to derive a statement, and representation must reach the required accuracy. The answer type supplies no other standard of warrant.
- **Soundness has two parts.** The topic presupposition states that the fact in question holds, and the existence presupposition states that a result of the demanded type exists, as the note on the [epistemic problem](../../objects/problem/epistemic-problem.md#^presuppositions) defines them. The warrant test of phenomenon established later reads, on the obtained answer, the same fact that the topic part requires.
- **The answer type holds component by component.** Like definiteness, the answer type holds field by field. A component left open on purpose, such as an admissible explanans with the maturity `open`, keeps the admissibility test that reads it `pending`, while the other components and their tests apply. Such a component counts as fixed for every dependency except that test, so the condition of candidates can be opened, but it can reach the state `established` only once the component is narrowed.
- **The admissibility tests check a candidate against the specification, mostly before evidence.** These tests compare the candidate with the answer type and with the declarations of the system, and most of their clauses apply before any evidence. The clauses of the tests of relation and of individuation that bear on interventions can require evidence. A candidate stated in words only can be proposed, but it cannot pass the admissibility tests of individuation and of admissible explanans, which require references to constituents and quantities declared by the target or by a model record. When the set $H$ is empty, or when all its candidates fail these tests, the condition of candidates is in the state `not established`, and proposing a candidate acts on it.
- **Representation keeps the advance part of scope.** Representation is checked before the answer is obtained, on the model on which access is exercised. That model is distinguished from a model that grounds the answer: a model on which the derivation, the proof or the simulation of the answer runs, and over whose symbols the claim of the answer is stated, as the element Route of the [answer form](../../../specification/answer.md#^answer-elements) records. When access is exercised on the target description, with no stand-in, representation holds trivially. Whether the obtained answer holds of the target is judged afterwards by the warrant tests of fidelity, robustness and selection. When access is exercised on a model that grounds the answer, representation and the warrant test of fidelity judge the same model against the same required accuracy, so representation is not a condition of the route, and the warrant test of fidelity alone judges the model afterwards.

## Evaluation of an obtained answer

Once the conditions of a route hold, the acts that exercise access obtain the quantity, a combination step composes the answer through the bridging inference, and the evaluation judges the answer. The warrant tests of the conditions of satisfaction perform that judgment: the tests of phenomenon established, foil evidence, law warrant, closure, fidelity, robustness and selection. An answer obtained along the route of construction was never checked as a candidate, so its evaluation also applies the admissibility tests, by `admissibility-check`. The warrant tests apply to the obtained answer, so they are not conditions for obtaining it. An answer enters the accepted knowledge $K$ only when the researcher accepts it, a decision informed by its assessment and never computed from it, as the [act of acceptance](../status/statuses-and-acceptance.md#^acceptance-act) states. ^evaluation

## States of a condition

At a given time, a condition is in one of three condition states: ^condition-states

- **established**, when the records show that it holds: the norm of the act whose outcome bears on the condition has passed, that outcome is positive, and, when the outcome is a claim, that claim has been accepted into $K$; or a record field whose definition shows the condition holds the value that shows it, such as the evidential status `established` of a phenomenon, cited by a pointer; or when the researcher asserts that it holds, with pointers to the records or the publications that show it;
- **not established**, when nothing yet shows whether it holds;
- **refuted**, when the records or the literature show that it fails.

The condition state `established` differs from the evidential status `established` of a phenomenon, as the [two senses of "established"](../status/statuses-and-acceptance.md#^two-established) state, although the second can show that the topic presupposition holds.

A refutation rests either on an argument or on the means tried:

- **Refuted outright.** An argument of impossibility shows that the condition fails, such as a proof that two candidates are not identifiable from the observables.
- **Refuted for lack of means.** The record names a finite set of means considered, drawn from the available means, and every member of that set has been tried and has failed. A member not yet tried keeps the condition in the state `not established`. Such a refutation holds relative to the means considered at its time, so the condition can reach the state `established` later, once a new instrument, data set, algorithm or proof technique exists. The note on [question decomposition](../../processes/inquiry/question-decomposition.md#^terminal-acts) states the same relativity for terminal questions.

## Dependencies between the conditions

A condition **depends on** another condition when the statement of the first refers to an object that only the second supplies. Within one question, the relation holds between conditions only. The table names each condition on which a condition depends in bold, and qualifies a dependency that holds on one route only. ^condition-dependencies

| Condition | Depends on |
| --- | --- |
| Definiteness | nothing: a term of a candidate exists once the candidate is proposed, and the proposal is a fact, not a condition |
| Answer type | **definiteness** of the terms of the explanandum, of the contrast and of the conditions held fixed |
| Soundness | for the topic presupposition, **definiteness** of its terms; for the existence presupposition, also the components of the **answer type** that fix the type of result that it names |
| Candidates | under selection, the components of the **answer type** that the admissibility tests read |
| Discrimination | under selection, the **candidates**, which supply the admissible candidates |
| Access | under selection, **discrimination**, which names the quantity; under construction, the **answer type** and **definiteness** of the terms of the explanandum |
| Bridging | **access**, since a measurement model refers to the procedure that obtains the quantity; the **answer type**, which fixes the proof obligations; under selection, also **discrimination** |
| Representation | **access**, which fixes the model on which the quantity is obtained; the **answer type**, which fixes the required accuracy and the reference class |

The definiteness of the terms of a candidate is part of the admissibility of that candidate, so it lies inside the condition of candidates rather than among its dependencies. Within one question, the relation has no cycle. The conditions can be listed in an order in which each depends only on conditions listed before it: definiteness, answer type, soundness, candidates, discrimination, access, bridging, representation. Therefore, when no condition of a route is refuted, a condition that is minimal among the conditions in the state `not established` depends only on conditions in the state `established`.

- **Across questions, two kinds of dependency arise.** First, the link `presupposes` between [linked questions](../../objects/question/question.md#^linked-questions) states that one question has a true direct answer only if another has a true direct answer, so the soundness of the first depends on the soundness of the second. Second, a condition of one question can depend on an answer to another question. Such a dependency is met by an accepted answer or by a provisional answer.
- **A provisional answer is adopted explicitly.** A provisional answer is an answer of the other question that the researcher adopts for the dependency, and the record of the dependency names the adopted answer. Every result that rests on the dependency stays conditional on that answer, and a revision of the answer withdraws the results that rest on it. Two dependencies in opposite directions form a cycle, which is resolved by iteration, as the note on [question decomposition](../../processes/inquiry/question-decomposition.md#^cycles) states. A provisional answer lets that iteration start, under the conditions of [controlled iteration](../../processes/inquiry/specification-order.md#^controlled-iteration).
- **A test that uses its own candidate is not a cycle between conditions.** When a measurement presupposes the theory that it tests, the theory is a candidate of the same question, and the bridging inference uses it. The condition of [tests that can fail](../../processes/inquiry/specification-order.md#^iteration-circularity) of controlled iteration decides whether such a test supports the candidate.
- **Soundness constrains the interrogative moves that serve one question.** In the interrogative model of inquiry, a question put to a source may be asked only once its presupposition is established [hintikka2007]. The model separates interrogative moves, which obtain an answer from a source outside the premises of the inquiry, from deductive moves, which draw consequences from those premises. Therefore, an observation, a measurement, an intervention or the consultation of a source that obtains an answer to a question requires the presuppositions of *that* question. The observation that establishes the soundness of a question answers another question, whether the presupposed effect occurs, and requires only the presuppositions of that other question. A derivation is a deductive move, and proposing candidates asks nothing, so neither requires soundness. This application of the rule to the acts of an inquiry is a reading adopted by this method.
- **A question needs identified slots.** The conditions apply to a question, and a question names each referent at the level `identified` at least, as the note on [problems and questions](../../objects/question/question.md#^commitment-levels) states. A question schema first needs its slots identified.
- **A question can be posed before it is sound.** The [minimal problem](../../objects/problem/epistemic-problem.md#^minimal-problem) of an inquiring question exists as soon as its answer is lacking. The minimal problem has an epistemic gap once the existence presupposition is in the accepted knowledge $K$, and the topic presupposition may also remain to be established.

## Relation to the obstacle of a problem

The two axes of the [types of problem](../../objects/problem/problem-types.md) read the obstacle of a problem in terms of these conditions and of the set $H$ of proposed candidates, for the associated question $Q_\pi$. The conditions divide between the two axes as follows: ^obstacle-axes

- the value *unsound presupposition* of axis A is soundness refuted outright; soundness refuted for lack of means leaves the problem standing, with its presupposition still to be established;
- the value *ill-defined terms* is definiteness in the state `not established` for an explicandum of the demand;
- the values *open gap* and *unassessed candidates* record whether $H$ holds a candidate, and whether none is accepted; they record the occupancy of $H$, not the condition of candidates, which also requires admissibility;
- the values *conflict* and *unwarranted claim* describe the accepted knowledge $K$, not a condition of $Q_\pi$;
- the values of axis B are definiteness without an adequate criterion, an answer type that no answer can meet, and discrimination, access, bridging or representation, each refuted outright or for lack of means. The condition of candidates is not refuted on its own: when the question presupposes that its candidates are complete and all are eliminated, soundness is refuted.

Each condition of axis B can be refuted under any value of axis A, with two exceptions. An unsound presupposition ends the problem, so no condition of answerability applies to it. Under selection, discrimination, access, bridging and representation all [depend](#^condition-dependencies), directly or through other conditions, on admissible candidates. Therefore, when no admissible candidate exists, none of them can be refuted along selection, and only access, bridging and representation can be refuted, along the route of construction.

## Necessity and joint sufficiency

Each condition of a route is **necessary** for that route, in one of two senses. When definiteness, the answer type, the candidates, discrimination, access or bridging fails, the route cannot obtain an admissible answer. When soundness or representation fails, the route can still obtain an admissible answer. When soundness fails, every direct answer is false, since each entails the presuppositions of the question, and only a partial or a corrective answer can still be true. When representation fails, the answer rests on a model that does not represent the target to the required accuracy. Therefore, soundness is necessary for a true direct answer, and representation for a warrant that rests on no failed condition. A [satisfying answer](question.md#^answer-sets) can still be obtained when one of them fails, since the warrant tests read these two conditions only in part, as the notes on soundness and on representation above state. The conditions of one route are meant to be **jointly sufficient** for obtaining an answer: once all hold, the acts that exercise access can run, and the bridging inference turns the value obtained into an answer, which the evaluation then judges. A combination step still has to compose that answer, and a check has to confirm that the combination is valid. The note on [question decomposition](../../processes/inquiry/question-decomposition.md#^synthesis) states what a combination that yields no answer reveals. ^sufficiency

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); a question may be asked only once its presupposition is established, and the distinction between interrogative and deductive moves
