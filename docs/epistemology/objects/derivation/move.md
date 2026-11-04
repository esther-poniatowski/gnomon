---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Moves and warrants
  - Move of a derivation
  - Warrant of a move
---
# Moves and warrants

> [!QUESTION] Goal: what is one step of a derivation, what makes it valid, and which steps must a record state?

A **move** is one step of a derivation: it takes intermediate objects already available and yields new ones. A move acts on intermediate objects only. A change to the laws or the members of a model is an operation of a derived model, as the [criterion of the boundary](../../processes/units-of-work.md#^work-unit-criterion) decides.

## Kinds of move

The kinds of move are atomic: each states one transformation. A way of deriving made of several moves, such as a multiple-scale expansion or a dominant balance, is a [scheme](segment-and-scheme.md), not a kind of move. The kinds group by their effect on the objects at hand:

| Group | Kinds | Effect of the move |
| --- | --- | --- |
| **Transformation** | substitute, transform, rescale, eliminate | rewrites an object in another form or another representation, without loss |
| **Approximation** | expand, truncate, take a limit, estimate | replaces an object by a simpler one, with an error |
| **Determination** | solve, impose, require self-consistency, match | fixes an unknown or a slot by solving an equation, by imposing a condition such as a solvability condition, by equating a slot with its own image, or by matching two expansions |
| **Inference** | apply a theorem, split into cases, induct, derive a contradiction | draws a statement from statements already available |
| **Computation** | compute, import | obtains a value by a computation, or brings into the derivation the output of an act of the itinerary |
| **Comparison** | compare | sets two objects side by side under one set of conditions |

**A self-consistency requires no cycle.** A mean-field argument assumes a value for an order parameter, computes the value implied by this assumption, and requires that the two values agree. The move *require self-consistency* equates the slot with its image. Therefore, the dependence between moves stays acyclic. The requirement that the two values agree is the output of one move, not a loop between two moves.

## Warrant of a move

The **warrant** of a move states the license of the move. The warrant names one of five sources:

- a definition;
- a theorem;
- an approximation;
- a computation;
- the verdict of the norm of an act whose output the move imports.

A warrant also states two properties:

- the **class of its error**, among the four [classes of the error of an operation](../answer/model-and-binding.md#^error-classes): exact, controlled, uncontrolled or singular;
- the **regime** of validity of the warrant, for an approximation, a limit or a truncation.

**The warrant names the property that makes it apply at this point.** A theorem applies to the objects at hand because they have some property: a self-adjoint operator, a finite index set, a small parameter. That property is an [interpretation](interpretation.md) of a structural or magnitude kind, established before the move, and the warrant cites it. Then, the property is stated once, at the point where it is established, and the warrant does not restate it. ^applies-because

A warrant states only why the move is valid. The [orientation](orientation.md) of the move states why the move is taken at that point.

## Routine and non-routine moves

A record need not state every move. A move is **non-routine** when it has any of six features: ^non-routine

- the record declares the move the kernel of the derivation;
- the move introduces a slot, or uses a posit;
- the move follows an impasse, or a diagnostic interpretation;
- the move belongs to one of five kinds: take a limit, truncate, require self-consistency, impose or match;
- the move imports the output of an act;
- the warrant of the move is not exact.

A non-routine move is stated, with its orientation. A routine move may be omitted inside a [segment](segment-and-scheme.md), provided that the segment states the objects consumed and the objects produced. The features are read from the record, so a move cannot be exempted by being called routine.

**The kernel test is a necessary condition.** The test passes when every route of the dependence from the premises to the consequence goes through the move. When a move fails this test, an alternative route avoids it, and the move is not the kernel. A move passing the test may still be routine, since every move of a linear chain passes it. Therefore, the record declares the kernel, and the test only checks that declaration.

---
## Sources

> [!NOTE] Status of the claims
> - **Proposals:**
> 	- the atomic kinds of move, in six groups, and the move that requires self-consistency without a cycle;
> 	- the five sources of a warrant, with the class of its error and its regime;
> 	- the property that makes a warrant apply, stated once as an interpretation and cited by the warrant;
> 	- the six features that make a move non-routine, and the kernel test as a necessary condition.
> - The classes of error are stated with the [operations of a derived model](../answer/model-and-binding.md#^derived-models).
