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

- [Surface syntax and parseable core of expressions](expression-syntax.md): to know which notation formulas must use, and which change of constraint would reopen that choice.
