---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Orientation of a move
  - Orientation
  - Prospective rationale
---
# Orientation of a move

> [!QUESTION] Goal: what identifies the next relevant move of a derivation, before that move is made?

An **orientation** states, from the current state of a derivation, the next move to make and its end. The orientation is the prospective rationale of a move: it precedes the move and selects it. A justification written after a move states why the move was valid. That justification is the [warrant](move.md) of the move, not its orientation.

## The orientation as a practical inference

An orientation has the form of a practical inference. An agent intends to bring about an end, and considers that the end cannot be reached without some act. Therefore, the agent sets out to do that act [vonwright1971]. The reasoning of the agent runs from the end to the means. The question "Why?", asked of a completed action, elicits the same descriptions in the reverse order [anscombe1957]. A sentence such as "to eliminate the secular term, introduce a slow time" states the order of the agent: the end first, then the means.

Problem solving follows the same order. In means–ends analysis, a difference between the current state and the goal selects the operator that reduces that difference [newell1972]. Strategic rules select the good moves among the admissible ones [hintikka2007]. The orientations of a derivation state those rules for the derivation at hand.

## Parts of an orientation

An orientation states five parts:

- **purpose**, the end of the move, always stated. The end is either a subordinate [sought](sought.md) to determine ("to determine the amplitude") or an intended change of state ("to eliminate the secular term at second order"). The intended changes form a closed vocabulary: eliminate, decouple, isolate, reduce, expose, close and match;
- **occasion**, the feature of the current state that makes the purpose relevant now, often a diagnostic [interpretation](interpretation.md) ("the naive expansion grows linearly in time"). The occasion is stated when the purpose does not follow from the sought alone;
- **means**, the move called for by the purpose: a kind of move, a [scheme](segment-and-scheme.md), or an act of the itinerary;
- **alternatives**, the moves considered at that point and set aside, each with one of five reasons: inapplicable, inconsistent, costlier, losing information, or already tried without success;
- **provenance**, contemporaneous when the orientation was written while the derivation was carried out, and reconstructed when it was written afterwards from a source.

An intended change is stated by the difference between the objects taken by the move and the objects yielded by it. The seven changes differ as follows: ^intended-changes

- **eliminate**: an item named by the purpose, a term of an expression or an unknown of a system, appears in the objects taken and is absent from the objects yielded, and the objects yielded keep every other item ("to eliminate the secular term at second order");
- **decouple**: a system whose equations share unknowns is rewritten as subsystems that share no unknown, with the same solutions as the system taken ("to decouple the relaxation of the representation into independent modes");
- **isolate**: among the components of an object, such as its modes, its terms or its scales, the objects yielded keep the components that determine a stated behavior in a stated regime, and set the others aside ("to isolate the mode that sets the long-time behavior");
- **reduce**: a measure of the size of the objects at hand is smaller in the objects yielded than in the objects taken: the number of unknowns, of equations or of independent variables, or the order of an equation ("to reduce the relation to a relation between pure numbers");
- **expose**: the object yielded is equivalent to the object taken, and its form shows a structure or a dependence not shown by the form of the object taken ("to expose the factor that each rate of change carries");
- **close**: a system with fewer independent relations than unknowns receives a relation that brings the two counts to equality, such as a [closure posit](posit.md) ("to close the hierarchy of moments at second order");
- **match**: two approximations of one object, each valid in its own region, are made to agree in a region in which both are valid, which fixes the constants left free by each approximation. The method of matched asymptotic expansions matches an inner and an outer expansion in this way [bender1999] ("to match the inner and the outer expansions").

Each reason states why an alternative was set aside, by a comparison with the move chosen: ^alternative-reasons

- **inapplicable**: a condition of application of the alternative fails for the objects at hand, such as the property that [makes its warrant apply](move.md#^applies-because) or a condition of application of its [scheme](segment-and-scheme.md), so the alternative cannot be carried out on them;
- **inconsistent**: the alternative can be carried out on the objects at hand, and its result would contradict a premise, a posit, or the regime of a warrant used earlier in the derivation;
- **costlier**: the alternative would reach the same end as the move chosen, with more moves, more computation, or a larger object to carry into the moves that follow;
- **losing information**: the objects yielded by the alternative would lack a content required by the end, such as the dependence of a result on a parameter, so the end cannot be reached from them. In this sense, information is lost only when the discarded content is required by the end;
- **already tried without success**: the alternative was carried out at this point in an earlier attempt, and that attempt did not reach the end.

The first two reasons record a constraint of validity, and the last three a strategic choice. The typed reason records that difference, so that the orientation does not present a constraint of validity as a choice.

## Prospectivity

**Prospective means prior in the order of information, not in the time of writing.** An orientation may cite only the objects established before its move. The orientation cites no object yielded by its own move, and no object depending on those yields. A check can verify this order over the dependences stated in the record. By contrast, the time of writing is absent from a record, so a check cannot read it. ^prospective-order

**A reconstruction attributes a plan.** A written proof need not state the plan of the proof activity, as [validity and understanding](derivation.md#^beyond-validity) state. Therefore, an orientation reconstructed from a published proof is a plan attributed by a reader. The reader takes the standpoint of an observer, who asks the question "Why?" of a completed action [anscombe1957]. The provenance of the orientation states the reconstruction, and its alternatives are those considered by the reconstructor.

## Nesting of orientations

**Purposes nest.** "To find the slow dynamics" is the purpose of a [segment](segment-and-scheme.md), and "to eliminate the secular term" is the purpose of a move inside it. The answers to "Why?" form a series in the same way, each end serving a further end [anscombe1957]. Likewise, the plans of a proof are partial and hierarchical [hamami2021]. Therefore, an orientation attached to a segment states the idea of the segment, and the orientations of its moves state the steps of that idea.

## Distinctions

- **An orientation and a warrant answer two questions.** The warrant states why a move is admissible, and the orientation states why the move is relevant at that point.
- **An orientation and an interpretation differ in their object.** An interpretation states the meaning of an item. An orientation states the next step of the derivation. A diagnostic interpretation often supplies the occasion of an orientation. Then, the orientation cites the interpretation rather than restating it.
- **An orientation and the rationale of an act differ in their object**, as the [units of research work](../../processes/units-of-work.md) state.
- **A change and a kind of move may share a token.** The kinds of move `eliminate` and `match` name the [transformation performed](move.md), whereas the changes `eliminate` and `match` name the state at which the move aims. A move of one kind can reach a change of another name: a solvability condition, imposed by a move of kind `impose`, eliminates a secular term.
- **Isolating a component and exposing a structure differ in the part of the object that the move keeps.** A move that isolates yields a part of the object taken: the components that determine the behavior, without the others. A move that exposes yields an object equivalent to the object taken, in another form. A step that both rewrites an object and drops a part of it is two moves, since the [kinds of move](move.md) are atomic, and each move has its own change.
- **Eliminating an item and reducing a size differ in the end that the purpose names.** When a move removes one named unknown, the count of unknowns also decreases. The change is `eliminate` when the end requires the absence of that item, and `reduce` when the end requires the smaller size.
- **The change `reduce` concerns the size of the objects at hand.** A [reduction of one problem to another](../problem/epistemic-problem.md#^reduction) is a relation between two problems, and a reduction between theories is an epistemic activity. A move that reduces the size of its objects may also realize a reduction of problems, but the change records only the decrease of size.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:**
> 	- the schema of practical inference;
> 	- the order of practical reasoning from end to means, and its reversal by the question "Why?";
> 	- means–ends analysis, and the strategic rules of inquiry;
> 	- plans as partial and hierarchical, as cited;
> 	- the matching of two expansions in a region where both are valid.
> - **Proposals:**
> 	- the orientation as the prospective rationale of a move, with its five parts;
> 	- the closed vocabulary of intended changes, and the typed reasons for setting an alternative aside;
> 	- prospectivity defined over the order of information, and the provenance of an orientation;
> 	- the nesting of orientations along segments and moves.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [anscombe1957] ◐ Anscombe, *Intention*, Basil Blackwell, 1957; the order of practical reasoning from end to means, the reverse order elicited by the question "Why?", and the series of answers to that question, checked through [Thompson, "Anscombe, Gertrude Elizabeth Margaret: intention", *Routledge Encyclopedia of Philosophy*](https://www.rep.routledge.com/articles/biographical/anscombe-gertrude-elizabeth-margaret-1919-2001/v-1/sections/intention-1)
- [bender1999] ◐ [Bender & Orszag, *Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic Methods and Perturbation Theory*, Springer, 1999](https://doi.org/10.1007/978-1-4757-3069-2), first published by McGraw-Hill, 1978; ch. 9, "Boundary-layer theory", pp. 419–483, the matching of an inner and an outer expansion, checked through the [chapter record](https://econpapers.repec.org/RePEc:spr:sprchp:978-1-4757-3069-2_9) and the [article on matched asymptotic expansions](https://en.wikipedia.org/wiki/Method_of_matched_asymptotic_expansions), which lists the book among its references without attributing the statement on the overlap region to it
- [hamami2021] ◐ [Hamami & Morris, "Plans and planning in mathematical proofs", *The Review of Symbolic Logic* 14(4), 1030–1065, 2021](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/plans-and-planning-in-mathematical-proofs/6F84A9D231721E7B1B60056F5493D795); plans as partial and hierarchical, checked through the abstract and the [authors' copy](https://www.yacinhamami.com/wp-content/uploads/2019/12/Hamami-Morris-2019-Plans-and-Planning-in-Mathematical-Proofs.pdf)
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); definitory and strategic rules, p. 19, checked through its quotation in [Hamami, "An inquisitive formalization of interrogative inquiry"](https://projects.illc.uva.nl/inquisitivesemantics/assets/files/papers/Hamami2012_IMI.pdf)
- [newell1972] ○ Newell & Simon, *Human Problem Solving*, Prentice-Hall, 1972; means–ends analysis
- [vonwright1971] ◐ von Wright, *Explanation and Understanding*, Cornell University Press, 1971; the schema of practical inference, checked through [Raatikainen, "Explanation and understanding revisited"](https://trepo.tuni.fi/bitstream/10024/134664/1/Raatikainen_von_Wright_100.pdf)
