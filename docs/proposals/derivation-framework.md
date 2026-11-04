---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the derivation framework
---
# Proposals for the derivation framework

The goal [`derivation-framework`](../../TODO.md) formalizes derivation, its results, and synthesis.

## Algebraic data types for propositional content

Propositional content is represented by a recursive algebraic data type, with the constructors `Atom`, `Not`, `And`, `Or` and `Implies`, rather than by a string or by prose. The grammar `φ ::= p | ¬φ | φ∧φ | φ∨φ | φ→φ` admits structural pattern matching, and a string does not. The [decision on expression syntax](../adr/expression-syntax.md) already gives each formula a term structure: an S-expression core, whose operators are head symbols. The open part is whether the claim of an answer admits logical connectives as operators of that core. The goal `audit-local-repairs` currently counts `and` written as an operator as a defect of the worked inquiries.

A grammar for propositional content must also state four constructs that the primitives of a programming language lack: quantification over an open domain, a condition or a regime under which a claim holds, approximate or conditional equality, and the distinction between using a claim and mentioning it.

**Literature.** None cited beyond the construct of algebraic data types.

**Bears on.** [`derivation-framework`](../../TODO.md).

## Statement modality

A statement need not assert its content. Two modalities appear in the test set:

- **A hypothetical statement.** A whole statement is conditional: "if such evidence held, it would mean Z" ([example 3](../../examples/adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [example 4](../../examples/adversarial-statements.md#^example-research-question-embedded-in-a-critique)).
- **A counterfactual claim.** A claim concerns what a computation would have been under an intervention that did not take place. "The feature contributes to the task" unpacks as a claim about the computation without the feature ([example 37](../../examples/adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)). Such a claim has a meaning only relative to a family of admissible interventions.

The [attitude of a claim](../epistemology/vocabulary/representations/claim-and-hypothesis.md#^attitude-support), `entertained`, `hypothesized`, `accepted` or `retracted`, already marks a claim that is not asserted. The candidate concerns the content instead: a conditional claim can be accepted as a whole while its antecedent is not asserted, and a counterfactual claim must name its family of interventions.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`derivation-framework`](../../TODO.md).
