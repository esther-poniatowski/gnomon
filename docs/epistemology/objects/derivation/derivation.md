---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Derivation
  - Derivation record
---
# Derivation

> [!QUESTION] Goal: what is a derivation, and what must its record state so that it conveys why its consequences hold, beyond the validity of its steps?

A **derivation** is the reasoning that establishes consequences from premises. Its premises are the laws of models and backgrounds, the grounds of an answer, and the posits introduced by the derivation itself. The record of a derivation states why each consequence holds, and how the derivation reached it. The [units of research work](../../processes/units-of-work.md#^work-unit-criterion) fix the place of a derivation among the records of a piece of work: a derivation holds the intermediate objects cited by no other record.

## Problems to prove and problems to find

Two kinds of problem start a derivation. A **problem to prove** gives a statement, and asks whether it holds. A **problem to find** asks for an unknown that satisfies a condition, from given data [polya1945]. Pappus already distinguished two kinds of analysis. The theoretical kind seeks the truth of a statement, and the problematical kind "serves to carry out what was desired to do", a construction [beaney2024]. ^prove-and-find

Every problem to prove is a problem to find, whose unknown is the truth of a stated claim. The converse reduction fails: a construction does not reduce to a statement given in advance, since its result may be unknown when the derivation starts. Therefore, a derivation may seek an unknown whose form, and even whose type, is not yet fixed, as the [sought of a derivation](sought.md) states.

## Validity and understanding

**The validity of each step is necessary, and not sufficient.** A proof bears mathematical knowledge beyond its theorem: its methods and its strategies transfer to other problems [rav1999]. Understanding a proof includes the ability to motivate its steps, beyond checking that each step is correct [avigad2008]. A proof also follows a plan. A written proof is a report of the proof activity, and the plan of that activity need not be stated in it [hamami2021]. ^beyond-validity

Three questions about each step receive separate answers:

- **Why is the step admissible?** Its warrant answers, after the definitory rules that state the admissible moves of an inquiry [hintikka2007].
- **Why is the step taken at that point?** Its orientation answers, after the strategic rules that state the good moves [hintikka2007].
- **What do the objects of the step mean?** Its interpretations answer.

## Parts of a derivation

Each of the seven kinds of unit of a derivation is stated in its own note:

- the **sought**, the unknown or the statement sought by the derivation, with its degree of determinacy: [sought of a derivation](sought.md);
- the **posits**, the premises introduced on trial by the derivation, and their tests: [posits and their tests](posit.md);
- the **moves**, the steps that transform intermediate objects, each licensed by a warrant: [moves and warrants](move.md);
- the **orientations**, the prospective reasoning that identifies the next relevant move: [orientation of a move](orientation.md);
- the **interpretations**, the meanings assigned to the items of a derivation: [interpretation in a derivation](interpretation.md);
- the **segments**, the groups of moves serving one sought, each citing the scheme applied, when one applies: [segments and schemes](segment-and-scheme.md);
- the **outcomes**, with the understanding gained beyond them: [consequences, impasses and understanding](consequences-and-understanding.md).

## Discovery and justification within a derivation

**A derivation constructs its result from its premises by licensed moves, and the acts producing its guesses carry the context of discovery.** The context of discovery concerns the finding of a hypothesis, and the context of justification concerns its defense [reichenbach1938]. A guessed form, such as an ansatz suggested by a numerical exploration, enters the derivation as a posit. Then, the derivation establishes consequences from that posit and from its other premises. A later test confirms or refutes the posit, so that the guess and its confirmation stay apart. Pappus describes a related order. Analysis assumes the sought as already obtained and works back to accepted principles, and the proof runs the analysis in reverse [beaney2024]. A derivation assumes a posit, never the sought itself, so that it requires no target in advance. ^deductive-construction

## Outcomes and role

Each sought of a derivation ends in an outcome of one of three kinds, so that one derivation may combine several outcomes:

- **consequences**: statements established by the derivation, each answering a sought;
- an **impasse**: an obstacle left by the derivation, so that a sought stays without answer;
- a **refutation**: a counterexample or a refuting test, against a posit, a lemma or a claim.

The epistemic role of a derivation is to license tracing a consequence, or an obstacle, back to its premises, as the [epistemic roles](../status/epistemic-objects.md#^unit-roles) state.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:**
> 	- the two kinds of problem and the two kinds of analysis;
> 	- the knowledge borne by a proof beyond its theorem, and the understanding of a proof as the ability to motivate its steps;
> 	- the plan of a proof and its report; the definitory and strategic rules;
> 	- the contexts of discovery and justification, and the order of analysis and proof, as cited.
> - **Proposals:**
> 	- the problem to prove as a problem to find whose unknown is the truth of a claim;
> 	- the three separate answers about each step: warrant, orientation and interpretations;
> 	- the seven kinds of unit of a derivation;
> 	- the construction of a result from posits by licensed moves, the guess staying with the act that produced it;
> 	- the three outcomes, and the epistemic role of a derivation.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [avigad2008] ◐ [Avigad, "Understanding proofs", in Mancosu (ed.), *The Philosophy of Mathematical Practice*, Oxford University Press, 316–353, 2008](https://academic.oup.com/book/2780/chapter/143298605); the ability to motivate the steps of a proof, p. 328, checked through secondary sources
- [beaney2024] ◐ [Beaney & Raysmith, "Analysis", *The Stanford Encyclopedia of Philosophy*, revised 2024](https://plato.stanford.edu/entries/analysis/s2.html); §2, Pappus on theoretical and problematical analysis, and the proof as the reverse of analysis
- [hamami2021] ◐ [Hamami & Morris, "Plans and planning in mathematical proofs", *The Review of Symbolic Logic* 14(4), 1030–1065, 2021](https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/plans-and-planning-in-mathematical-proofs/6F84A9D231721E7B1B60056F5493D795); the plan of a proof as the plan of its agents, and the written proof as a report of the proof activity, checked through the abstract and the [authors' copy](https://www.yacinhamami.com/wp-content/uploads/2019/12/Hamami-Morris-2019-Plans-and-Planning-in-Mathematical-Proofs.pdf)
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); definitory and strategic rules, p. 19, checked through its quotation in [Hamami, "An inquisitive formalization of interrogative inquiry"](https://projects.illc.uva.nl/inquisitivesemantics/assets/files/papers/Hamami2012_IMI.pdf)
- [polya1945] ◐ Pólya, *How to Solve It: A New Aspect of Mathematical Method*, Princeton University Press, 1945; the unknown, the data and the condition of a problem to find, checked through a [summary of the second edition](https://math.ucr.edu/~res/math133/polya.pdf), 1957
- [rav1999] ◐ [Rav, "Why do we prove theorems?", *Philosophia Mathematica* 7(1), 5–41, 1999](https://doi.org/10.1093/philmat/7.1.5); proofs, rather than theorems, as the bearers of mathematical knowledge, checked through secondary summaries
- [reichenbach1938] ○ [Reichenbach, *Experience and Prediction: An Analysis of the Foundations and the Structure of Knowledge*, University of Chicago Press, 1938](https://catalogo.biblio.unc.edu.ar/Record/ffyh.39329)
