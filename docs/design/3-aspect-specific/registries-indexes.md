# Registries and indexes

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria for the derived registries and indexes the build produces. Traces to [t2-dependency-management](vendor/gnomon/docs/design/2-architecture/constraints#^t2-dependency-management), [t2-single-source-of-truth](vendor/gnomon/docs/design/2-architecture/constraints#^t2-single-source-of-truth), [t1-dual-usability](../1-framework/cost-ergonomics#^t1-read-side-automation), and the read-locus rule fixed at [relation storage locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus).

---

## Criteria

### Dependency graph as first-class derived structure ^t3-dependency-graph-first-class

The dependency graph is a first-class derived structure, not a property derivable on demand from object fields. The build emits it as an addressable artifact.

### Typed imports for references ^t3-typed-imports

References specify their import kind (definition, theorem, assumption, proof pattern, etc.) so that reuse is auditable.

### Staging area pattern for registry updates ^t3-staging-area-pattern

Updates to the registry are written to a `staging/` area first; promotion to the active registry requires validation plus human review. This guards against silent corruption of the read model.

### Orphan detection via reachability ^t3-orphan-detection

Orphans (objects unreachable from any inquiry root) are detectable by reachability analysis on the registry. The build emits a diagnostic, not a deletion.

---

## Decisions

*To be drafted at the registries-and-indexes work.*

---

## Open questions

*To be drafted at the registries-and-indexes work.*
