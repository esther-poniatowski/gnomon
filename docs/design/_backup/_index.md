---
tags:
  - index
  - backup
index: "[Design documentation](../_index.md)"
aliases:
  - Superseded design proposals
---
# Superseded design proposals

Each proposal records the reasoning that produced a current commitment and binds no decision, since the [tiered design folder](../_index.md) is authoritative. A proposal is kept because the alternatives it weighed are not restated in the tier files.

| Proposal | Content |
| --- | --- |
| [Layered model proposal](architecture-1-layered-model.md) | The conditions each layer must satisfy for a layered model to be appropriate. |
| [Operational framework specification](architecture-2-spec.md) | The layers that represent how inference progresses locally. |
| [Operational framework audit](architecture-2-audit.md) | Where that framework leaves a transition unaccounted for, beginning with the step from a question to a goal. |
| [Architecture C](architecture-C.md) | A representation stratified into three granularity levels, each argued necessary and non-redundant. |
| [Identifier and versioning proposal](ids-versioning.md) | The stable identifiers each object carries. |
| [Schema and fields proposal](schema-fields-base.md) | The fields each object type must define. |
| [User workflow proposal](workflow-for-users.md) | The routine a user follows, anchored on questions rather than on documents. |

Three groups of proposals are held in their own folders.

- [Argument and reasoning proposals](arguments-reasoning/_index.md): how a justification path is assembled, and how the steps inside a derivation are encoded.
- [Object-kind candidates](object-types-ontology/_index.md): one specification per candidate object kind, with the encoding scheme each receives.
- [Rendering proposals](rendering/_index.md): how a note is generated from a specification, and how it is audited afterwards.
