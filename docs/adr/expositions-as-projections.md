---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Expositions as projections
---
# Expositions as projections

> [!QUESTION] Goal: which tool specifies the records of an exposition, and what may an exposition add to the research that it presents?

An exposition, such as a brief, a talk or an article, selects results of an inquiry and orders them for an audience. The exposition also tells the reader how each part serves the argument. `gnomon` already admits a copy of a unit only when a tool [generates it from its source](one-source-per-unit.md#^generated-copies-only), so an expository view is derived from the records and never edited. The records that specify an exposition had no owner, so a consumer specified them in its own workspace, apart from the research records that they present.

## Decision

`gnomon` specifies two families of records. Research records hold the content of an inquiry as research units, together with the itinerary of its epistemic acts. A research unit is a research record, or a unit of such a record. Exposition records hold no content: they select research units, order them for an audience, and add sentences without content.

Every statement of an exposition that carries content presents a research unit. Therefore, every example, motivation or illustration is first recorded as a research unit. The sentences without content are announcements, connectors, and syntheses that restate a relation held by the research records. The key `move` declares the rhetorical move of a part or a block of an exposition.

## Constraints that decide the owner

- **An exposition is a projection of research.** Each statement traces to its presented research unit, so the projection depends on the definitions of the research records. The tool defining those records is therefore the coherent owner of the projection.
- **Content has one source.** A motivation or an example stated only in an exposition would be content without a canonical record. The single source of truth of `gnomon` excludes such content.
- **The research family records acts, the exposition family records rhetoric.** A research record adds the epistemic acts that produce each content. An exposition record adds the moves, connectors, announcements and syntheses that deliver it.
- **A name already in use keeps its meaning.** "Operation" names an operation schema. "Profile" names an audience profile. Neither names a notion of the exposition family. "Move" already names an epistemic move of reasoning, so the key `move` of an exposition always reads as a rhetorical move.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Each consumer specifies its expositions | `gnomon` stays limited to inquiry | The projection depends on the research records, so each consumer would restate their definitions |
| A separate tool for expositions | Each tool keeps one family | No second tool would read the definitions of exposition records yet, and the projection still depends on the research records |
| `gnomon` specifies both families | One owner for the content and its projections | The scope of `gnomon` widens beyond inquiry |
| An exposition may add motivation, framing and worked illustrations | An author writes an exposition without first recording every example | Such an exposition holds content without a canonical record |

## Consequences

- The [motivation of the README](../../README.md#motivation) adds the projection of research into expositions to the aims of `gnomon`.
- The exposition family declares the parts and blocks of an exposition, its moves with the kind of output that each move requires, its connectors, its announcements and syntheses, and its traces to research units.
- A correction goes to the research records, and the exposition is rendered again, since a rendered view is never edited.
- The view specifications of `gnomon` declare the audience profile. A consumer keeps its audience records, conforming to that profile, together with its rendering conventions and its artifacts.
