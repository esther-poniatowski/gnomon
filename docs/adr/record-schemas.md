---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Record schemas
tags: []
source:
---
# Record schemas

> [!QUESTION] Goal: which file declares the shape of an inquiry record, so that a program can validate it and an editor can render it as a form?

The records of `gnomon` are specified by YAML templates, whose comments state the admitted values and the guidance for each field. A comment is read by an author only. No program validates the shape of a record against it, and Ekphrasis, the form editor used by the consumers of `gnomon`, renders a record only from a JSON Schema.

## Decision

Each record type is declared by a JSON Schema in `src/gnomon/data/schemas/`, written in YAML under the draft 2020-12. The schema requires a root property `_schema`, fixed by `const` to a logical identifier `gnomon:<type>@<version>`, and it keeps its own `$id`. Each field carries a `title`, a `description` and `examples` for the author, and an `x-kind` that selects its control in Ekphrasis. A closed vocabulary stays declared in its registry, and a generator writes its values into the schemas. The templates are generated from the schemas.

## Constraints that decide the source

- **Ekphrasis renders and validates only JSON Schemas.** A record bound to a schema through `_schema` opens as a form, and a schema states its rules in standard keywords or under `x-rules`.
- **A registry declares each closed vocabulary once.** The [decision on registries](registries-as-source.md) makes package data the source of every vocabulary, so a schema that restated an option list by hand would hold a second copy.
- **A template restated by hand would drift.** Declaring the fields in both a template and a schema would need a check whose only purpose is to hold them equal, as the [single field per fact](single-field-per-fact.md) forbids.
- **A rule across records exceeds JSON Schema.** The resolution of symbols, the itinerary check and the conditions of answerability read several records, so they stay in the checkers of `gnomon`.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Keep the templates as the only specification | No new file per record type | No program validates the shape of a record, and no editor renders it as a form |
| Write each schema by hand, beside its template | Each schema reads on its own | The option lists and the fields exist twice, once in the registries or templates and once in the schemas |
| Generate the schemas from the templates | The templates stay the single source | A comment carries no type, so the types and controls of the fields have no source |
| Declare the shape in the schemas, write the vocabularies from the registries, and generate the templates | Each fact has one source, and both a program and an editor read the schema | A generator must run after each change to a registry or a schema |

## Consequences

- The index of `src/gnomon/data/schemas/` lists one schema per record type, with its logical identifier.
- The schemas are exported for consumers through a generated registry of logical identifiers, so that a workspace resolves `gnomon:<type>@<version>` to the schema of the installed version.
- A check reports a schema whose vocabularies differ from the registries, and a template that differs from its generated form.
- A rule across several records stays in the checkers of `gnomon`, and Ekphrasis may call such a checker as a custom checker.
