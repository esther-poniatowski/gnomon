---
tags:
  - examples
index: "[Turbulence anomalous scaling](_index.md)"
aliases:
  - Turbulence anomalous-scaling specification issues
---
# Current assessment of the turbulence specification

## Result

The target uses spatial position as an index rather than a constituent. The phenomenon defines scalar increments and structure functions for the longitudinal and transverse sectors separately. Each sector has its own scaling exponent. The question requests numerical agreement for both exponent families and structural agreement for their joint distribution.

The foil now compares longitudinal and transverse scaling exponents. The foil does not call their difference anisotropy, because distinct longitudinal and transverse intermittency can occur in statistically isotropic turbulence.

## Global issue

The local `stationary` predicate has a precise input and Boolean output, but the `regions` constructor still has an open output type. As in the active-matter case, the expression language cannot state that a constructor returns a spatial set suitable as an index extent.

## Deliberately open science and design

The exponent values and the range of forcing and boundary families over which they are universal are research products. Their scope quantification therefore remains open. The two numerical tolerance bounds are also inquiry-design choices, and no cited result fixes them for this inquiry.

No candidate artifact is supplied.
