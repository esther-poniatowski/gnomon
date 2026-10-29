---
role: definition
status: revision
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Conditions of answerability
  - Answerability
  - Route to an answer
tags: []
source:
---
# Conditions of answerability

> [!QUESTION] Goal: which conditions must hold for an answer to a question to be obtained and justified, and how do these conditions depend on each other?

A question is **answerable** at a given time when an admissible answer can be obtained and justified with the means available at that time. Every answer must meet five requirements:

- the question is sound;
- the space of admissible answers is delimited;
- one answer is obtained;
- the answer is justified;
- the answer holds of the target.

The [question-decomposition framework](../../methods-reasoning/question-decomposition-framework.md) splits these requirements into seven conditions, as its own proposal rather than as a result of one source: soundness, conceptual definiteness, answer space, discrimination, access, bridging and scope. This note splits its answer space into two conditions, the type of the admissible answers and the admissible candidates proposed within that type, so it counts eight conditions. The present note is the canonical statement of the conditions. Its tables are checked against a [model of the conditions](../../../tests/test_gnomon/answerability_model.yml), whose quotations of the vault are themselves checked by a [test](../../../tests/test_gnomon/test_answerability_model.py).

## Two routes to an answer

An answer is reached along one of two routes: ^routes

- **Selection.** Candidates are proposed, a quantity takes different values under them, and the value obtained selects one candidate. *Example*: two rival accounts of gamma oscillations, separated by the effect of blocking the excitatory input to the interneurons.
- **Construction.** A procedure is named that would yield a direct answer once it is developed or run, and no rival candidates need to be separated. *Example*: an algorithm that enumerates the fixed points of a network at each gain.

A construction route is compatible with an [epistemic gap](epistemic-problem.md#^gap). The gap holds while no direct answer has been obtained and accepted. A procedure that has not been run has obtained no answer, and a result obtained but not yet assessed is a proposed candidate. Access along this route holds when a procedure of the available means applies to the demanded result, which means that the procedure is designed for that result and that its inputs exist. Establishing access therefore does not close the gap.

The conditions of one route are jointly necessary. Alternatives arise at two levels: between the two routes, and between procedures that meet one condition, such as an analytic derivation and a simulation that both give access to a quantity. The question-decomposition framework records such alternatives as disjunctive nodes of a decomposition.

## The eight conditions

Each condition is stated for one question. The last column names the corresponding types of the [question-hierarchy framework](../../methods-reasoning/question-hierarchy-framework.md), which divides the same ground differently. ^eight-conditions

| Condition | Holds when | Route | Typical serving question | Question-hierarchy framework |
| --- | --- | --- | --- | --- |
| Definiteness of a term | the term has a definition or an operational criterion adequate to its use | both | what counts as a disentangled representation, and how is it measured? | conceptual; formal, for a term |
| Soundness | the presuppositions of the question are true: existence, uniqueness, reality of an effect | both | does the phenomenon occur robustly? | — |
| Answer type | the type of the admissible answers is fixed: the components of the [epistemic task](../epistemic-task.md), the grain of the explanandum, the extent over the reference class and the domain, and the contrast | both | at which grain, over which class, and to which accuracy must the answer hold? | formal, for a class of models |
| Candidates | at least one proposed candidate is admissible | selection | which mechanisms could produce the effect? | — |
| Discrimination | a quantity with an operational criterion takes different values under the admissible candidates | selection | which observable separates mechanism A from mechanism B? | identifiability; evidential, for consequences that differ |
| Access | a procedure of the available means applies to the quantity: the discriminating quantity under selection, the demanded result under construction | both | how can the observable be computed or measured? | evidential; feasibility |
| Bridging | an inference links the quantity to the answer, at the standard of warrant that the answer type fixes: an auxiliary hypothesis, a measurement model, a lemma | both | does the observable index the property under the assumptions made? | interpretability |
| Scope | the answer obtained on the model studied holds of the target | both, when access uses a model of the target | does the result for the linear model hold for the nonlinear network? | — |

- **Definiteness holds term by term.** A term can be definite while another term of the same question is not. For a slot of a question, the level `specified` of the [levels of commitment](problem-and-question.md#^commitment-levels) is necessary for definiteness: it writes the formal declarations of the slot. Whether these declarations are adequate to their use is judged separately. The level `identified` fixes the referent of the slot without a criterion.
- **The explicandum of a question of explication is not a slot.** A question that asks which criterion should define a term demands the definiteness of that term as its answer. The explicandum enters the question through its anchored use, as an explicandum of the [problem record](../problem.md) does, not as a typed slot. Therefore, definiteness of that term is not a condition of the question, and a dependency on it is void.
- **The answer type includes the standard of warrant.** The epistemic task fixes the admissible explanans, the required accuracy and the proof obligations of the answer. The required accuracy and the proof obligations state the warrant that the answer requires, so bridging reaches the standard that the answer type fixes.
- **A candidate is admissible when it passes the admissibility tests.** The [conditions of satisfaction](../satisfaction-conditions.md) state these tests. Their clauses check three things: that the candidate has the answer type, that its terms are definite, and that its structure is complete and consistent with the declared system. A question whose candidates all fail these tests has its condition of candidates not established.

Each clause of the tests bears on one condition, as the following table states. A test whose clauses bear on two conditions lists both. ^tests-to-conditions

| Test | Level | Conditions |
| --- | --- | --- |
| Scope | admissibility | **answer type**, for the extent of the claim and of its laws |
| Grain | admissibility | **answer type**, for the resolution; **definiteness**, for the explanandum defined over the units of the answer |
| Contrast | admissibility | **answer type** |
| Relation | admissibility | **answer type**, for the kind of relation; **candidates**, for each factor reaching its effect through named laws |
| Individuation | admissibility | **definiteness**, for each bearer declared or expressed; **candidates**, for the agreement with the declared system |
| Admissible explanans | admissibility | **definiteness**, for each quantity declared or expressed and each aggregate with a defined effect; **answer type**, for the bound of the task |
| Modal strength | admissibility | **answer type**, for the strength claimed; **scope**, for its realization in the target |
| Product | admissibility | **answer type** |
| Phenomenon established | warrant | **soundness** |
| Foil evidence | warrant | **access**, for the data on the foil |
| Law warrant | warrant | **bridging** |
| Closure | warrant | **bridging** |
| Fidelity | warrant | **scope** |
| Robustness | warrant | **scope** |
| Selection | warrant | **scope** |

## States of a condition

At a given time, a condition is in one of three states: ^condition-states

- **established**, when the records or the cited literature show that it holds;
- **not established**, when nothing yet shows whether it holds;
- **refuted**, when the records or the literature show that it fails.

A refutation rests either on an argument or on the means tried:

- **Refuted outright.** An argument of impossibility shows that the condition fails, such as a proof that two candidates are not identifiable from the observables.
- **Refuted for lack of means.** The record names a finite set of means considered, drawn from the available means, and every member of that set has been tried and has failed. A member not yet tried keeps the condition not established. Such a refutation holds relative to the means considered at its time, so the condition can be established later, once a new instrument, data set, algorithm or proof technique exists. The question-decomposition framework states this relativity as its amendment on termination.

## Dependencies between the conditions

A condition **depends on** another condition when the statement of the first refers to an object that only the second supplies. Within one question, the relation holds between conditions only, and the table names each condition on which a condition depends in bold. ^condition-dependencies

| Condition | Depends on |
| --- | --- |
| Definiteness | nothing: a term of a candidate exists once the candidate is proposed, and the proposal is a fact, not a condition |
| Soundness | **definiteness** of the terms of the presupposition, and of the terms of the proposed candidates when the presupposition states that they are complete |
| Answer type | **definiteness** of the terms of the explanandum, of the contrast and of the domain |
| Candidates | the **answer type**, since admissibility tests a candidate against it; **definiteness** of the terms of at least one candidate |
| Discrimination | the **candidates**, which supply the admissible candidates |
| Access | under selection, **discrimination**, which names the quantity; under construction, the **answer type** and **definiteness** of the terms of the explanandum |
| Bridging | **access**, since a measurement model refers to the procedure that obtains the quantity; the **answer type**, which fixes the standard of warrant; under selection, also **discrimination** |
| Scope | **access**, which fixes the model on which the quantity is obtained; the **answer type**, whose required accuracy the match with the target must reach |

Within one question, the relation has no cycle. The conditions can be listed in an order in which each depends only on conditions listed before it: definiteness, soundness, answer type, candidates, discrimination, access, bridging, scope. Therefore, when no condition of the question is refuted, a condition that is minimal among the conditions not established depends only on established conditions.

- **Across questions, a dependency can be met provisionally.** A condition of one question can depend on an answer to another question. The link `presupposes` between [linked questions](problem-and-question.md#^linked-questions) records the commonest such dependency: the first question has a true answer only if the second has one, so the soundness of the first depends on an answer to the second. Such a dependency is met by an accepted answer, or by a provisional answer, in which case every result that rests on it stays conditional on that answer. Two dependencies in opposite directions form a cycle, which the question-decomposition framework resolves by iteration, in its amendment on termination. A provisional answer lets the iteration start, under the conditions of [controlled iteration](../specification-order.md#^controlled-iteration).
- **A test that uses its own candidate is not a cycle between conditions.** When a measurement presupposes the theory that it tests, the theory is a candidate of the same question, and the bridging inference uses it. The condition of [tests that can fail](../specification-order.md#^iteration-circularity) of controlled iteration decides whether such a test supports the candidate.
- **Soundness constrains the interrogative moves that serve one question.** In the interrogative model of inquiry, a question put to a source may be asked only once its presupposition is established [hintikka2007]. The model separates interrogative moves, which obtain an answer from a source outside the background, from deductive moves, which draw consequences from the background. Therefore, an observation, a measurement, an intervention or the consultation of a source that obtains an answer to a question requires the presupposition of *that* question. The observation that establishes the soundness of a question answers another question, whether the presupposed effect occurs, and requires only the presupposition of that other question. A derivation is a deductive move, and proposing candidates asks nothing, so neither requires soundness. This application of the rule to the acts of an inquiry is a reading adopted by this method.
- **A question needs identified slots.** The conditions apply to a question, and a question names each referent at the level `identified` at least, as the note on [problems and questions](problem-and-question.md#^commitment-levels) states. A question schema first needs its slots identified.
- **A question can be posed before it is sound.** The associated question $Q_\pi$ of a problem presupposes that a result of the demanded type exists, and the background $K$ establishes that presupposition when it evokes the question, as the [epistemic gap](epistemic-problem.md#^gap) states. The [minimal problem](epistemic-problem.md#^minimal-problem) of any inquiring question states that its answer is lacking, while its presupposition may still be unestablished.

## Relation to the obstacle of a problem

The two axes of the [types of problem](problem-types.md) read the obstacle of a problem in terms of these conditions and of the set $H$ of proposed candidates, for the associated question $Q_\pi$:

- the value *unsound presupposition* of axis A is the state refuted of soundness;
- the value *ill-defined terms* is definiteness not established for an explicandum of the demand;
- the values *open gap* and *unassessed candidates* record whether $H$ holds a candidate, and whether none is accepted; they record the occupancy of $H$, not the condition of candidates, which also requires admissibility;
- the values *conflict* and *unwarranted claim* describe the background $K$, not a condition of $Q_\pi$;
- the values of axis B are the conditions other than soundness in the state refuted: definiteness without an adequate criterion, an answer type that no answer can meet, and discrimination, access, bridging or scope refuted outright or for lack of means.

## Necessity and joint sufficiency

Each condition is **necessary**: when it fails, no admissible answer can be obtained and justified. The conditions of one route are meant to be **jointly sufficient**: once all hold, an answer justified at the required standard follows from the value obtained and the bridging inference. A combination step still has to compose that answer, and a check has to confirm that the combination is valid. When the conditions are met and no justified answer follows, a condition is missing, most often a bridging assumption, as the question-decomposition framework states in its amendment on analysis and synthesis.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); a question may be asked only once its presupposition is established, and the distinction between interrogative and deductive moves
