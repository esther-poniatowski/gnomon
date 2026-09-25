---
tags:
  - examples
index: "[Turbulence anomalous scaling](test/turbulence-anomalous-scaling/_index.md)"
aliases:
  - Turbulence anomalous-scaling specification issues
---
# Current assessment of the turbulence specification

## Result

The target uses spatial position as an *index*. The phenomenon defines scalar increments and structure functions for the longitudinal and transverse sectors separately. Each sector has its own scaling exponent. The question requires the answer to match both exponent families numerically and their joint distribution structurally.

The foil now compares longitudinal and transverse scaling exponents. The foil does not call their difference anisotropy, because distinct longitudinal and transverse intermittency can occur in statistically isotropic turbulence.

## Global issue

The local `stationary` predicate has a precise input type and returns a Boolean, but the result type of the `regions` constructor is still open. As in the case of active matter, the expression language cannot state that a constructor returns a spatial set suitable as an index extent.

## Deliberately open science and design

Two quantities are research products: the values of the exponents, and the range of forcing and boundary families over which they are universal. The quantification of their scope therefore remains open. The two numerical bounds on tolerance are also design choices of the inquiry: no cited result fixes either bound.

No candidate artifact is supplied.
