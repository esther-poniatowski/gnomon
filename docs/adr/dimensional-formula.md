---
tags:
  - decision
status: accepted
created: 2026-11-04
revised: 2026-11-04
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Dimensional formula
  - Dimensional formula of a quantity
---
# Dimensional formula of a quantity

> [!QUESTION] Goal: where does a record state the dimension of a quantity, so that a check can test the dimensional homogeneity of a law?

The value set of a quantity holds its dimensionality, and its signature holds its indexing. No field stated its [dimension](../epistemology/vocabulary/quantities/dimension.md) in the sense of dimensional analysis: the change of its numerical value when the units of the base quantities are rescaled. Therefore, no check could test the dimensional homogeneity of a law, and a move warranted by the Π-theorem could cite no formula supporting its warrant.

## Decision

**A quantity may state its dimensional formula.** The optional attribute `dimensional_formula` of a quantity holds a monomial over base dimensions, such as `M L T^-2`, or `1` for a pure number. The attribute applies to parameters, variables and observables alike.

**The base dimensions come from two sources.** The package data declare the seven base dimensions of the International System of Quantities. The operator record of a problem may declare further **base scales**, such as the scale of the parameters and the scale of the loss of a learning system, next to the operators added by the problem to the canonical set.

**Each operator states how dimensions combine.** The operator registry gives each operator a rule of dimension:

- a product adds the exponents of its factors, and a quotient subtracts them;
- a power multiplies the exponents by its exponent, and that exponent must be a pure number;
- a derivative divides the dimension of its argument by the dimension of its variable, and an integral multiplies by it;
- the argument of an exponential, a logarithm or a trigonometric function must be a pure number;
- a sum, a difference, a minimum and a maximum require that their terms share one formula;
- the number zero is homogeneous with every formula, so an equation such as `mean_{x}(p) = 0` is homogeneous.

**A check tests homogeneity.** The terms of a sum, and the two sides of an equation, must share one dimensional formula, as the [dimensional homogeneity](../epistemology/vocabulary/quantities/dimension.md#^dimensional-homogeneity) of a law requires. A tool computes the formula of each expression by the declared rules, as the [admitted computations](no-run-time-inference.md#^admitted-computation) allow. When a law names a quantity without a dimensional formula, the law is left unchecked. In a problem that declares a formula for at least one quantity, the check reports that gap, so that a problem that does not use dimensional analysis receives no report.

## Constraints that decide the attribute

- **The word "dimension" has three senses.** In machine learning, the word names dimensionality, already stated by the value set of a quantity. An attribute named `dimension` would read in that sense.
- **Dimensional reasoning reaches beyond physics.** A problem whose quantities carry no physical unit can still declare independent base scales, so the base dimensions cannot be fixed by the package alone.
- **The computation must follow a declared rule.** A homogeneity check reads authored formulas and applies the rules of the operator registry, so no rule of dimension may be inferred from the meaning of an operator.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| An attribute named `dimension` | The name follows the usage of dimensional analysis | The name collides with dimensionality, its common sense in machine learning |
| Units in place of dimensions, such as `kg m s^-2` | A unit fixes the numerical values as well as their transformation | A model often has no chosen unit, and homogeneity depends on the dimension alone, so a unit would demand a choice that the claim does not need |
| A required attribute on every quantity | Every law is checked | Many quantities, such as counts and indices, are pure numbers by construction, and the requirement would force a value that the author has not considered |
| The seven base dimensions only | One canonical set, with no declaration per problem | The quantities of a learning system or of a formal model have base scales that are not physical |
| No attribute | No change to the records | No check tests homogeneity, and a move warranted by the Π-theorem cites no formula |

## Consequences

- The specification of a quantity gains the optional attribute `dimensional_formula`, and the schemas of the records that declare quantities gain it with the grammar of a monomial.
- The package data gain the base dimensions, and the operator record of a problem gains its base scales.
- The operator registry gains a rule of dimension for each operator.
- The checks gain a homogeneity check, tested on planted laws that fail it, and a report of the laws left unchecked in a problem that declares formulas.
- An index set declares no formula, so a derivative along an index, such as a time derivative, stays undecided.
- A move of a [derivation record](derivation-record.md) warranted by the Π-theorem cites the dimensional formulas of its quantities, as the property that makes its warrant apply.
