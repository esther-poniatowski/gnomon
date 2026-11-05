---
tags:
  - decision
status: accepted
created: 2026-11-05
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Requirements of a law
  - Assumptions of a law
---
# Requirements of a law

> [!QUESTION] Goal: how does a law name the assumptions on which it rests, so that every record using the law inherits them?

A law of a model or of a background rested on its assumptions through the field `rests_on`, a sentence. No check could read which assumption, operation, posit or law the sentence named. Therefore, an answer citing the law did not inherit the assumptions of the law, and the [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link) could not reach them. The goal `research-corrections` asked for typed premises in place of that sentence.

## Decision

**A law lists the units that it requires.** The field `requires` of a law names, by dotted identifier, each unit on which the law rests:

- an assumption or an operation of a model;
- a law of a background or of a model;
- a posit or a consequence of a derivation.

The field `rests_on` keeps only the grounds that no unit names, such as a source or a data set. A law whose descent a derivation records leaves its premises to that derivation, so it lists none. A check reports a unit on which no law may rest, a law that requires itself, and a derived law that lists the premises that its derivation records. The view of exposure follows each unit required by a law that an answer rests on.

**An assumption keeps the record that gives it its role.** Six objects bear the name of an assumption. They license different reasoning operations, as the [table of epistemic roles](../epistemology/objects/status/epistemic-objects.md#^unit-roles) places them:

- a premise asserted true of the target, stated as a posited law of a background;
- an idealization, stated among the assumptions of a model and classified by each answer;
- a premise on trial, stated as a posit of a derivation;
- a presupposition, held by its question, by the condition of a quantity, or by a claim;
- a regime, stated by a warrant, an operation or the domain of an answer;
- a way of assuming reused across targets, stated as a posit of a scheme.

Each of these is a unit with a dotted identifier, so it is reused by reference. An assertion shared by several models of one target is a law of their background. An idealization shared by sibling models belongs to their common parent, and an assumption reused across targets belongs to a scheme.

## Constraints that decide the field

- **Assembly follows declared dependence.** An answer inherits the assumptions of the laws that it cites only when a field states the dependence that a tool can follow, as the [admitted computations](no-run-time-inference.md#^admitted-computation) require.
- **One field per fact.** A derivation already states the premises of the law that it establishes, so `requires` does not restate them, as the decision on a [single field per fact](single-field-per-fact.md) requires.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| A record kind `assumption`, cited by laws, models, derivations and answers | One record and one identifier for each assumption | The kind fails the [conditions of admission](record-kind-admission.md#^admission-conditions): its instances license different operations, and its fields would apply to some instances only, tests to a posit, a motive to an idealization, a holder to a presupposition; whether an assumption idealizes a target is relative to each answer, and the asserted assumptions are already laws of a background |
| The sentence `rests_on` alone | No change to the records | No check reads the dependence, and no answer inherits the assumptions of its laws |
| Identifiers of the assumptions of the model only | The idealizations of a law are named | A law also rests on the operations of its model, on admitted laws and on posits, and the list would leave them in prose |

## Consequences

- The laws of the model and the background records gain the field `requires`, with its specification, its schema and its template; `rests_on` keeps the prose that `requires` cannot state.
- The checks gain the reports `completeness/misdirected-requirement` and `derivation/restated-premises`.
- The view of exposure gains the units that the laws of an answer require, an assumption of a model reported with its motive and its removability.
