---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Posits and their tests
  - Posit
---
# Posits and their tests

> [!QUESTION] Goal: which premises may a derivation introduce on trial, and when does a consequence that rests on such a premise hold without condition?

A **posit** is a premise introduced by the derivation itself, rather than inferred or taken from another record. Every posit is stated in the record, with its origin and its tests. A posit lets a construction proceed before its justification. The derivation assumes a form or a relation, derives its consequences, and leaves the justification to a test. Thus, the guess and its justification stay apart, as the [construction from posits](derivation.md#^deductive-construction) requires.

## Kinds of posit

| Kind | Assumption | Example |
| --- | --- | --- |
| **ansatz** | a trial form of an object, possibly of the sought result itself, with parameters left undetermined | a self-similar form $u = t^{\alpha} f(x/t^{\beta})$, whose exponents and profile the derivation determines |
| **closure** | a relation closing an intermediate system of equations | a moment of a hierarchy expressed through lower moments |
| **choice of relevant quantities** | the quantities entering a relation | a spectrum depending only on the dissipation rate and the wavenumber |
| **complete similarity** | complete similarity of the relation in a dimensionless group, so that the group can be dropped | the radius of a strong blast wave set by its energy, the ambient density and the time alone |
| **incomplete similarity** | incomplete similarity of the relation in a dimensionless group | a spreading law with an anomalous exponent determined by the derivation |

The [dimension of a quantity](../../vocabulary/quantities/dimension.md) defines complete and incomplete similarity. A posit fixes at most the form of a result, never the result itself. An ansatz on the form of the result leaves its parameters undetermined, and under incomplete similarity even its exponent comes out of the derivation.

Two neighbors of a posit lie in other homes. A change of variables cannot be false, so it is a [move](move.md) warranted by a definition, not a posit. When a closure adds a law over the quantities of a model, the closure is an operation of a derived model, as the [object acted on](../../processes/units-of-work.md) decides.

## Origin of a posit

The origin of a posit states the source of the guess, among four:

- an act of the itinerary, such as an abduction, a simulation or an analogy;
- a published source;
- a [scheme](segment-and-scheme.md) prescribing the posit;
- no traceable origin, for an insight that left no record.

When an act produced the guess, the derivation names that act and does not restate it.

## Tests of a posit

A posit supports a consequence without condition only once a test confirms it. A test may come from a later move of the same derivation, or from another record, such as a theorem proved later or a comparison with data. Each test takes one of six kinds:

- **consistency**: the terms neglected by the posit remain smaller than the terms kept;
- **limit**: the consequence recovers a known result in a limit within the domain of that result;
- **exact**: a proof that the posited form or relation holds;
- **approximation**: a bound on the distance between the consequence and the exact object;
- **empirical**: a comparison of the consequence with data;
- **computation**: a computation, certified or numerical, of the posited object.

A test either supports or refutes its posit. A refuting test is a [refutation](consequences-and-understanding.md#^refutation) of the posit.

**A posit is confirmed only by an exact test, a test of approximation, or a certified computation.** These three tests bound the distance between the consequence and the exact object. The other tests support a posit without confirming it: a test of consistency, a test of limit, an empirical comparison, and a numerical computation. An empirical comparison checks the consequence on the data compared, and bounds no distance beyond those data. ^posit-confirmation

**Consistency does not bound an error.** A multiple-scale expansion, a dominant balance or a WKB approximation can be consistent order by order, each neglected term staying smaller than the terms kept. Yet the constructed object can stay far from the exact one on long times. Only a test of approximation or an exact test bounds the distance to the exact object. Therefore, a test of consistency leaves its posit exposed to revision. ^consistency-not-validity

Each posit not confirmed enters the exposure of the consequences resting on it, as the [exposure of a derivation](../knowledge/grounds-and-dependence.md#^derivation-exposure) states.

---
## Sources

> [!NOTE] Status of the claims
> - **Proposals:**
> 	- the posit as a premise introduced on trial, apart from the test that justifies it;
> 	- the five kinds of posit, and their separation from a change of variables and from a model operation;
> 	- the origins of a posit;
> 	- the six kinds of test, the three tests that confirm a posit, and the rule that a test of consistency bounds no error.
