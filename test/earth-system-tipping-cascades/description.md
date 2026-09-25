---
tags:
  - examples
index: "[Earth-system tipping cascades](test/earth-system-tipping-cascades/_index.md)"
aliases:
  - Climate tipping-cascade test description
---
# Tipping cascades under warming and overshoot

## Research problem

Tipping elements of the Earth system may interact, so one transition can change the conditions that govern another. Under specified warming trajectories, what probability distribution governs transition sequences and their timing? How does temporary temperature overshoot alter that distribution?

## Formal target

The target is the actual Earth system represented by four coupled subsystems: the Greenland and West Antarctic ice sheets, the Atlantic Meridional Overturning Circulation, and the Amazon rainforest. Each subsystem has empirically constrained dynamics, but the joint laws and coupling strengths remain only partially known. External forcing trajectories condition predictions about future transition sequences.

## Expressivity challenge

The test is built to require the framework to:

- represent a particular empirical target with partial closure and explicit interfaces among subsystems;
- describe every attribute of a future transition sequence (identity, order, and timing) through an ensemble distribution;
- distinguish a forcing trajectory that conditions a prediction from restrictions that delimit the question's domain;
- request a statistical prediction with separate accuracy requirements for event probabilities and transition times;
- distinguish sources of predictive spread (physical randomness, imprecisely known parameter values, and an unsettled model structure).

The [phenomenon template](../../src/gnomon/data/templates/phenomenon.yml) admits scope axes that repeat and that condition the requested distribution. The case tests whether those axes keep the distinct sources of predictive uncertainty apart in that distribution.

## Scope boundary

The case does not assume that every proposed tipping element belongs in one model. The case also withholds a preferred coupling architecture and a fixed warming scenario.

## Scientific basis

Interactions among tipping elements can alter thresholds and enable cascades ([wunderling2024](https://esd.copernicus.org/articles/15/41/2024/)). Temporary warming overshoots increase the risk of tipping cascades in a stylized network model ([wunderling2023](https://www.nature.com/articles/s41558-022-01545-9)).
