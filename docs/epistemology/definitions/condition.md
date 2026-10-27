---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Condition
  - Initial condition
  - Boundary condition
  - Ceteris paribus clause
tags: []
source:
---
# Condition

> [!QUESTION] Goal: which sense of "condition" does a statement use, and where does each condition of an inquiry belong in a record?

"**Condition**" carries six senses across logic, physics and the philosophy of science, and none of them is primary for a record. A record classifies the conditions of an inquiry by their **place** alone, as the [places of a condition](#^condition-places) list them.

## Senses

| Sense | Community | Definition | Source |
| --- | --- | --- | --- |
| Antecedent condition | deductive-nomological explanation | a particular fact $\kappa_1,\ldots,\kappa_m$ that, together with laws, entails the explanandum | [hempel1948] |
| Initial and boundary conditions | dynamical systems, physics | the state $x_0$ at the initial time, and the values imposed on the boundary of the domain | — |
| Ceteris paribus clause | philosophy of laws | a clause that restricts a law to circumstances in which other factors are absent or constant | [cartwright1983] |
| Set-up and termination conditions | mechanistic philosophy | the states at which the description of a mechanism starts and ends | [machamer2000] |
| Background, causal field | causation | the circumstances held fixed by a causal question | [mackie1974] |
| Necessary, sufficient, INUS condition | logic, causation | a necessary or a sufficient condition; an INUS condition is an insufficient but non-redundant part of an unnecessary but sufficient condition | [mackie1965] |

The first five senses name a constraint fixed from outside the derivation: a fact entering the derivation, a starting state, or a restriction on circumstances. The sixth sense is logical: it names a relation between two states of affairs, and a condition in that sense can be derived.

## Distinctions

- **A value fixed by a condition takes its role from the role test of a quantity.** The [role test](variable-value-observable.md#^role-test) places each value relative to the course of a phenomenon. *Example*: the initial state $x_0$ is constant along the course and varies across the instances, so a phenomenon names it as an index of an observable or as a source of variation. The question restricts its admitted values in $D$. The state $x(t)$ at a later time varies along the course, and the system determines it.
- **One quantity can change role between descriptions.** The temperature of a heat bath is a parameter of the system surrounded by the bath, and a boundary condition of the bath itself.
- **The logical sense of condition is told apart from the other five by derivability.** The other five senses name constraints admitted without derivation. A necessary or sufficient condition is a claim about a dependence, and an inquiry can establish such a claim.

## Consequences for a record

The conditions of an inquiry fall in four places of a record, each owned by another note: ^condition-places

| Condition | Place in the record |
| --- | --- |
| A restriction imposed by the question on admitted values, including clamped, initial or stationary states | the [domain of conditions](../domain.md) $D$ |
| A precipitating, inhibiting or modulating condition of the behavior, or a nonstandard circumstance | the [conditions of the phenomenon](../phenomenon.md#^conditions-byproducts) |
| A constraint on the states that may hold together, including at the start and at the boundary | a law with the role *state-constraint*, in a [background record](../background.md) or in an answer |
| An assumption introduced by the analysis, such as a mean-field limit | not a condition: the [idealizations of the answer](../answer-form.md#^idealizations), unless the question is asked of the limit system itself, as the [rule for limits](idealization-and-abstraction.md#^limit-rule) decides |

- **A restriction of the domain narrows the value set of a declared quantity.** The target declares the quantity once, for every role that the [role test](variable-value-observable.md#^role-test) gives it in a phenomenon, and the question narrows its value set in $D$.
- **A condition of the phenomenon belongs to the explanandum.** Its relation to the behavior belongs to the characterization of the phenomenon, so such a condition is not an input of the derivation.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [cartwright1983] ◐ [Cartwright, *How the Laws of Physics Lie*, Clarendon Press, 1983](https://doi.org/10.1093/0198247044.001.0001)
- [hempel1948] ◐ [Hempel & Oppenheim, "Studies in the logic of explanation", *Philosophy of Science* 15(2), 135–175, 1948](https://doi.org/10.1086/286983)
- [machamer2000] ◐ [Machamer, Darden & Craver, "Thinking about mechanisms", *Philosophy of Science* 67(1), 1–25, 2000](https://doi.org/10.1086/392759)
- [mackie1965] ◐ [Mackie, "Causes and conditions", *American Philosophical Quarterly* 2(4), 245–264, 1965](https://www.jstor.org/stable/20009173)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
