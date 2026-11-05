---
tags:
  - decision
status: accepted
created: 2026-11-05
revised: 2026-11-05
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Content of a claim
---
# Content of a claim

> [!QUESTION] Goal: how does a claim state its propositional content, the commitments that it takes for granted, and a content that is conditional or counterfactual?

The claim of an answer holds a reading and, once formalized, an expression. The proposals for the derivation framework, `docs/proposals/derivation-framework.md` at commit c5a1614, asked three questions about that content. First, whether propositional content needs a data type of its own. Second, where the commitments that a claim takes for granted are recorded, since a claim that absorbs them silently hides a dependency. Third, how a conditional or a counterfactual statement is written, since a conditional written as a plain claim reads its antecedent as asserted, and a counterfactual names no intervention. Amended on 2026-11-05: a presupposition carries no strength, is held by a statement, and lives in one of four homes; the interventions of a counterfactual are a list.

## Decision

**Propositional content is the tree of an expression.** The [expression syntax](expression-syntax.md) gives each formula a term structure, whose head symbols are the constructors of an algebraic data type. The connectives `and`, `or` and `not`, and the relation `implies`, are constructors of that type. The canonical operators gain two binders, `forall` and `exists`, which quantify over the indices of a declared index set, as in `exists_{i}( lambda(i) > 0 )`. The four constructs that the proposals required find these homes:

- quantification: over an indexed domain, the binders `forall` and `exists`; over the values that a law ranges over, the places of its signature;
- a condition or a regime: the domain of an answer, the range of a law and the regime of a warrant;
- approximate equality: declined, since an approximation without a stated error asserts nothing checkable, and the method states the error in the class of a warrant or in a tolerance;
- use and mention: an expression uses a claim, and a dotted identifier mentions it.

**Each presupposition has one home.** The [theory of presupposition](../epistemology/objects/knowledge/presupposition.md) places each commitment that a claim takes for granted:

- a question records its presuppositions, and every direct answer inherits them;
- a quantity defined by a condition carries the existence that the condition presupposes;
- a claim records the further presuppositions that its own terms incur, each with its reading, its expression once formalized, and the statement that holds it;
- a relation `presupposes` links an answer to the answer that establishes one of its commitments.

A presupposition of a claim is held by a law of a background or of a model, or by a consequence of a derivation. An undischarged presupposition exposes the answer, and a held presupposition passes on the exposure of its holder.

**A conditional claim is an implication.** Its expression is written with `implies`, read as a material implication, and its attitude applies to the whole implication, as the [conditional claim](../epistemology/vocabulary/representations/claim-and-hypothesis.md#^conditional-claim) states. No field marks the conditional, since the expression already states it.

**A counterfactual claim names its interventions.** The field `interventions` of the claim lists each admissible intervention, as the [counterfactual claim](../epistemology/vocabulary/representations/claim-and-hypothesis.md#^counterfactual-claim) requires. An entry names an experiment or a simulation run whose protocol states the intervention, or the parameter or the variable of a model that the intervention sets, for a claim evaluated on the model. Naming its interventions marks the claim as counterfactual.

## Constraints that decide the content

- **A silent commitment is a hidden dependency.** When the truth of a claim rests on an unstated presupposition, the claim stays exposed to it, and the exposure is reported only once the record states the presupposition.
- **One field per fact.** The expression states a conditional, and the list of interventions states a counterfactual. The question states its own presuppositions, and the relation `presupposes` states a commitment that another answer holds. Therefore, no field restates these facts, as the decision on a [single field per fact](single-field-per-fact.md) requires.
- **No inference at run time.** A presupposition is discharged by an authored change of the record only, so no tool infers that a statement holds it.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| A data type of propositional content apart from the expression syntax | Pattern matching on constructors named for logic | The tree of an expression is already that type, with its head symbols as constructors, so a second type would duplicate it |
| An operator of approximate equality | A short form for "of the order of" | An approximation without a stated error asserts nothing checkable; the error belongs to a warrant or a tolerance |
| Presuppositions as grounds of the role `assumption` | No new field | A ground supports the truth of the claim, whereas the failure of a presupposition leaves neither the claim nor its negation correct |
| A strength of each presupposition: a local role, a provisional commitment or an axiom | The scope of a commitment is read from one field | The strength separates no check: the failure of a local role leaves the claim describing no situation, as the failure of a provisional commitment does, and an axiom is a presupposition held by a law, so the holder states it |
| Every presupposition recorded on the claim that it concerns | One place to read them | A presupposition of a question, or the existence that a condition presupposes, would be restated on every claim that inherits it |
| A field `modality` with the values `asserted`, `conditional` and `counterfactual` | The modality is read from one field | A conditional is already stated by its expression, and a counterfactual by the list of its interventions |
| The interventions stated in prose | No reference to another record | No check can verify that an intervention is admissible, nor that an experiment, a simulation or a model carries it out |

## Consequences

- The claim of an answer gains the fields `presuppositions` and `interventions`, with their specification and their schema.
- The canonical operators gain the binders `forall` and `exists`, each yielding a statement under the rules of dimension.
- The checks gain three reports:
	- a presupposition held by no law and no consequence of a derivation;
	- a presupposition restating one of the question;
	- an intervention that names no experiment, no simulation run stating an intervention and no quantity of a model.
- The view of exposure gains the undischarged presuppositions of each answer, the holders of the others, and the answers that each answer presupposes.
- The two remaining entries of the proposals for the derivation framework are settled, and the note of those proposals is retired.
