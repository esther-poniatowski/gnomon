---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Capacity and disposition
  - Capacity
  - Disposition
tags: []
source:
---
# Capacity and disposition

> [!QUESTION] Goal: what does a record claim when it ascribes a capacity to a system, and how does a capacity differ from a function, an activity and an occurrence?

A **disposition** is a property held by a thing whether or not the property is manifested, such as fragility or solubility. A disposition is ascribed through a conditional: if a stimulus condition obtained, the thing would show a manifestation [choi2018]. A **capacity** is a disposition of a system to produce outputs of a class when it receives inputs of a class [cummins1975] [cummins1983]. A record states a capacity as such a conditional, together with a criterion of performance.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Disposition | metaphysics | a property ascribed through a conditional, from a stimulus condition to a manifestation | [choi2018]; [mumford1998] |
| Capacity | philosophy of psychology | a disposition of a system to produce outputs of a class given inputs of a class; capacities are the primary explananda of psychology, and functional analysis explains them | [cummins1975]; [cummins1983] |
| Capacity of a linear classifier | learning theory | the number of points in general position, $2d$ in $d$ dimensions, at which a hyperplane through the origin separates exactly half of their labelings | [cover1965] |

The simple conditional analysis fails on finks and masks [choi2018]. A fink removes the disposition when the stimulus occurs, and a mask blocks the manifestation. In both cases, the thing has the disposition while the conditional is false. An ascription can still entail a conditional restricted to ideal conditions, without being analysed by that conditional [mumford1998]. Therefore, a record states the conditional as the test of the capacity, and leaves open the analysis of the disposition.

## Distinctions

- **A capacity belongs to a system, whereas a function relates a component to a system.** A capacity is fixed by its classes of inputs and outputs and by its criterion. A [function](function.md) of a component, in the causal-role sense, is the contribution of that component to a capacity of the containing system [cummins1975]. Therefore, ascribing a causal-role function presupposes a capacity.
- **A capacity is held, whereas an activity occurs.** A system has a capacity whether or not the capacity is exercised. One exercise of a capacity is an occurrence, a [process or an event](process-event-history.md), produced by [activities](activity.md).
- **The phenomenon category *capacity* selects a capacity as explanandum.** A phenomenon of that category has no occurrence class, so its field `occurrence` takes `not-applicable`. One observed exercise of the capacity is a phenomenon of category *particular-occurrence*.

## Consequences for a record

- **A capacity is recorded with its conditional and its criterion.** The [phenomenon](../phenomenon.md) of category *capacity* states the class of inputs, the class of outputs and the criterion of performance in its manifestations. *Example*: for every labeling of the mixture classes in a stated family, a linear readout separates the encoded mixtures. The criterion is linear separability. The count of separable labelings bounds this criterion. For $n$ encoded points in general position in $d$ dimensions, a hyperplane through the origin separates every labeling only when $n\leq d$, and exactly half of the labelings when $n=2d$ [cover1965].
- **A capacity can be the explanandum of a question whose explanans is a representation geometry.** The performance of a readout is a capacity among the [representational items of the benchmark](representation-and-encoding.md#^decision-table).

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [choi2018] ◐ [Choi & Fara, "Dispositions", *Stanford Encyclopedia of Philosophy*, substantive revision 22 June 2018](https://plato.stanford.edu/entries/dispositions/); §1.2, the simple conditional analysis, finks and masks; the names of the authors were not shown on the fetched page
- [cover1965] ◐ [Cover, "Geometrical and statistical properties of systems of linear inequalities with applications in pattern recognition", *IEEE Transactions on Electronic Computers* EC-14(3), 326–334, 1965](https://doi.org/10.1109/PGEC.1965.264137); the counting function $C(n,d)=2\sum_{k=0}^{d-1}\binom{n-1}{k}$, checked through secondary sources
- [cummins1975] ◐ [Cummins, "Functional analysis", *Journal of Philosophy* 72(20), 741–765, 1975](https://doi.org/10.2307/2024640)
- [cummins1983] ◐ [Cummins, *The Nature of Psychological Explanation*, MIT Press, 1983](https://philpapers.org/rec/CUMTNO); checked through the catalogue record and a summary of the book
- [mumford1998] ◐ [Mumford, *Dispositions*, Clarendon Press, 1998](https://philpapers.org/rec/MUMD-3); ascriptions entail conditionals without being analysed by them, checked through reviews
