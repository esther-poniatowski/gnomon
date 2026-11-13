---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-11-10
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Record schemas
---
# Record schemas

> [!QUESTION] Goal: which file declares the shape of an inquiry record, so that a program can validate the record and an editor can render it as a form?

**Amended** on 2026-11-01 by the decision of `geonexus` on [tool roles](https://github.com/esther-poniatowski/geonexus/blob/827474dca64daef110b9d7fe36a4127c2b32b167/docs/_decisions/tool-roles.md): a schema that narrows no vocabulary keeps its binding to `gnomon:<type>@<n>`; a schema that narrows a vocabulary follows rule 4 of that decision, an unbound base schema and a bound contract.

Before this decision, YAML templates specified the records of `gnomon`, and their comments stated the admitted values and field guidance. A comment is read by an author only. No program validates the shape of a record against it, and Ekphrasis, the form editor of the consumers of `gnomon`, renders a record only from a JSON Schema.

## Decision

Each record type is declared by a JSON Schema in `src/gnomon/data/schemas/`, written in YAML under the draft 2020-12. The schema requires a root property `_schema`, fixed by `const` to a logical identifier `gnomon:<type>@<version>`, where the version is a positive integer, and it keeps its own `$id`. Its keyword `x-identifier` designates the field `id`, so that links by identifier resolve. Each field carries a non-empty `title` and `description` for the author. Schema keywords and extensions, including `x-kind`, describe the data and the intended interaction without assigning Gnomon ownership of the rendered control. An authored entry of `examples` gives representative content. The generated contract gives each field governed by an epistemic note a canonical GitHub link. When no authored example exists, the contract publishes the parsed `x-template` value through the standard `examples` keyword. This value shows the input shape rather than representative research content.

Structural constraints on one record are stated in standard JSON Schema keywords. Conditional epistemic requirements, including requirements that relate several records, stay in the [requirement registry](../../src/gnomon/data/requirements.yml) and the checkers of `gnomon`. Ekphrasis invokes those checkers rather than reimplementing them. A closed vocabulary stays declared in its registry, and a generator writes its values into the schemas. The templates are generated from the schemas.

The generated contracts and their referenced base schemas are the integration source for record shapes, field guidance, interaction metadata and closed vocabularies. The generated view schemas are the integration source for view shapes. Conditional epistemic requirements must reach Ekphrasis through Gnomon findings after the custom-checker bridge is implemented, not through a copied form rule. Ekphrasis owns the controls, their progressive display and the presentation of issues. Ekphrasis edits the YAML source while preserving fields and comments outside the edited value. The [saving specification](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/features/saving.md) defines that editing behavior. ^ekphrasis-schema-interface

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
- The resource record `specs/schema-resources.yml` lists the exported contracts and view schemas, and Kleisis generates the registry `specs/schema-registry.yml` from it. The view schemas lie in the subfolder `views/` of the schema folder, so that Kleisis, which reads one folder of owned schemas, exports them with the contracts; each binds `gnomon:view.<name>@<version>`. Each schema file ends in `.schema.yml`, the suffix by which Kleisis recognizes an owned schema. A base schema declares no property `_schema`, since Kleisis reads such a property as the binding of a contract.
- The installed package carries the resulting Gnomon schemas and the pinned external contracts required by their closure. The command `gnomon setup` copies this closure into configurable paths below an Obsidian vault and derives a registry that names only those copies. Thus, Kleisis remains the source-dependency boundary of the Gnomon project, while Ekphrasis receives no path or behavior tied to the Gnomon checkout.
- The [schema compatibility decision](schema-contract-compatibility.md) determines when a logical contract advances and when an earlier contract may retire.
- A check reports a schema whose vocabularies differ from the registries, and a template that differs from its generated form. Such a check compares a generated copy with its source, unlike a check holding two authored copies equal, and it replaces the check of template comments of the decision on registries.
