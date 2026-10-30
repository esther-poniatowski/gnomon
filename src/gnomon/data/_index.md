---
tags:
  - index
aliases:
  - Framework data
---
# Framework data

The data the package ships: the shapes a project fills, and the vocabularies and requirements the checkers read. A specification note documents each vocabulary and is checked against it, so no check depends on a document.

- [The record shapes a project copies and fills](templates/_index.md) carry one file per inquiry layer, in the order of the specification note that documents each.
- [The operators the framework supplies](operators.yml) fix what a formula may use before a problem declares mathematics of its own. Documented by [the syntax of symbols and expressions](../../../docs/specification/expressions.md).
- [The values each closed field admits](vocabularies.yml) fix what a filled record may hold, per field, and give each epistemic aim its category and its answer conditions. Documented by the option list beside each field of [the record shapes](templates/_index.md), and by [the aims an inquiry can pursue](../../../docs/epistemology/objects/task/epistemic-aim.md).
- [What a filled inquiry must carry](requirements.yml) lists the specifications every record holds, what each level of commitment requires of a target system or a phenomenon, what an aim block of an answer holds, and what each epistemic aim adds or produces. Documented by [the aims an inquiry can pursue](../../../docs/epistemology/objects/task/epistemic-aim.md) and by the requirement column of each specification note.
- [The epistemic activities and the product types](registries/_index.md) fix what each step of an itinerary may take and produce. Documented by [the taxonomy of epistemic activities](../../../docs/epistemology/processes/activities/epistemic-activities.md).
- [The shape of each record type](schemas/_index.md) is declared once, so that a program validates a record and Ekphrasis renders it as a form. Documented by [the decision on record schemas](../../../docs/adr/record-schemas.md).
