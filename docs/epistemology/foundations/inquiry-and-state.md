---
tags:
  - theory
index: "[Foundations](docs/epistemology/foundations/_index.md)"
aliases:
  - Inquiry and its state
  - Inquiry
  - State of an inquiry
  - Research record
  - Admitted and accepted
  - Obtained and accepted
---
# Inquiry and its state

> [!QUESTION] Goal: what is an inquiry, what does its state hold at a given time, and how does an accepted claim differ from an admitted claim and from an obtained claim?

An **inquiry** is a course of epistemic acts directed at one or several problems. An inquiry starts from a body of accepted knowledge, poses the questions that serve its problems, and changes that knowledge by proposing, assessing and accepting answers to those questions. ^inquiry

Three accounts of inquiry ground this definition, each for one of its parts:

- **An inquiry starts from a problem.** Dewey defines inquiry as the transformation of an indeterminate situation into a determinate one, and a situation becomes a problem once an inquiry states it [dewey1938]. The note on the [epistemic problem](../objects/problem/epistemic-problem.md) states a problem relative to the accepted knowledge, so that its existence and its solution can be checked.
- **An inquiry changes a corpus of accepted knowledge.** The corpus of an inquirer is the standard of serious possibility, and inquiry revises it by expansion and contraction [levi1980].
- **An inquiry proceeds by questions.** In the interrogative model, an inquiry alternates questions put to sources with deductions from the knowledge already held [hintikka2007]. The [question](../objects/question/question.md) is the unit of that course.

The definition adds one element that the records require: each act of an inquiry is typed by the [epistemic activity](../processes/activities/epistemic-activities.md) that it performs, a type of operation fixed by its inputs, its output and its norm, so that the course can be checked step by step.

- **An inquiry is not a question.** One problem motivates one or several questions, and one question serves one or several problems, as the [comparison of a problem and a question](../objects/problem/epistemic-problem.md#^problem-vs-question) states. A question is therefore a part of an inquiry. A research project, in the sense of the [README](../../../README.md#motivation), holds one or several inquiries.
- **An inquiry is a course of acts, and its records represent it.** The acts are performed by inquirers, whether or not a record describes them, as the [status of an epistemic activity](things-and-constructs.md#^layer-test) states. The research records hold the content that the acts produce, and the itinerary records the acts themselves.

## Records of an inquiry

A **record** is an authored document that states one object of an inquiry in the format of its kind, such as a problem, a question or an answer. The records of a project form two families, told apart by the content that they hold: ^record

- the **research records** hold the content of the inquiry: its problems, questions, declarations, data, laws and answers. The **itinerary**, a research record of its own, holds the acts that produced that content, each typed by its activity;
- the **exposition records** hold no content: each selects research units and orders them for an audience, as the note on [exposition](../expression/exposition.md#^exposition) states.

A **research unit** is a research record, or a unit of such a record with an identifier of its own, as the [decision on expositions](../../adr/expositions-as-projections.md) fixes. Content is cited, revised and presented at the grain of the research unit. The [inventory of epistemic objects](../objects/status/epistemic-objects.md) places each kind of research unit with the epistemic role that it bears.

## The state of an inquiry

The **state** of an inquiry at a given time holds four components: ^state

- the **accepted knowledge** $K$: the finite set of claims that an act of acceptance has placed in it;
- the **proposed candidates** $H$: the answers put forward and not yet accepted;
- the **open questions**: the questions posed whose problems still exist, each with the state of its [conditions of answerability](../objects/question/conditions-of-answerability.md#^condition-states), the conditions that must hold before an answer can be obtained;
- the **admitted background** of each target: the laws admitted about that target before any answer is sought, as the note on the [background](../objects/knowledge/background.md) states.

Each item of these components carries statuses, such as the attitude of a claim or the maturity of a specification, which the [axes of the statuses](../objects/status/statuses-and-acceptance.md#^status-axes) place on their bearers. The itinerary is not a component of the state. The itinerary records the acts through which each item entered the state.

**The accepted knowledge is a belief base.** A belief base is a set of claims that is not closed under logical consequence, so a consequence of its members belongs to it only once it is itself accepted [hansson1999]. Two features of the method make $K$ a base. First, a claim enters $K$ only by an act of acceptance, never because it follows from members of $K$, as the [relation between obtained and accepted claims](#^obtained-accepted) states. Second, no tool of `gnomon` derives a claim that no record states, as the [decision against inference at run time](../../adr/no-run-time-inference.md#^no-inference) fixes. The revision of $K$ therefore follows the norm of base revision, stated with the activity [`belief-revision`](../processes/activities/revision.md).

**The inquiries of one project share one accepted knowledge.** An acceptance revises the corpus of the project, which a record of the [act of acceptance](../objects/status/statuses-and-acceptance.md#^acceptance-act) would name. An answer accepted in one inquiry is therefore a member of $K$ for every inquiry of the same project. A claim of another project enters $K$ only when the researcher of the project accepts it, by the rule that governs a cited publication below. A concept that several projects reference adds nothing to $K$, since a concept is assessed for its adequacy and is never accepted. Whether one project may keep several corpora, for instance one for each of two rival programmes, is left open. ^shared-knowledge

## Obtained and accepted

Two relations hold between a claim $s$ and the accepted knowledge, and only the second makes $s$ a member of $K$: ^obtained-accepted

- $s$ is **obtained**, written $\mathrm{Obt}_{\mathcal{M}}(s)$, when the available means $\mathcal{M}$, the methods, data, instruments and proof techniques that can be applied, have yielded $s$;
- $s$ is **accepted**, written $s\in K$, when the researcher has accepted $s$ by the [act of acceptance](../objects/status/statuses-and-acceptance.md#^acceptance-act).

Both relations are actual, not dispositional. A claim that the means could yield, but have not yet yielded, is not obtained: an unproven theorem about a formal model stays outside $K$, although it follows from the laws of that model. A claim obtained and not yet accepted stays a candidate of $H$. Neither relation is a consequence relation, since no claim enters $K$ because it follows from claims already in it.

Citing a publication accepts none of its claims. A claim of a cited publication enters $K$ only when the researcher accepts it. A publication cited to dispute it, or whose claims are only admitted, adds nothing to $K$.

The [existence of a problem](../objects/problem/epistemic-problem.md#^problem-existence) and its [epistemic gap](../objects/problem/epistemic-problem.md#^gap) are therefore stated by membership in $K$.

## Admitted and accepted

Two relations hold between a claim and an inquiry, and they vary independently: ^admitted-accepted

- a claim is **admitted** when the inquiry takes it as a premise, with a stated warrant, whether or not the claim is accepted as known;
- a claim is **accepted** when it is a member of $K$.

| Claim | Admitted | Accepted |
| --- | --- | --- |
| a law posited as a working assumption in the background of a target | yes | no |
| a provisional answer adopted for a dependency between two questions | yes | no |
| an accepted answer cited as a ground of another answer | yes | yes |
| a claim of a cited publication, accepted by a record and used by no answer | no | yes |
| a claim of a publication cited to dispute it | no | no |
| a candidate of $H$, neither adopted nor accepted | no | no |

The second row comes from the rule on [provisional answers](../objects/question/conditions-of-answerability.md#^condition-dependencies): a result that rests on an adopted answer stays conditional on it. Every result that rests on an admitted claim that is not accepted stays conditional on that claim in the same way, as the note on [grounds and dependence](../objects/knowledge/grounds-and-dependence.md#^propagation) states.

> [!WARNING] Two uses of "acceptance" in the literature
> Cohen defines the acceptance of a proposition as a voluntary policy of taking it as a premise, distinct from believing it [cohen1992]. That sense corresponds to *admitted* in this method. The acceptance into a corpus, in the sense of Levi [levi1980], corresponds to *accepted*.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the accounts of inquiry, belief bases and the two senses of acceptance, as cited.
> - **Proposals:**
> 	- the definition of an inquiry, which combines the three accounts with typed acts;
> 	- the four components of the state, and the separation of admitted from accepted claims;
> 	- the separation of obtained from accepted claims, and the rule that citing a publication accepts none of its claims;
> 	- one accepted knowledge shared by the inquiries of a project.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [cohen1992] ◐ Cohen, *An Essay on Belief and Acceptance*, Clarendon Press, 1992; acceptance as premising, distinct from belief, checked through secondary sources
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987); ch. 6; checked through secondary sources
- [hansson1999] ◐ [Hansson, *A Textbook of Belief Dynamics: Theory Change and Database Updating*, Kluwer, 1999](https://doi.org/10.1007/978-94-007-0814-3); belief bases, as opposed to belief sets closed under consequence
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); interrogative and deductive moves
- [levi1980] ◐ Levi, *The Enterprise of Knowledge: An Essay on Knowledge, Credal Probability, and Chance*, MIT Press, 1980; the corpus of knowledge, revised by expansion and contraction
