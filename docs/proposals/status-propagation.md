---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for status propagation
---
# Proposals for status propagation

The goal [`status-propagation`](../../TODO.md) decides which changes of the attitude or of the support of a claim mark the records resting on it for review.

## Revision operations

Belief revision names five operations on an epistemic state: expansion adds a claim without resolving a conflict, revision adds a claim while preserving consistency, contraction removes a commitment, consolidation restores consistency after a contradiction, and merge combines two epistemic states. The [note on revision](../epistemology/activities/revision.md) already adopts expansion, contraction and revision, under the AGM postulates, as the activity `belief-revision`. The candidate adds consolidation and merge, and offers the five operations as the classes of change that the goal sorts: the goal can state, for each operation, whether it marks the records resting on the changed claim for review.

**Literature.** The AGM theory of belief revision, as stated in [belief revision and dynamic epistemic logic](../references/belief-revision-dynamic-epistemic-logic.md).

**Bears on.** [`status-propagation`](../../TODO.md).

## Kinds of a content revision

A revision of content takes one kind or several:

- `retraction`: a record that was once active is no longer pursued;
- `scope_narrowing` and `scope_generalization`: the domain of a record shrinks or extends;
- `reorientation`: the content is reframed without narrowing or generalizing, as when a question is reformulated;
- `taxonomic_restructure`: the classification of a record changes, by renaming, regrouping, splitting or merging;
- `correction`: the content changes within its scope, as when an error of a proof is fixed.

The sensitivity of a dependent follows from the warrant of the relation through which it rests on the revised record. A monotonic warrant is sensitive only to `retraction`, `correction` and `taxonomic_restructure`. A defeasible warrant is sensitive as well to the kinds that bring qualifying evidence: `scope_narrowing`, `scope_generalization` and `reorientation`. Each flagged dependent then records its state: `pending`, `revised`, `confirmed_unaffected` or `retracted`. The recorded state holds the judgment that the [decision on revision accountability](../adr/revision-accountability.md#^flag-not-edit) leaves to the researcher for each dependent.

**Literature.** None cited.

**Bears on.** [`status-propagation`](../../TODO.md), and `relation-registry` for the [warrant kinds](relation-registry.md#warrant-kinds).

**Retired source.** `docs/design/3-aspect-specific/revision-vocabulary.md`, at commit 9e138e2.
