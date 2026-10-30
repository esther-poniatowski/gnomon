---
tags:
  - theory
  - wip
index: "[Course of an inquiry](docs/epistemology/processes/inquiry/_index.md)"
aliases:
  - Question decomposition
  - Decomposition of a question
  - Serving question
---
# Question decomposition

> [!QUESTION] Goal: how is a question decomposed into questions that serve it, and how does the decomposition stay valid as the inquiry proceeds?

A precise question does not fix the route to its answer. Decomposing the question supplies that route: it infers intermediate questions whose resolution is progress toward a justified answer, not an accumulation of related information. The method is a form of **regressive analysis**, in which a goal is reduced to the conditions under which it is attained, and each unmet condition becomes a subgoal. Regressive analysis has three classical formulations:

- the analysis of Pappus, which Pólya reworked as working backward [polya1945];
- means–ends analysis, in the theory of problem solving of Newell and Simon [newell1972];
- the erotetic logics, which break questions into questions: the interrogative model of Hintikka [hintikka1999] and the erotetic search scenarios of Wiśniewski [wisniewski2013].

The method applies to a question already posed. In the exploratory phase of research, before the question is fixed, the first serving question is usually the one that makes the main question well posed.

**Governing criterion.** A serving question is admissible only when its resolution changes the status of the question that it serves: it reduces the set of admissible answers, forces a reformulation, makes a distinction visible that was not yet visible, or establishes a condition of answerability of the served question. The criterion applies at two moments: when the inquiry is planned, before substantial work, and when an obstacle met during the inquiry calls for a local revision. ^governing-criterion

## The decomposition graph

A decomposition is a graph whose nodes are questions. Each edge is one of the [links between questions](../../objects/question/question.md#^linked-questions), and one of its two questions *serves* the other. For `subquestion-of` and `enables`, the question that carries the link serves the linked question; for `presupposes` and `explanans-from`, the linked question serves the question that carries the link. This sense of serving is broader than the service of a problem, which requires erotetic implication, as the note on the [epistemic problem](../../objects/problem/epistemic-problem.md#^problem-vs-question) states. ^decomposition-graph

A demand that is a conjunction is decomposed by `subquestion-of`, one serving question per conjunct. A presupposition posed as a question is linked by `enables`, not by `presupposes`. The question whether the presupposition holds always has a true answer, so `presupposes` would make soundness depend on a question that is trivially sound.

The serving questions of one question stand in one of three relations. Serving questions are *conjunctive* when all are needed, *disjunctive* when any one suffices, such as an analytic derivation and a simulation that both give access to a quantity, and *sequential* when the answer of one fixes the form of another. Disjunctive serving questions require a choice among routes, made by the [ranking of acts](choice-of-act.md#^ranking-criteria).

## Sources of serving questions

Serving questions arise from four sources. ^serving-sources

**First, the unmet conditions of answerability.** The conditions are identified from the logical form of the question, in four steps:

1. **Fix the form.** State the interrogative type, the subject and the set of admissible answers, as Hamblin and Belnap and Steel model a question [hamblin1958] [belnap1976]. For a why-question, the form also requires a contrast and a [requested relation](../../objects/task/requested-relation.md) [vanfraassen1980].
2. **Extract the presuppositions.** Every proposition entailed by all the admissible answers is a presupposition. "Why does the network learn disentangled features?" presupposes that the network learns them.
3. **State what the answer must reach.** The [answer type](conditions-of-answerability.md#^eight-conditions) fixes the resolution of the answer, and the [epistemic task](../../objects/task/epistemic-task.md) fixes its required accuracy and its proof obligations. Hintikka calls the epistemic state to be reached the *desideratum* of the question [hintikka2007].
4. **Work backward.** For each admissible answer, ask what must be known to select it over its rivals. Each item missing from the present records is an unmet condition.

An unmet condition becomes a serving question, linked by `enables`, when the researcher chooses to pose it, as the [choice of the next act](choice-of-act.md#^condition-to-question) states.

**Second, a conjunctive demand.** Each conjunct of the demand becomes a serving question linked by `subquestion-of`.

**Third, a blockage met during the inquiry.** A blockage is whatever prevents progress at a given stage. The serving question is found in three moves: identify the blockage, state why it prevents progress on the served question, and formulate the smallest question whose answer would remove it. The usual blockages map onto the conditions of answerability:

| Blockage | Practical meaning | Serving question | Condition |
| --- | --- | --- | --- |
| Conceptual | a central notion is vague, overloaded, undefined or unstable | which notion is needed, under which constraints, and how is it defined so that it serves the aim? | definiteness |
| Formal, without a representation | no usable framework represents the objects and relations | which formal object or simplified setting captures the issue? | definiteness, or representation when a simplified setting is studied |
| Formal, without a criterion | no measurable or computable criterion exists | which proxy, observable or derived quantity is valid? | definiteness |
| Discriminative, between interpretations | incompatible interpretations of the question coexist | which interpretation does the aim require, and what excludes the others? | definiteness |
| Discriminative, between explanations | several explanations or formalisms remain equally compatible | what would discriminate between them? | discrimination |
| Tractability | the problem is too hard or too broad in its full form | which reduced setting keeps the core difficulty? | access, or representation when a reduced model is studied |
| Interpretive | a result can be derived or computed, but its meaning for the question is unclear | which relation links the formal result to the claim sought? | bridging |

**Fourth, the burden of justification of the claim.** When the blockage alone does not show what is missing, the logical type of the claim sought does. Each type of claim imposes a **burden of justification**, which yields canonical serving questions. The burdens are named by the kind of claim that bears them; they are distinct from the warrant tier of the [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md) and from the warrant of a law. ^burdens

| Burden of justification | Discharged when | Canonical serving questions |
| --- | --- | --- |
| Conceptual | the claim is well formed and delimited | which traits are essential? which criteria include and exclude? how does the notion differ from its neighbors? is the definition adequate to its use? |
| Ontological | the object or mechanism claimed is possible or real | what would count as an instance? could the evidence come from an alternative? what separates existence from artefact? |
| Structural | the internal organization of the object is correctly described | which formal object captures the structure? which invariants matter? which transformations preserve the property? |
| Causal | the factors invoked produce the phenomenon | which factors covary? which are efficacious? which interventions would change the outcome, and through which mechanism? |
| Inferential | the conclusion follows from the assumptions | what exactly is to be shown? which assumptions are necessary? which intermediate steps? which domain of validity? |
| Modal or regime | the conditions of validity, breakdown or transition are identified | which parameters control the phenomenon? are there thresholds? which conditions are necessary, sufficient, or both? |
| Epistemic | the method that detects, measures or validates the claim is trustworthy | which signatures indicate the target? are they specific? which false positives and negatives? does success reflect the intended property or a confound? |

## Functional types of serving questions

A serving question belongs to one of three functional types, which fix how it is generated and how long it stays valid. ^functional-types

| Type | Trigger | Role | Validity |
| --- | --- | --- | --- |
| Analytic | at planning, a condition of answerability is unmet | remove an obstacle already visible | unconditional, as long as the served question stands |
| Abductive | during the inquiry, a resistance appears: an obstacle that the current formulation cannot remove | identify a hidden assumption, a missing property or an inadequate formalism | conditional on the resistance hypothesis $\eta$ that explains the resistance |
| Constructive | the vocabulary collapses distinctions that matter: distinct situations receive the same answer, every candidate notion needs corrections at its boundary, or rival frameworks agree formally and differ structurally | expand the framework: define a concept, construct a formal object, or find a representation under which the question becomes tractable | a semantic prerequisite: the questions downstream are undefined until this one is resolved |

A question generated by a failure must not acquire unconditional status silently. A derivational impasse often generates a local explanatory hypothesis, and once that hypothesis is overturned, the questions spawned by it need reassessment.

## Relevance of a serving question

Each candidate serving question receives one of three statuses: ^relevance

| Status | Criterion |
| --- | --- |
| Necessary | without it, answering the served question would be impossible, invalid or uninterpretable |
| Useful | not strictly required, but improving robustness, scope or explanatory force |
| Decorative | adjacent or interesting, but without material effect on the answer |

The status is found by three questions: what would become impossible if the serving question were resolved negatively, what would become supported if it were resolved positively, and what would become newly distinguishable. When all three answers are empty, the serving question is decorative and is removed. The [choice of the next act](choice-of-act.md#^ranking-criteria) applies the same test to acts.

## The register of serving questions

The serving questions of an inquiry are recorded in a register: ^register

| Column | Content |
| --- | --- |
| Question | the serving question |
| Type | analytic, abductive or constructive |
| Link | the linked question and the relation of the link |
| Depends on | the questions that must be answered before this one is meaningful, tractable or interpretable |
| Effect | what its resolution changes in the served question |
| Status | open, answered, abandoned |
| Conditioned on | for an abductive question, the resistance hypothesis $\eta$ under which it was generated; for a constructive question, the marker *vocabulary-expanding* |

When a resistance hypothesis $\eta$ is refuted, every question conditioned on it is invalidated and reconsidered. This cascade applies to serving questions the [recorded dependencies](specification-order.md#^iteration-circularity) of controlled iteration. The dependencies of a register often show three levels: foundational questions on definitions, assumptions, formalization and criteria of success; structural questions on mechanisms, derived properties, invariants and tractable regimes; and validation questions on tests, simulations, comparisons, robustness and generalization.

## Terminal questions and synthesis

A serving question is **terminal** when some procedure has all its inputs available and yields an admissible answer that meets the answer type, its proof obligations and its required accuracy included. Terminality holds relative to the means of a given researcher at a given time, as the [states of a condition](conditions-of-answerability.md#^condition-states) state. Terminal acts are classified by the source of the support that they deliver, since that source fixes what the answer can be trusted for: ^terminal-acts

| Source of support | Act | Serving questions typically closed |
| --- | --- | --- |
| Existing knowledge | retrieval from the literature, a database or an expert | any type, when an accepted or published result already answers it |
| Reasoning alone | proof, analytic calculation, conceptual analysis | bridging; definiteness; the consequences that discriminate candidates within a formal model |
| Observation of the target | measurement, analysis of existing data | soundness; the value of a discriminating quantity, by exercising access |
| Intervention on the target | controlled experiment | the value of a quantity that discriminates causal hypotheses, by exercising access |
| Study of a surrogate | numerical simulation, analysis of a model | the value of a quantity within the model, by exercising access, with representation for the target |
| Generation | abduction; construction of a model, an instrument or an algorithm | candidates; access |
| Decision | stipulative definition, choice of an idealization, choice of a standard | definiteness; answer type |

Acts of generation add candidates or tools and justify no answer, and acts of decision fix a commitment and establish no fact. An answer obtained by either is therefore recorded as a revisable assumption, and these assumptions are the first to re-examine when the served answer fails.

**Analysis is followed by synthesis.** Working backward identifies necessary conditions, and the steps of analysis cannot always be reversed. A combination step therefore composes the answers of the serving questions into an answer to the served question, and a check confirms that the combination is valid, as the [necessity and joint sufficiency of the conditions](conditions-of-answerability.md#^sufficiency) require. When the conditions hold and no answer follows, a condition is missing, most often a bridging assumption. ^synthesis

## Revision during the inquiry

**A serving question can correct the served question.** Its answer can show that a presupposition of the served question is false or that a term of it is ill defined. The served question is then reformulated before any answer is sought for it, a case that a strictly top-down tree cannot represent. ^revision

**Local revision.** The usual triggers of a local revision are the following:

| Trigger | Meaning |
| --- | --- |
| Impasse in derivation | the current route presupposes a missing property or an inadequate formalism |
| Empirical or formal anomaly | a result contradicts the working view, so some assumption or mechanism is false, incomplete or too crude |
| Conceptual tension | two branches rely on incompatible implicit assumptions |
| Interpretive ambiguity | a result is obtained but cannot be interpreted |
| Counter-example | the formulation is too general or misses a constraint |

A local revision follows five steps:

1. Record the resistance in one sentence.
2. State what it suggests is missing, false or misaligned.
3. Formulate one serving question that repairs, discriminates or reconstructs. For a false local explanatory structure, abduce the simplest resistance hypothesis $\eta$ consistent with the resistance and the accepted knowledge $K$, and add an abductive question conditioned on $\eta$. For an insufficient vocabulary, add a constructive question.
4. Invalidate every question conditioned on a hypothesis that the resistance refutes.
5. Remove or postpone the older questions that the revision makes secondary.

**Global revision.** A global reorganization is needed only when the served question itself is malformed. Three revisions turn a question $Q$ into a refined question $Q'$: a *disambiguation*, when $Q$ conflated two questions; a *restriction of scope*, when the conditions of answerability hold only under narrower conditions held fixed; and a *replacement of a concept*, when constructive work supplies a more precise notion. The relation between $Q$ and $Q'$ is stated, and the earlier serving questions are reassessed under $Q'$. The main question is re-examined at intervals for these three revisions. ^global-revision

**Cycles between questions.** A condition of one question can depend on the answer to another, and two such dependencies in opposite directions form a cycle. Further decomposition cannot resolve the cycle, so it is resolved by iteration, under the conditions of [controlled iteration](specification-order.md#^controlled-iteration), as the [dependencies between conditions](conditions-of-answerability.md#^condition-dependencies) state. ^cycles

## Failure modes

| Failure | Description |
| --- | --- |
| Decomposing by related themes | the serving questions mirror the literature or the topic, not the structure of the problem |
| Decomposing by workflow | the inquiry is split into stages, such as review, data, experiment and interpretation, not into epistemic obstacles |
| Decomposing by available tools | questions are chosen because a method is available, not because they are needed |
| Decorative branching | time goes to adjacent questions that do not affect the answer |
| Treating all serving questions as independent | no dependency structure is recorded |
| Validating prematurely | validation precedes the clarification of concepts and criteria, and yields correct but uninterpretable results |
| Vocabulary inertia | the vocabulary is kept although it cannot express the distinctions needed |
| No falsifying leverage | no serving question can eliminate a central assumption, so no resolution changes the admissible answers |
| Revising the register globally | a new obstacle triggers a complete reorganization when a local revision suffices |
| Unrecorded resistance hypotheses | questions induced by a failure carry no resistance hypothesis $\eta$, so its refutation propagates invisibly |

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976; a question modeled by its admissible answers
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211); checked through secondary sources
- [hintikka1999] ○ Hintikka, *Inquiry as Inquiry: A Logic of Scientific Discovery*, Kluwer, 1999; the interrogative model of inquiry
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); the desideratum of a question
- [newell1972] ○ Newell & Simon, *Human Problem Solving*, Prentice-Hall, 1972; means–ends analysis
- [polya1945] ○ Pólya, *How to Solve It*, Princeton University Press, 1945; working backward
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, Clarendon Press, 1980, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [wisniewski2013] ○ Wiśniewski, *Questions, Inferences, and Scenarios*, College Publications, 2013; erotetic implication and erotetic search scenarios
