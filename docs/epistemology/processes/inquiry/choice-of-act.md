---
tags:
  - theory
  - wip
index: "[Course of an inquiry](docs/epistemology/processes/inquiry/_index.md)"
aliases:
  - Choice of the next act
  - Open condition
  - Readiness of an act
  - Ranking of acts
---
# Choice of the next act

> [!QUESTION] Goal: given the state of an inquiry, which acts of research can come next, and on which grounds is one of them chosen?

An act of research is chosen relative to the [state of an inquiry](../../foundations/inquiry-and-state.md#^state): its accepted knowledge $K$, its proposed candidates $H$ and its open questions, each item with its statuses. Four criteria narrow the acts that can come next:

1. an act addresses a condition of answerability that is open or refuted;
2. an act is ready when its inputs exist and are unimpeached;
3. the ready acts are ranked by stated criteria;
4. the choices that no criterion settles are left to the researcher.

Choosing an act that reduces the difference between the present state and the solution of the problem is an instance of means–ends analysis [newell1972]. The criteria and their combination are a proposal of this method, and the sources cited supply their parts. The [procedure for choosing the next act](../../../procedures/inquiry/next-act.md) applies these criteria to the records, and maps each condition to the activities that act on it.

## An act addresses an open or a refuted condition

The acts that can come next are read off the [conditions of answerability](../../objects/question/conditions-of-answerability.md) of the questions under diagnosis: an open condition calls for an act that can establish it, and a refuted condition calls for a revision.

### Open condition

A condition is **open** when it is in the state `not established` and every condition on which it [depends](../../objects/question/conditions-of-answerability.md#^condition-dependencies) is in the state `established`. A dependency on another question is met as the conditions of answerability state: through the soundness of the other question, for the link `presupposes`, and otherwise through an accepted or a provisional answer. ^open-condition

- **The diagnosis does not stall on the order.** Within one question, the dependencies have no cycle. Therefore, when no condition of a route is refuted, either all its conditions are in the state `established` or at least one is open. Across questions, a condition can wait on another question, which then joins the questions under diagnosis. A cycle of such waits is broken by adopting a provisional answer. In particular, the condition of candidates is open as soon as the answer type is in the state `established`, even when no candidate has been proposed.
- **An open condition can become a question.** The new question asks for the object that the condition lacks, such as a procedure of measurement, and it is linked to the question that it serves by `enables`, among the [links between questions](../../objects/question/question.md#^linked-questions). Its answers do not narrow the answers of the served question, so it does not serve the problem in the sense of erotetic implication, and the activity `question-decomposition`, whose norm requires erotetic implication, does not produce it. The note on [question decomposition](question-decomposition.md#^serving-sources) states this move as the first source of serving questions. ^condition-to-question
- **A slot is specified on demand.** A slot is raised to the level `identified` when the question is posed, since a question names each referent. A slot is raised to the level `specified` only when an open condition needs the definiteness of its term: the answer type, soundness, or access along the route of construction. The condition of candidates can also require specified slots, since its admissibility tests read declared constituents and quantities, as the [conditions of answerability](../../objects/question/conditions-of-answerability.md#^eight-conditions) state. Deferring each specification until a condition requires it is the device of least commitment [weld1994], which the [order of specification](specification-order.md) adopts. ^specified-on-demand

### Refuted condition

A refuted condition calls for a revision, and the researcher chooses among the revisions of its row. ^refuted-condition

| Refuted condition | Revisions |
| --- | --- |
| Soundness of the associated question $Q_\pi$ | refuted outright: the problem is dissolved, as the [outcomes of a problem](../../objects/problem/epistemic-problem.md#^problem-outcomes) state; refuted for lack of means: the presupposition becomes a question linked to $Q_\pi$ by `enables`, and the problem stands |
| Soundness of a generated question | the generated question is revised, or abandoned while the problem stands |
| Definiteness, when no adequate criterion exists | the term is sharpened when it is vague, replaced by a concept that separates the situations which it conflated, or abandoned when its extension is empty |
| Answer type, when no answer can meet it | the epistemic task is revised, for instance by a weaker modal strength or a coarser accuracy |
| Discrimination | the contrast of the question, or the conditions that it holds fixed, are narrowed; its resolution is coarsened so that the inseparable candidates form one answer; or the development of a new quantity or instrument becomes a question |
| Access | the other route is taken, or the development of a procedure becomes a question |
| Bridging | another quantity is chosen, or the missing auxiliary hypothesis becomes a question |
| Representation | the reference class of the question, or the conditions that it holds fixed, are restricted; access is moved to a model that represents the target, or to the target description with no stand-in; or a new version of the binding is committed, under the [rule on revised bindings](../../../specification/binding.md#^binding-version) |

The condition of candidates has no row. When all candidates fail the admissibility tests or are eliminated, the condition is in the state `not established`, and the acts that address it are those of an open condition. When the question presupposed that its candidates were complete, the elimination of all of them refutes that presupposition, and the row of soundness applies.

A revision of a question takes one of the three forms that the note on [question decomposition](question-decomposition.md#^global-revision) names: disambiguation, restriction of scope, and replacement of a concept. After any revision that changes a question under diagnosis, the diagnosis restarts. Apart from any refutation, the main question is also re-examined at intervals, to find whether it needs one of these three revisions.

## Readiness of an act

An **act instance** is an activity whose inputs are assigned to records, to the outputs of earlier steps, or, for a `source`, to pointers. The condition served by the instance guides the assignment. An act instance is **ready** when its inputs exist and are **unimpeached**: no step upstream of them failed its norm. ^ready-act

- **An input must exist.** When an input does not exist, the search proceeds backward through the activity types: the missing input becomes a subgoal, and the activities that produce it are examined in turn.
- **An input must be unimpeached.** A record is impeached when a step of the itinerary that produced it failed its norm, or when such a step took as input an impeached record. Therefore, impeachment propagates from producer to consumer along the steps of the itinerary, whatever the output types of the steps. Impeachment differs from the warrant of a law and from the warrant tests of an assessment, since it reads only the verdicts of the norms of the steps. An act that uses an impeached record inherits the failure, so the repair of the failed step becomes a subgoal, ranked before the act. A pending verdict propagates in the same way, and the result of an act that rests on it stays conditional on it.
- **A pending norm stays to be judged.** When the record produced by a step is stabilized while the verdict of the step is pending, the norm of the step remains to be judged, and the record is treated as the product of a pending step until then.
- **The necessity of a subgoal is read over itineraries.** A missing input is necessary for the goal when every itinerary that reaches the goal contains an act instance that requires it. A particular act that produces that input is necessary only when, in addition, no other activity produces the input. Even a necessary subgoal does not reach the goal, since the remaining steps are activities whose norms can fail. The problem reduces to the problem of producing that input only when the remaining steps form a recorded, uniform method, as the definition of [reduction](../../objects/problem/epistemic-problem.md#^reduction) requires. Hierarchical task-network planning decomposes a task by methods that replace it with subtasks [erol1994]. Erotetic search scenarios start from a principal question and lead, through auxiliary questions, to its answers [wisniewski2013].

## Ranking of acts

Before the ranking, each act receives one of three statuses by the [test of relevance](question-decomposition.md#^relevance): necessary, useful or decorative. Decorative acts are removed, and the necessary and useful acts are compared by the first five criteria below. The sixth criterion orders the open conditions of one route, not the acts. ^ranking-criteria

| Criterion | Preferred | Source |
| --- | --- | --- |
| Diagnostic power | the act whose outcome most constrains the admissible answers, by eliminating candidates, refuting an assumption, or forcing a reformulation of the question | [lindley1956]; [chaloner1995] |
| Least favorable outcome | the act whose least favorable plausible outcome eliminates the largest share of the live candidates | [wald1950], with the departure stated below |
| Structural centrality | the act that bears on a load-bearing assumption, concept or mechanism, whose failure would restructure the problem | — |
| Feasibility | the act that the available means, or a simplified setting, allow to complete now, with the higher probability of completion and at the lower cost | this method |
| Strength of warrant | the act that delivers the stronger warrant for the answer | this method |
| Order of tests | among the open conditions of one route, the condition whose test has the lowest ratio of cost to probability of refutation | [unluyurt2025] |

- **A decisive negative result carries the most weight, together with its auxiliary hypotheses.** Confirmation accumulates slowly, whereas one decisive negative result can eliminate a structural hypothesis. Therefore, the criteria of diagnostic power and of the least favorable outcome favor acts designed as potential refutations of an assumption, as Popper's severe tests are [popper1963]. A negative result refutes a candidate only together with the auxiliary hypotheses of the bridging inference, and the refutation may indict these hypotheses instead [duhem1906].
- **Expected information gain measures diagnostic power over candidates.** Lindley measures the information that an experiment provides by the expected reduction of the uncertainty over the parameters or hypotheses [lindley1956]. Bayesian experimental design maximizes an expected utility, and Lindley's information is one choice of that utility [chaloner1995]. The measure is defined over candidates already proposed, so it does not capture the outcome that forces a reformulation.
- **The least favorable outcome departs from Wald's rule.** Wald's minimax rule prefers the act whose worst outcome is best, and it ranges over all states [wald1950]. The criterion ranges over the plausible outcomes only. This restriction is a departure from the rule, adopted so that an implausible outcome does not decide the ranking.
- **The order of tests is a heuristic.** For a series system, where every test must pass, testing in increasing ratio of cost to probability of failure minimizes the expected cost, a result due to Butterworth [unluyurt2025]. The result assumes tests with two outcomes, fixed costs, independent outcomes, and a stop at the first failure. The conditions of a route meet none of these assumptions exactly: an act can leave a condition in the state `not established`, a refutation for lack of means is revisable, and correlated conditions such as discrimination and access are not independent. The dependencies between conditions do not constrain the sort, since the open conditions have no unmet dependency among themselves. Sorting the open conditions by the ratio is therefore a heuristic. This heuristic is analogous to the fail-first principle of search over constraints, which tries first the choice most likely to fail, so that dead ends are found early [haralick1980].
- **Feasibility and the order of tests use different probabilities.** Feasibility uses the probability that an act completes. The order of tests uses the probability that a condition is refuted.
- **The criteria can conflict.** A feasible act can have a low diagnostic power. One rule settles the main conflict: prefer the act that is both highly constraining and reasonably tractable. Beyond that rule, the researcher weighs the criteria, and the first act whose value reaches a level stated in advance can be accepted without a search for the best one, as satisficing allows [simon1956].

Four heuristics propose acts instead of ranking them:

- **Problem solving.** Look at the unknown; find a related problem already solved; solve a part of the problem; specialize or generalize; work backward [polya1945].
- **Positive heuristic.** A research programme plans a sequence of models, from an idealized model to corrected models [lakatos1970]. *Example*: a mean-field limit followed by its finite-size corrections, each step typed by `de-idealization`.
- **Discovery of mechanisms.** Schema instantiation, modular subassembly, forward chaining from the causes, and backward chaining from the effects [craver2013].
- **Strategic rules.** The interrogative model separates its definitory rules, which state the admissible moves, from its strategic rules, which state the good moves [hintikka2007]. A deductive step can establish the presupposition of a question, and thereby allow the interrogative moves that obtain its answer.

## Choices left to the researcher

The criteria above either return a determinate result or present alternatives. The method leaves the following choices to the researcher: ^researcher-choices

- which question stands for the associated question of a problem, when a stated question narrows the demand of the problem;
- the judgments that fix axis A of the [types of problem](../../objects/problem/problem-types.md), such as whether a datum is improbable under the accepted knowledge, or whether the support of an accepted claim is weaker than the demand requires;
- which question a conflict generates;
- whether a candidate whose verdict is negative is withdrawn or revised;
- whether a construction route is named;
- whether a condition is asserted in the state `established` or `refuted`, including the judgment that a definition is adequate to its use;
- the finite set of means considered, which separates a refutation for lack of means from a condition in the state `not established`;
- whether a provisional answer is adopted for a dependency on another question;
- whether an open condition is pursued through the activities that act on it, or turned into a question;
- which revision of a refuted condition is taken, when its row offers several;
- how the inputs of an act are assigned, when several records fit;
- whether an unsupported claim is admitted as a working assumption under the warrant `posited`;
- whether the acts that rest on a verdict are run before the norms of the steps that produced it are judged;
- whether an assessed answer is accepted into the accepted knowledge $K$, an [act of acceptance](../../objects/status/statuses-and-acceptance.md#^acceptance-act) informed by the verdicts, the disposition and the credence of its assessment, never computed from them;
- when the main question is re-examined;
- the weighing of the ranking criteria, beyond the rule that settles their main conflict.

## Dependencies between acts

The dependencies between acts form cycles among types: a concept serves a question, the question selects a model, and the model can revise the concept. These cycles are resolved by iteration, under the conditions of [controlled iteration](specification-order.md#^controlled-iteration). An iteration starts in three places: a refuted condition triggers a revision, a withdrawn record removes the support of the acts that used it, and a provisional answer to another question is later revised. The [register of serving questions](../../../procedures/inquiry/decomposing-a-question.md#^register) tracks withdrawn records by marking each serving question with the resistance hypothesis $\eta$ on which it is conditioned, so that a refuted hypothesis invalidates the serving questions that rest on it.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [chaloner1995] ◐ [Chaloner & Verdinelli, "Bayesian experimental design: a review", *Statistical Science* 10(3), 273–304, 1995](https://doi.org/10.1214/ss/1177009939); expected utility, with Lindley's information as one utility, read in the authors' preprint, §§1.3 and 2.2
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html); strategies of schema instantiation, modular subassembly and forward and backward chaining
- [duhem1906] ◐ Duhem, *La théorie physique : son objet et sa structure*, Chevalier et Rivière, 1906; 2nd ed., Marcel Rivière, 1914, translated as *The Aim and Structure of Physical Theory*, Princeton University Press, 1954; a hypothesis is tested only together with auxiliary hypotheses; p. 187 of the translation, checked through the [SEP entry on underdetermination](https://plato.stanford.edu/entries/scientific-underdetermination/)
- [erol1994] ✓ [Erol, Hendler & Nau, "HTN planning: complexity and expressivity", *Proceedings of the Twelfth National Conference on Artificial Intelligence*, 1123–1128, 1994](https://mlanthology.org/aaai/1994/erol1994aaai-htn/)
- [haralick1980] ◐ [Haralick & Elliott, "Increasing tree search efficiency for constraint satisfaction problems", *Artificial Intelligence* 14(3), 263–313, 1980](https://doi.org/10.1016/0004-3702(80)90051-X); the fail-first principle, read in the abstract and the introduction
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); definitory and strategic rules, p. 19, checked through its quotation in [Hamami, "An inquisitive formalization of interrogative inquiry"](https://projects.illc.uva.nl/inquisitivesemantics/assets/files/papers/Hamami2012_IMI.pdf)
- [lakatos1970] ◐ [Lakatos, "Falsification and the methodology of scientific research programmes", in Lakatos & Musgrave (eds.), *Criticism and the Growth of Knowledge*, Cambridge University Press, 91–196, 1970](https://doi.org/10.1017/CBO9781139171434.009); the positive heuristic
- [lindley1956] ◐ [Lindley, "On a measure of the information provided by an experiment", *Annals of Mathematical Statistics* 27(4), 986–1005, 1956](https://doi.org/10.1214/aoms/1177728069)
- [newell1972] ◐ Newell & Simon, *Human Problem Solving*, Prentice-Hall, 1972; means–ends analysis
- [polya1945] ◐ Pólya, *How to Solve It: A New Aspect of Mathematical Method*, Princeton University Press, 1945
- [popper1963] ◐ Popper, *Conjectures and Refutations: The Growth of Scientific Knowledge*, Routledge & Kegan Paul, 1963; severe tests
- [simon1956] ◐ [Simon, "Rational choice and the structure of the environment", *Psychological Review* 63(2), 129–138, 1956](https://doi.org/10.1037/h0042769); satisficing, p. 129, checked through a quotation
- [unluyurt2025] ◐ [Ünlüyurt, "Sequential testing problem: a follow-up review", *Discrete Applied Mathematics* 377, 356–369, 2025](https://doi.org/10.1016/j.dam.2025.07.039); §3.1 of the [arXiv version](https://arxiv.org/abs/2511.15742) checked in full text: the optimal order for a series system with independent tests (Butterworth, 1972)
- [wald1950] ◐ Wald, *Statistical Decision Functions*, Wiley, 1950; the minimax rule, which minimizes the maximum risk
- [weld1994] ◐ [Weld, "An introduction to least commitment planning", *AI Magazine* 15(4), 27–61, 1994](https://www.cs.uky.edu/~sgware/reading/papers/weld1994introduction.pdf); deferring decisions, p. 34
- [wisniewski2013] ◐ [Wiśniewski, *Questions, Inferences, and Scenarios*, Studies in Logic 46, College Publications, 2013](https://philpapers.org/rec/WINQIA); erotetic search scenarios
