---
tags:
  - definition
  - wip
index: "[Regularities and phenomena](docs/epistemology/vocabulary/regularities/_index.md)"
aliases:
  - Mechanism and mechanistic model
  - Mechanism (term)
  - Mechanistic model
---
# Mechanism and mechanistic model

> [!QUESTION] Goal: which definition of "mechanism" does a statement use, and when does a model of a mechanism explain?

A **mechanism** is a set of entities and activities organized so that they produce a phenomenon. A **mechanistic model** is a representation of a mechanism. The aspects that a mechanistic answer must state are given in the note on the [mechanistic answer](../../objects/answer/mechanism.md). This note fixes the senses of the terms and the test of a mechanistic model.

## Senses

| Definition | Wording | Source |
| --- | --- | --- |
| Entities and activities | "Mechanisms are entities and activities organized such that they are productive of regular changes from start or set-up to finish or termination conditions." | [machamer2000] |
| Complex system | a mechanism for a behavior is a complex system that produces the behavior by the interaction of its parts, the interactions being characterized by direct, invariant, change-relating generalizations | [glennan2002] |
| Minimal | "A mechanism for a phenomenon consists of entities and activities organized in such a way that they are responsible for the phenomenon." | [illari2012] |
| Function-performing structure | a structure that performs a function by virtue of its component parts, their operations and their organization | [bechtel2005] |
| Characteristic process | the mechanism $\mathsf{Mech}(\sigma)$ of a system $\sigma$ is the set of its characteristic processes | [bunge2004] |

The first four definitions agree that a mechanism is **organized** and that it is a mechanism **for** a phenomenon. These four definitions differ on regularity: the first definition requires regular changes, whereas the minimal definition drops that requirement to cover mechanisms that act once [illari2012]. The fifth definition differs in kind, since it identifies the mechanism with processes and leaves the constituents to the [composition of the system](../systems/system-constituent-environment.md).

## Distinctions

- **A mechanism lies in the target or acts on it, and a mechanistic model represents that mechanism.** In the [frame of things and constructs](../../foundations/things-and-constructs.md), the mechanism has the relational status, since its entities and activities belong to the world while the phenomenon chosen individuates them, and the model has the representational status. A mechanistic model can describe a merely possible mechanism, in a *how-possibly* model, or the actual mechanism, in a *how-actually* model [craver2006].
- **A model is mechanistic by its form, and it explains through a mapping.** Two tests apply in sequence: ^mechanistic-model-test
    - *mechanistic form*: the model decomposes the behavior into components that engage in activities. A [dynamic](../change/dynamic.md) or a law stated over aggregate variables alone fails this test. Such a model is *phenomenological*: it reproduces a behavior from its variables. A how-possibly model can pass this test;
    - *explanatory mapping*: the components and the activities of the model map onto constituents and activities of the target, or onto parts declared admissible by the record, either through a stated map or through a [pair of type `component`](../../objects/answer/model-and-binding.md#^component-pairs) of a binding. A mechanistic model explains, in the how-actually sense, only when it passes this test [craver2006] [kaplan2011]. *Example*: a rate model with $N$ units has mechanistic form. The model explains only when its units map onto declared constituents of the target, such as neurons or populations, or when a binding pairs each unit with a population that the [admissible explanans](../../objects/task/admissible-explanans.md) admits as a part.
- **"Mechanistic" qualifies the form of a model, not its role.** A mechanistic model is any model, in the representational sense, that passes the test of mechanistic form. The description of a target is a mechanistic model if its constituents produce the phenomenon through their activities and their organization, and a model system is one if its components do. The explanatory mapping is satisfied by construction for the description of a target, whose components are its declared constituents, so the mapping decides only for a model system. The [roles and forms of a model](../representations/model.md#^target-description-is-a-model) separate the two classifications.
- **A mechanism produces its phenomenon or constitutes it.** The two relations are the causal-mechanistic and the constitutive values of the [requested relation](../../objects/task/requested-relation.md), and the [mechanistic answer](../../objects/answer/mechanism.md#^production-constitution) states the formalism of each. In a constitution, the mechanism lies in the target. In a production, it also includes external entities, outside the target system, which act on the target.
- **Four terms share the root "mechanism" and name four objects.** A mechanism lies in the target or acts on it. A mechanistic model is a representation of mechanistic form. A [mechanistic answer](../../objects/answer/mechanism.md) is an answer to a question whose requested relation is causal-mechanistic or constitutive, and it rests on a mechanistic model. A [mechanistic activity](../change/mechanistic-activity.md) is one producer of change within a mechanism.
- **A mechanistic model keeps the components relevant to its phenomenon.** The model omits the parts of the microstructure irrelevant to the phenomenon. An exhaustive description, by contrast, can leave implicit the organization relevant to the phenomenon. *Example*: a full connectivity matrix describes every synapse of a network, whereas one behavior may depend only on a feedback cycle, a modular partition or a bottleneck of that matrix.
- **An activity and a mechanism differ in scope.** The criterion is stated in the [vocabulary of activity](../change/mechanistic-activity.md): one activity produces a change, and a mechanism produces a phenomenon through the organization of several activities.

## Relations to the method

- **The notation of the method maps a mechanism onto the elements of a model.** The [notation of the method](../notation/notation.md) maps the components of a mechanism onto the constituents $C$ of the [model](../representations/model.md#^model-elements), and its organization onto $O$. Each law of $L$ represents one activity $a_j$ of the mechanism, so the activity and the law that represents it remain two objects. A mechanistic answer rests on such a model.
- **The explanatory mapping reads the declarations of the constituents of the model.** A component fails the [explanatory mapping](#^mechanistic-model-test) when its map, declared under the [perspective of the model](../../objects/answer/model-and-binding.md#^perspective), reaches neither a declared constituent nor an admissible part of the target. A unit of the model alone states no map, so it passes only through a [pair of type `component`](../../objects/answer/model-and-binding.md#^component-pairs).
- **The modal strength decides whether a how-possibly model suffices.** When the [modal strength](../../objects/task/modal-strength.md) of the question requests an actual explanation, the model on which the answer rests must pass the explanatory mapping for its activities as well as for its components. Otherwise, the mechanistic form suffices.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bechtel2005] ◐ [Bechtel & Abrahamsen, "Explanation: a mechanist alternative", *Studies in History and Philosophy of Biological and Biomedical Sciences* 36(2), 421–441, 2005](https://doi.org/10.1016/j.shpsc.2005.03.010)
- [bunge2004] ◐ [Bunge, "How does it work? The search for explanatory mechanisms", *Philosophy of the Social Sciences* 34(2), 182–210, 2004](https://doi.org/10.1177/0048393103262550)
- [craver2006] ◐ [Craver, "When mechanistic models explain", *Synthese* 153(3), 355–376, 2006](https://doi.org/10.1007/s11229-006-9097-x); how-possibly and how-actually models, and mechanism sketches, checked through the abstract
- [glennan2002] ◐ [Glennan, "Rethinking mechanistic explanation", *Philosophy of Science* 69(S3), S342–S353, 2002](https://doi.org/10.1086/341857); the definition is paraphrased, and its wording was checked through its quotation by Tabery
- [illari2012] ◐ [Illari & Williamson, "What is a mechanism? Thinking about mechanisms across the sciences", *European Journal for Philosophy of Science* 2(1), 119–135, 2012](https://doi.org/10.1007/s13194-011-0038-2); p. 120, checked through secondary quotations
- [kaplan2011] ◐ [Kaplan & Craver, "The explanatory force of dynamical and mathematical models in neuroscience: a mechanistic perspective", *Philosophy of Science* 78(4), 601–627, 2011](https://doi.org/10.1086/661755); the model-to-mechanism-mapping requirement, checked through the abstract
- [machamer2000] ◐ [Machamer, Darden & Craver, "Thinking about mechanisms", *Philosophy of Science* 67(1), 1–25, 2000](https://doi.org/10.1086/392759); p. 3
