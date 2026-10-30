---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Binding record
---
# Binding record

> [!QUESTION] Goal: what does a researcher write in each field of a binding record, and when is each field required?

A binding records the surrogative inferences from a model to its target that its asserter licenses, as the [theory of the binding](../epistemology/answer/model-and-binding.md) states. Similarity holds in respects and to degrees fixed by a purpose [giere2004] [weisberg2013], so the pairs of a binding state those respects, and the tolerance of the question states those degrees. ^binding-record

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Model — the model in use | always | the identifier of one model record | the rate model of an excitatory and an inhibitory population |
| Target — the denotation of the phenomenon, and the level at which the model is compared | always | the identifier of one phenomenon, and the target level: `phenomenon`, when the model is compared with the explanandum variables that the phenomenon estimates; `data`, when it is compared with a version of the data through an observation operator | the gamma oscillations of the network (phenomenon); the recorded local field potentials, version 3 (data) |
| Asserter — the agent who licenses the inferences | always | a person, a group or a publication | the authors of the answer; the publication that proposed the model |
| Feature pairs | always | per pair, a feature that the model exemplifies and the feature of the target to which it is imputed, typed: `quantity` · `pattern` · `regime` · `invariance-class` (an invariance or a universality class) · `modal-profile` · `component` (a unit of the model and the constituent or the admissible part of the target that it denotes); the [mode](../epistemology/answer/model-and-binding.md#^pair-modes) of the pair, `computed` or `argued`; and, for a computed pair, the key that carries the one onto the other | the model frequency and the peak of the measured spectrum (quantity); the oscillating regime of the model and the synchronous regime of the network (regime); the scaling exponents shared by a universality class (invariance class) |
| Condition pairs | when a condition of the model is set to stand for a condition of the target | per pair, a condition of the model, the condition of the target that it stands for, and the key; a parameter fitted to the data is marked as a *calibration parameter* | the external drive of the model and the stimulus contrast; the coupling strength (calibration parameter) |
| Domain of comparison | always | the conditions of the target over which the pairs are asserted, each region marked as *interpolation*, within the range of the calibration data, or *extrapolation*, outside it | contrasts from 10 % to 80 % (interpolation); a contrast of 100 % (extrapolation) |
| Structural discrepancy | when the grain is quantitative | the model of the systematic difference between the output of the model at its best parameters and the value of the target, or a stated bound on it [kennedyohagan2001]; a discrepancy model fitted to data counts as calibration on those data, and the calibration provenance records it | a Gaussian process over the contrast; a bound of 5 Hz on the frequency |
| Calibration provenance | when a pair carries a calibration parameter | per calibration parameter, the version of the data that fitted it, the method of fitting, and whether the parameter is identifiable under the structural discrepancy [brynjarsdottir2014] | the coupling strength, fitted by least squares to the session of day 1, not identifiable apart from the discrepancy |
| Grain | always | `quantitative`, when the pairs are compared by a metric · `qualitative`, when they are compared by a match of patterns or regimes | — |
| Version | always | a version identifier, and the time at which the binding was committed | version 2, committed before the recordings of version 3 |

- **The binding belongs to neither the model nor the answer.** One model grounds several answers, so a binding owned by an answer would be repeated across every answer that shares the model, together with its keys. The binding therefore stands between the model and the phenomenon, and an answer cites the binding through which its claim bears on the target. ^binding-owner

- **A calibration parameter states whether the data identify it.** When the structural discrepancy is ignored, a calibrated parameter can absorb the discrepancy and take a value without physical meaning [brynjarsdottir2014]. The calibration provenance therefore states, per parameter, whether the parameter is identifiable apart from the discrepancy. ^calibration-provenance

- **A revised binding is a new version.** A change of a pair, a key, the domain or the discrepancy creates a new version with its own time of commitment. The earlier version, and every comparison computed from it, stays unchanged, so that a reader can tell a binding fixed before the data from a binding adjusted to them. A version of the data whose comparison motivated the revision counts as calibration data for the new version. A comparison of the new version with those data therefore reports its [calibration treatment](../epistemology/answer/model-and-binding.md#^comparison-reports), as for any data used to fit a parameter. ^binding-version

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [brynjarsdottir2014] ◐ Brynjarsdóttir & O'Hagan, "Learning about physical parameters: the importance of model discrepancy", *Inverse Problems* 30, 114007, 2014
- [giere2004] ◐ Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004
- [kennedyohagan2001] ◐ Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society B* 63(3), 425–464, 2001
- [weisberg2013] ◐ Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013
