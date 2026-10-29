---
tags:
  - index
index: "[gnomon documentation](docs/_index.md)"
aliases:
  - Architecture decisions
---
# Architecture decisions

Each record fixes one decision that later work must respect. To let a reader decide whether a changed constraint reopens the decision, each record states:

- the constraint that forced the choice;
- the options weighed against that constraint;
- the cost of the choice.

The records:

- [Surface syntax and parseable core for expressions](expression-syntax.md): fixes the notation that formulas must use, and the change of constraint that would reopen that choice
- [Flat symbol table per record](flat-symbol-table.md): places a declaration, and explains why no block of a record opens a scope of its own
- [Single field per fact](single-field-per-fact.md): tells a field that carries a fact from a field that restates that fact
- [Grounds for a shared field](shared-field-grounds.md): decides whether a proposed field belongs in every record or in the case that raised it
- [Registries for vocabularies and requirements](registries-as-source.md): locates the file that declares an admitted value, before a vocabulary is extended
- [Itinerary and product types](itinerary-and-product-types.md): names the record of the acts of an inquiry and the types of their products
- [Dotted identifiers](dotted-identifiers.md): fixes the form of a reference to a record or to a unit nested inside it
- [Record schemas](record-schemas.md): locates the file that declares the shape of a record, for validation and for rendering in Ekphrasis
- [Expositions as projections](expositions-as-projections.md): bounds what an exposition may add to the research that it presents, and names the tool that specifies it
- [Terminology, audience and project specifications](terminology-audience-project-specifications.md): places the mechanism of a notation, a glossary, an audience or a project specification apart from its instances
- [Concepts, glossaries and notations](concepts-glossaries-notations.md): separates the meaning of a concept from its names, and composes the symbols of a notation
- [Answers, models and bindings](answers-models-bindings.md): tells which records hold a candidate answer, its model and the relation of that model to the phenomenon
- [Records as the only input of checks](checks-read-records.md): bounds the files that a check reads, and names the process that produces its verdict
- [Grammatical fields and prose readings](grammatical-fields-and-readings.md): separates the fields that a tool interprets from the prose written for a reader
- [One source per unit of content](one-source-per-unit.md): locates the single authored source of each unit, and the copies admitted beside it
- [No inference at run time](no-run-time-inference.md): divides the values that a tool computes from the judgments that the researcher authors
- [Revision accountability](revision-accountability.md): states the requirements that every mechanism recording a revision must meet
- [Closed typed relations](closed-typed-relations.md): fixes the types, the ends and the graph of the relations between records
- [Admission of a record kind](record-kind-admission.md): decides whether a proposed construct becomes a record of its own or a unit of an existing record
- [Versions and history](versions-and-history.md): tells where a reference fixes the state of its target, and where git alone keeps the history
