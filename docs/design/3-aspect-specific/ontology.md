# Ontology of object kinds

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria that constrain the ontology decision (which object kinds the canonical store admits). Traces to [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t2-coverage-completeness](vendor/gnomon/docs/design/2-architecture/constraints#^t2-coverage-completeness), and the [object-kind admission test](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission). The actual taxonomy is deferred to [the project TODO](vendor/gnomon/docs/TODO).

---

## Criteria

### Admissibility under the five-condition test ^t3-admissibility-five-conditions

A candidate becomes a canonical object kind only if it satisfies all five conditions of [the object-kind admission test](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission): independent identity, context-transcendent reuse, local validity, independent editability, irreducibility.

### Attributes vs. objects ^t3-attributes-vs-objects

A candidate that fails any of the five conditions belongs in a field, status, relation, or higher-layer annotation, not as a new object kind.

### Decision table with one row per candidate ^t3-decision-table-row-per-candidate

The ontology decision must be recorded as a table with one row per candidate kind and one justification per decision (admit, reject, route to field/status/relation).

### Primary-content, operational, and non-distortion conditions ^t3-primary-content-conditions

The set of object kinds must satisfy primary-content, operational, and non-distortion conditions: it carries the system's substantive content; it supports the operations the architecture requires; it does not distort an aspect into a shape that misrepresents it.

### Ontology stability under growth ^t3-ontology-stability

The ontology begins small, allows subtypes gradually under [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance), and is itself versioned so that taxonomic restructuring is recordable.

---

## Decisions

*To be drafted at the ontology work in [the project TODO](vendor/gnomon/docs/TODO).*

---

## Open questions

*To be drafted at the ontology work in [the project TODO](vendor/gnomon/docs/TODO).*
