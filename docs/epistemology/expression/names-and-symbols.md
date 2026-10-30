---
tags:
  - theory
index: "[Expression](docs/epistemology/expression/_index.md)"
aliases:
  - Glossary and notation
  - Names and symbols
  - Glossary (theory)
  - Notation of a project
---
# Glossary and notation

> [!QUESTION] Goal: what do a glossary and a notation hold, and how do they express the concepts of a project without changing them?

A **name** is a word or a phrase that designates a [concept](../objects/concept/concept.md#^concept), and a **symbol** is a written form that designates a quantity or a concept in formulas. A concept keeps one meaning, whereas its names and symbols vary with the audience and the context of a text. The glossary holds the names of the concepts of one project, and the notation composes its symbols. Both belong to expression: they change how a content is presented, never the content. ^names-symbols

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
> - **Established:** the separation of concepts from labels, the distinction between sense and reference, and the principle of compositionality, as cited.
> - **Proposals:**
> 	- the glossary and the notation as records of one project, apart from the concept;
> 	- the rule that two forms designate one concept only when they carry the same meaning in the contexts listed.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [frege1892a] ◐ Frege, "Über Sinn und Bedeutung", *Zeitschrift für Philosophie und philosophische Kritik* (N.F.) 100(1), 25–50, 1892; sense and reference
- [skos2009] ◐ [Miles & Bechhofer (eds.), *SKOS Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009](https://www.w3.org/TR/skos-reference/); preferred and alternative labels, and the relation `broader`, checked through the namespace document
- [szabo2020] ◐ [Szabó, "Compositionality", *Stanford Encyclopedia of Philosophy*, substantive revision 17 August 2020](https://plato.stanford.edu/archives/fall2022/entries/compositionality/); principle (C), §1
