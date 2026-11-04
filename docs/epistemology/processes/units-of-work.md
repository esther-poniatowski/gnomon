---
tags:
  - theory
  - wip
index: "[Processes of inquiry](docs/epistemology/processes/_index.md)"
aliases:
  - Units of research work
---
# Units of research work

> [!QUESTION] Goal: which record holds each fact about a piece of research work, so that each fact is recorded exactly once?

A piece of research work gives rise to four kinds of fact:

- the occurrence of an act;
- the content established once the act is done;
- the justification of that content, and the route leading to it;
- the general manner of doing such work.

Each kind of fact has one home. The four homes differ by the grain of their content and by the standard that judges that content.

## Four homes

| Home | Fact recorded | Grain | Judged by |
| --- | --- | --- | --- |
| **Act**, a step of an [itinerary](../../specification/itinerary.md) | the occurrence of an act of a registered activity, with its inputs, its output, and its purpose for the inquiry | one product | the norm of its [activity](activities/epistemic-activities.md#^activity-criterion) |
| **Product**, such as a model, a law or an answer | the content established, including a relation between two products, such as the operations relating a [derived model](../objects/answer/model-and-binding.md#^derived-models) to its parent | the content of one product | the [conditions of satisfaction](../objects/answer/satisfaction-conditions.md) |
| **Derivation** | the justification of a consequence, and the route leading to it: the posits, the orientations, the moves and the interpretations of a [derivation](../objects/derivation/derivation.md) | below the product: intermediate objects cited by no other record | the warrants of its moves; the norm of the act producing the derivation judges the whole |
| **Method**, a design of kind `method` | the general manner of doing such work, as a [scheme](../objects/derivation/segment-and-scheme.md) | reusable across products | its adequacy to its task |

A written proof is a report of the proof activity, as [validity and understanding](../objects/derivation/derivation.md#^beyond-validity) state. The four homes keep the same distinction: the act records the activity, and the derivation records the reasoning produced by the activity.

## Criterion of the boundary

**The grain of its output decides the home of a unit of work.** When the output belongs to a registered [product type](activities/epistemic-activities.md#^product-types) held by a record kind, the unit is an act, and the verdict of a norm judges it. Otherwise, the output is an intermediate object, and the unit is a move of a derivation, whose correctness rests on its warrant. ^work-unit-criterion

The criterion reads the output, and not the records citing it. The citing records change whenever an unrelated record begins to cite a unit, so a home assigned by citation would change with them. *Example*: a numerical computation inside a derivation yields an intermediate value, so the computation is a move. Its warrant cites the design or the code computing the value, with the class of its error. By contrast, when a simulation outputs a consequence recorded in a model or in an answer, the simulation is an act of the activity `simulation`.

## Consequences of the criterion

- **A step decomposes into sub-steps only along products.** A compound step of an itinerary decomposes into steps whose outputs are products, as a compound task does in [hierarchical task network planning](../../references/hierarchical-task-network-planning.md). Below the grain of a product, the work of a step is held by a derivation.
- **A model operation states the content established, and a derivation states the route.** An operation of a derived model states the relation between the derived model and its parent: its kind, its error and its regime. When reasoning establishes that relation, a derivation names the operation established, and the operation does not restate the derivation.
- **The object acted on separates an operation from a move.** A change to the laws or to the members of a model is an operation of a derived model, regardless of the reasoning yielding it. A change to an intermediate expression is a move. *Example*: when a closure adds a law over the quantities of a model, the closure is an operation. When a closure completes an intermediate system of equations, the closure is a posit of a derivation.
- **A derivation points to the act producing a guess.** A guess produced by an abduction, a simulation or an analogy enters a derivation as a [posit](../objects/derivation/posit.md), whose origin names that act. The act keeps its context of discovery, and the derivation does not restate the act.
- **An abandoned route belongs to the history of acts.** The itinerary keeps the sequence of acts, abandoned attempts included. A derivation records a route not taken only as an [impasse](../objects/derivation/consequences-and-understanding.md), or as an alternative rejected by an [orientation](../objects/derivation/orientation.md).
- **The purpose of an act and the purpose of a move differ in their object.** The rationale of a step of an itinerary names the question served by the act and the condition acted on. The orientation of a move names the sought of the derivation served by the move.
- **A derivation may call for an act.** An orientation may conclude that a sought calls for a computation or an observation beyond the reach of reasoning. Then, the computation or the observation is a step of the itinerary. Its output re-enters the derivation through a move that imports it, warranted by the verdict of the norm of that act.

---
## Sources

> [!NOTE] Status of the claims
> - **Proposals:**
> 	- the four homes of the facts of a piece of research work;
> 	- the criterion that decides a unit of work by the grain of its output;
> 	- the decomposition of a step along products only, and the separation of a model operation from the derivation that establishes it.
