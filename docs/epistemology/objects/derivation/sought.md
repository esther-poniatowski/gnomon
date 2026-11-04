---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Sought of a derivation
  - Sought
---
# Sought of a derivation

> [!QUESTION] Goal: what does a derivation seek, and how can it seek a result that it cannot state in advance?

The **sought** of a derivation is the target of its reasoning: a statement to prove, or an unknown to find under a condition, as the [two kinds of problem](derivation.md#^prove-and-find) distinguish. A problem to find has an unknown, data and a condition, and the condition may or may not suffice to determine the unknown [polya1945].

## Degrees of determinacy

A sought may leave its result unstated, and even the type of its result. Three degrees of determinacy are distinguished: ^sought-determinacy

| Degree | Known when the derivation starts | Example |
| --- | --- | --- |
| **determinate** | the type of the unknown and its condition | the amplitude equation obeyed by the slow envelope of a pattern near onset |
| **typed** | the type of the unknown, without a condition fixing it | the law setting the scale of a delay |
| **open** | only a direction of inquiry, without a type or a condition | "what governs the long-time behavior of a representation?" |

A determinate sought states its condition, whether or not that condition suffices to determine the unknown. Once its type is known, the unknown takes one of five types:

- a law;
- a value or a bound;
- an object, such as a witness or a counterexample;
- a classification;
- the truth of a stated claim, for a problem to prove.

**No sought requires its result in advance.** A sought states only the facts known when the derivation starts. Therefore, an open sought keeps a genuine construction possible. The derivation explores, and the consequences reached answer the sought as they are found. An [open question](../answer/answer-form.md#^question-fixes-type) of an inquiry has no answer type yet. Such a question is an open sought at the grain of the inquiry. ^no-required-target

## Root and subordinate soughts

**The root sought of a derivation is the current state of the record served by the derivation.** That record is a question, a proof obligation, or a law or an operation of a derived model stated in advance for the derivation to prove. The derivation does not restate it. A derivation constructing a law or an operation serves no such record. Then, the derivation declares its own root sought, open or typed, and the record of the law or the operation states the consequence once the derivation has found it. Thus, no record requires the result in advance.

The root sought can sharpen while the derivation proceeds. When the root sought is an open question, sharpening it fixes the answer type of that question. That change belongs to the question, so it is an act of the itinerary and not a move of the derivation. While the root sought stays open, the derivation states its consequences as laws or as properties of a model, and no consequence yet answers the question.

**A subordinate sought is a sought set by the derivation for itself.** The subordinate sought corresponds to the auxiliary problem of Pólya: a problem solved for the sake of another [polya1945]. An [orientation](orientation.md) sets a subordinate sought when its purpose is to determine an unknown. The consequence answering a subordinate sought is a [lemma](consequences-and-understanding.md#^lemma). A subordinate sought becomes a serving question of the inquiry only when it is posed apart from the derivation, or when an impasse generates it. The [sources of serving questions](../../processes/inquiry/question-decomposition.md#^serving-sources) state both routes.

## Sharpening and replacement

Two changes of a sought differ by their cause:

- **Sharpening**: the sought becomes more determinate as the construction reveals which unknowns can be found. The earlier sought was not wrong, only undetermined, so sharpening is none of the [kinds of revision](../knowledge/grounds-and-dependence.md#^revision-kinds). ^sought-sharpening
- **Replacement**: a subordinate sought proves ill-posed and is replaced, with the reason for the replacement. *Example*: a proof depends on a hidden condition, and that condition is made explicit and built into the conjecture. This repair is the lemma-incorporation of Lakatos [lakatos1976]. ^sought-replacement

A replacement stays local to the derivation. By contrast, a change of a type already fixed for a question is a revision of that question, of the kind *reorientation*.

## Slots

A construction often introduces its unknown while it proceeds. *Example*: a multiple-scale expansion introduces the amplitude of the pattern, and then the derivation determines the evolution of that amplitude. Such an unknown is a **slot**: a symbol introduced by a move or by a posit, and bound later by a move of the derivation. Slots are introduced by moves and posits only. Therefore, a sought need not name the objects of its result before the derivation creates them.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the unknown, the data and the condition of a problem to find; the auxiliary problem; lemma-incorporation, as cited.
> - **Proposals:**
> 	- the three degrees of determinacy of a sought, and the types of its unknown;
> 	- the rule that no sought requires its result in advance;
> 	- the root sought read from the record served by the derivation, and its sharpening as an act on the question;
> 	- the distinction between sharpening and replacement;
> 	- the slot, introduced by a move or a posit and not by the sought.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [lakatos1976] ◐ Lakatos, *Proofs and Refutations: The Logic of Mathematical Discovery*, Worrall & Zahar (eds.), Cambridge University Press, 1976; lemma-incorporation and proof-generated concepts, checked through [secondary sources](https://arxiv.org/pdf/1310.1625)
- [polya1945] ◐ Pólya, *How to Solve It: A New Aspect of Mathematical Method*, Princeton University Press, 1945; the unknown, the data and the condition of a problem to find, and the auxiliary problem, checked through a [summary of the second edition](https://math.ucr.edu/~res/math133/polya.pdf), 1957
