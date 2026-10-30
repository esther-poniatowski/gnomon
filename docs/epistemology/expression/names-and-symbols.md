---
tags:
  - theory
index: "[Expression](docs/epistemology/expression/_index.md)"
aliases:
  - Concepts and names
  - Concept and designation
  - Glossary (theory)
  - Notation of a project
---
# Concepts and names

> [!QUESTION] Goal: what keeps a concept apart from the names and symbols that express it, and what do a glossary and a notation hold?

A **concept** is a unit of meaning that a project uses to describe its objects, such as "disentangled representation" or "fixed point". A **name** is a word or a phrase that designates a concept, and a **symbol** is a written form that designates a quantity or a concept in formulas. A concept keeps one meaning across projects and audiences, whereas its names and symbols vary with the audience and the context of a text. Therefore, the meaning and the names are held in separate places. ^concept

## Grounds of the separation

Two traditions separate a concept from its names:

- **The semiotic triangle.** A symbol relates to its referent only through a thought or reference, which the symbol expresses [ogden1923]. A name and the concept that it expresses are therefore two objects, and the same concept can be expressed by several names.
- **Concept-oriented terminology.** Terminology work starts from the concept and attaches to it one or several designations: terms, symbols and appellations [iso704]. A concept is fixed by its characteristics and its definition, and a designation is chosen for a concept within a subject field.

The decision on [concepts, glossaries and notations](../../adr/concepts-glossaries-notations.md) applies this separation to the records of a project, for two reasons stated as its constraints. First, a name differing by audience would otherwise duplicate the meaning. Second, two projects that hold one concept would otherwise define it twice, against the [rule of one source](../../adr/one-source-per-unit.md#^one-source).

## The concept

A concept is stated by a gloss, a kind, at most one broader concept, the note that sources it, and its confusions with neighboring concepts, each with the distinction that separates them, as the decision on concepts lists. A concept of another project is referenced, never copied.

- **A concept differs from a term of the theory.** The [vocabulary](../vocabulary/_index.md) fixes the senses of the terms in which the theory of `gnomon` is written, such as "model" or "law". A concept in the sense of this note belongs to the research of a project, and its record is one of the research units of that project.
- **A concept in use before its definition is an explicandum.** A problem may use a term without a definition, with a pointer to the use that fixes its sense, as the [explicanda of a problem](../objects/problem/epistemic-problem.md#^problem-triple) do. An explication replaces the explicandum by an exact explicatum, which is judged by the adequacy of an explication: similarity to the explicandum, exactness, fruitfulness and simplicity [carnap1950_logical].
- **A concept differs from a declared quantity.** A target specification declares a quantity with a symbol and a value set. The quantity can instantiate a concept, and the symbol of the quantity then denotes the quantity, not the concept. The [adequacy of a declaration](../foundations/things-and-constructs.md#^declaration-adequacy) applies to the quantity.

## Names: the glossary

A **glossary** holds the names of the concepts of one project: for each concept, its label, its variants, its alternative forms with the contexts in which each is admitted, and its names in other frameworks. A form forbidden for some audiences keeps its replacement, its reason and the audiences concerned. A glossary holds no meaning: each entry designates one concept and points to it. ^glossary

The Simple Knowledge Organization System separates a concept from its lexical labels in the same way, with a preferred label and alternative labels, and relates two concepts by a broader concept [skos2009]. The glossary differs on one point. The lexical labels of that system belong to the concept itself, whereas a glossary belongs to one project, so two projects can name one concept differently without changing it.

**Two names designate one concept only when they carry the same meaning.** Two names of one referent can differ in sense, as "the morning star" and "the evening star" do [frege1892a]. Under a proposal of this method, a glossary admits two forms for one concept only when they carry the same meaning in the contexts listed. A name that carries a different meaning designates a different concept, which receives its own record, with a confusion entry that states the distinction.

## Symbols: the notation

A **notation** composes the symbols of a project from declared parts: bases, each with its meaning; modifiers, such as a label, a superscript or an accent, each with its meaning and its admitted positions; index sets, which bind the letters that range over them; and conventions of typography. The meaning of a compound symbol is composed from the meanings of its parts. A compound whose meaning does not follow from its parts is declared explicitly. ^notation

- **Composition follows the principle of compositionality.** The meaning of a complex expression is determined by the meanings of its parts and by the way in which they are combined [szabo2020]. A compound declared explicitly is the counterpart of an idiom, whose meaning the rule of composition does not yield.
- **A symbol of a declared quantity has one declaration.** Once a record of the inquiry declares a quantity, the notation refers to that record for its symbol and does not restate it, as the decision on [terminology, audience and project specifications](../../adr/terminology-audience-project-specifications.md) states.

## Distinctions

- **A glossary and a notation hold forms, and a text in those forms is a view.** The glossary and the notation are authored, so neither is a generated view of the concepts. Each maps concepts, or quantities, to the forms that express them in one project. A text written in those forms presents the concepts without changing them, as an [exposition](exposition.md) does.
- **A forbidden form is a fact about a name, not about a meaning.** A form may be forbidden for one audience and admitted for another, while the concept stays the same. The prohibition therefore belongs to the glossary, never to the concept.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the semiotic triangle, concept-oriented terminology, the requirements of an explication, the separation of concepts from labels, the distinction between sense and reference, and the principle of compositionality, as cited.
> - **Proposals:**
> 	- the separation of the concept, the glossary and the notation into three places, as the decision on concepts adopts it;
> 	- the rule that two forms designate one concept only when they carry the same meaning in the contexts listed.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum, explicatum and the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [frege1892a] ◐ Frege, "Über Sinn und Bedeutung", *Zeitschrift für Philosophie und philosophische Kritik* (N.F.) 100(1), 25–50, 1892; sense and reference
- [iso704] ◐ International Organization for Standardization, *ISO 704:2022 Terminology work — Principles and methods*, 2022; the links between objects, concepts, definitions and designations, checked through the catalogue entry of the standard
- [ogden1923] ◐ Ogden & Richards, *The Meaning of Meaning: A Study of the Influence of Language upon Thought and of the Science of Symbolism*, Kegan Paul, Trench, Trubner & Co., 1923; the triangle of symbol, thought or reference, and referent, pp. 10–12 of the 8th edition (1946), checked through a quotation
- [skos2009] ◐ [Miles & Bechhofer (eds.), *SKOS Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009](https://www.w3.org/TR/skos-reference/); preferred and alternative labels, and the relation `broader`, checked through the namespace document
- [szabo2020] ◐ [Szabó, "Compositionality", *Stanford Encyclopedia of Philosophy*, substantive revision 17 August 2020](https://plato.stanford.edu/archives/fall2022/entries/compositionality/); principle (C), §1
