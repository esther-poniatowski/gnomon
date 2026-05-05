# Object kinds and their admission

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions that govern what may live as a canonical object kind, what every kind must share, and how the schema represents variants of a kind.
>
> Cross-cutting Tier-2 criteria that constrain decisions in this file: see [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints), in particular [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t2-coverage-completeness](vendor/gnomon/docs/design/2-architecture/constraints#^t2-coverage-completeness), [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance), [t2-subtype-safety](vendor/gnomon/docs/design/2-architecture/constraints#^t2-subtype-safety), [t2-field-typing](vendor/gnomon/docs/design/2-architecture/constraints#^t2-field-typing).

---

## Decisions

### Object-kind admission ^t2-object-kind-admission

> [!QUESTION] What rule decides whether a candidate concept becomes a canonical object kind, a field, a status, a relation, a note, a record local to a target, or a view specification?

The architecture does not fix the object taxonomy, which is deferred to [the project TODO](vendor/gnomon/docs/TODO), but it fixes the admission rule. A candidate becomes a canonical object kind only if it satisfies all five conditions:

- **Independent identity** — meaningful without reference to any inquiry that uses it.
- **Reuse across inquiries** — the same object can be cited from many inquiries.
- **Local validity conditions** — its content can be evaluated on its own terms.
- **Independent editability** — revisable without rewriting inquiries that cite it.
- **Irreducibility** — not derivable by build from other canonical objects.

A candidate that fails any condition belongs as a field, status, relation, note, record local to a target, or view specification. This rule resolves tension [X3](vendor/gnomon/docs/design/2-architecture/constraints#^t2-x3) between a narrow ontology and full coverage.

### Common abstract base ^t2-common-abstract-base

> [!QUESTION] Do record kinds in the canonical store share a common abstract base, and if so what does it declare?

Every record kind in the canonical store shares a common abstract base (`EpistemicObject`) that declares an interface contract. Minimally:

- a stable identifier,
- a kind tag,
- a status field (per [t2-epistemic-status](#^t2-epistemic-status)),
- a field for outgoing edges (per [t2-relation-storage-locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus)).

Concrete kinds extend the contract with fields that belong to the kind under [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance) (tagged unions, not OOP inheritance). The abstract base commits the schema only; it does not create a runtime class hierarchy.

*Source*: ratified Tier-2 promotion (CT2-1). This was originally a Tier 3 criterion for fields and schema ("Common abstract base"). It moved to Tier 2 because it constrains every record kind in the canonical store, not the contents of one theme.

### Question vs. Goal ^t2-question-vs-goal

> [!QUESTION] Are `Question` and `Goal` distinct top-level kinds, or is the distinction operational?

**Single kind with operational mode.** The distinction between question and goal is operational rather than ontological: a goal is a question with an operational mode that licenses planning moves. The mode is encoded by a typed objective field — for example `target.objective: prove | compute | compare | test | construct | explain` — with the target object referenced separately. The objective is a controlled value, not an unstructured imperative.

This assimilation avoids overengineering the object ontology (per [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology)) and lets the system reclassify objects as questions or goals without changing identity or relations.

### Epistemic status (maturity record) ^t2-epistemic-status

> [!QUESTION] How does the framework record the maturity of an epistemic object — where it stands in the lifecycle from initial conjecture to established result — and how does it transition through that lifecycle?

**Per-kind enums declared in the schema**, closed at design time. Each object kind declares its own status enum.

For enum entries by kind, the contrast between maturity and warrant kind, and the open question on status transitions, see [status vocabulary](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary).

---

## Open questions

### Subtype discipline ^t2-subtype-discipline

> [!QUESTION] How are object variants represented within a kind, given that [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance) rules out OOP-style inheritance and [t2-subtype-safety](vendor/gnomon/docs/design/2-architecture/constraints#^t2-subtype-safety) forbids using one variant where another is required?

Alternatives:

- **Tagged unions** — each variant is selected by a discriminator and has its own field contract.
- **Schema refinement** — variants extend a base schema by adding fields and constraints, without assuming that one variant can stand in for another.
- **Hybrid** — tagged union at the semantic level, schema refinement at the validation level.

OOP-style inheritance is excluded by [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance).

Bearing criteria: [t2-no-inheritance](vendor/gnomon/docs/design/2-architecture/constraints#^t2-no-inheritance), [t2-subtype-safety](vendor/gnomon/docs/design/2-architecture/constraints#^t2-subtype-safety), [t2-narrow-ontology](vendor/gnomon/docs/design/2-architecture/constraints#^t2-narrow-ontology), [t2-layer-replaceability](vendor/gnomon/docs/design/2-architecture/constraints#^t2-layer-replaceability).
