---
tags:
  - examples
index: "[Stable microbial coexistence](_index.md)"
aliases:
  - Microbial stable-coexistence specification issues
---
# Current assessment of the microbial-coexistence specification

## Result

The evolved framework represents the two model families as target variants and assigns every declaration only to members that possess it. Feasibility and local stability are separate manifestations. Two proof obligations preserve the directions of necessity and sufficiency. The `not-applicable` value keeps theorem validity out of measurement accuracy.

## Global issue

The complete equilibrium state and Jacobian dimension depend on the target variant. [The local operator record](operators.yml) must therefore leave the member-specification and complete-state input types open, as well as the Jacobian output type. A dependent sum or variant-indexed state type would allow the same complete-dynamics operators to be checked without duplicating the coexistence observables.

## Deliberately open science

The sufficient condition's antecedent and the necessary condition's consequent are requested modal knowledge. Their valid class and supply ranges are also requested. The two implication terms and their quantified ranges must remain open. Existing results support stability only under narrower structural assumptions; they do not justify a universal implication across both admitted variants.

No candidate artifact is supplied.
