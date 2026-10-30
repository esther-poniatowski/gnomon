---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Key record
---
# Key record

> [!QUESTION] Goal: what does a researcher write in each field of a key record, and when is each field required?

A key states one map between the two sides of a binding: an observation operator, a map of units, a map of aggregation, or a qualitative abstraction. Several bindings use the same observation operator or the same map of units, so a key is a record of its own, which those bindings reference by identifier and version. A key carries a version because a measurement outcome is itself inferred through a model, which can be revised [tal2013] [parker2017]. ^key-record

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Kind | always | `observation-operator` · `unit-map` · `aggregation-map` · `qualitative-abstraction` | the forward model from population rates to a local field potential (observation operator); the conversion of the dimensionless time of a model to seconds (unit map) |
| Domain and codomain | always | the side of the model and the side of the target that the key connects, each as a set expression or a type | from the rates of two populations to one potential; from trajectories to the labels `oscillating` and `silent` |
| Expression | always | an expression over the symbols of its domain, or a pointer to the procedure that computes the map | the mean over the neurons of a population; a threshold on the power in the gamma band |
| Version | always | a version identifier | version 1 |

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [tal2013] ◐ Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013
