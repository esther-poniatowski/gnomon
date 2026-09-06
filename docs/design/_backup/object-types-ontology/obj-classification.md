---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Classification (object candidate)
---
# Object candidate — Classification / Taxonomy / Typology

## Role

A classification divides a domain into types or classes under an explicit criterion.

Its role is to make a domain surveyable by exposing class membership, class relations, and coverage.

*Example*: a taxonomy that divides learning tasks into supervised, unsupervised, and reinforcement learning tasks is a classification.

*Usages*:

- case split
- typology
- ontology
- hierarchical concept graph

## Properties

**Truth-apt**: Derivative. The partition can be adequate or inadequate; its membership and inclusion claims are truth-apt.

**Functional stratum**: Taxonomic

**Internal structure**:

- **Domain.** Space being divided.
- **Criterion.** Basis for assigning items to classes.
- **Classes.** Categories produced by the criterion.
- **Coverage.** Whether the classes are exhaustive, exclusive, overlapping, or partial.
- **Hierarchy** (context-dependent). Subsumption or parent-child links among classes.

## Encoding options

### Taxonomic model

**Category:** Subtype object

**Specification:** Treat a taxonomy as a `MODEL` subtype (e.g., species hierarchy).

**Pros.**
- Preserves the unified structure of a domain partition under a criterion.
- Supports hierarchy, coverage, exclusion, and overlap constraints.
- Works when the whole class structure organizes a domain and can be queried independently of local class claims.

**Cons.**
- May overstate modelhood for simple typologies.

### Concept relation network

**Category:** Composite object

**Specification:** Build the taxonomy from `CONCEPT` nodes, typed relation edges among them, and `CLAIM`s that justify the class boundaries (e.g., mammal includes primate).

**Pros.**
- Reuses concept and claim structure.

**Cons.**
- Loses the single object that carries the partition criterion unless reified.
- Can obscure that a taxonomy organizes a domain rather than many local inclusion claims.

### Classificatory claim

**Category:** Subtype object

**Specification:** Use a `CLAIM` that asserts membership, inclusion, or exclusion for a limited target set (e.g., whales are mammals).

**Pros.**
- Fits narrow class-membership or inclusion judgments.

**Cons.**
- Too small for taxonomies with hierarchy and coverage constraints.

## Subtypes

Subtypes are meaningful along one dimension: the form of domain organization.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Partition | Divides a domain into mutually exclusive classes. | `CLASSIFICATION` subtype with exhaustiveness and exclusion constraints. | Stable when coverage and exclusion drive evaluation. |
| Hierarchy | Orders classes by inclusion or dependence. | `CLASSIFICATION` subtype built from `CONCEPT` nodes and inclusion edges. | Stable when parent-child structure matters. |
| Typology | Groups cases by salient dimensions without full hierarchy. | `CLASSIFICATION` subtype linked to comparison criteria. | Useful for exploratory domains. |
| Taxonomy | Organizes a domain through named kinds and relations. | `CLASSIFICATION` subtype or `MODEL` subtype. | Stable when the class system functions as a representational structure. |
