---
tags:
  - definition
  - wip
index: "[Bearers and systems](docs/epistemology/definitions/systems/_index.md)"
aliases:
  - Property, attribute, predicate and relation
  - Property
  - Attribute
  - Predicate
  - Relation
---
# Property, attribute, predicate and relation

> [!QUESTION] Goal: when a record describes a feature of a bearer, does it name a feature of the world, a concept of it, or an expression?

The four terms describe the features of a bearer and the ways in which bearers stand to one another. Property, attribute and predicate differ in the layer holding them:

- a property belongs to the bearer;
- an attribute is a concept that represents the property;
- a predicate is an expression of a language.

A relation is the counterpart of a property for several bearers, and it has the same three layers.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Property | realist ontology | a feature possessed by a thing whether or not anyone represents it; *intrinsic* when the thing has it alone, *relational* when it holds of the thing together with others | [bunge1977] |
| Property | model theory | a unary relation: a subset of the domain $\mathcal{U}$ of a structure | [hodges1993] |
| Attribute | realist ontology | a construct that represents a property | [bunge1977] |
| Attribute | ordinary usage, data science | a synonym of property, such as a column or a feature of a data set | — |
| Predicate | logic | an expression with $n$ places that yields a sentence once the places are filled; interpreted in a structure as a subset of $\mathcal{U}^n$ | [frege1891]; [hodges1993] |
| Predicate | set-theoretical axiomatization | a predicate defined in set theory whose satisfiers are the models of a theory: axiomatizing a theory amounts to defining such a predicate | [suppes1957]; [suppes2002] |
| Relation | logic, model theory | the extension $\rho\subseteq\mathcal{U}^n$ of a predicate with $n$ places | [hodges1993] |

The pairs of terms are synonyms only in some communities:

- *property and attribute* coincide in ordinary and data-science usage, whereas realist ontology keeps them apart [bunge1977];
- *attribute and predicate* coincide in realist ontology [bunge1977], whereas logic separates an expression from its content [frege1892];
- *property and relation* coincide in model theory, where a property is a relation with one place [hodges1993].

## Distinctions

- **Property, attribute and predicate are separated by two substitutions.** Translating a predicate into another language changes the predicate and keeps the attribute expressed by the predicate. Changing the unit of an attribute changes the attribute and keeps the property. *Example*: temperature in degrees Celsius and in kelvin are two attributes that represent one property. ^substitution-test
- **The correspondence from predicates to properties is many-to-one and partial.** One property admits several attributes, as the [substitution test](#^substitution-test) shows. Moreover, some predicates represent no property: "grue" applies to things examined before a given time and found green, and to other things if they are blue [goodman1955]. Such a predicate is well formed, but no generalization stated with it is projectible.
- **A relation need not be causal.** "Taller than", "adjacent to" and "has the same value as" are relations, yet none of them transmits a change. The criterion separating a relation from an interaction is stated in the [vocabulary of interaction](../change/interaction-and-cause.md).
- **A predicate has no truth value.** A predicate becomes true or false only once its places are filled and the result is asserted. A predicate is separated from a claim and from a law statement in the [vocabulary of claims](../representations/claim-and-hypothesis.md).

## Consequences for a record

- **A declared quantity carries all three layers.** Its reading names the property in words. Its symbol, its signature and its value set make the attribute a [variable](../quantities/variable-value-observable.md). The expressions of the record using the symbol are predicates of the expression language.
- **A well-formed declaration does not guarantee that a property is represented.** The checks of a record resolve symbols and value sets, so a quantity in the manner of "grue" passes them. One test of the method bears on this question: the [admissibility of an aggregate](../../target-system.md#^aggregate-admissibility) rejects an aggregate whose interventions have ambiguous effects.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0); ch. 2, "Form", opens with the section "Property and Attribute"
- [frege1891] ◐ [Frege, *Function und Begriff*, Hermann Pohle, Jena, 1891](https://plato.stanford.edu/entries/frege/)
- [frege1892] ◐ [Frege, "Ueber Begriff und Gegenstand", *Vierteljahrsschrift für wissenschaftliche Philosophie* 16(2), 192–205, 1892](https://commons.wikimedia.org/wiki/File:Gottlob_Frege,_Ueber_Begriff_und_Gegenstand,_1892.pdf)
- [goodman1955] ◐ [Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955](https://plato.stanford.edu/entries/goodman/); first edition Athlone Press, London, 1954; "grue" in ch. III, §4
- [hodges1993] ◐ [Hodges, *Model Theory*, Cambridge University Press, 1993](https://doi.org/10.1017/CBO9780511551574)
- [suppes1957] ◐ [Suppes, *Introduction to Logic*, Van Nostrand, 1957](https://archive.org/details/introductiontolo0000supp); ch. 12, "Set-Theoretical Foundations of the Axiomatic Method", §12.2
- [suppes2002] ◐ [Suppes, *Representation and Invariance of Scientific Structures*, CSLI Publications, 2002](https://web.stanford.edu/group/cslipublications/cslipublications/site/1575863332.shtml)
