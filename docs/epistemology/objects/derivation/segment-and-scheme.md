---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Segments and schemes
  - Segment of a derivation
  - Scheme of derivation
  - Proof technique
---
# Segments and schemes

> [!QUESTION] Goal: how do the moves of a derivation group under one idea, and how is a way of deriving reused across derivations?

A derivation follows ideas larger than one move, such as a reduction to the linearized problem or the search for a conserved quantity. A **segment** groups the moves of one derivation serving one sought under one idea. A **scheme** states such an idea apart from any derivation, so that many derivations can apply it.

## Segment

A segment groups contiguous moves serving one [sought](sought.md). Its idea is the purpose of the [orientation](orientation.md) attached to the segment, and the orientations of its moves state the steps of that idea. The plans of a proof are partial and hierarchical [hamami2021]. The nesting of segments states that hierarchy in the record. A derivation with a single idea is its own segment.

**A segment states its inputs and its outputs.** These two statements bridge the [routine moves](move.md#^non-routine) omitted from the record, so that the dependence from the premises to the consequences stays traceable. Without them, an omitted move would cut every route through the segment, and the moves on either side would appear idle.

## Scheme

A **scheme** is a reusable way of deriving, such as:

- linear stability analysis;
- a dominant balance;
- a multiple-scale expansion with a solvability condition;
- a Lyapunov argument;
- the proof technique of a problem.

A scheme is a [design](../../../adr/design-record.md) of kind *scheme*, written by a researcher and cited by each derivation applying it. A scheme shares the inputs, the steps and the modes of failure of every design, and it adds the parts below, which a method lacks.

A scheme states four parts:

- the **conditions of application**: the situations admitting the scheme;
- the **steps** and the **posits** prescribed by the scheme, such as the slow scale and the ansatz of a multiple-scale expansion;
- the **effect** of a successful application: the type of consequence yielded;
- the **modes of failure**, each with the situation announcing it, at the boundary of the conditions of application or where a posit fails, and the patch required.

Automated proof planning states its methods in the same form. A method specifies a tactic by two parts: the preconditions of the tactic, and the effects of its successful application. A planner composes methods by matching the preconditions of later tactics to the effects of earlier ones [bundy2002]. A critic has the form of a method. Its preconditions describe the situations leading a tactic to fail, and its instructions patch the failed proof in place of a tactic [bundy2002]. The modes of failure of a scheme play the part of these critics. ^scheme-form

The critical questions of an argumentation scheme state the conditions defeating an argument of that scheme [walton2008]. The modes of failure of a scheme of derivation play the same part.

## Segment and scheme

A segment **applies** a scheme when its moves fill the steps of that scheme under its conditions of application. When the idea of a segment has not been stated apart, the segment applies no scheme. A scheme states a way of deriving. The record of a derivation as one instance of a scheme is the pattern of the derivation, stated with its [consequences](consequences-and-understanding.md).

---
## Sources

> [!NOTE] Status of the claims
> - **Established:**
> 	- plans as partial and hierarchical;
> 	- methods with preconditions and effects, composed by matching, and critics as methods for failures;
> 	- critical questions of defeasible argumentation schemes, as cited.
> - **Proposals:**
> 	- the segment as the group of moves that serves one sought under one orientation;
> 	- the inputs and the outputs of a segment, as the bridge over omitted moves;
> 	- the scheme as a design of kind scheme, with its conditions of application, steps, posits, effect and modes of failure;
> 	- the modes of failure of a scheme, in the part of critics and of critical questions.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bundy2002] ◐ [Bundy, "A critique of proof planning", in Kakas & Sadri (eds.), *Computational Logic: Logic Programming and Beyond*, Part II, LNAI 2408, Springer, 160–177, 2002](https://doi.org/10.1007/3-540-45632-5_7); methods with preconditions and effects, and proof critics after Ireland, §1.1, read on the [author's copy](https://www.inf.ed.ac.uk/publications/online/1311.pdf)
- [hamami2021] ◐ [Hamami & Morris, "Plans and planning in mathematical proofs", *The Review of Symbolic Logic* 14(4), 1030–1065, 2021](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/plans-and-planning-in-mathematical-proofs/6F84A9D231721E7B1B60056F5493D795); plans as partial and hierarchical, checked through the abstract and the [authors' copy](https://www.yacinhamami.com/wp-content/uploads/2019/12/Hamami-Morris-2019-Plans-and-Planning-in-Mathematical-Proofs.pdf)
- [walton2008] ◐ Walton, Reed & Macagno, *Argumentation Schemes*, Cambridge University Press, 2008; each scheme paired with critical questions that state its defeasibility conditions, checked through the [review in *Notre Dame Philosophical Reviews*](https://ndpr.nd.edu/reviews/argumentation-schemes/)
