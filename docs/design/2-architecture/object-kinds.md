# Object kinds and their admission

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions that govern what may live as a canonical object kind, what every kind must share, and how the schema represents variants of a kind.
>
> This file opens with a `## Criteria` section of theme-local Tier-2 criteria — [object-kind set smallness](#^t2-ontology-small), [role purity](#^t2-ontology-role-pure), [subtype safety](#^t2-ontology-subtype-safety), and the meta-schema [field-typing discipline](#^t2-field-typing) — that constrain its decisions. Framework-level criterion bearing on this theme: [activity coverage](../1-framework/expressive-depth#^t1-activity-coverage).

---

## Criteria

### Object-kind set smallness ^t2-ontology-small

The set of object kinds must remain **small**. Every additional kind raises the cognitive cost of learning the ontology and widens the field-typing surface the schema must declare and validate. Smallness is a system-shape property: it follows from [human action cost](../1-framework/cost-ergonomics#^t1-human-action-cost) and [system scale](../1-framework/cost-ergonomics#^t1-system-scale), and it is one pole of tension [X3](../1-framework/_tensions#^t2-x3) against coverage.

### Object-kind role purity ^t2-ontology-role-pure

Each object kind must be **role-pure**: it carries one epistemic function and is not a catch-all. Rhetorical, procedural, target-relative, and presentational distinctions are encoded as fields, statuses, or layer-specific annotations — not as new object kinds. Two kinds with overlapping epistemic function would duplicate each other, so role purity is a consequence of [non-redundancy](../1-framework/modular-content-organization#^t1-non-redundancy). The discriminator that keeps the set role-pure is the five-condition test at [object-kind admission](#^t2-object-kind-admission).

### Object-kind subtype safety ^t2-ontology-subtype-safety

Subtype labels must not imply that one subtype can stand in for another, shares the same validity semantics, or plays the same graph role when those properties do not hold. A `lemma` cannot stand in for a `theorem` in a proof context, because their roles in the dependency graph differ structurally. Introducing a subtype must not silently inherit interchangeability from a base type. Substituting a non-interchangeable subtype would falsify the recorded reasoning, so this criterion follows from [inquiry content and progression](../1-framework/framework-foundations#^t1-inquiry-content-and-progression); the chosen *implementation* that satisfies it is the open question [subtype discipline](#^t2-subtype-discipline).

### Field-typing discipline ^t2-field-typing

Every field declared by any canonical kind, assembly kind, revision object, or operation schema must be one of: a scalar/enum, an embedded record, a typed reference, or a typed list of references. No field admits free composition outside this typed surface.

This is a **meta-schema rule**: it binds every theme that introduces fields — object kinds here, assemblies and reasoning notes in [reasoning structure](reasoning-structure.md), revision objects in [validity-revision](validity-revision.md), and operation schemas in [operations and modes](operations-and-modes.md). It is recorded here because object kinds are the primary field-declaring surface; the themes that declare their own fields conform to it.

## Decisions

### Object-kind admission ^t2-object-kind-admission

> [!QUESTION] What rule decides whether a candidate concept becomes a canonical object kind, a field, a status, a relation, a note, a record local to a target, or a view specification?

The architecture does not fix the object taxonomy, which is deferred to [the project TODO](vendor/gnomon/docs/TODO), but it fixes the admission rule. A candidate becomes a canonical object kind only if it satisfies all five conditions:

- **Independent identity** — meaningful without reference to any inquiry that uses it.
- **Reuse across inquiries** — the same object can be cited from many inquiries.
- **Local validity conditions** — its content can be evaluated on its own terms.
- **Independent editability** — revisable without rewriting inquiries that cite it.
- **Irreducibility** — not derivable by build from other canonical objects.

A candidate that fails any condition belongs as a field, status, relation, note, record local to a target, or view specification. This rule resolves tension [X3](../1-framework/_tensions#^t2-x3) between a narrow ontology and full coverage.

### Common abstract base ^t2-common-abstract-base

> [!QUESTION] Do record kinds in the canonical store share a common abstract base, and if so what does it declare?

Every record kind in the canonical store shares a common abstract base (`EpistemicObject`) that declares an interface contract. Minimally:

- a stable identifier,
- a kind tag,
- a status field (per [t2-epistemic-status](#^t2-epistemic-status)),
- a field for outgoing edges (per [t2-relation-storage-locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus)).

Concrete kinds extend the contract with fields that belong to the kind — by tagged unions, not OOP inheritance, per the [subtype discipline](#^t2-subtype-discipline) open question. The abstract base commits the schema only; it does not create a runtime class hierarchy.

*Source*: ratified Tier-2 promotion (CT2-1). This was originally a Tier 3 criterion for fields and schema ("Common abstract base"). It moved to Tier 2 because it constrains every record kind in the canonical store, not the contents of one theme.

### Question vs. Goal ^t2-question-vs-goal

> [!QUESTION] Are `Question` and `Goal` distinct top-level kinds, or is the distinction operational?

**Single kind with operational mode.** The distinction between question and goal is operational rather than ontological: a goal is a question with an operational mode that licenses planning moves. The mode is encoded by a typed objective field — for example `target.objective: prove | compute | compare | test | construct | explain` — with the target object referenced separately. The objective is a controlled value, not an unstructured imperative.

This assimilation avoids overengineering the object ontology (per [object-kind set smallness](#^t2-ontology-small)) and lets the system reclassify objects as questions or goals without changing identity or relations.

> [!important] Underlying construct: the epistemic gap
> The unified kind represents an **epistemic gap** — a localised lack of resolution that motivates inquiry. Interrogative framing surfaces the gap as a Question; imperative framing surfaces it as a Goal. The `objective` field carries the framing; the kind itself carries the gap. This reading sharpens the rationale for the collapse without altering it: a single underlying construct admits two surface framings.
>
> Two follow-ups are parked here, neither requiring re-ratification:
>
> - Kind-naming. If the gap reading is taken seriously, `EpistemicGap` is a more faithful name for the kind than `Question`. The choice is editorial, not architectural, and can be made when the ontology decision is drafted.
> - Subtypes of the gap. A candidate five-type taxonomy (paradox, missing mechanism, incomplete characterisation, case mapping, comparison) is recorded as an open question under [subtypes of the epistemic-gap kind](vendor/gnomon/docs/design/3-aspect-specific/ontology#^t3-epistemic-gap-subtypes). Resolution is bounded by [t2-subtype-discipline](#^t2-subtype-discipline).

### Epistemic status (maturity record) ^t2-epistemic-status

> [!QUESTION] How does the framework record the maturity of an epistemic object — where it stands in the lifecycle from initial conjecture to established result?

**Settled.** Maturity is recorded in a schema-declared status field, closed at design time. The status field records the object's *current standing* only; supersession is excluded from the maturity vocabulary, since version history lies outside framework scope per [no version history](../1-framework/framework-foundations#^t1-no-version-history). Maturity is independent of [warrant kind](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary), per [t3-status-distinct-warrant](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary#^t3-status-distinct-warrant).

**Unsettled — the enum grain.** Whether each object kind declares its *own* status enum or all kinds share *one uniform* maturity enum is open: per-kind enums fit each kind's lifecycle but widen the schema surface, against [object-kind set smallness](#^t2-ontology-small). The grain question is the Tier-3 open question [per-kind status enums](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary#^t3-per-kind-status-enums); this decision commits only *that* maturity is enum-recorded, not the grain of the enum.

For the candidate enum entries, the contrast between maturity and warrant kind, and the open question on status transitions, see [status vocabulary](vendor/gnomon/docs/design/3-aspect-specific/status-vocabulary).

---

## Open questions

### Subtype discipline ^t2-subtype-discipline

> [!QUESTION] How are object variants represented within a kind, given that [object-kind subtype safety](#^t2-ontology-subtype-safety) forbids using one variant where another is required?

Alternatives:

- **Tagged unions** — each variant is selected by a discriminator and has its own field contract. This is the currently ratified path.
- **Schema refinement** — variants extend a base schema by adding fields and constraints, without assuming that one variant can stand in for another.
- **Hybrid** — tagged union at the semantic level, schema refinement at the validation level.
- **OOP inheritance** — admitted as a candidate primitive by the staged Python-inspired-formalism proposal; see the reopen below. The standing rationale for *excluding* OOP subtype polymorphism: epistemic subtypes cannot stand in for one another by default — a `lemma` cannot stand in for a `theorem` in a proof context because their dependency-graph roles differ structurally. An interface contract on a base kind is appropriate (per [common abstract base](#^t2-common-abstract-base)); inheritance with implicit substitutability is not. The reopen weighs this rationale against the staged proposal.
- **Type classes / traits** — an interface is satisfied by a type without the satisfying type being a subtype of the interface; gives polymorphism without subtype substitutability.

> [!missing] Reopen pending
> OOP-style inheritance was excluded on the rationale folded into the OOP-inheritance alternative above, but a staged proposal in [fleeting-ideas](../_fleeting-ideas#^fleeting-python-oop) admits OOP inheritance as a candidate primitive, with type classes / traits staged as the counter-proposal. The five alternatives above are the full set on the table; the last two are live only while the reopen stands. Downstream commitments that travel with this reopen and must be re-evaluated together: [object-kind subtype safety](#^t2-ontology-subtype-safety), [layering replaceability](layering#^t2-layering-replaceability), and [common abstract base](#^t2-common-abstract-base).

Bearing criteria: [object-kind subtype safety](#^t2-ontology-subtype-safety), [object-kind set smallness](#^t2-ontology-small), [layering replaceability](layering#^t2-layering-replaceability).

### Schema-specification meta-rule ^t2-schema-specification

> [!QUESTION] What must every registry schema specify, and is that set of required aspects closed?

[Field-typing discipline](#^t2-field-typing) constrains the *fields* a schema may declare; this question concerns the schema document itself — what every registry schema must pin down so that a drifting agent cannot silently widen it. Each required aspect is a meta-schema commitment, distinct from the concrete schema of any one registry.

Required aspects gathered so far:

- **Closed field admission** — a schema must forbid fields beyond its declared set, so that a novel field name is rejected rather than silently accepted.
- **Typed imports** — a schema must require references to be declared with explicit kind and target fields, not bare identifiers.
- **Typed exports** — a schema must require an object's exportable outputs to be declared as addressable anchors with an explicit type, not left implicit in the object body.
- **Enum-constrained vocabularies** — every categorical field must draw from a closed, schema-declared value set.
- **Uniform identifier format** — every identifier field must satisfy one schema-declared format constraint.

> [!example] Realisation in the registry schemas
> Schema per object type can be stored under `governance/schemas/`. The concrete directory, regex, and enum fields are one realisation, not part of the meta-rule.

Resolution must state whether the four required aspects above are the closed set or whether further aspects (for example, required-versus-optional field cardinality, cross-object invariants) belong in it. The validators that check conformance are catalogued at [t2-validator-catalogue](validation-views#^t2-validator-catalogue); this question fixes what those validators read against. The format that realises the typed-imports and typed-exports aspects is fixed at [typed references](../3-aspect-specific/registries-indexes#^t3-typed-references).

Bearing criteria: [field-typing discipline](#^t2-field-typing), [object-kind set smallness](#^t2-ontology-small).

### Object identity: absolute or grain-relative ^t2-object-identity-grain

> [!QUESTION] Is the decomposition of content into typed objects unique, or does the same content yield different object sets at different grains of analysis?

[t1-typed-object-decomposition](../1-framework/framework-foundations#^t1-typed-object-decomposition) requires inquiry content to be decomposed into typed objects, but it does not guarantee the decomposition is unique. The same content can split into different sets of typed objects depending on the grain of analysis, and no grain is inherently privileged. The question is whether an object's identity is:

- **absolute** — fixed once and for all; one content has one canonical object decomposition;
- **grain-relative** — the same content yields different object sets at different analysis grains, none privileged.

A worked example exhibits the problem: [a conceptual move that changes granularity](vendor/gnomon/docs/design/_worked-examples#^example-conceptual-move-that-changes-granularity). A candidate answer is staged at [grain-indexed object decompositions](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-object-scope) — a family of decompositions indexed by analysis grain. Resolution must state which regime holds, and if grain-relative, how the [object-kind admission](#^t2-object-kind-admission) test applies per grain.

Bearing criteria: [t1-typed-object-decomposition](../1-framework/framework-foundations#^t1-typed-object-decomposition).
