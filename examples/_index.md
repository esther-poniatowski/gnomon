---
tags:
  - index
index: "[gnomon documentation](docs/_index.md)"
aliases:
  - Worked inquiries
---
# Worked inquiries

Tests the records of `gnomon` on completed inquiries, to consult before filling the [record templates](../src/gnomon/data/templates/_index.md), and on single research statements that resist formalization.

> [!IMPORTANT] Folders of the test suite
> The tests parametrize over the folders of this directory. Their location and the expected folders are fixed in the [paths of the test suite](../tests/test_gnomon/paths.py), so a new or renamed folder is registered there as well. A test set kept as one file at this level, rather than as a folder, stays outside the parametrization.

## Inquiries

- [Phase exploration in active matter](active-matter-phase-exploration/_index.md): tests whether an open phenomenon can be specified without presupposing its macroscopic categories
- [Delayed generalization](grokking-delayed-generalization/_index.md): tests whether a known temporal regularity can be kept apart from its competing explanations
- [Anomalous scaling in turbulence](turbulence-anomalous-scaling/_index.md): tests whether a question about a limit system can keep its statistical target apart from requirements of universality
- [Tipping cascades in the Earth system](earth-system-tipping-cascades/_index.md): tests whether a prediction can carry several sources of uncertainty about a partially known system
- [Stable microbial coexistence](microbial-stable-coexistence/_index.md): tests whether necessary and sufficient conditions stay distinct across model variants
- [Localized Swift-Hohenberg states](swift-hohenberg-localized-states/_index.md): tests whether a description can name the features that it seeks without supplying their values
- [Neural tangent dynamics](neural-tangent-kernel-model-knowledge/_index.md): tests whether an inquiry can specify the knowledge that it seeks about a formal class of models

## Statements

- [Adversarial statements](adversarial-statements.md): tests whether the records of `gnomon` can state research statements that resist formalization
