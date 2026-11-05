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

The claim of an answer holds a reading and, once formalized, an expression. Three parts of its content had no home. A claim takes commitments for granted without asserting them, and no field recorded them, so they were absorbed silently. The proposals asked whether propositional content needs a data type of its own. A conditional or a counterfactual statement was written as a plain claim, so the antecedent of a conditional read as asserted, and a counterfactual named no intervention.

## Decision

**Propositional content is the tree of an expression.** The [expression syntax](expression-syntax.md) gives each formula a term structure, whose head symbols are the constructors of an algebraic data type. The connectives `and`, `or`, `not` and `implies` are constructors of that type. The canonical operators gain two binders, `forall` and `exists`, which quantify over the indices that they bind, as in `exists_{i}( lambda(i) > 0 )`. The four constructs that the proposals required find these homes:

- quantification over an open domain: the binders `forall` and `exists`, and the places of a signature, over which a law ranges;
- a condition or a regime: the domain of an answer, the range of a law and the regime of a warrant;
- approximate equality: declined, since an approximation without a stated error asserts nothing checkable, and the method states the error in the class of a warrant or in a tolerance;
- use and mention: an expression uses a claim, and a dotted identifier mentions it.

**A claim lists its presuppositions.** Each presupposition states its content, its strength and the record that holds it, as the [theory of presupposition](../epistemology/objects/knowledge/presupposition.md) defines them. A presupposition differs from a ground by the [negation test](../epistemology/objects/knowledge/presupposition.md#^presupposition-test). An undischarged presupposition of the strength `provisional` or `axiom` enters the view of exposure. A presupposition of the strength `axiom` names a law of a background or a concept record, and a check verifies that it names one.

**A conditional claim is an implication.** Its expression is written with `implies`, and its attitude applies to the whole implication, as the [conditional claim](../epistemology/vocabulary/representations/claim-and-hypothesis.md#^conditional-claim) states. No field marks the conditional, since the expression already states it.

**A counterfactual claim names its interventions.** The field `interventions` of the claim names a design of the kind `experiment` or `simulation-run`, whose protocol states the admissible interventions, as the [counterfactual claim](../epistemology/vocabulary/representations/claim-and-hypothesis.md#^counterfactual-claim) requires. A check verifies that the design has that kind and states its intervention.

## Constraints that decide the content

- **A silent commitment is a hidden dependency.** When the truth of a claim rests on an unstated presupposition, the claim stays exposed to it, and the exposure is reported only once the record states the presupposition.
- **One field per fact.** The expression already states a conditional, so a modality field would restate it, as the decision on a [single field per fact](single-field-per-fact.md) forbids.
- **No inference at run time.** The strength of a commitment changes by an authored change only, so no tool promotes a local role to an axiom.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| A data type of propositional content apart from the expression syntax | Pattern matching on constructors named for logic | The tree of an expression is already that type, with its head symbols as constructors, so a second type would duplicate it |
| An operator of approximate equality | A short form for "of the order of" | An approximation without a stated error asserts nothing checkable; the error belongs to a warrant or a tolerance |
| Presuppositions as grounds of the role `assumption` | No new field | A ground supports the truth of the claim, whereas a presupposition supports the claim and its denial alike, so the failure of each reaches the claim differently |
| A field `modality` with the values `asserted`, `conditional` and `counterfactual` | The modality is read from one field | A conditional is already stated by its expression; a counterfactual needs its family of interventions, which a value of a closed list cannot name |
| The family of interventions stated in prose | No reference to another record | No check can verify that the family is admissible, nor that an experiment or a simulation carries it out |

## Consequences

- The claim of an answer gains the fields `presuppositions` and `interventions`, with their specification, their schema and the vocabulary of strengths.
- The canonical operators gain the binders `forall` and `exists`, each yielding a pure number under the rules of dimension.
- The checks gain the report of an axiom held by no background law and no concept, and of interventions that name no experiment or simulation run with a stated intervention.
- The view of exposure gains the undischarged presuppositions of each answer.
- The two remaining entries of the proposals for the derivation framework are settled, and the note of those proposals is retired.
