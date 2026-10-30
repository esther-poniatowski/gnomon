---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/definitions/representations/_index.md)"
aliases:
  - Representation and encoding
  - Encoding
  - Readout
  - Representation geometry
---
# Representation and encoding

> [!QUESTION] Goal: what does a statement about the representation of a network, or about its geometry, fix, and in which field of a record does each representational item belong?

An **encoding** is a map $e:\mathcal{U}\to\mathcal{X}$ from an input space $\mathcal{U}$ to the state space $\mathcal{X}$ of a system. *Example*: the map $u\mapsto x^*(u)$ sends each input $u$ to the fixed point $x^*(u)$ of $\dot x=-x+\phi(Wx+u)$. A **readout** is a map $r:\mathcal{X}\to\mathcal{Y}$ from the state space to an output space. A **representation** is an encoding together with the readouts that use it [decharms2000] [shea2018]. The **representation geometry** is a property of the encoding map alone.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Encoding | neuroscience | the way in which information about inputs is carried by the activity of neurons, in their firing rates or in the timing of their spikes | [decharms2000] |
| Representation | neuroscience | encoded information, considered together with the way in which it is used to produce behavior | [decharms2000] |
| Representation | philosophy of cognitive science | a vehicle whose content is fixed by exploitable relations, such as correlation or structural correspondence, together with the functions of the system that uses the vehicle | [shea2018] |
| Representational geometry | cognitive neuroscience | the dissimilarities among the activity patterns evoked by a set of inputs | [kriegeskorte2013] |
| Neural population geometry | computational neuroscience | the shape of the manifolds of population responses, a descriptor shared by biological and artificial networks | [chung2021] |

The geometry of an encoding is described by its kernel
$$K(u,u')=\langle e(u),e(u')\rangle,$$
which fixes the Euclidean distances between the images of two inputs, $\|e(u)-e(u')\|^2=K(u,u)+K(u',u')-2K(u,u')$. The kernel is invariant under every rotation of $\mathcal{X}$, since a rotation preserves inner products. Therefore, the geometry does not depend on the orthonormal basis chosen to write the states.

## Distinctions

- **A representation geometry is not a structure.** The [structure of a system](../systems/system-constituent-environment.md) is a set of relations among its constituents. The kernel, by contrast, relates pairs of *inputs* through their images. *Example*: two networks with different connectivities can share one kernel.
- **A representation geometry is not a configuration.** A [configuration](../quantities/state-and-configuration.md) is the arrangement of the constituents at one point of the course. The geometry ranges over the whole input space, and each image $e(u)$ belongs to its own course, such as the relaxation that reaches the fixed point under the input $u$.
- **A representation geometry is not one state.** One state $e(u)$ is one point of $\mathcal{X}$, whereas the geometry is a relation among all the points $e(u)$.
- **An encoding becomes a representation once a readout uses it.** One encoding supports several readouts, so a claim about the content represented by a network names its readout. *Example*: the mixtures of two inputs are represented for a linear readout only when the classes of mixtures are linearly separable in the state space $\mathcal{X}$. The ability of a linear readout to sort the mixtures is a [capacity](../regularities/capacity-and-disposition.md) of the network, and linear separability is the criterion of that capacity.

## Consequences for a record

- **One geometry can be the explanandum of one question and the explanans of another.** The example of the [linked questions](../../inquiry/question.md#^linked-questions) states the link between the two questions.
- **Each representational item of the benchmark takes one place in the records.** The benchmark targets networks in their most abstract form, a [class of possible systems](model.md), so no item below is a claim about cortex. ^decision-table

| Item | `phenomenon.category` | `explanans.factor` | Law `role` | Reading |
| --- | --- | --- | --- | --- |
| Representation geometry, described by Q1 | `structural-property` | — | — | the explanandum of Q1 |
| Representation geometry, invoked by Q2 | — | `structural-property` | — | a factor of the explanans of Q2, linked to Q1 by `explanans-from` |
| Response to mixtures of inputs | `regularity`, with a manifestation of form `dependence` | — | — | the dependence of the response on the composition of the mixture |
| Divisive normalization formula | — | — | `input-output`, with warrant `fitted` or `posited` | a law of an answer or of a background record; as a [canonical computation](../change/computation.md), it fixes no mechanism |
| Performance of a readout | `capacity` | — | — | a [disposition](../regularities/capacity-and-disposition.md) of the network to sort inputs for a readout |
| Relaxation to the fixed point | — | — | `evolution` | an occurrence of the [process class](../change/process-event-history.md#^process), generated by a law of role `evolution`; it realizes the input–output map |

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [chung2021] ◐ [Chung & Abbott, "Neural population geometry: an approach for understanding biological and artificial neural networks", *Current Opinion in Neurobiology* 70, 137–144, 2021](https://doi.org/10.1016/j.conb.2021.10.010); checked through the abstract
- [decharms2000] ◐ [deCharms & Zador, "Neural representation and the cortical code", *Annual Review of Neuroscience* 23, 613–647, 2000](https://doi.org/10.1146/annurev.neuro.23.1.613); the abstract defines representation through the information carried by firing rates and temporal patterns, with emphasis on its use in behavior; the body was not read
- [kriegeskorte2013] ◐ [Kriegeskorte & Kievit, "Representational geometry: integrating cognition, computation, and the brain", *Trends in Cognitive Sciences* 17(8), 401–412, 2013](https://doi.org/10.1016/j.tics.2013.06.007); dissimilarities as distances in the representational space, checked through passages of the full text; the invariance under rotations is not stated there, and this note derives it from the kernel
- [shea2018] ◐ [Shea, *Representation in Cognitive Science*, Oxford University Press, 2018](https://academic.oup.com/book/26604); content fixed by exploitable relations and task functions, checked through reviews and the publisher page
