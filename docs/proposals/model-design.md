---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the model design
---
# Proposals for the model design

The goal [`model-design`](../../TODO.md) revises the model design, following the [decision on answers, models and bindings](../adr/answers-models-bindings.md).

## Analogy between models

An analogy maps a source onto a target. The analogy holds the source, the target, the correspondences between their elements, the transfer that the correspondences license, and the limits where the mapping breaks. Under the decision on answers, models and bindings, an analogy has two possible homes: a typed operation by which a derived model comes from its parent, or a binding whose target is a model instead of a phenomenon. Four subtypes differ by function:

- a **structural** analogy preserves the relations between the elements of source and target;
- a **model-transfer** analogy reuses a source model to structure a target domain;
- a **heuristic** analogy guides a search without licensing a claim;
- an **illustrative** analogy clarifies a target without inferential force.

The [reified relation](relation-registry.md#the-reified-relation) already gives an analogy a bounded scope.

**Literature.** None cited.

**Bears on.** [`model-design`](../../TODO.md).

**Retired source.** `docs/design/_backup/object-types-ontology/obj-analogy.md`, at commit 9e138e2.
