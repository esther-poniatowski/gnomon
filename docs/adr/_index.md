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
- [Dimensional formula of a quantity](dimensional-formula.md): decides where a record states the dimension of a quantity, for a check of homogeneity
- [Dotted identifiers](dotted-identifiers.md): fixes the form of a reference to a record or to a unit nested inside it
- [Grammatical fields and prose readings](grammatical-fields-and-readings.md): separates the fields that a tool interprets from the prose written for a reader
- [Single field per fact](single-field-per-fact.md): tells a field that carries a fact from a field that restates that fact
- [Grounds for a shared field](shared-field-grounds.md): decides whether a proposed field belongs in every record or in the case that raised it
- [Content of a claim](claim-content.md): decides how a claim states its propositional content, its presuppositions and a conditional or counterfactual content
- [Requirements of a law](law-requirements.md): decides how a law names the assumptions on which it rests, so that every record using the law inherits them
- [Records neutral on existence](neutral-records-on-existence.md): bounds the presuppositions that a record may hold about the existence of the objects that it describes

## Sources and checks

- [One source per unit of content](one-source-per-unit.md): locates the single authored source of each unit, and the copies admitted beside it
- [Registries for vocabularies and requirements](registries-as-source.md): locates the file that declares an admitted value, before a vocabulary is extended
- [Record schemas](record-schemas.md): locates the file that declares the shape of a record, for validation and for rendering in Ekphrasis
- [Records as the only input of checks](checks-read-records.md): bounds the files that a check may read
- [No inference at run time](no-run-time-inference.md): divides the values that a tool computes from the judgments that the researcher authors
- [Findings output](findings-output.md): fixes the rule, the resource and the locus under which a check reports a defect to the gate

## Record kinds and relations

- [Admission of a record kind](record-kind-admission.md): decides whether a proposed construct becomes a record of its own or a unit of an existing record
- [Answers, models and bindings](answers-models-bindings.md): decides which records hold a candidate answer, its model and the relation of that model to the phenomenon
- [Itinerary and product types](itinerary-and-product-types.md): names the record of the acts of an inquiry and the types of their products
- [Design record](design-record.md): decides which record holds a plan of acts, and the role that it bears
- [Derivation record](derivation-record.md): decides which record holds the reasoning that establishes a consequence, and the parts of that record
- [Concepts, glossaries and notations](concepts-glossaries-notations.md): decides how a concept, its names and its symbols are recorded
- [Closed typed relations](closed-typed-relations.md): decides how a relation between records is typed and checked
- [Assembly of a level](assembly-of-a-level.md): decides which records state the assembly of a level of an inquiry, and which part of it is authored

## Versions and revision

- [Versions and history](versions-and-history.md): tells where a reference fixes the state of its target, and where git alone keeps the history
- [Revision accountability](revision-accountability.md): states the requirements that every mechanism recording a revision must meet
- [Relation registry](relation-registry.md): decides which file declares the relations between research units, and how a revision travels along them

## Ecosystem ownership

- [Research as the scope of gnomon](research-scope.md): decides whether a record, a check or a note belongs to `gnomon` or to `ekthesis`
- [Expositions as projections](expositions-as-projections.md): records the earlier placement of exposition in `gnomon`, superseded by the decision on research as the scope of gnomon
- [Terminology, audience and project specifications](terminology-audience-project-specifications.md): places the mechanism of a notation, a glossary, an audience or a project specification apart from its instances
- [Knowledge interchange format](knowledge-interchange-format.md): decides whether the Open Knowledge Format serves `gnomon` as a source format, a derived export or a source of trust fields
