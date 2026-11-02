---
tags:
  - audit
index: "[Stable microbial coexistence](examples/microbial-stable-coexistence/_index.md)"
aliases:
  - Microbial stable-coexistence specification issues
---
# Current assessment of the specification for microbial coexistence

## Result

The evolved framework represents the two model families as target variants. Each declared element is assigned only to the members that possess it. Feasibility and local stability are separate manifestations. Two proof obligations preserve the directions of necessity and sufficiency. The `not-applicable` accuracy standard keeps the validity of a theorem separate from measurement error.

## Global issue

The complete equilibrium state and the dimension of the Jacobian depend on the target variant. The [operators](operators.yml) that this problem declares must therefore leave three types open:

- the input type of the member specification;
- the input type of the complete state;
- the output type of the Jacobian.

A dependent sum, or a state type indexed by the variant, would let the checker verify the same operators on the complete dynamics without duplicating the coexistence observables.

## Deliberately open science

The antecedent of the sufficient condition and the consequent of the necessary one are requested modal knowledge. The class and the supply ranges over which each condition holds are also requested. Existing results do not settle these requests: they support stability only under narrower structural assumptions, so they do not justify a universal implication across both admitted variants.

## Answer and assessment trial

The [consumer-resource theorem](answer.yml) supplies one of those narrower results. In its [assessment](assessment.yml), the theorem passes the sufficient proof obligation for the stated subclass and fails three checks:

- the obligation of the necessary direction;
- the scope, which covers both variants;
- the product over the full class.

Because the obligations are ordered, the assessment keeps necessity and sufficiency distinct and does not turn a unidirectional theorem into a biconditional.

The answer names the target variant `community with explicit resources`, and its core declares the narrower domain of the theorem: communities whose resource pools are at least as numerous as the populations and whose microbes consume resources without producing any. Each hypothesis of the theorem is a ground of role `condition`, as the [decision on answers, models and bindings](../../docs/adr/answers-models-bindings.md) provides.
