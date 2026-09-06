---
tags:
  - index
  - backup
index: "[Superseded design proposals](../_index.md)"
aliases:
  - Object-kind candidates
---
# Object-kind candidates

Each candidate notion receives one specification, which names the encoding scheme the candidate takes. A candidate that survives admission stays a primitive object kind; the others are absorbed into a carrier, a supertype, a composite, or a relation.

## Encoding scheme categories

| Category | Description |
| --- | --- |
| Annotation on another object | The notion lives as a visible property on a carrier object. The specification names the carrier and the controlled values or properties. |
| Primitive object | The notion remains an irreducible object type because no carrier preserves its graph behavior and direct use in inquiry. |
| Subtype object | The considered notion is encoded as a subtype of another object type. The specification names the supertype and the distinctive relation or graph behavior. |
| Variant decomposition | The considered notion is dissolved into more specific object variants that replace it. The specification names the variant axis and the replacement variants. |
| Composite object | The notion combines several object types into one structured unit. The specification names the consumed objects and the extra relations or annotations. |
| Relation (graph edge) | The notion is a simple relation between objects and has no internal structure. The specification names the related objects and whether the edge is symmetric or asymmetric. |
| Reduction to another object | The notion is equivalent to another object type under stated conditions. The specification names the target object and any required property on that target. |

| Object                                                | Boundaries |
| ----------------------------------------------------- | ---------- |
| [CONCEPT](obj-concept.md)                             |            |
| [CLAIM](obj-claim.md)                                 |            |
| [DEFINITION](obj-definition.md)                       |            |
| [QUESTION](obj-question.md)                           |            |
| [PROBLEM](obj-problem.md)                             |            |
| [ARGUMENT](obj-argument.md)                           |            |
| [DERIVATION / PROOF](obj-derivation-proof.md)         |            |
| [STRATEGY / PLANNING](obj-strategy-planning.md)       |            |
| [METHOD](obj-method-procedure.md)                     |            |
| [NORM](obj-norm-criterion.md)          |            |
| [EVIDENCE](obj-evidence.md)                           |            |
| [EXAMPLE](obj-example.md)                             |            |
| [COUNTEREXAMPLE](obj-counterexample.md)               |            |
| [OBJECTION](obj-objection.md)                         |            |
| [FRAMEWORK](obj-framework.md)                         |            |
| [MODEL](obj-model.md)                                 |            |
| [MECHANISM](obj-mechanism.md)                         |            |
| [EXPLANATION](obj-explanation.md)                     |            |
| [INTERPRETATION](obj-interpretation.md)               |            |
| [CLASSIFICATION](obj-classification.md)               |            |
| [DISTINCTION](obj-distinction.md)                     |            |
| [COMPARISON](obj-comparison.md)                       |            |
| [ANALOGY](obj-analogy.md)                             |            |
| [RATIONALE](obj-rationale-motivation.md)              |            |
| [EVALUATION (meta-epistemic)](obj-evaluation-meta.md) |            |

## Cross-cutting records

| Record | Content |
| --- | --- |
| [Families of objects](taxo-families-objects.md) | The families into which the candidate kinds group. |
| [Object boundary comparisons](taxo-boundaries.md) | Pairs of kinds a reader may conflate, each compared under one structure. |
| [Object admission criteria](taxo-criteria-ontology.md) | The five conditions a candidate must satisfy to exist as a canonical object. |
| [Typed graph edges](relations-graph-edges.md) | The typed relations between objects that raise query precision. |
| [Unlabelled object candidate](obj-.md) | A specification carrying no object label, retained as the template of the others. |
