---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - IDs, namespaces, versioning
---
# IDs, namespaces, versioning

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria for stable identifiers, namespace structure, and ontology versioning. Traces to [t1-modularity](../1-framework/modular-content-organization#^t1-reuse), [revision accountability](../1-framework/research-activities-workflows#^t1-revision-accountability), and [t1-feasibility](../1-framework/cost-ergonomics#^t1-system-scale). Cross-references the [git-delegation policy](vendor/gnomon/docs/design/1-framework/framework-foundations#^t1-no-version-history): in-state identity at HEAD only.

---

## Criteria

### Stable persistent identifiers ^t3-stable-identifiers

Identifiers are persistent and not content-addressable. A reference resolves to the same logical object across revisions, even when the object's content changes (per [t1-modularity](../1-framework/modular-content-organization#^t1-reuse)).

### Namespace hierarchy with declared interfaces ^t3-namespace-hierarchy

Namespaces are hierarchical with declared interfaces at each level. A namespace exposes a closed set of references; downstream consumers depend on the interface, not the internals.

### Versioning separate from ontology ^t3-versioning-separate-from-ontology

The ontology itself is versioned, separately from the instance content it governs. Ontology revisions invoke the [revision machinery](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary) at the schema layer.

---

## Decisions

*To be drafted at the IDs-and-versioning work.*

---

## Open questions

*To be drafted at the IDs-and-versioning work.*
