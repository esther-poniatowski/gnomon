---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the assembly schema
---
# Proposals for the assembly schema

The goal [`assembly-schema`](../../TODO.md) specifies the assembly of a level and its components. The status `core` or `elaboration` of a component, the views and the check of the core route move to `ekthesis`, as the [decision on the scope of gnomon](../adr/research-scope.md) states.

## Locus of the content that depends on an inquiry

Content that depends on an inquiry belongs to an assembly or to one of its steps, never to a reusable record: the motivation for citing a record, its strategic role, and the gain that it yielded. A record takes part in several inquiries, each with its own gap and its own gain, so a field of the record would let one inquiry stand for all of them. The assemblies that cite a record, with their roles, are found by a query over the graph of relations.

The assembly is no record kind, because its identity is relative to an inquiry and a target. The same records arranged toward another target form another assembly, and a lemma may serve as a premise in one assembly and as a conclusion in another. A record local to an assembly, such as an internal lemma, a named rejected route or the end of a support relation, is promoted to a record of its own once it passes the [admission of a record kind](../adr/record-kind-admission.md#^admission-conditions). Strategic notes, work metadata and the records of applied operations stay local. A check flags a candidate for promotion, and the author performs the promotion.

Three fields complete the assembly: its gaps, which are the dependencies not yet resolved; its limits of validity, which are its scope and its exclusions; and its deferred components, left out at the current grain. A query reports the laws to which each answer of the assembly is exposed, computed over its grounds, as the [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link) states.

**Literature.** None cited.

**Bears on.** [`assembly-schema`](../../TODO.md), and `relation-registry` for the [relations relative to an inquiry](relation-registry.md#semantic-and-justificatory-dependence).

**Retired source.** `docs/design/2-architecture/reasoning-structure.md`, `docs/design/_backup/arguments-reasoning/argument-bundles.md` and `docs/design/_backup/schema-fields-base.md`, at commit 9e138e2.
