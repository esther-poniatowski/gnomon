---
tags:
  - examples
index: "[Active-matter phase exploration](_index.md)"
aliases:
  - Active-matter phase exploration issues
---
# Current assessment of the active-matter specification

## Result

The current records use the evolved framework correctly. Target variants separate continuum and lattice declarations. Signatures retain every observable index. Named scope axes distinguish realizations from sampled operators. The `not-applicable` value correctly closes the accuracy requirement for a formal exploration.

## Global issue

The type of a problem-specific domain constructor remains `open` in [the operator record](operators.yml). The framework can check the constructor's arity but cannot express that `regions(...)` returns a spatial set and `sites(...)` a finite lattice set. The open return type is a limitation of the expression language, not an unknown phase property.

## Deliberately open science

Every field that would assert the discovered phase remains a product of the exploration. The open values are therefore required. The detection procedures already require recurrence and separation in control space together with finite-size persistence.

No answer or assessment record is warranted before a phase catalogue is produced.
