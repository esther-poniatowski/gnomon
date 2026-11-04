---
tags:
  - definition
  - wip
index: "[Quantities and states](docs/epistemology/vocabulary/quantities/_index.md)"
aliases:
  - Dimension
  - Dimension of a quantity
  - Dimensional formula
  - Dimensional analysis
---
# Dimension

> [!QUESTION] Goal: which sense of "dimension" does a statement use, and which statements does the dimension of a quantity license?

The word "dimension" has three senses, and each sense names a distinct property of a quantity. Only the first sense is the subject of dimensional analysis, and the word alone does not tell the senses apart. In machine learning, the word usually takes the second sense.

| Sense | Property named | Place where the method states it | Example |
| --- | --- | --- | --- |
| **dimension** in the sense of dimensional analysis | the change of the numerical value of a quantity when the units of the base quantities are rescaled | the dimensional formula of the quantity | a force, of dimension $M\,L\,T^{-2}$ |
| **dimensionality** | the number of components of a value, or the dimension of a space | the [value set](variable-value-observable.md) of the quantity | a velocity in $\mathbb{R}^3$ |
| **indexing** | the quantities indexing a quantity, as the arguments of its value | the signature of the quantity | a field indexed by position and time |

## Dimension function

When the units of the base quantities are rescaled, the numerical value of a quantity is multiplied by a factor. The **dimension function** of the quantity gives that factor from the factors of the base units, and it is always a power-law monomial [barenblatt1996]. The **dimensional formula** writes that monomial over the base dimensions: $M\,L\,T^{-2}$ for a force. A quantity whose formula is $1$ is a **pure number**, and no change of units alters its value.

**A change of units has the form of a ratio-scale transformation.** A change of units is a similarity $x \mapsto a x$, the form of the admissible transformations of a [ratio scale](scale-and-level.md). The dimension function fixes the factor $a$ of every quantity jointly, from the factors of the base units. Therefore, a dimensional formula ties together the similarities of all quantities, without presupposing a measurement.

**The dimension is a property of a change of units, not of a measurement.** The dimension states how values transform when the units change. Therefore, the dimension holds for the quantities of a formal model whose values carry units, whether or not the quantities are measured. Measurement enters only through the units expressing the values. The base quantities need not be physical: a problem may declare its own **base scales**. *Example*: in a learning system, the scale of the parameters and the scale of the loss are two independent base scales. Then, a learning rate carries the ratio of their powers.

## Dimensional homogeneity

A law is **dimensionally homogeneous** when two conditions hold:

- every term of a sum, and each side of an equation, has the same dimensional formula;
- the argument of an exponential, a logarithm or a trigonometric function is a pure number.

A homogeneous law keeps its truth under every change of units. Therefore, such a law is meaningful in the sense of the [scales of measurement](scale-and-level.md): its truth is constant under the admissible transformations of its values. ^dimensional-homogeneity

**A homogeneous relation reduces to fewer variables.** Consider a homogeneous relation among $n$ quantities, and let $r$ be the rank of the matrix of the exponents of their dimensional formulas. The relation can be rewritten as a relation among $n - r$ pure numbers: the Π-theorem, in its modern form [barenblatt1996]. Buckingham stated the theorem with the number of fundamental units in place of the rank [buckingham1914]. When a derivation applies the theorem, the homogeneity of its relation is the [property that makes its warrant apply](../../objects/derivation/move.md#^applies-because).

## Similarity

A pure number of a reduced relation may tend to zero or to infinity in a regime of interest. Then, two cases differ [barenblatt1996]:

- **complete similarity**: the relation tends to a finite and nonzero limit, so the pure number can be dropped in that regime;
- **incomplete similarity**: the relation has no such limit but behaves as a power of the pure number, and dimensional analysis does not fix the exponent of that power.

When the relation has neither a finite limit nor a behavior as a power, similarity fails in that pure number.

Under incomplete similarity, the exponent comes out of the derivation, not out of the dimensions. A posit of similarity states the kind of similarity assumed, as the [kinds of posit](../../objects/derivation/posit.md) distinguish.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the dimension function as a power-law monomial; the Π-theorem, in its original and its modern form; complete and incomplete similarity, as cited.
> - **Proposals:**
> 	- the three senses of "dimension", and the place where the method states each of them;
> 	- changes of unit as similarities, in the form of ratio-scale transformations, and dimensional homogeneity as an instance of meaningfulness;
> 	- base scales declared by a problem, beyond physical base quantities.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [barenblatt1996] ◐ Barenblatt, *Scaling, Self-Similarity, and Intermediate Asymptotics*, Cambridge University Press, 1996; the dimension function as a power-law monomial, the Π-theorem in its modern form, and complete and incomplete similarity, checked through [secondary sources](https://arxiv.org/pdf/2406.03896)
- [buckingham1914] ◐ [Buckingham, "On physically similar systems; illustrations of the use of dimensional equations", *Physical Review* 4(4), 345–376, 1914](https://doi.org/10.1103/PhysRev.4.345); the Π-theorem, checked through the publisher record and secondary summaries
