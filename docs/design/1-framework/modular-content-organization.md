---
tags:
  - criteria
index: "[Framework-level criteria](_index.md)"
aliases:
  - Modular content organization (criteria)
---
# Modular content organization — Framework-level criteria

## Addressability ^t1-addressability

Every piece of **epistemic content** can be referenced by a stable identifier.

**Failure mode prevented.** Content that cannot be referenced cannot be reused, validated, or re-rendered, and is thus inert in the system.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations.md#^t1-inquiry-content-and-progression) (parent criterion): research artefacts must be referable by construction.
- [Reuse](#^t1-reuse) (peer sub-criterion): mutually presupposed.

**Downstream consequences.**

- Identifier-stability mechanism (decision in the ids-versioning theme): how identifiers persist as content evolves.
- Namespace organisation (decision in the ids-versioning theme): how identifiers are scoped.
- Typed-import mechanism (decision in the registries-indexes theme): how a referring object declares the type of its references.

## Reuse ^t1-reuse

The same **epistemic achievements** (e.g. definition, claim, proof, mechanism, interpretation...) can participate in **multiple inquiries** without duplication. This implies that contents are involved in inquiries by *reference*, not by copy.

**Failure mode prevented.** Duplication of epistemic content forces the author to maintain divergent copies. Edits to one copy silently leave the others stale; readers cannot identify which copy is authoritative.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations.md#^t1-inquiry-content-and-progression) (parent criterion): research artefacts are reused across inquiries by construction.
- [Addressability](#^t1-addressability) (peer sub-criterion): mutually presupposed — reuse without addressability cannot reach the content.

**Downstream consequences.**

- [Non-redundancy](#^t1-non-redundancy) (peer sub-criterion): the consistency condition that makes reuse enforceable across the system.

## Non-redundancy ^t1-non-redundancy

Each piece of content is stated **exactly once across the system**. This implies validators that enforce a **single canonical locus**. Subsequent occurrences are replaced by a cross-reference to the first.

**Failure mode prevented.** Duplication — verbatim restatement or paraphrase that adds no new content — splits the source of truth and creates drift between copies.

**Upstream dependencies.**

- [Single source of truth](research-activities-workflows.md#^t1-single-source-of-truth) (cross-group parent criterion in *Research activities and workflows*): a single canonical locus per content is the precondition for stating each piece of content exactly once.
- [Activity access rights](research-activities-workflows.md#^t1-activity-access-rights) (cross-group criterion in *Research activities and workflows*): once each activity writes only within its declared scope, non-redundancy is enforceable across the system.
- [Reuse](#^t1-reuse) (peer sub-criterion): non-redundancy is the consistency condition that makes reuse enforceable.

**Downstream consequences.**

- [Layer replaceability](../2-architecture/layering.md#^t2-layering-replaceability) (theme-local criterion): a layer that duplicates content of another cannot be replaced cleanly.
- [Layering with no silent coupling](../2-architecture/layering.md#^t2-layering-no-silent-coupling) (theme-local criterion): silent coupling between layers introduces hidden duplication.
- [Object-kind role purity](../2-architecture/object-kinds.md#^t2-ontology-role-pure) (theme-local criterion): two kinds with overlapping epistemic function would duplicate each other.

## Canonical terminology ^t1-canonical-terminology

**Terminology is canonical.** Each concept has a designated name (an optionally, a notation); aliases and local overrides may be admitted but must be explicitly linked and centralized. The framework enforces canonicity automatically rather than relying on author discipline.

**Failure mode prevented.** Several references that designate the same concept under different names appear unrelated to a syntactic tool. Terminology drift defeats both human reading and machine tracking; uncaught, it accumulates without limit.

**Upstream dependencies.**

- [Functional separation of concerns](framework-foundations.md#^t1-functional-separation) (cross-group parent criterion in *Framework foundation*): canonical names are one mechanism by which component boundaries remain unambiguous in prose. Canonical terminology is the prose-grain specialisation of that criterion's commitment to clearly bounded, functionally separated components.

**Downstream consequences.**

- Terminology-enforcement mechanism (decision in the validation-views theme): the chosen tool that flags non-canonical names.
- [Validation externality](research-activities-workflows.md#^t1-validation-externality) (peer sub-criterion): the enforcement tool runs outside the authoring loop.

This criterion commits to canonical terminology but does not fix the *scope* over which canonicity holds — global across the corpus, or local to a project or module. That scope question is the open decision [scope of terminology canonicity](../3-aspect-specific/ontology.md#^t3-canonicity-scope).

A second tension concerns a term whose plurality is deliberate rather than scoped.

> [!missing] Tension with deliberate productive ambiguity
> A term may be *deliberately* left plural because the ambiguity carries cognitive value, with resolution refused or deferred by an authored choice.
> *Examples*: a [term kept plural by intentional overload](../_worked-examples.md#^example-statement-where-a-term-is-intentionally-overloaded) and the [statement that preserves representation-geometry ambiguity](../_worked-examples.md#^example-statement-whose-role-is-to-preserve-ambiguity).

## Relational queryability ^t1-relational-queryability

**Relations** between objects are **queryable as an addressable structure**. First-class operations include dependency analysis, reverse-impact lookups, orphan detection, etc.

**Failure mode prevented.** When relations are scattered across objects and never aggregated, answering "what depends on X?" or "what does Y impact?" requires re-traversing the corpus. Refactoring proceeds without dependency information; orphans accumulate silently.

**Upstream dependencies.**

- [Addressability](#^t1-addressability) (parent criterion): queryability presupposes that targets have stable references.

**Downstream consequences.**

- Relational-graph representation (decision in the relations-graph theme): the chosen mechanism — alternatives are relational tables and triple stores.
- Build-aggregation rule (decision in the relations-graph theme): how object-local relations are collected into a queryable structure.
- Orphan-detection mechanism (decision in the registries-indexes theme): one queryability operation made first-class.