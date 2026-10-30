---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Itinerary and product types
---
# Itinerary and product types

> [!QUESTION] Goal: which names do the record of the acts of an inquiry and the types of its products take?

Two names of `gnomon` misled the authors who applied it. The record named `plan` lists the acts of an inquiry with the verdicts of their norms, yet the name suggests a preparation made before the inquiry starts. The registry `artifact-types.yml` calls its entries epistemic artifacts, yet `geonexus`, a consumer of `gnomon`, calls an artifact a deliverable such as a slide deck or a poster.

## Decision

The record of the acts of an inquiry is the **itinerary**, of type `itinerary` and prefix `itin`, checked by the itinerary check. The types of the products of activities are the **product types**, declared in `product-types.yml`. The epistemic product of an epistemic aim is named by the product types that the aim admits.

## Constraints that decide the names

- **The record is built progressively.** An author adds a step once an act is chosen, and records its verdict once its norm is judged. A failed verdict sends the author back to an earlier state of the record. A name for that record must admit pending and performed steps alike.
- **A name must not collide with a term of `gnomon` or of its consumer.** The phenomenon record already uses `course`, the ontology uses process and history for categories of phenomena, and the [note on dynamics](../epistemology/definitions/change/dynamic.md) uses trajectory. The workspaces use log for task records and decision logs.
- **The word "output" is a field.** A step carries a field `output`, so a type named "output type" would name a field and its type with one word.
- **One name serves one notion.** The table of epistemic aims already names an epistemic product for each aim, so a second notion of product would collide with it unless the two are one.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep `plan` | No rename of the template, the checker or the fixtures | The name suggests a preparation, and the record tracks acts already performed |
| Name the record a log or a history | The name states that the record tracks acts | "Log" collides with the task records and decision logs of the workspaces, and "history" with the ontology of phenomena |
| Name the record an itinerary | The name admits a route followed and a route still to follow, built step by step | Every file, command, anchor and fixture that names the plan changes |
| Name the types output types | The type matches the field that holds its instance | The field `output` and its type would share one name |
| Name the types epistemic object types | `activities.yml` already calls a product an epistemic object | The key `object` is planned for the assembly schema of the task `assembly-schema` |
| Name the types product types, and make the product of an aim a set of product types | One notion of product serves both the activities and the aims | Every note and comment that reads "artifact type" changes, and each aim must name the product types that it admits |

## Consequences

- The template `plan.yml` becomes `itinerary.yml`, the record type `plan` becomes `itinerary`, and the prefix `plan` becomes `itin`.
- The block `plan` of `vocabularies.yml` becomes `itinerary`, the module `plans.py` becomes `itineraries.py`, and the command `gnomon plan` becomes `gnomon itinerary`. The method note on the plan, its anchor `plan-check`, the fixtures and the tests follow.
- The registry `artifact-types.yml` becomes `product-types.yml`, with the identifier `registry.product-types`, the type `product-type-registry` and the key `product_types`. The comments of `activities.yml`, the placeholder `ARTIFACT-TYPE` of the template and the notes that read "artifact type" follow.
- The column of epistemic products in the table of [epistemic aims](../epistemology/epistemic-task/epistemic-aim.md) names, for each aim, the product types admitted by the aim.
- The word "planning" keeps its sense of choosing the next act.
