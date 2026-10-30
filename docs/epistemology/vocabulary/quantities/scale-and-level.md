---
tags:
  - definition
  - wip
index: "[Quantities and states](docs/epistemology/vocabulary/quantities/_index.md)"
aliases:
  - Scale and level
  - Scale
  - Level
  - Scale of measurement
  - Level of organization
  - Level of description
---
# Scale and level

> [!QUESTION] Goal: which sense of "scale" or "level" does a statement use, and which statements does each sense license?

"Scale" carries two unrelated senses: a mapping into numbers, in measurement theory, and the extent and resolution of a description. "Level" carries two related senses, applied respectively to the parts of a system and to descriptions of the system.

## Scale of measurement

A **scale** is a homomorphism $f$ from an empirical relational structure into a numerical one [krantz1971]. *Example*: the relation "at least as long as" between rods is mapped onto $\geq$ between reals, and the concatenation of rods onto addition.

The **scale type** is fixed by the group of admissible transformations: the maps $g$ such that $g\circ f$ is again a homomorphism [stevens1946] [krantz1971].

| Scale type | Admissible transformations | Statements that keep their truth | Example |
| --- | --- | --- | --- |
| Nominal | bijections | identity of values | labels of cell types |
| Ordinal | strictly increasing maps | order of values | ranks of preference |
| Interval | positive affine maps $x\mapsto ax+b$, $a>0$ | order, and ratios of differences | temperature in degrees Celsius |
| Ratio | similarities $x\mapsto ax$, $a>0$ | order, and ratios of values | length; firing rate |

A statement is **meaningful** when its truth survives every admissible transformation. The definition reads: "A numerical statement is meaningful if and only if its truth (or falsity) is constant under admissible scale transformations of any of its numerical assignments" [suppes1963]. *Example*: "the rate doubled" is meaningful on a ratio scale, whereas "the temperature doubled" is not meaningful in degrees Celsius.

## Scale of description

In its second sense, the **scale** of a description is its extent and its resolution along one dimension: space, time, or the hierarchy of organization. *Example*: a description of cortex at the scale of millimetres and seconds resolves columns and population rhythms, and no single spike. This sense has no relation to the homomorphism of the measurement sense.

## Level

| Sense | Ordering relation | Example | Source |
| --- | --- | --- | --- |
| Level of organization | part–whole: an entity at a lower level is a component of a mechanism at the higher level | channel, neuron, circuit | [craver2007] |
| Level of description | abstraction over one system: each level describes the same system in another vocabulary | computational, algorithmic and implementational levels of a visual process | [marr1982] |

## Distinctions

- **A variable and its scale are separated by meaningfulness.** The value set of a variable fixes the values that exist. The scale type fixes the meaningful statements about those values. Two variables with the same value set can carry different scale types. *Example*: integer codes of cell types and counts of spikes both take values in the natural numbers, yet only the counts form a ratio scale.
- **The two senses of scale are told apart by their object.** A scale in the measurement sense maps a structure onto numbers, so it has a type and admissible transformations. A scale in the descriptive sense is a range and a grain, so it has neither.
- **The two senses of level are told apart by the item that changes when the level is lowered.** Lowering a level of organization replaces the system by its parts. Lowering a level of description keeps the system and replaces the vocabulary. *Example*: the implementational level describes the visual system itself in physical terms [marr1982], whereas the level of ion channels describes components of a neuron [craver2007].

## Relations to the method

- When a claim holds on one scale type and fails under the admissible transformations of that type, the claim is an artefact of the representation.
- **The descriptive scale of a phenomenon sets the default grain of its explanans.** The [proportionality requirement](../../objects/subject/phenomenon.md#^resolution-proportionality) uses scale in the descriptive sense.
- **The bound on the explanans uses levels of organization on one of its two axes.** The compositional axis of the [bound on the explanans](../../objects/task/admissible-explanans.md) $\lambda$ restricts the parts that may appear in an answer, so it uses level in the sense of organization. The bound itself is not a level, since its second axis, substrate dependence, orders no parts.

The fields that bear on the scale of a quantity are documented in the [target-system record](../../../specification/target-system.md) and the [phenomenon record](../../../specification/phenomenon.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Clarendon Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [krantz1971] ◐ [Krantz, Luce, Suppes & Tversky, *Foundations of Measurement*, vol. I, *Additive and Polynomial Representations*, Academic Press, 1971](https://shop.elsevier.com/books/additive-and-polynomial-representations/krantz/978-0-12-425401-5)
- [marr1982] ◐ [Marr, *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*, W. H. Freeman, 1982](https://discovery.nypl.org/research/research-catalog/bib/b10771196)
- [stevens1946] ◐ [Stevens, "On the theory of scales of measurement", *Science* 103(2684), 677–680, 1946](https://doi.org/10.1126/science.103.2684.677)
- [suppes1963] ◐ [Suppes & Zinnes, "Basic measurement theory", in Luce, Bush & Galanter (eds.), *Handbook of Mathematical Psychology*, vol. I, Wiley, 1–76, 1963](https://suppescorpus.stanford.edu/sites/g/files/sbiybj32751/files/media/file/basic_measurement_theory_43.pdf); §5.1, Definition 33, p. 66
