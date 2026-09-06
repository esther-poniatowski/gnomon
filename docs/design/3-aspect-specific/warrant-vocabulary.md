---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Warrant vocabulary
---
# Warrant vocabulary

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Instantiates the architectural commitment at [warrant-kind annotation on support relations](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation), resolved as warrant kind on each edge, with node defeasibility derived from incoming edges. The architecture commits *that* a closed enum for warrant kinds exists, *that* edges carry warrant kinds, and *that* a combination rule over incoming edges determines node defeasibility. This file fixes the enum entries and the combination rule.

---

## Criteria

### Defeasibility derived from edges ^t3-derived-defeasibility

Node defeasibility must be derivable from warrant kinds on incoming edges; it is never authored on the node.

### Warrant enum classification completeness ^t3-warrant-enum-completeness

Every enum entry for a warrant kind must declare whether it is monotonic or defeasible, so that the combination rule is total.

---

## Decisions

### Warrant-kind enum ^t3-warrant-kind-enum

> [!QUESTION] Which warrant kinds does the system recognize?

Closed enum declared in the schema. Initial entries:

`deductive`, `empirical`, `abductive`, `analogical`, `heuristic`, `methodological`, `definitional`, `interpretive`.

Recording warrant kind on the edge keeps each support relation independently auditable and supports reuse of canonical objects across contexts.

### Combination rule for node defeasibility ^t3-defeasibility-combination-rule

> [!QUESTION] How do warrant kinds on incoming edges combine to determine whether a node's conclusion is monotonic or defeasible?

For each node, the warrant kinds of its incoming support edges combine as follows:

- deductive warrants yield monotonic support;
- empirical, abductive, analogical, and heuristic warrants yield defeasible support;
- a node whose support is composed of mixed warrant kinds is defeasible if any constituent warrant is defeasible.

`methodological`, `definitional`, and `interpretive` warrants are listed in the enum but their monotonic/defeasible classification is not yet fixed. The combination rule must be extended once those classifications are decided (per [t3-warrant-enum-completeness](#^t3-warrant-enum-completeness)).

---

## Open questions

### Assembly-internal warrant enum ^t3-assembly-internal-warrant

> [!QUESTION] Does the warrant enum inside assemblies coincide with the enum for canonical edges above, or admit looser kinds used only in assemblies?

[promotion of assembly-local records](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-assembly-record-promotion) admits support edges inside assemblies between endpoints that are not canonical. Those edges carry `warrant_kind`; the enum choice depends on which fields [the reasoning note schema](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields) selects.

### Methodological / definitional / interpretive classification ^t3-mdi-warrant-classification

> [!QUESTION] Are `methodological`, `definitional`, and `interpretive` warrants monotonic, defeasible, or context-dependent?

The combination rule above leaves these unclassified. Their monotonic or defeasible status must be settled to satisfy [t3-warrant-enum-completeness](#^t3-warrant-enum-completeness).
