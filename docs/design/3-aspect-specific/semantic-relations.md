---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Semantic relations
---
# Semantic relations

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Stub file. Holds criteria that constrain the typed relation vocabulary between epistemic objects. Traces to [object-kind role purity](../2-architecture/object-kinds.md#^t2-ontology-role-pure), [non-redundancy](../1-framework/modular-content-organization.md#^t1-non-redundancy), [relational graph representation](../2-architecture/relations-graph.md#^t2-relational-graph-representation), [closed typed relations](../2-architecture/relations-graph.md#^t2-typed-relation-vocabulary), and [relation storage locus](../2-architecture/relations-graph.md#^t2-relation-storage-locus) (objects author edges). The actual relation vocabulary is deferred to [the project TODO](../../TODO.md).

---

## Criteria

### Minimal closed relation vocabulary ^t3-minimal-closed-relation-vocabulary

No relation label may exist outside the schema-declared set. The vocabulary is closed at design time.

### Typed relations with declared endpoints ^t3-typed-relations

Every relation has a declared source type and target type. A relation that does not constrain its endpoints is ill-formed.

### Two strata: canonical vs. inquiry-relative relations ^t3-two-strata-relations

Relations split into two strata: relations declared in the canonical schema between canonical objects, and relations that live inside an assembly because they depend on the inquiry. The second stratum lives inside the assembly's authored content per [locus of justificatory annotations](../2-architecture/reasoning-structure.md#^t2-reasoning-annotation-attachment) and [promotion of assembly-local records](../2-architecture/reasoning-structure.md#^t2-assembly-record-promotion); it is not exposed as canonical edges.

### Semantic vs. justificatory dependence ^t3-semantic-vs-justificatory-dependence

The relation vocabulary distinguishes semantic dependence (what an object's content presupposes) from justificatory dependence (what supports an object's claim). Conflating them obscures both.

---

## Decisions

*To be drafted at the relation-vocabulary work in [the project TODO](../../TODO.md).*

---

## Open questions

*To be drafted at the relation-vocabulary work in [the project TODO](../../TODO.md).*
