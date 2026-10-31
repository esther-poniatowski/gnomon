---
tags:
  - theory
index: "[Concept](docs/epistemology/objects/concept/_index.md)"
aliases:
  - Notation of a project
---
# Notation of a project

> [!QUESTION] Goal: what does the notation of a project hold, and why does it serve research rather than the presentation of research?

A **symbol** is a written form that designates a quantity or a [concept](concept.md#^concept) in formulas. A concept keeps one meaning, whereas the symbols that designate it may follow different conventions. The **notation** of a project composes its symbols. The notation serves research, since a researcher formulates and manipulates concepts in a notation and writes derivations with its conventions, as the [decision on the scope of gnomon](../../../adr/research-scope.md) states. The names that a glossary gives a concept for an audience serve readers, and they are specified in `ekthesis`. ^symbol

## The notation

A **notation** composes the symbols of a project from declared parts: bases, each with its meaning; modifiers, such as a label, a superscript or an accent, each with its meaning and its admitted positions; index sets, which bind the letters that range over them; and conventions of typography. The meaning of a compound symbol is composed from the meanings of its parts. A compound whose meaning does not follow from its parts is declared explicitly. ^notation

- **Composition follows the principle of compositionality.** The meaning of a complex expression is determined by the meanings of its parts and by the way in which they are combined [szabo2020]. A compound declared explicitly is the counterpart of an idiom, whose meaning the rule of composition does not yield.
- **A symbol of a declared quantity has one declaration.** Once a record of the inquiry declares a quantity, the notation refers to that record for its symbol and does not restate it, as the decision on [terminology, audience and project specifications](../../../adr/terminology-audience-project-specifications.md) states.

## Distinctions

- **A notation designates meanings without defining them.** The meaning of a base or of a modifier is the concept or the quantity that it designates, which a concept record or another record of the inquiry defines. The notation is authored, so it is not a generated view of the concepts.
- **A symbol keeps its identifier when an artifact renames it.** An artifact may print a symbol in the convention of its venue, and the renaming changes the printed form only, so every check of the records still resolves the symbol, as the [decision on the scope of gnomon](../../../adr/research-scope.md) states.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the principle of compositionality, as cited.
> - **Proposals:** the notation as a record of one project, apart from the concept, and composed from bases, modifiers and index sets.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [szabo2020] ◐ [Szabó, "Compositionality", *Stanford Encyclopedia of Philosophy*, substantive revision 17 August 2020](https://plato.stanford.edu/archives/fall2022/entries/compositionality/); principle (C), §1
