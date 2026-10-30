---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the definitions framework
---
# Proposals for the definitions framework

The goal [`definitions-framework`](../../TODO.md) formalizes definitions, and produces the full definition object to which a concept record may link.

## Legitimate mutual constraint

Two structures look circular without being vicious cycles of justification:

- **Co-definition.** Two definitions can depend on each other. "Task variable" cannot be fixed independently of "task", because what counts as a variable depends on which distinctions the task makes relevant ([example 29](../../examples/adversarial-statements.md#^example-conceptual-dependence-between-two-definitions)). Such definitions are admitted together, as a cluster that records its mutual constraint as legitimate.
- **Co-determination.** Two objects can each explain an aspect of the other. The task explains the geometry, and the geometry explains which aspects of the task are treated as relevant ([example 32](../../examples/adversarial-statements.md#^example-ambiguous-explanatory-priority)). A directed relation `explains` cannot state this. A distinction, here between the task and the effective task, often removes the apparent circle, because it separates the endpoints of the two relations.

The note on the [order of specification](../epistemology/inquiry/specification-order.md#^iteration-circularity) already separates circularity in the order of execution from circularity in warrant, and admits cycles between questions resolved by iteration. The candidate draws the same distinction for definitions and for explanatory relations.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`definitions-framework`](../../TODO.md) for co-definition, and `relation-registry` for co-determination.

## Identity criterion of a concept

A concept carries an identity criterion, which decides whether two records denote the same concept, instead of serving as a label without conditions. The concept record of the [decision on concepts, glossaries and notations](../adr/concepts-glossaries-notations.md) holds a gloss, a kind, a broader concept, a source note and its confusions with other concepts, but no identity criterion. The criterion is therefore a candidate part of the full definition object to which the record may link. The same proposal held an equivalence criterion, which the decision on answers already places in the block of an exploration.

**Literature.** None cited.

**Bears on.** [`definitions-framework`](../../TODO.md).

## Normal form of a definition

A definition holds six fields:

- the **definiendum**, the concept, predicate or term that the definition fixes;
- the **definiens**, the content that fixes its use;
- the **force**: `stipulative`, `descriptive`, `operational`, `canonical` or `revisionary`;
- the **scope**, the domain in which the definition applies;
- the **boundaries**, the borderline uses and the uses ruled out;
- the **variants**, such as an equivalent or a scope-restricted definition.

The genus–differentia form splits the definiens further, into a genus, which the definiendum specializes, and a differentia, which is an attribute of the genus together with the value that the attribute takes. The definitional force of the definiens is recorded apart, as necessary, sufficient, biconditional or informal: prose rarely marks it, and the record must not commit to the strongest reading. A registry of surface templates maps a sentence to the roles of its parts:

| Template | Role |
| --- | --- |
| `X is a Y` | subtype |
| `X is a Y where Z is W` | genus–differentia |
| `X is defined as Y` | equivalence |
| `X refers to Y` | terminological |
| `X consists of A, B, C` | compositional |
| `X is characterized by P` | property-based |
| `X differs from Y by P` | contrastive |
| `X is used to Y` | functional |
| `X measures Y` | operational |
| `X approximates Y` | methodological approximation |
| `X is not P but Q` | negative: rejects a competing definition P |

Three operations on a definition stay separate: normalization makes the roles explicit, completion defines every referenced term, and validation checks that every reference is well formed. A definition is accepted once normalized. The separation fails for a concept whose meaning is fixed by its test, such as the contribution of a feature to a task ([example 37](../../examples/adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)).

An undefined term enters as a typed placeholder, not as a bare token. The position of the term in its template fixes its kind: a genus is a system, and an attribute is a property. The placeholder carries a candidate set of referents and a resolution policy:

- `will-resolve`: one candidate will be selected later;
- `cannot-resolve`: the object forces the plurality, which is permanent;
- `will-not-resolve`: the author keeps the plurality by choice, and a check of canonical terms exempts the term.

A placeholder is shared, so resolving it once resolves it in every statement that uses it. A statement may also assert a usage norm, that is, how a named community uses a term, such as "in neuroscience, 'represented' often means recoverable from activity". A usage norm is a claim with a source and a truth value, and differs from the concept that the project fixes for the term.

As a record kind, the definition passes the first five of the seven conditions of the [admission of a record kind](../adr/record-kind-admission.md#^five-conditions). Non-distortion and unitary epistemic role remain to be checked. Its alternative home is the aim block of an answer of explication, which the goal `problem-record` decides together with the question whether explication becomes an aim.

**Literature.** Carnap's explication; implicit definition by a theory, after Hilbert and Carnap; and the holism of Quine and Putnam, which denies that a finite set of definitional claims exhausts a theoretical concept. The retired notes also name frame semantics, typed feature structures and Abstract Meaning Representation as precedents of the normalization.

**Bears on.** [`definitions-framework`](../../TODO.md), and `problem-record` for the alternative home.

**Retired source.** `docs/design/_backup/object-types-ontology/obj-definition.md`, `docs/design/3-aspect-specific/ontology.md` (anchor `^t3-definition-normal-form`) and `docs/design/3-aspect-specific/arguments-reasoning.md`, at commit 9e138e2.
