---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for research actions
---
# Proposals for research actions

The goal [`research-actions`](../../TODO.md) decides whether the activities of the registry of activities are primitive, or derive from a smaller set of constructors.

## Multiple dispatch

An operation need not belong to one of its arguments. A generic function holds several methods, and the method that applies is selected on the types of all its arguments together. Several operations on research content have no single owner:

| Operation | Arguments that select the method | Reason that no argument owns the operation |
| --- | --- | --- |
| `supports(argument, claim)` | the kind of argument, the kind of claim | support depends on both kinds |
| `contradicts(statement, statement)` | two kinds of statement | contradiction is a relation, often symmetric |
| `instantiates(example, concept)` | the structure of the example, the kind of concept | instantiation depends on both |
| `formalizes(textual_claim, formal_object)` | the informal and the formal representation | formalization depends on both representations |
| `translates(object, target_language)` | the source object, the target formalism | translation depends on both |
| `equivalent(x, y, criterion)` | two objects and a criterion | equivalence holds relative to a criterion |
| `applies(theorem, model, assumptions)` | a theorem, a model, a set of assumptions | applicability depends on all three |
| `proves(proof, proposition, formal_system)` | a proof, a proposition, a formal system | provability holds relative to a system |
| `task_relevant(representation, task, equivalence)` | a representation, a task, an equivalence | relevance holds relative to a task and a criterion |

The activities of the registry already declare the product types of their inputs. An activity could therefore be one generic operation, with one method for each tuple of input types, instead of one entry per combination.

**Literature.** The Common Lisp Object System (CLOS) and Julia.

**Bears on.** [`research-actions`](../../TODO.md).

## Moves that improve an idea

A vocabulary of moves transforms research content:

- *clarify* reduces an ambiguity;
- *distinguish* splits two conflated notions;
- *generalize* and *specialize* change the scope of a claim;
- *operationalize* and *formalize* give a notion a procedure or a formal object;
- *weaken* removes an excessive commitment, and *strengthen* adds conditions or support;
- *integrate* combines ideas, and *rise above* states a formulation of higher level that synthesizes partial ideas;
- *problematize* exposes a hidden assumption or a limitation;
- *metadiscourse* reasons about the state of the inquiry itself.

These moves are finer than the activities of the registry, so they are candidate constructors from which the activities could derive. Revisionary relations, such as *refines*, *weakens* and *splits into*, name the same changes as relations between two states of the content. The moves and the relations must therefore be reconciled into one vocabulary, not adopted as two.

**Literature.** Knowledge Building theory.

**Bears on.** [`research-actions`](../../TODO.md), and `relation-registry` for the revisionary relations.

## Constructors of operations

An activity could derive from four constructors applied to schemas of operations, instead of standing as a primitive entry of the registry:

- `compose(s1, s2, …)` applies schemas in order, and passes the output of each schema to the next;
- `parallel(s1, …, sn)` applies schemas to disjoint parts of a target, and gathers their outputs;
- `branch(condition, s_true, s_false)` selects a schema by a predicate over its inputs;
- `iterate(s, until)` applies a schema until a predicate of termination holds.

Each constructor, and each schema treated as primitive, declares five parts: a typed signature, its conditions of admissibility, the semantics of its transformation, its condition of success, and the kind of licence that justifies it. A schema that lacks one part does not enter the library. The registry of activities already declares a signature, a mode and a norm for each activity, so the candidate adds the semantics of the transformation and the condition of success. In an itinerary, `branch` and `iterate` would give a step a branch and a fallback, which a sequence of steps cannot state.

**Literature.** The precedents that the retired notes name: the inference rules of [proof theory](../references/proof-theory.md), the primitive instructions of a programming language, the typed tasks of a workflow system, and the morphisms of category-theoretic semantics.

**Bears on.** [`research-actions`](../../TODO.md), and `inquiry-records-round-2` for the branches and fallbacks of an itinerary.

**Retired source.** `docs/design/3-aspect-specific/operation-schemas.md`, `docs/design/_backup/architecture-2-audit.md` and `docs/design/_backup/arguments-reasoning/primitive-operations.md`, at commit 9e138e2.
