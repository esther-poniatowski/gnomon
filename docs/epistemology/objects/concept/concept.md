---
tags:
  - theory
index: "[Concept](docs/epistemology/objects/concept/_index.md)"
aliases:
  - Concept
  - Concept and designation
  - Concept of a project
---
# Concept

> [!QUESTION] Goal: what is a concept, how does an inquiry produce one, and what keeps it apart from the names and symbols that express it?

A **concept** is a unit of meaning that a project uses to describe its objects, such as "disentangled representation" or "fixed point". A concept is an epistemic object: its meaning fixes the objects that the questions and the claims of an inquiry are about. A concept is produced by explication, which replaces a term in use by an exact one, or by the other [conceptual activities](../../processes/activities/conceptual-activities.md) that output a concept: an explicit definition, or the revision of an existing concept. A concept is defined once, in the project that introduces it, and the other projects that use it reference that definition. Its symbols, by contrast, follow the conventions of a [notation](notation.md), and its names vary with the audience of a text, which a glossary of `ekthesis` holds. Therefore, the meaning, the symbols and the names are held in separate places. ^concept

## Grounds of the separation

Two traditions separate a concept from its names:

- **The semiotic triangle.** A symbol relates to its referent only through a thought or reference, which the symbol expresses [ogden1923]. A name and the concept that it expresses are therefore two objects, and the same concept can be expressed by several names.
- **Concept-oriented terminology.** Terminology work starts from the concept and attaches to it one or several designations: terms, symbols and appellations [iso704]. A concept is fixed by its characteristics and its definition, and a designation is chosen for a concept within a subject field.

The decision on [concepts, glossaries and notations](../../../adr/concepts-glossaries-notations.md) applies this separation to the records of a project, for two reasons stated as its constraints. First, a name differing by audience would otherwise duplicate the meaning. Second, two projects that hold one concept would otherwise define it twice, against the [rule of one source](../../../adr/one-source-per-unit.md#^one-source).

## The concept

A concept is stated by a gloss, a kind, at most one broader concept, the note that sources it, and its confusions with neighboring concepts, each with the distinction that separates them, as the decision on concepts lists. A concept of another project is referenced, never copied.

- **A concept differs from a term of the theory.** The [vocabulary](../../vocabulary/_index.md) fixes the senses of the terms in which the theory of `gnomon` is written, such as "model" or "law". A concept in the sense of this note belongs to the research: its record is a research unit of the project that defines it, and other projects reference that unit.
- **A concept in use before its definition is an explicandum.** A problem may use a term without a definition, with a pointer to the use that fixes its sense, as the [explicanda of a problem](../problem/epistemic-problem.md#^problem-triple) do. An explication replaces the explicandum by an exact explicatum, which is judged by the adequacy of an explication: similarity to the explicandum, exactness, fruitfulness and simplicity [carnap1950_logical].
- **A concept differs from a declared quantity.** A target specification declares a quantity with a symbol and a value set. The quantity can instantiate a concept, and the symbol of the quantity then denotes the quantity, not the concept. The [adequacy of a declaration](../../foundations/things-and-constructs.md#^declaration-adequacy) applies to the quantity.
- **A concept is assessed for its adequacy, never accepted.** A concept makes no claim, so it has no truth value and never enters the [accepted knowledge](../../foundations/inquiry-and-state.md#^state). Its epistemic role is that of a definition, which licenses substitution, as the [inventory of epistemic objects](../status/epistemic-objects.md#^unit-roles) places it. A problem that demands a concept is solved by the [claim of its adequacy](../problem/epistemic-problem.md#^solution-claim).

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the semiotic triangle, concept-oriented terminology and the requirements of an explication, as cited.
> - **Proposals:**
> 	- the separation of the concept from its names and symbols into separate places, as the decision on concepts adopts it;
> 	- one definition of a concept, referenced by every project that uses it.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum, explicatum and the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [iso704] ◐ International Organization for Standardization, *ISO 704:2022 Terminology work — Principles and methods*, 2022; the links between objects, concepts, definitions and designations, checked through the catalogue entry of the standard
- [ogden1923] ◐ Ogden & Richards, *The Meaning of Meaning: A Study of the Influence of Language upon Thought and of the Science of Symbolism*, Kegan Paul, Trench, Trubner & Co., 1923; the triangle of symbol, thought or reference, and referent, pp. 10–12 of the 8th edition (1946), checked through a quotation
