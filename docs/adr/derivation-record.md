---
tags:
  - decision
status: accepted
created: 2026-11-04
revised: 2026-11-05
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Derivation record
---
# Derivation record

> [!QUESTION] Goal: which record holds the reasoning that establishes a consequence, and which parts of that reasoning must it state?

The activity `derivation` outputs a consequence. The [records of a consequence](../epistemology/processes/activities/model-analysis.md#^consequence-records) state the statement established, but no record held the reasoning establishing it. The route of an answer named a derivation only by a pointer. Therefore, a check could neither trace a consequence to its premises nor report the assumptions and the approximations supporting it. The [theory of derivations](../epistemology/objects/derivation/_index.md) states the parts of that reasoning.

## Decision

**A derivation record holds the reasoning below the grain of a product.** The [criterion of the units of research work](../epistemology/processes/units-of-work.md#^work-unit-criterion) assigns to it the intermediate objects cited by no other record. The record states:

- the [sought](../epistemology/objects/derivation/sought.md): a root sought read from the record served, or declared by the derivation when it serves no record, and the subordinate soughts set by the derivation; the type and the condition stated by a sought fix its degree of determinacy, so no field restates that degree;
- the [posits](../epistemology/objects/derivation/posit.md), each with its kind, its origin and its tests;
- the [moves](../epistemology/objects/derivation/move.md), each with its kind, its inputs and outputs, and its warrant, stating its source, the class of its error, its regime and the property that makes it apply;
- the [orientations](../epistemology/objects/derivation/orientation.md) of the non-routine moves and of the segments, each with its purpose, and with its occasion, its means, its alternatives and its provenance when they apply;
- the [interpretations](../epistemology/objects/derivation/interpretation.md), each with its item, its kind and its ground;
- the [segments](../epistemology/objects/derivation/segment-and-scheme.md), each with its inputs, its outputs and the scheme applied, when a scheme applies;
- the [outcomes](../epistemology/objects/derivation/consequences-and-understanding.md): each consequence named by the record that states it, each lemma kept in the derivation, each impasse with its diagnostic interpretation, and each refutation;
- the gain expected from each orientation, and the gain obtained, the principle and the pattern stated with the consequences.

**No field requires the result in advance.** A sought may be open, and an unknown introduced by a move or a posit is a slot of the derivation, bound later by a move.

**A derivation bears the role Derivation.** A derivation licenses tracing a consequence, or an obstacle, back to its premises, as the [epistemic roles](../epistemology/objects/status/epistemic-objects.md#^unit-roles) state.

**The record states the non-routine moves, and a segment bridges the others.** The [features of a non-routine move](../epistemology/objects/derivation/move.md#^non-routine) are read from the record, so no author exempts a move by calling it routine.

**The exposure of a consequence extends to the parts of its derivation.** The [exposure of a derivation](../epistemology/objects/knowledge/grounds-and-dependence.md#^derivation-exposure) adds, for the moves and the segments upstream of each consequence, the posits not confirmed or refuted, the warrants and the operations not exact, the premise laws, and the exposure of each consequence of another derivation used. A unit whose state is not stated counts as exposed. A tool computes that set by walking the dependence back from the answer, under this declared rule, as the [admitted computations](no-run-time-inference.md#^admitted-computation) allow.

**A derivation sees the symbol tables of the records holding its premises.** The [visible tables](flat-symbol-table.md#^visible-tables) gain a row for the derivation, and the slots of a derivation are declared in its own table.

The record takes the prefix `derivation`, with three segments, and the contract `gnomon:derivation@1`.

## Defects that a check reports

The proposals for the derivation framework, `docs/proposals/derivation-framework.md` at commit c5a1614, listed three conditions of adequacy and six named defects of a derivation. A check reports a defect only when the record states the units on which its verdict rests, as the [decision against inference at run time](no-run-time-inference.md) requires. The other defects need a judgment of relevance or of generality, so the norm of the act producing the derivation judges them. Amended on 2026-11-04.

| Defect | Disposition |
| ------ | ----------- |
| A blind step: a warrant without a local reason | reported for a non-routine move or a segment without an orientation; a routine move needs none, since a segment bridges it |
| An untyped transition: a move outside the vocabulary | reported by the closed vocabulary of the kinds of move |
| A state ambiguity: the facts active at a step are unclear | prevented by the inputs and the outputs required of each move and each segment, which must name units of the record; reported for a move of a segment that takes what the segment neither takes nor yields, and for a consequence stated by an object that no move yields |
| An idle step, or a spurious move that makes no progress | reported for a move that yields only what it takes, or whose outputs reach no outcome and no interpretation cited by the record |
| Subgoals that do not form a well-founded order | reported for segments that enclose one another, or soughts that replace one another, in a cycle; the record links a subordinate sought to the sought that it replaces, not to the sought that it serves, so the check covers the order of replacement and of nesting only |
| A warrant stated at the wrong generality | judged by the norm: the generality of a warrant is not read from its fields |
| A reason without a contrastive alternative | judged by the norm: the alternatives of an orientation stay optional, since a move may have no salient rival |
| A hidden obstacle, a teleological gap, or an avoidable detour | judged by the norm: each rests on the relevance of a move, or on a route that the record does not hold |

## Conditions of admission

The kind meets the seven [conditions of admission](record-kind-admission.md#^admission-conditions):

- **independent identity**: a derivation is meaningful without the answer that cites it, as a published proof or a published calculation is;
- **reuse**: several answers, assessments and derived laws can cite one derivation, and one derivation can establish several consequences;
- **local validity**: a check judges the warrants, the posits and their tests, the admitted pairs of the interpretations, the order of the orientations and the declared kernel without reading the records citing the derivation;
- **independent editing**: an author can add a move, an interpretation or a test without rewriting the records that cite the derivation;
- **irreducibility**: no tool generates a derivation, as the [decision against inference at run time](no-run-time-inference.md) requires;
- **non-distortion**: each existing kind would distort a derivation:
    - an answer holds one typed claim and its grounds, whereas a derivation holds intermediate objects and many moves, so an answer would hold those moves in prose;
    - an itinerary records acts, each judged by the norm of its activity, whereas a move produces no product, so a move recorded as an act would break the [criterion of the boundary](../epistemology/processes/units-of-work.md#^work-unit-criterion);
    - a model holds a system and its laws, whereas the moves of a derivation act on intermediate expressions;
    - a design of kind `method` states a way of deriving apart from any derivation, whereas a derivation applies it to one problem;
- **unitary epistemic role**: every derivation, whether it proves a stated claim or constructs an unknown result, licenses the same operation, tracing its outcomes to their premises.

## Constraints that decide the record

- **Every problem to prove is a problem to find.** A problem to prove is a problem to find whose unknown is the truth of a claim, as the [two kinds of problem](../epistemology/objects/derivation/derivation.md#^prove-and-find) state. A record shaped around a stated conclusion would fail every construction whose result is unknown when the derivation starts.
- **Validity does not convey understanding.** A record of transformations alone states only that a consequence follows. Such a record states neither the reason for each step nor the meaning of its objects. Therefore, the warrant, the orientation and the interpretations answer three separate questions.
- **One fact has one home.** A change to the laws or the members of a model is an operation of a derived model. When the output of an act is a product, the act is a step of an itinerary. Therefore, the record holds neither.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep the derivation in the prose of an answer | No kind is added | No check traces a consequence to its premises, and the posits and approximations leave the exposure rule |
| Record each move as a step of the itinerary | The acts and the moves share one structure | A move outputs no product, so its norm would be the warrant of one step, and the itinerary would merge two grains |
| A proof object with the terms and tactics of a proof assistant | Mechanical checking becomes possible | The [decision on expression syntax](expression-syntax.md) declines the term language of a proof assistant, and an approximation or a posit has no term |
| A closed vocabulary of moves in four families: structural, transport, search and closure | Each family states the cost of annotating its moves | The families mix the effect of a move with its rationale, and they hold no approximation. The six groups of [atomic kinds of move](../epistemology/objects/derivation/move.md) replace them, and the orientation states the rationale |
| One derivation record per answer | The route of an answer points to one record | One derivation may establish the consequences of several answers, and one answer may rest on several derivations |
| A record of its own for each intermediate lemma | A lemma gains an identifier outside its derivation | A lemma cited by no other record fails the condition of reuse; a lemma that holds beyond its derivation is stated as a derived law, so it already has a home |
| A plan of the derivation, apart from its segments | The plan reads as a whole | The purposes of the orientations of the segments already state the plan, nested along the segments, so a second statement would duplicate them |
| A sufficient kernel test | The kernel is computed, not declared | Every move of a linear chain passes the test, so the test is a necessary condition only, and the record declares the kernel |

## Consequences

- The record kinds gain `derivation`, with its specification, its base schema, its template and its contract.
- The registries gain the closed vocabularies of the derivation: the kinds of move, of posit and of test, the intended changes of a purpose, the reasons for setting an alternative aside, and the items and kinds of interpretation with their admitted pairs.
- The checks gain the rules listed in the [checks of a derivation](../specification/derivation.md#^derivation-checks), which is their one statement, and the exposure of a derivation.
- A law marked `derived` names its descent: a derivation stating it as a consequence, or an origin holding the published derivation.
- The norm of the activity `derivation` requires that each move is licensed by its warrant and that each posit is stated with its origin and its tests, as the [model analysis](../epistemology/processes/activities/model-analysis.md#^explicative-derivation) states.
- The route of an answer, the obligations of an assessment and the step of an itinerary that produced a derivation point to derivation records; a passed step of the activity `derivation` names its record, whose consequences land in the output of the step.
- The adopted entries of the proposals for the derivation framework are retired; the entries left open are settled by the decision on the [content of a claim](claim-content.md), and the note of those proposals is retired.
