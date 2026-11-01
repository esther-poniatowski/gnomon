---
tags:
  - theory
  - wip
index: "[Problem](docs/epistemology/objects/problem/_index.md)"
aliases:
  - Types of problem
  - Obstacle of a problem
  - Demand of a problem
---
# Types of epistemic problem

> [!QUESTION] Goal: why is the demand of a problem unmet, and which aims, question forms and answer forms does the demand admit?

An [epistemic problem](epistemic-problem.md) $\pi=\langle K,d,\Phi\rangle$ is classified in two ways:

- by its **obstacle**: the reason why the accepted knowledge $K$ does not yet meet the demand;
- by its **demand**: the type of result sought; this type fixes the admissible aims, question forms and answer forms.

## Diagnosis of the obstacle

The obstacle is not a fourth component of the problem. The obstacle is *diagnosed* from the accepted knowledge $K$, from the [proposed candidates](epistemic-problem.md#^candidates) $H$, and from the [associated question](epistemic-problem.md#^associated-question) $Q_\pi$. A problem can carry several obstacles at once, so the diagnosis is a set of values, each with pointers to the records or publications that establish it. The diagnosis runs along two axes. The two axes record different facts, so their values combine, within the exceptions that the [division of the conditions between the two axes](../question/conditions-of-answerability.md#^obstacle-axes) states.

### Axis A: the state of the knowledge about the associated question

| Value | Condition | In words | Example | Source |
| --- | --- | --- | --- | --- |
| Open gap | the problem exists, and $H$ is empty | a result is lacking, and none is proposed | the number of fixed points of a class of recurrent networks at each gain, when the admitted dynamics guarantee that fixed points exist | [wisniewski1995] |
| Unassessed candidates | the problem exists, and $H$ holds one or several candidates, none accepted | answers are proposed, and none is selected | two candidate mechanisms of gamma oscillations, which current experiments do not discriminate: interneurons alone, or the loop between pyramidal cells and interneurons | [tiesinga2009] |
| Conflict | $K$ holds two claims that are inconsistent together, or a datum not yet accepted is improbable under $K$ | accepted claims clash, or a datum surprises | overparameterized networks generalize, while their capacity to memorize random labels predicts that they need not | [laudan1977]; [zhang2017] |
| Unwarranted claim | $K$ holds a claim whose support is weaker than the demand requires | a result is held without the warrant asked for | a scaling law of the delay of generalization, fitted on small networks, while the demand asks for a derivation | — |
| Ill-defined terms | an explicandum of the demand has no exact criterion, so the direct answers of $Q_\pi$ are fixed only through the anchored use of the term, and no candidate can be checked against them | the question has answers, but a term lacks the criterion needed to check them | "are the representations of mixtures compositional?", before "compositional" has a criterion | [simon1973_ill] |
| Unsound presupposition | $K$ holds the negation of a presupposition of $Q_\pi$ | the result sought does not exist | an account of the delay of generalization, once the delay is shown to exist only in a thresholded accuracy | [wisniewski1995] |

- **Evocation is recorded apart.** The values *open gap* and *unassessed candidates* require only that the [problem exists](epistemic-problem.md#^problem-existence). Whether $K$ also evokes $Q_\pi$, so that the problem has an [epistemic gap](epistemic-problem.md#^gap), is the existence part of soundness among the [conditions of answerability](../question/conditions-of-answerability.md), recorded with its own state. The value named *open gap* therefore does not imply an epistemic gap.
- **The values are not exclusive.** *Example*: "characterize the geometry of the fixed points as the input mixture varies" carries an open gap and ill-defined terms, until "geometry" has a criterion.
- **An unsound presupposition ends the problem.** The problem is dissolved, as the [outcomes of a problem](epistemic-problem.md#^problem-outcomes) state. The value requires an outright refutation, in which $K$ holds the negation of a presupposition of $Q_\pi$. A presupposition that the means considered have failed to establish is not unsound: it stays to be established, and the problem stands.
- **Laudan's anomaly is comparative.** An anomalous problem, in Laudan's sense, is an empirical problem that a theory has not solved and that a rival theory has solved [laudan1977]. A mismatch between a model and data is a conflict, and the mismatch becomes an anomaly only when a rival account removes it.

### Axis B: the unmet conditions of answerability

The second axis records which **condition of answerability** of $Q_\pi$ is refuted. A condition of answerability is a condition that must hold before an answer can be obtained, such as the definiteness of a term, access to a quantity, or a bridging inference from that quantity to the answer. The [conditions of answerability](../question/conditions-of-answerability.md) are defined, with their states and their dependencies, after the notes on the question. The values of axis B are the conditions that can be refuted: definiteness without an adequate criterion, an answer type that no answer can meet, and discrimination, access, bridging and representation. The [division of the conditions between the two axes](../question/conditions-of-answerability.md#^obstacle-axes) states which conditions axis A records instead, and the values of axis A under which each value of axis B can occur.

- **Axis B records refuted conditions only.** A condition not yet established is not an obstacle on axis B: discrimination is not established for any problem whose candidates have just been proposed. A condition is refuted outright, by an argument of impossibility, or for lack of means, when every means considered has been tried and has failed, as the [states of a condition](../question/conditions-of-answerability.md#^condition-states) define.
- **A lack of means falls on axis B.** When every means considered fails to meet a condition, that condition is refuted for lack of means. Access fails when no instrument, data set, algorithm or proof technique considered yields the quantity. Discrimination fails when no quantity considered separates the candidates from their alternatives. Bridging and representation fail in the same way, when no auxiliary hypothesis considered holds, or when no model considered represents the target to the required accuracy.
- *Example*: the number of fixed points is an open gap. Suppose, in addition, that no algorithm enumerates the fixed points of a network of a thousand units within the available computing time. In that case, the condition of access fails as well.

## Classification by demand

The type of result of the demand fixes the admissible [aims](../task/epistemic-aim.md), the interrogative form of the questions that serve the problem, and the form of their answers. Each row names a [product type](../../processes/activities/epistemic-activities.md#^product-types). The request of the demand fixes the number and the completeness of the answers.

| Type of result | Admissible aims | Question form (request) | Answer form | Example |
| --- | --- | --- | --- | --- |
| `phenomenon`, not yet stated | exploration | which patterns appear as the conditions vary (`over-a-parameter`) | a phenomenon record with its detection criterion | which collective states appear as the noise level varies |
| `phenomenon`, already named | description | which features does the phenomenon have (`all`, `over-a-parameter`) | the values of its observables | the dimension of the population activity during a task |
| `consequence` | model knowledge; modal knowledge, when the background of the target is closed (its admitted laws define the system completely, so every truth about it follows from them) | whether a statement holds of a model (to prove); which object satisfies a condition (to find); whether a property can or must hold | a derived law, a proof, a proof of existence, a counterexample, or a proof of impossibility | whether the fixed point of a rate network is unique below a critical gain |
| `target-claim`: a claim about the target, as opposed to a consequence, which holds of a model | prediction; modal knowledge, when the background of the target is not closed | which outcome occurs in the target when a condition changes; whether a property can or must hold in the target | a predicted value with its uncertainty, compared with the observed outputs; an instance of the target that exhibits the property | the change of the firing rate when the input contrast doubles; whether a network without inhibitory neurons can oscillate at gamma frequency |
| `model` | description; explanation, at modal strength `possible` | which model of a class reproduces the phenomenon (`one`) | a model record | which rate model reproduces the measured tuning curves |
| `explanation` | explanation | why the phenomenon holds rather than its contrast; how the system produces it | an answer that holds the [block of an explanation](../answer/answer-form.md#^explanation-block), resting on a model when its route runs on one | why the network oscillates rather than stays asynchronous |
| `classification` | exploration; description | which kinds or regimes exist (`all`) | a partition with its criteria | which dynamical regimes divide the parameter space of a network |
| `concept` or `measurement-procedure` | none: an explication | which criterion should define the explicandum | an explicatum with its criteria of adequacy | the criterion of a compositional representation |
| `knowledge-state-change` | none: a revision | which accepted claim to withdraw | the revised status of the records concerned | which of two clashing claims to withdraw |
| `inter-theory-relation` | none: an integration | how two accounts of one phenomenon relate | a relation between theories (no record yet) | how two accounts of training relate: the mean-field account, which replaces the interactions of each unit by their average, and the kernel account, in which training at infinite width is governed by a fixed kernel |

### Clarifications

- **An explicatum is not judged true or false.** An explication is judged by its similarity to the explicandum, its exactness, its fruitfulness and its simplicity [carnap1950_logical]. Therefore, a demand for a concept calls for criteria of adequacy, not for a test of truth.
- **A decision is a request, not the type of result of a demand.** A demand with the request `decision` asks for a decision on candidates already proposed. The type of result stays the type of those candidates, and each question that serves the demand keeps the aim of that type. The [evaluation activities](../../processes/activities/evaluation.md) produce the decision.
- **Not every why-question asks for an explanation.** A why-question can ask for the reasons to believe a claim [hempel1965]. Such an answer is a justification, and a justification falls under the request `decision`.
- **How-possibly and how-actually are modal strengths, not question forms.** A how-question takes either strength, as the [modal strength](../task/modal-strength.md) of the task states. A how-question can also ask for a prediction ("how does the rate change when the contrast doubles?").
- **A prediction concerns the target, and a consequence concerns a model.** A consequence holds of a model, and it may fail of the target. A prediction claims an outcome of the target, so it is compared with observed outputs.
- **One question can fall under several types.** *Example*: "does the fixed point of a rate network remain unique when the gain exceeds one?" can ask for two types of result:
  - a consequence: a proof for a formally defined class of networks;
  - a hypothesis: a prediction for a given network of the target.

  The [closure of the admitted laws](../knowledge/background.md#^laws) selects between the two types. When the laws define the system, the target is a formal class, and a formal class admits a consequence. A candidate answer already proposed changes the request to `decision`.

## Questions generated by each obstacle

The demand of a problem, its request included, is a given of the problem, and the obstacle is diagnosed relative to that demand. Each obstacle generates the questions that serve the problem: ^obstacle-questions

| Obstacle (axis A) | Question generated | Demand of that question |
| --- | --- | --- |
| Open gap | none: the associated question $Q_\pi$ itself | — |
| Unassessed candidates | whether each proposed candidate meets the demand | the request `decision`, on the type of the candidates |
| Conflict | which of the clashing claims to withdraw, or why a claim holds despite an expectation drawn from another claim | a change of accepted claims, or an explanation |
| Unwarranted claim | whether the claim holds at the warrant that the demand requires | the request `decision`, on the type of the claim |
| Ill-defined terms | which criterion should define the explicandum | a concept or a measurement procedure |
| Unsound presupposition | none: the problem is dissolved | — |

- **Several obstacles generate several questions.** The values of axis A are not exclusive, so a problem can carry several obstacles, and each obstacle adds its own questions. *Example*: an open gap together with ill-defined terms generates one question of explication beside $Q_\pi$.
- **A problem can carry such a demand from the start.** A problem whose demand is a verdict, or a concept, states that demand in its own record, and its associated question is then the question of the table.

## Relations to the method

- **The type of the demand bounds the aim of each question.** The table of the types of result admits, for each type, the aims whose direct answers can supply that result, so a question that serves the problem takes one of those aims.

The fields by which a record states a problem, and the aim of a question that serves it, are documented in the [problem record](../../../specification/problem.md) and in the [epistemic task of a question](../../../specification/question-task.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [hempel1965] ◐ [Hempel, *Aspects of Scientific Explanation and Other Essays in the Philosophy of Science*, Free Press, 1965](https://swisscollections.ch/Record/991016796259705501); explanation-seeking and reason-seeking why-questions
- [laudan1977] ◐ [Laudan, *Progress and Its Problems: Towards a Theory of Scientific Growth*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper); ch. 1–2; anomalous problems as empirical problems solved by a rival theory, and conceptual problems, checked through secondary sources
- [simon1973_ill] ○ Simon, "The structure of ill structured problems", *Artificial Intelligence* 4, 181–201, 1973
- [tiesinga2009] ◐ [Tiesinga & Sejnowski, "Cortical enlightenment: are attentional gamma oscillations driven by ING or PING?", *Neuron* 63(6), 727–732, 2009](https://doi.org/10.1016/j.neuron.2009.09.009)
- [wisniewski1995] ◐ [Wiśniewski, *The Posing of Questions: Logical Foundations of Erotetic Inferences*, Kluwer, 1995](https://doi.org/10.1007/978-94-015-8406-7), ch. 5; evocation and the soundness of a question, checked through [Wiśniewski, "Erotetic logic and explanation by abnormic hypotheses"](https://www.bu.edu/wcp/Papers/Logi/LogiWisn.htm)
- [zhang2017] ◐ [Zhang, Bengio, Hardt, Recht & Vinyals, "Understanding deep learning requires rethinking generalization", *International Conference on Learning Representations*, 2017](https://arxiv.org/abs/1611.03530)
