---
tags:
  - theory
index: "[Expression](docs/epistemology/expression/_index.md)"
aliases:
  - Exposition
  - Exposition as a projection
  - Audience of an exposition
---
# Exposition

> [!QUESTION] Goal: what is an exposition, what may it add to the research that it presents, and what does its audience change?

An **exposition**, such as a brief, a talk or an article, is a projection of the research units of an inquiry to a declared audience. An exposition selects research units, orders them for that audience, and adds only sentences that carry no content: announcements, connectors, and syntheses that restate a relation already held by the research records. Every statement of an exposition that carries content presents a research unit. ^exposition

The [decision on expositions](../../adr/expositions-as-projections.md) gives the exposition records to `gnomon` and fixes their parts. This note states the concept of a projection and its grounds.

## An exposition adds no content

A statement **carries content** when it states a claim, a definition, a datum, an example or a motivation: anything that could be true or false of the objects of the inquiry, or adequate or inadequate to them. A statement **carries no content** when it states only the place of a unit in the text, the relation between two units already recorded, or a summary of relations already recorded. ^adds-no-content

Three grounds support the rule that an exposition adds no content:

- **Communication is not an epistemic activity.** A paper, a talk or a figure carries the content of existing epistemic objects into another medium, so it adds no content to the questions, the knowledge or the warrants of the inquiry, as the [criterion of an epistemic activity](../processes/activities/epistemic-activities.md#^epistemic-criterion) states. An exposition is the product of such communication.
- **Content has one source.** A motivation or an example stated only in an exposition would be content without a canonical record, against the [rule of one source](../../adr/one-source-per-unit.md#^one-source). Every example, motivation or illustration is therefore first recorded as a research unit.
- **Several views over one store keep the store unchanged.** In the architecture of database systems, each group of users reads its own external schema, a view derived from one conceptual schema, and no view stores data of its own [tsichritzis1978]. Literate programming draws a document for human readers and a program for the machine from one source [knuth1984]. An exposition stands to the research records as such a view stands to its store, and a correction therefore goes to the records, after which the exposition is rendered again.

The connectors of an exposition fall under the same rule. Rhetorical Structure Theory separates two kinds of relation between spans of a text [mann1988]. A subject-matter relation, such as cause or elaboration, states a relation between the contents of the spans. A presentational relation, such as motivation or background, aims to change the inclination of the reader. Under a proposal of this method, a connector that states a subject-matter relation restates a relation recorded between the two research units, such as `supports` or `tests`, and a presentational connector adds no content.

## The audience

The **audience** of an exposition is a readership described by its knowledge, its skills and its register, as an audience specification records them under the decision on [terminology, audience and project specifications](../../adr/terminology-audience-project-specifications.md). The design brief of an exposition cites its audiences. ^audience

Argumentation is relative to the audience that it addresses: it seeks the adherence of that audience, and starts from premises that the audience grants [perelman1958]. The audience therefore changes four properties of an exposition:

- the **selection** of units, since a unit that the audience already holds can be referenced instead of presented;
- the **order** of units, and the moves that deliver them;
- the **names** in which the units are stated, which the glossary of the project admits or forbids for that audience, as the note on [concepts and names](concepts-and-names.md#^glossary) states;
- the **granularity** of the presentation, such as the steps of a derivation that are shown.

The audience changes neither the content nor the warrant of a unit. The warrant of a claim is fixed by its grounds and its assessment, which do not depend on the reader.

> [!WARNING] Departure from the theory of argumentation
> In the new rhetoric, a speaker may introduce a premise because the audience grants it [perelman1958]. Such a premise would be content added by the exposition. The method requires instead that a premise needed by an audience first be recorded as a research unit, for instance as a motivation of the object that it motivates.

## Distinctions

- **The order of an exposition is free relative to the itinerary.** The itinerary records the order in which the acts of the inquiry ran. An exposition orders its units for its audience, for instance a claim before its support, so its order need not follow the itinerary.
- **A rhetorical move differs from an epistemic act.** A move is a unit of a text that performs one communicative function [swales1990]. An epistemic act produces an epistemic object and is judged by the norm of its activity. A move is judged by whether it delivers its unit to its audience.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** external schemas over one conceptual schema, literate programming, the relations of Rhetorical Structure Theory, the relativity of argumentation to its audience, and rhetorical moves, as cited.
> - **Proposals:**
> 	- the criterion that separates a statement that carries content from a statement that carries none;
> 	- the analogy between an exposition and a view over a store;
> 	- the restatement of a recorded relation by each connector that states a subject-matter relation;
> 	- the four properties of an exposition that its audience changes, and the departure from the new rhetoric.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [knuth1984] ○ Knuth, "Literate programming", *The Computer Journal* 27(2), 97–111, 1984
- [mann1988] ○ Mann & Thompson, "Rhetorical Structure Theory: toward a functional theory of text organization", *Text* 8(3), 243–281, 1988; subject-matter and presentational relations
- [perelman1958] ◐ Perelman & Olbrechts-Tyteca, *La nouvelle rhétorique : traité de l'argumentation*, Presses Universitaires de France, 1958; English translation *The New Rhetoric: A Treatise on Argumentation*, University of Notre Dame Press, 1969; argumentation relative to its audience, checked through the publisher description
- [swales1990] ○ Swales, *Genre Analysis: English in Academic and Research Settings*, Cambridge University Press, 1990; the rhetorical move
- [tsichritzis1978] ○ Tsichritzis & Klug (eds.), "The ANSI/X3/SPARC DBMS framework", *Information Systems* 3(3), 173–191, 1978; external, conceptual and internal schemas
