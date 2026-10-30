---
tags:
  - index
index: "[gnomon documentation](docs/_index.md)"
aliases:
  - Architecture decisions
---
# Architecture decisions

Records the decisions that later work on `gnomon` must respect, so that a reader can judge whether a changed constraint reopens one of them.

> [!IMPORTANT] Form of a decision record
> Each record states the constraint that forced the choice, the options weighed against that constraint, and the cost of the choice. Its frontmatter states its status and its dates, under the [rules of the frontmatter block](../../CONTRIBUTING.md#frontmatter-block).

## Record language

- [Surface syntax and parseable core for expressions](expression-syntax.md): fixes the notation that formulas must use
- [Flat symbol table per record](flat-symbol-table.md): decides where a symbol is declared within a record
- [Dotted identifiers](dotted-identifiers.md): fixes the form of a reference to a record or to a unit nested inside it
- [Grammatical fields and prose readings](grammatical-fields-and-readings.md): separates the fields that a tool interprets from the prose written for a reader
- [Single field per fact](single-field-per-fact.md): tells a field that carries a fact from a field that restates that fact
- [Grounds for a shared field](shared-field-grounds.md): decides whether a proposed field belongs in every record or in the case that raised it

## Sources and checks

- [One source per unit of content](one-source-per-unit.md): locates the single authored source of each unit, and the copies admitted beside it
- [Registries for vocabularies and requirements](registries-as-source.md): locates the file that declares an admitted value, before a vocabulary is extended
- [Record schemas](record-schemas.md): locates the file that declares the shape of a record, for validation and for rendering in Ekphrasis
- [Records as the only input of checks](checks-read-records.md): bounds the files that a check may read
- [No inference at run time](no-run-time-inference.md): divides the values that a tool computes from the judgments that the researcher authors

## Record kinds and relations

- [Admission of a record kind](record-kind-admission.md): decides whether a proposed construct becomes a record of its own or a unit of an existing record
- [Answers, models and bindings](answers-models-bindings.md): decides which records hold a candidate answer, its model and the relation of that model to the phenomenon
- [Itinerary and product types](itinerary-and-product-types.md): names the record of the acts of an inquiry and the types of their products
- [Concepts, glossaries and notations](concepts-glossaries-notations.md): decides how a concept, its names and its symbols are recorded
- [Closed typed relations](closed-typed-relations.md): decides how a relation between records is typed and checked

## Versions and revision

- [Versions and history](versions-and-history.md): tells where a reference fixes the state of its target, and where git alone keeps the history
- [Revision accountability](revision-accountability.md): states the requirements that every mechanism recording a revision must meet

## Ecosystem ownership

- [Expositions as projections](expositions-as-projections.md): bounds the content that an exposition may add to the research that it presents
- [Terminology, audience and project specifications](terminology-audience-project-specifications.md): places the mechanism of a notation, a glossary, an audience or a project specification apart from its instances
- [Knowledge interchange format](knowledge-interchange-format.md): decides whether the Open Knowledge Format serves `gnomon` as a source format, a derived export or a source of trust fields
