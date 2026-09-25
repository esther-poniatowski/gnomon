---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Single field per fact
tags: []
source:
---
# Single field per fact

> [!QUESTION] Goal: when does a second field restate a fact that the record already carries?

An inquiry record states each fact in one field. A second field holding the same fact admits a record in which the two fields disagree, and it obliges a check whose only purpose is to hold them equal. Two shapes produce the duplication: a field determined by another field, and a block whose boundary encodes a distinction that an entry already names.

## Decision

A fact is carried by one field. A field that another field determines is retired, and a rule that a retired boundary carried is stated as a check.

## Constraints that decide the assignment

- **A block fixes the role of the formula that it holds.** A law can be false of the system and a definition cannot, but the block already separates the two, so two field names encoded that distinction twice.
- **A boundary between blocks earns its place by a rule of its own.** Restrictions on a parameter and on a variable differ in the kind of quantity that they name, and the target record already classifies that kind. The separate blocks left implicit and unchecked the only rule that the boundary carried: only a variable can be clamped or held stationary.
- **A derived fact is read from its source.** Every index absent from the signature was consumed by a binder that already names the map, so the retention field restated the grain.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep both fields and check that they agree | Each fact sits where a reader expects it, and the check reports a record that contradicts itself | Input, output and coupling restated whether a variable is exogenous or internal, so the redundancy required a check that exists only to hold two fields equal |
| Keep a block whose boundary encodes a distinction | A reader sees the distinction in the shape of the record | The boundary states no rule that a check can read, so the one rule that it carried stayed implicit and unenforced |
| Retire the determined field, and state as a check the rule that its boundary carried | Each fact has one source, and each rule has one enforcer | A reader reaches a derived fact through the field that determines it, and a block that survives must justify its boundary by a rule |

## Consequences

One rule produced every retirement of the reorientation: each retired field or block gave way to the field that already determined it.

| Retired | Determined by |
| ------- | ------------- |
| The grain, and the retention field that restated it | The signature of the quantity |
| The declared direction of a shared variable | The block that declares the variable |
| The three restriction blocks | The kind of quantity that each entry names |
| The two variable blocks | The key stating where the quantity is determined |
| The interaction block | The law that asserts the interaction |

- A block survives wherever its boundary carries a rule. The parameters stay apart from the variables because a parameter may not be indexed by the course.
- A record that states an interaction states it as a law, since a dependence of a growth law on a coefficient is falsifiable and expressible with the canonical relations.
