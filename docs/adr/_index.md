---
tags:
  - index
index: "[gnomon documentation](docs/_index.md)"
aliases:
  - Architecture decisions
---
# Architecture decisions

One record per decision that later work must respect. Each states the constraint that forced the choice, the options weighed against it, and what the choice costs, so a reader can tell whether a changed constraint reopens the question.

- [Surface syntax and parseable core for expressions](expression-syntax.md) keeps the infix form authors write and defines it over an S-expression core, so a parser becomes available without changing what a record looks like.
