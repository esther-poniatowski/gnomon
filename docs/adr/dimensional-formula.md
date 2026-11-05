---
tags:
  - decision
status: accepted
created: 2026-11-04
revised: 2026-11-05
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Dimensional formula
  - Dimensional formula of a quantity
---
# Dimensional formula of a quantity

> [!QUESTION] Goal: where does a record state the dimension of a quantity, so that a check can test the dimensional homogeneity of a law?

The value set of a quantity holds its dimensionality, and its signature holds its indexing. No field stated its [dimension](../epistemology/vocabulary/quantities/dimension.md) in the sense of dimensional analysis: the change of its numerical value when the units of the base quantities are rescaled. Therefore, no check could test the dimensional homogeneity of a law, and a move warranted by the Π-theorem could cite no formula supporting its warrant.

## Decision

**A quantity may state its dimensional formula.** The optional attribute `dimensional_formula` of a quantity holds a monomial over base dimensions, such as `M L T^-2`, or `1` for a pure number. A fractional exponent is written in parentheses, as in `T^(1/2)`, so that the formula reads as the expression syntax reads it. The attribute applies to parameters, variables, observables and the features of a manifestation alike. An index set may state it too, for the coordinate that it collects, such as `L` for a spatial domain or `T` for a time axis; amended on 2026-11-04, and on 2026-11-05 for the features.

**The base dimensions come from two sources.** The package data declare the seven base dimensions of the International System of Quantities. The operator record of a problem may declare further **base scales**, such as the scale of the parameters and the scale of the loss of a learning system, next to the operators added by the problem to the canonical set.

**Each operator states how dimensions combine.** The operator registry gives each operator a rule of dimension:

- a product adds the exponents of its factors, and a quotient subtracts them;
- a power multiplies the exponents by its exponent, and that exponent must be a pure number;
- a derivative divides the dimension of its argument by the dimension of its variable, which may be an index set; a gradient and a divergence divide by the dimension of the coordinates that they name, and a Laplacian by its square; a Jacobian divides by the dimension of its coordinates, and its point of evaluation must share that dimension;
- an operator that a problem declares with the rule `pure-argument`, such as an exponential, a logarithm or a trigonometric function, requires a pure argument; the canonical set holds no such operator;
- a sum and a difference require that their terms share one formula, and a minimum, a maximum, a mean or a sum over the indices that it binds preserves the formula of its body;
- a connective, `and`, `or`, `not`, `implies`, `forall` or `exists`, takes statements and yields a statement; a relation, such as `depends_on`, yields a statement and checks each of its arguments on its own; a membership `x in S` states the type of `x` and compares no formulas;
- a scaling `S ~ r^z` compares no formulas, since its prefactor may carry any formula, so the check counts it as checked;
- a limit `m -> v` compares its two sides as an equation does;
- the number zero is homogeneous with every formula, so an equation such as `mean_{x}(p) = 0` is homogeneous.

**A check tests homogeneity.** The terms of a sum, and the two sides of an equation, must share one dimensional formula, as the [dimensional homogeneity](../epistemology/vocabulary/quantities/dimension.md#^dimensional-homogeneity) of a law requires. A tool computes the formula of each expression by the declared rules, as the [admitted computations](no-run-time-inference.md#^admitted-computation) allow. The check reads every field that the [registry of dimensions](../../src/gnomon/data/registries/dimensions.yml) lists as holding a statement: the laws and their ranges, the conditions of the quantities, the constraints of the external systems, the criteria and the manifestations of a phenomenon, and the regimes and bounds of an operation. A statement that names a quantity without a dimensional formula, or an operator that states no rule, is left unchecked. In a problem that declares a formula for at least one quantity, index set or feature, the check reports that gap with its cause, so that a problem that does not use dimensional analysis receives no report. The rule `unchecked` is a declared waiver, and its operator is not reported.

**A check reports the formulas that cannot hold together.** A malformed formula is reported where it is declared, a symbol to which two records seen together give two formulas is reported, and a base scale of a problem that takes the symbol of a base dimension of the package is reported. Amended on 2026-11-05: the fields read, the report of the operators without a rule, the rules of the connectives and the relations, and the reports of conflicting formulas and colliding bases. Amended again on 2026-11-05: the rules of the relations `~` and `->`.

## Limits of the attribute

- **One formula per quantity.** A monomial assumes that every component of a quantity shares one dimension. A vector of mixed dimension, such as a point of phase space or the parameters of layers of different scales, has no single formula, and the record leaves it without one.
- **No formula that depends on an index.** A moment of order $p$ of a velocity increment has the formula $(L T^{-1})^p$. No monomial states a formula of this form, so such a quantity declares no formula, and the statements naming it stay unchecked.
- **No rule reads the indices that a binder binds.** An integral or a transform multiplies the formula of its body by the formula of its variable, so the rules of the registry cannot state it; the transform `ft` is therefore waived as `unchecked`, and the canonical set holds no integral.

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
| Gradient, divergence and Laplacian over an implicit domain | `grad(u)` stays short | The variable of differentiation is unstated, so for a field over space and time no rule can choose the formula to divide by; amended on 2026-11-04 by naming the coordinates as a second argument |
| No formula on index sets | The attribute stays on quantities alone | A derivative along a time axis or a spatial domain stays undecided, so the evolution laws of a field are never checked; added on 2026-11-04 |
| No attribute | No change to the records | No check tests homogeneity, and a move warranted by the Π-theorem cites no formula |

## Consequences

- The specification of a quantity gains the optional attribute `dimensional_formula`, and the schemas of the records that declare quantities gain it with the grammar of a monomial, as a pattern that the validation of a record applies.
- The package data gain the base dimensions, and the operator record of a problem gains its base scales.
- The operator registry gains a rule of dimension for each operator.
- The checks gain a homogeneity check, tested on planted laws that fail it, and a report of the laws left unchecked in a problem that declares formulas.
- An index set may declare a formula, so that a derivative along an index, such as a time derivative, is checked; in a problem that declares formulas, a derivative along an index without one is reported as a gap.
- A move of a [derivation record](derivation-record.md) warranted by the Π-theorem cites, as the property that makes its warrant apply, a magnitude interpretation whose grounds name the quantities whose formulas the theorem uses.
