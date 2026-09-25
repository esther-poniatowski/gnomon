---
tags:
  - examples
index: "[Delayed generalization](test/grokking-delayed-generalization/_index.md)"
aliases:
  - Grokking test description
---
# Delayed generalization in trained neural networks

## Research problem

Delayed generalization occurs when a network reaches near-zero training error long before its test error falls. For overparameterized networks trained on algorithmic tasks, what produces this delay? What determines its duration and its variation across random initial conditions?

## Formal target

The target is a class of finite neural networks trained by gradient-based algorithms on sampled data. Training and test losses define a temporal regularity across runs with distinct initial conditions. Immediate generalization and persistent memorization supply two substantive foils.

## Expressivity challenge

The later test must require the framework to:

- represent a system class whose training specification assigns distinct roles to its components (architecture, optimizer, and data distribution);
- define a known phenomenon through trajectories observed across time and an ensemble of initial conditions;
- distinguish the observed regularity from the requested mathematical explanation;
- connect parameter dynamics to derived collective quantities without fixing the explanatory level prematurely;
- require unification and structural transparency independently of predictive accuracy.

## Scope boundary

The case does not presuppose that one proposed mechanism explains every instance of delayed generalization. A prediction for one benchmark does not constitute a complete answer by itself.

## Scientific basis

In an effective theory, structured representations emerge within a restricted regime near memorization, so generalization is delayed ([liu2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/dfc310e81992d2e4cedc09ac47eff13e-Abstract-Conference.html)). Local complexity measures provide a distinct account of the transition from memorization to generalization ([humayun2024](https://proceedings.mlr.press/v235/humayun24a.html)).
