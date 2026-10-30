---
tags:
  - definition
  - wip
index: "[Quantities and states](docs/epistemology/vocabulary/quantities/_index.md)"
aliases:
  - Invariant and symmetry
  - Invariant
  - Symmetry
  - Invariance
---
# Invariant and symmetry

> [!QUESTION] Goal: what is preserved under which transformations, when a law, a scale or a pattern is said to be invariant?

An **invariant** is a quantity or a relation that a set of transformations preserves. A **symmetry** is a transformation that preserves a structure, such as the laws of a model or the relations of a scale. The two notions are dual: fixing a set of transformations determines the invariants, and fixing a structure determines its symmetries [suppes2002].

## Uses across the vocabulary

The criterion of invariance recurs in several notes of this folder, each time with a different set of transformations:

| Use | Transformations | Invariant | Source |
| --- | --- | --- | --- |
| [Scale type and meaningfulness](scale-and-level.md) | the admissible transformations of a scale, forming a group | the truth of a meaningful statement | [krantz1971]; [suppes1963] |
| [Law](../regularities/law.md) in the interventionist sense | interventions on the variables of the law, over some range | the truth of the law statement | [woodward2003] |
| Symmetry of a law | a group of transformations of the state space, such as translations in time | the form of the dynamic | [suppes2002] |
| [Pattern](../regularities/pattern-and-phenomenon.md) | the passage from one instance of a set to another | the feature shared by the instances | — |
| [Implementation of a computation](../change/computation.md#^implementation-map) | the map $\psi$ from physical to abstract states | the abstract dynamic, commuting with $\psi$ | — |

## Distinctions

- **Invariance under interventions differs from symmetry under a group.** A set of interventions is in general not a group, since an intervention that sets a variable has no inverse in the set. Invariance under interventions is also graded: a law can hold over a narrower or a wider range of interventions [woodward2003]. Symmetry under a group, by contrast, holds for every element of the group or fails.
- **An invariant of the record differs from an invariant of the target.** When a statement holds in one representation and fails under an admissible change of representation, the statement is an artefact of that representation. The meaningfulness criterion of scales shows this consequence [suppes1963].

## Relations to the method

- **A claim of invariance must name its set of transformations.** "The frequency is invariant" is incomplete until the claim states its set of transformations, such as the instances, the interventions on a parameter, or the admissible changes of units.
- **The scope over instances of a phenomenon states one invariance claim.** A claim quantified as *universal* over the reference class, in the [scope over instances](../../objects/subject/phenomenon.md), asserts that a feature is preserved across every member.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [krantz1971] ◐ [Krantz, Luce, Suppes & Tversky, *Foundations of Measurement*, vol. I, *Additive and Polynomial Representations*, Academic Press, 1971](https://shop.elsevier.com/books/additive-and-polynomial-representations/krantz/978-0-12-425401-5)
- [suppes1963] ◐ [Suppes & Zinnes, "Basic measurement theory", in Luce, Bush & Galanter (eds.), *Handbook of Mathematical Psychology*, vol. I, Wiley, 1–76, 1963](https://suppescorpus.stanford.edu/sites/g/files/sbiybj32751/files/media/file/basic_measurement_theory_43.pdf)
- [suppes2002] ◐ [Suppes, *Representation and Invariance of Scientific Structures*, CSLI Publications, 2002](https://web.stanford.edu/group/cslipublications/cslipublications/site/1575863332.shtml)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
