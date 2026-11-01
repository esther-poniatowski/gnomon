---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-29
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Record schemas
---
# Record schemas

> [!QUESTION] Goal: which file declares the shape of an inquiry record, so that a program can validate the record and an editor can render it as a form?

**Amended** on 2026-11-01 by the decision of `geonexus` on [tool roles](https://github.com/esther-poniatowski/geonexus/blob/827474dca64daef110b9d7fe36a4127c2b32b167/docs/_decisions/tool-roles.md): a schema that narrows no vocabulary keeps its binding to `gnomon:<type>@<n>`; a schema that narrows a vocabulary follows rule 4 of that decision, an unbound base schema and a bound contract.

The records of `gnomon` are specified by YAML templates, whose comments state the admitted values and the guidance for each field. A comment is read by an author only. No program validates the shape of a record against it, and Ekphrasis, the form editor of the consumers of `gnomon`, renders a record only from a JSON Schema.

## Decision

Each record type is declared by a JSON Schema in `src/gnomon/data/schemas/`, written in YAML under the draft 2020-12. The schema requires a root property `_schema`, fixed by `const` to a logical identifier `gnomon:<type>@<version>`, where the version is a positive integer, and it keeps its own `$id`. Its keyword `x-identifier` designates the field `id`, so that links by identifier resolve. Each field carries a `title`, a `description` and `examples` for the author, and an `x-kind` that selects its control in Ekphrasis.

A rule on one record is stated in standard keywords or under `x-rules`. A rule across several records stays in the checkers of `gnomon`, and Ekphrasis may call those checkers as custom checkers. A closed vocabulary stays declared in its registry, and a generator writes its values into the schemas. The templates are generated from the schemas.

## Constraints that decide the source

- **Ekphrasis renders and validates only JSON Schemas.** A record bound to a schema through `_schema` opens as a form.
- **A registry declares each closed vocabulary once.** The [decision on registries](registries-as-source.md) makes package data the source of every vocabulary, so a schema that restated an option list by hand would hold a second copy.
- **A field is declared once.** A template written by hand beside its schema would hold a second copy of the fields. The [single field per fact](single-field-per-fact.md) excludes that copy.
- **A rule across records exceeds JSON Schema.** The resolution of symbols, the itinerary check and the conditions of answerability read several records.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep the templates as the only specification | No new file per record type | No program validates the shape of a record, and no editor renders it as a form |
| Write each schema by hand, beside its template | Each schema reads on its own | The option lists and the fields exist twice, once in the registries or templates and once in the schemas |
| Generate the schemas from the templates | The templates stay the single source | A comment carries no type, so the types and controls of the fields have no source |
| Declare the shape in the schemas, write the vocabularies from the registries, and generate the templates | Each fact has one source, and both a program and an editor read the schema | A generator must run after each change to a registry or a schema |

## Consequences

- The record schemas live in `src/gnomon/data/schemas/`, whose index gives the logical identifier of each schema.
- The schemas are exported as files of a Git revision. A consumer materializes them from an exact commit, and resolves `gnomon:<type>@<version>` through its own generated registry.
- A check reports a schema whose vocabularies differ from the registries, and a template that differs from its generated form. Such a check compares a generated copy with its source, unlike a check holding two authored copies equal, and it replaces the check of template comments of the decision on registries.
