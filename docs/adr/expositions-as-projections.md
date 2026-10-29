---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Expositions as projections
tags: []
source:
---
# Expositions as projections

> [!QUESTION] Goal: which tool specifies the records of an exposition, and what may an exposition add to the research that it presents?

An exposition, such as a brief, a talk or an article, selects results of an inquiry, orders them for an audience, and tells the reader how each part serves the argument. The [layering](../design/2-architecture/layering.md) of `gnomon` already derives expository views from canonical records, forbids edits to a rendered view, and keeps epistemic content out of view specifications. The records that specify an exposition had no owner, so a consumer specified them in its own workspace, apart from the research records that they present.

## Decision

`gnomon` specifies two families of records. Research records hold the content of an inquiry and the itinerary of its epistemic acts. Exposition records project that content for an audience. An exposition adds no content. Every statement of an exposition presents a research unit, and every example, motivation or illustration exists as a research object before an exposition presents it. An exposition adds only sentences that carry no content: announcements, connectors, and syntheses that restate a relation held by the research records. The rhetorical move of an exposition level is declared by the key `move`.

## Constraints that decide the owner

- **An exposition is a projection of research.** Each statement traces to its presented research unit, so the projection depends on the definitions of the research records. The tool defining those records is therefore the coherent owner of the projection.
- **Content has one source.** A motivation or an example stated only in an exposition would be content without a canonical record. The single source of truth of `gnomon` excludes such content.
- **A rendered view is never edited.** A correction goes to the records, and the view is rendered again.
- **The research family records acts, the exposition family records devices.** Both families share the content and its architecture, whereas a research record adds the epistemic acts that produce each content, and an exposition record adds the rhetorical devices that deliver it.
- **A name already in use keeps its meaning.** "Operation" names an operation schema and "profile" names a formalization profile in `gnomon`, so neither names a notion of the exposition family.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Each consumer specifies its expositions | `gnomon` stays limited to inquiry | The projection depends on the research records, so each consumer would restate their definitions, and the content shared by both families would have two owners |
| A separate tool for expositions | Each tool keeps one family | No second tool uses the shared contract yet, and the projection still depends on the research records |
| `gnomon` specifies both families | One owner for the content, its architecture and its projections | The scope of `gnomon` widens beyond inquiry |
| An exposition may add motivation, framing and worked illustrations | An author writes an exposition without first recording every example | Such an exposition holds content without a canonical record |

## Consequences

- The [project overview](../project-overview.md) adds the projection of research into expositions to the aims of `gnomon`.
- The exposition family declares its levels, its rhetorical moves with the product type required by each move, its transitions, its announcements and syntheses, and its traces to research units.
- A consumer keeps its bindings: its rendering conventions, its audience records and its artifacts.
