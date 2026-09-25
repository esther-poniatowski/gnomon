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

- [Surface syntax and parseable core for expressions](expression-syntax.md): to know which notation formulas must use, and which change of constraint would reopen that choice.
- [Flat symbol table per record](flat-symbol-table.md): to place a declaration, and to know why no block of a record opens a scope of its own.
- [Single field per fact](single-field-per-fact.md): to tell a field that carries a fact from a field that restates that fact.
- [Grounds for a shared field](shared-field-grounds.md): to decide whether a proposed field belongs in every record or in the case that raised it.
- [Registries for vocabularies and requirements](registries-as-source.md): to reach the file that declares an admitted value, before extending a vocabulary.
