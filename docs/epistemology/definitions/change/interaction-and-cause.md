---
tags:
  - definition
  - wip
index: "[Change](docs/epistemology/definitions/change/_index.md)"
aliases:
  - Interaction and cause
  - Interaction
  - Cause
  - Causal interaction
  - Statistical interaction
---
# Interaction and cause

> [!QUESTION] Goal: which sense of "interaction" does a statement use, and what notion of cause does each sense presuppose?

"Interaction" carries two senses. A **causal interaction** is a mutual action between things. Its one-way case is an **action**: a thing $x$ acts on a thing $y$ when the presence of $x$ changes the history of $y$ [bunge1977]. A **statistical interaction** is a property of a model of effects: the effect of two factors is not the sum of their separate effects. Both senses, together with mechanism and law, presuppose a notion of cause.

## Senses

| Sense | Community | Definition | Source |
| --- | --- | --- | --- |
| Action | realist ontology | a thing $x$ acts on a thing $y$ when the presence of $x$ changes the history of $y$ | [bunge1977] |
| Causal interaction | realist ontology | mutual action: $x$ acts on $y$ and $y$ acts on $x$ | [bunge1977] |
| Causal interaction | mechanistic philosophy | an interaction of parts characterized by direct, invariant, change-relating generalizations | [glennan2002] |
| Statistical interaction | statistics | non-additivity: the effect of one factor on a response depends on the level of another factor | [cox1984] |
| Cause | interventionism | a variable $U$ causes a variable $W$ when some intervention on $U$ would change $W$, other variables being held fixed appropriately | [woodward2003] |
| Cause | structural causal models | $U$ is a cause of $W$ when $U$ enters the structural equation of $W$, directly or through a chain of equations | [pearl2009] |

## Distinctions

- **An action is one-way, and an interaction is mutual.** An interaction between $x$ and $y$ holds when $x$ acts on $y$ and $y$ acts on $x$. A statement of one direction alone states an action, so a claim of interaction requires a test in each direction. ^action-interaction
- **A relation becomes an action when it changes histories.** "Taller than" and "adjacent to" hold between things without changing the history of either. The test is counterfactual: it asks whether removing $x$ changes the history of $y$. Relations in general are defined in the [vocabulary of properties](../systems/property-attribute-predicate.md).
- **Causal and statistical interaction are independent.** Neither entails the other:
    - a one-way action can produce a statistical interaction, as when a drug multiplies the effect of a dose of another drug without either drug acting on the other;
    - a mutual action can produce effects that add up, so that no statistical interaction appears between two treatments.
- **A statistical interaction is relative to a scale.** When effects multiply on the original scale, they add up on the logarithmic scale, so a transformation can remove an interaction [cox1984]. Therefore, a statement of statistical interaction is [meaningful](../quantities/scale-and-level.md) only on a stated scale.
- **An interaction is a kind of activity.** The criterion that separates the two is stated in the [vocabulary of activity](mechanistic-activity.md).

## Consequences for a record

- **A relation of an organization need not be an interaction.** The [organization](../../background.md#^organization) of a background record holds directed and joint relations. A directed relation is an action. A reciprocal pair of directed relations is a causal interaction. A relation with three or more components can encode a joint effect carried by no pair.
- **A requested relation of the causal kind presupposes the interventionist notion of cause.** The [requested relation](../../requested-relation.md) uses interventions to state causal dependence, so a claim of causal interaction in an answer must survive the corresponding intervention test.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0); ch. 5, "Change", pp. 215–275; the definitions of action and of interaction were checked through secondary sources, not at the page
- [cox1984] ◐ [Cox, "Interaction", *International Statistical Review* 52(1), 1–24, 1984](https://doi.org/10.2307/1403235)
- [glennan2002] ◐ [Glennan, "Rethinking mechanistic explanation", *Philosophy of Science* 69(S3), S342–S353, 2002](https://doi.org/10.1086/341857); the wording "direct, invariant, change-relating generalizations" was checked through its quotation by Tabery
- [pearl2009] ◐ [Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009](https://doi.org/10.1017/CBO9780511803161)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
