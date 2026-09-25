---
tags:
  - examples
index: "[Active-matter phase exploration](test/active-matter-phase-exploration/_index.md)"
aliases:
  - Active-matter phase exploration issues
---
# Current assessment of the specification for active matter

## Result

The current records use the evolved framework correctly:

- target variants separate continuum and lattice declarations;
- signatures retain every observable index;
- named scope axes distinguish realizations from sampled operators;
- the `not-applicable` value correctly closes the accuracy requirement for a formal exploration.

## Global issue

The return type of each domain constructor in [the operators that this problem declares](operators.yml) remains `open`. The framework can check the arity of each constructor, but it cannot express that `regions(...)` returns a spatial set and `sites(...)` a finite lattice set. The open return type is therefore a limitation of the expression language, not an unknown phase property.

## Deliberately open science

Every field reserved for the discovered phase is filled only by the exploration. The open values are therefore required. Although the discovered phase stays open, the detection procedures already require that each candidate recur, separate from others in control space, and persist in finite systems.

## Answer and assessment trial

[The candidate catalogue](answer.yml) intentionally imports a published continuum result without treating it as the completed exploration. [The catalogue correctly fails six tests of the assessment](assessment.yml):

- at the admissibility level: scope, grain, modal strength, and product;
- at the warrant level: closure and robustness.

The admissibility failures follow from incomplete coverage of the target and from missing persistence tests. The warrant failures follow from the derivation of the candidate laws: the generic target laws do not select the ordered state or the normal form from which they are derived, and the answer relaxes neither its noiseless idealization nor its reduction to weak amplitude.

The trial also exposes a defect of the answer form shared across cases: an exploratory product has no explanans, yet the form requires an `explanans` block. The candidate must therefore represent its classification rule as an explanans that “produces” the catalogue. The rule, however, identifies phases and does not explain an antecedently fixed phenomenon. The defect is recorded once, together with [the other flaws shared by the answer and assessment templates](../answer-assessment-template-issues.md).
