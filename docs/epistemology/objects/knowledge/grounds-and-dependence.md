---
tags:
  - theory
index: "[Knowledge](docs/epistemology/objects/knowledge/_index.md)"
aliases:
  - Grounds and dependence
  - Ground of an answer
  - Propagation of warrant
  - Defeat between answers
---
# Grounds and dependence

> [!QUESTION] Goal: what is a ground of an answer, how do the warrant and the withdrawal of a ground reach the claims that rest on it, and how does the dependence among claims relate to the dependence among questions and among conditions of answerability?

A **ground** of an answer is an item that the derivation or the evidence of its claim uses: a law, a datum, an assumption, an idealization, a condition or a criterion. Every claim has grounds, under every aim of a question, as the [generality of grounds](../answer/answer-form.md#^grounds-are-general) states. The answer states each ground with its **role**, and states how the claim depends on its grounds: by a minimal sufficient set, a sensitivity analysis or a robustness analysis. The [answer record](../../../specification/answer.md#^answer-elements) documents the roles and the forms of dependence. ^ground

## The role of a ground

A role states how the claim uses the ground, and therefore the effect of a failure of the ground on the claim. ^ground-roles

| Role | The claim uses the ground as | A failure of the ground |
| --- | --- | --- |
| `datum` | evidence: a version of recorded or derived data | removes the evidence; the claim keeps only its other grounds |
| `warrant` | a law that licenses the step from the other grounds to the claim | removes the step; the claim no longer follows |
| `assumption` | a premise asserted true of the target | removes the support of every step that uses it |
| `idealization` | a premise known to be false of the target, which licenses the derivation and bounds the claim | is no failure, since its falsity is declared; the claim fails only when it does not survive the removal of the idealization, which the robustness test checks |
| `condition` | a restriction under which the claim holds | places a case outside the domain of the claim, without refuting the claim |
| `criterion` | a standard fixed by the question, such as a tolerance | changes the standard against which the claim is judged, not the claim |

The layout of an argument in the theory of argumentation supplies three of these roles [toulmin1958]. Toulmin separates the data appealed to, the warrant that licenses the step from the data to the claim, the backing that supports the warrant, the qualifier that states the force of the claim, and the rebuttal that states the circumstances in which the warrant does not apply. The correspondence differs from an identity in three places:

- the role `datum` is Toulmin's data, and the role `warrant` is his warrant, restricted to a law of a model or of a background;
- the [warrant of a law](background.md#^law-warrant), which states its provenance, takes the place of the backing, and records the kind of support rather than its content;
- the role `condition` states positively the circumstances in which the claim holds, whereas the rebuttal states the circumstances of an exception.

The roles `assumption`, `idealization` and `criterion` have no counterpart in the layout. An idealization in particular is a ground that is not asserted true, so a ground cannot be defined as a premise whose truth the claim requires.

## Propagation along dependence

Three properties of a ground reach the claims that rest on it. Each case is stated in one note, linked below: ^propagation

- **Exposure to revision.** A result that rests on a law marked `posited`, `fitted` or `measured` inherits the exposure of that law to new evidence, and an answer built on the result inherits it in turn, as the [warrant of a law](background.md#^law-warrant) states.
- **Conditionality.** A result that rests on a provisional answer, or on an admitted claim that is not accepted, stays conditional on it, as the [rule on provisional answers](../../processes/inquiry/conditions-of-answerability.md#^condition-dependencies) states. A result that rests on the output of a step whose verdict is pending stays conditional on that verdict, as the [readiness of an act](../../processes/inquiry/choice-of-act.md#^ready-act) states.
- **Loss.** A record produced by a step that failed its norm lacks warrant, and every act that uses it inherits the failure, as the same rule of readiness states. A ground withdrawn from the accepted knowledge leaves every claim that rests on it without that ground.

**The weakest-link rule.** The test of law warrant among the [conditions of satisfaction](../answer/satisfaction-conditions.md#^conditions-satisfaction) checks each ground against its role, on the ground that a conclusion inherits the weakest warrant among the laws that it uses. The rule comes from the theory of defeasible reasoning: in the absence of other arguments, the degree of justification that an argument confers on its conclusion is the minimum of the degrees of its premises and of the strengths of its reasons [pollock2001]. Pollock states the rule for degrees ordered on one scale, and rejects the probability calculus for them, since a conjunction of independent premises is less probable than each premise. ^weakest-link

The warrant of a law is a kind of provenance, not a degree. The values `posited`, `fitted` and `measured` are not ordered among themselves, and the value `derived` points to other laws instead of grading the law. The method therefore adopts the rule in a qualitative form, as a proposal: a conclusion is exposed to revision through every law marked `posited`, `fitted` or `measured` among its grounds, and through every such law from which a derived law among its grounds descends. The set of these exposed laws is reported, not a degree, and the researcher judges which of them is the weakest.

**Propagation is reported, never applied.** A tool follows the authored relations backward from a revised unit and reports every record that rests on it, and the researcher decides whether each dependent holds, needs an adjustment or is retracted, as the [decision on revision accountability](../../../adr/revision-accountability.md#^flag-not-edit) fixes. A truth-maintenance system tracks the same dependencies, but relabels each belief automatically, in or out, according to whether one of its justifications still holds [doyle1979]. The method keeps the dependencies of such a system and leaves out its relabeling. This choice is consistent with the [accepted knowledge as a belief base](../../foundations/inquiry-and-state.md#^state): an accepted result is a member of the base on its own, so withdrawing one of its grounds does not remove it until the researcher revises the base.

## Defeat and the relations between answers

Five relations link one answer to another, as the [relations between answers](../answer/answer-form.md#^answer-relations) define them. The five relations play four parts: ^defeat

| Relation | Part | Effect on the dependence among claims |
| --- | --- | --- |
| `supports` | dependence | the claim of one answer is a ground of the other |
| `presupposes` | dependence | one answer is admissible only if the other is true |
| `tests` | evidence | the claim of one answer is a consequence of the other, compared with the target |
| `defeats` | attack | the claim of one answer, once accepted, removes a ground of the other |
| `revises` | lineage | none: the relation records that one answer replaced another over time |

The theory of structured argumentation separates three attacks on an argument: an attack on a premise, called undermining; an attack on the conclusion, called rebutting; and an attack on an inference step, called undercutting [prakken2010]. Rebutting and undercutting come from Pollock's account of defeasible reasoning [pollock1987]. The relation `defeats` covers two of the three:

- an answer that removes a ground with the role `datum` or `assumption` **undermines** the other answer;
- an answer that removes a ground with the role `warrant` **undercuts** it, since the warrant licenses the step to the claim.

A **rebuttal**, an answer whose claim contradicts the claim of another answer to the same question, is not one of the five relations. The two answers stand as rival candidates in $H$, the condition of [discrimination](../../processes/inquiry/conditions-of-answerability.md#^eight-conditions) separates them, and the assessment and the acceptance decide between them. A relation between rival explanations of one observation remains open under the goal `relation-registry` of the [project goals](../../../../TODO.md).

Two features separate `defeats` from defeat in argumentation. First, the relation takes effect only once the defeating answer is accepted, so before acceptance it records an attack and not a defeat. Second, its effect is a report to the researcher, not a status computed for the defeated answer: an engine that computes the acceptance of arguments from their attacks [dung1995] is excluded by the [decision against inference at run time](../../../adr/no-run-time-inference.md#^excluded-inference).

The relation `presupposes` between answers is a homonym of the [link `presupposes` between questions](../question/question.md#^linked-questions). Between answers, it conditions the admissibility of one answer on the truth of another. Between questions, it conditions the existence of a true answer to one question on the existence of a true answer to the other.

## Three graphs of dependence

An inquiry holds three graphs of dependence, each over its own nodes: ^three-graphs

- among **claims**: the grounds of each answer and the relations between answers, stated in this note;
- among **questions**: the [links between questions](../question/question.md#^linked-questions) and the [decomposition graph](../../processes/inquiry/question-decomposition.md#^decomposition-graph);
- among the **conditions of answerability** of one question: a condition depends on another when its statement refers to an object that only the other supplies, and this graph has no cycle, as the [dependencies between conditions](../../processes/inquiry/conditions-of-answerability.md#^condition-dependencies) state.

The graph of conditions orders the work on one question: it states which condition can be established first. The graph of claims orders the warrant: it states which claim supports which. The links between questions connect the two, since each link predicts where an answer to one question will enter the other question:

| Link between questions | Where an answer to the linked question enters this question |
| --- | --- |
| `subquestion-of` | an accepted answer to the subquestion narrows the answers of the linked question, and becomes a ground of its answer, by `supports` |
| `explanans-from` | nowhere as an answer: the two questions share the record of one phenomenon, which is a factor of this question and the explanandum of the linked one, so a revision of that record reaches both |
| `presupposes` | the condition of soundness of this question depends on the soundness of the linked question; two answers carry `presupposes` only when the admissibility of one depends on the truth of the other |
| `enables` | an accepted or provisional answer establishes a condition of answerability of the linked question; it becomes a ground of the claim only when the bridging inference of the answer uses it |

Cycles are treated differently in the three graphs. A cycle between questions is admitted and resolved by iteration, as the [cycles of a decomposition](../../processes/inquiry/question-decomposition.md#^cycles) state. The graph of conditions has none. A cycle of grounds among claims is judged by the condition of [tests that can fail](../../processes/inquiry/specification-order.md#^iteration-circularity), which decides whether a claim supported through itself is circular in warrant.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the layout of an argument, the weakest-link principle for degrees of justification, the three attacks of structured argumentation, truth maintenance, and abstract argumentation, as cited.
> - **Proposals:**
> 	- the effect of a failure of a ground, read from its role;
> 	- the correspondence between the roles of a ground and the layout of an argument;
> 	- the weakest-link rule in a qualitative form, as a set of exposed laws;
> 	- the mapping of `defeats` onto undermining and undercutting;
> 	- the place where each link between questions enters the dependence among claims.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [doyle1979] ◐ [Doyle, "A truth maintenance system", *Artificial Intelligence* 12(3), 231–272, 1979](https://doi.org/10.1016/0004-3702(79)90008-0)
- [dung1995] ◐ [Dung, "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", *Artificial Intelligence* 77(2), 321–357, 1995](https://doi.org/10.1016/0004-3702(94)00041-X)
- [pollock1987] ◐ [Pollock, "Defeasible reasoning", *Cognitive Science* 11(4), 481–518, 1987](https://doi.org/10.1207/s15516709cog1104_4); rebutting and undercutting defeaters
- [pollock2001] ◐ [Pollock, "Defeasible reasoning with variable degrees of justification", *Artificial Intelligence* 133(1–2), 233–282, 2001](https://doi.org/10.1016/S0004-3702(01)00145-X); the weakest-link principle, checked through the [revised version on the author's site](https://www.johnpollock.us/ftp/OSCAR-web-page/Degrees.pdf)
- [prakken2010] ◐ [Prakken, "An abstract framework for argumentation with structured arguments", *Argument & Computation* 1(2), 93–124, 2010](https://doi.org/10.1080/19462160903564592); undermining, rebutting and undercutting, read in the abstract of the [author's preprint](https://webspace.science.uu.nl/~prakk101/pubs/aspicAF.pdf)
- [toulmin1958] ◐ Toulmin, *The Uses of Argument*, Cambridge University Press, 1958; data, warrant, backing, qualifier and rebuttal
