---
tags:
  - examples
index: "[Localized Swift-Hohenberg states](test/swift-hohenberg-localized-states/_index.md)"
aliases:
  - Swift-Hohenberg description issues
---
# Current assessment of the specification of localized Swift–Hohenberg states

## Result

The phenomenon is fixed as the capacity to possess stationary localized profiles. Its named structural features remain open. The descriptive question uses `structures_to_match` to require every feature without treating any of them as a measurement or asking for an explanation.

## Global issues

The requirement registry adds no field for the `description` aim. The Swift–Hohenberg question voluntarily lists every requested feature under `structures_to_match`. The validator would nevertheless also accept a descriptive question with no coverage targets. The aim should require a list of the features to cover, or the accuracy block should make such targets mandatory when `standard: structural-only`.

The requested targets identify the features that a description must cover. The targets do not state the resolution at which the variation of the branches over `(r, b)` must be reported. A coverage domain or grain declared per target would make partial catalogues assessable.

The local `powerset` constructor leaves its result type open. The records can still state sets of profiles, of topology labels, and of stability intervals, but the operator checker cannot verify the type of these sets.

## Deliberately open science

The requested characterization of the branches is the descriptive product. The feature values of this characterization therefore remain open in the phenomenon record, pending a candidate answer.

## Answer and assessment trial

[The qualitative catalogue](answer.yml) supplies the observed topology and the symmetry classes. The candidate also supplies the stability criterion. [The catalogue passes individuation and actual modal strength](assessment.yml). Formal closure also passes. The catalogue fails scope and grain. Product and fidelity fail because the candidate does not report every stability interval across `(r, b)`.

The answer has no structured field that binds its proposed values to the three manifestation features. The answer instead asserts `topology` and `symmetry` inside laws. A third law asserts `stability`, and the answer recasts the three descriptive procedures as explanans factors. Both workarounds compensate for template problems that recur across cases and are recorded among [the findings shared by all answer trials](../answer-assessment-template-issues.md).
