---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Dotted identifiers
---
# Dotted identifiers

> [!QUESTION] Goal: in which form does a reference name a record, or a unit declared inside a record?

The [flat symbol table](flat-symbol-table.md) lets a reference from another record name a record and a symbol, written `system.TOPIC#SYMBOL`. A record identifier is already a sequence of dots, such as `quest.TOPIC.NAME`, so a reference to a unit carries two separators. The consumers of `gnomon` name a unit by a dotted subrecord identifier, and they cite the steps of an itinerary from other repositories.

## Decision

Every reference to a record, or to a unit of a record, is a uniform sequence of dots. The prefix of a record fixes how many segments its identifier holds: two for `system` and `ops`, three for the other record types. One further segment names a unit of the record by its own identifier: the `symbol` of a declared element, or the `id` of a unit without a symbol, such as a step of an itinerary. A step is named in this full form, inside and outside its itinerary.

The decision amends only the reference form of the flat symbol table. Each record keeps one flat table, so one segment names any unit. The identifiers of registries, vocabularies and norms, such as `registry.activities` or `norm.derivation`, keep their own forms.

## Constraints that decide the form

- **A reference must separate the record from the unit.** A resolver must locate the record first, then the unit inside it. Since the prefix fixes the number of segments of the record, the split needs no lookup.
- **A unit keeps its identifier when it moves between fields.** An idealization reclassified as an abstraction stays the same unit, so a field name inside an identifier would break every reference to it.
- **Consumers need a subrecord identifier.** The cross-repository resolution of `geonexus` names a unit by a record identifier and an optional subrecord identifier. The segment beyond the record supplies that subrecord identifier.
- **A field path is not an identifier.** The key `maturity` names fields by their paths, such as `laws.expression`, and those paths address values, never units.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep `system.TOPIC#SYMBOL` | No change to the notes, the checkers or the fixtures | A reference carries two separators, and the subrecord identifiers of the consumers take another form |
| Dots throughout, with the record found by the longest identifier declared | Record identifiers of any length | Each resolution needs a lookup in the declared records, and a record named as the prefix of another one makes the split ambiguous |
| Dots throughout, with the number of record segments fixed by the prefix and one segment for the unit | One separator, and a split read from the prefix alone | A new record type must declare its number of segments, and every unit without an identifier must gain one |

## Consequences

- The notes on [symbols and expressions](../epistemology/language/symbols-and-expressions.md) and the flat symbol table state the dotted reference form, and the templates, checkers and fixtures follow.
- Idealizations, abstractions and explanans factors gain an `id`, under the task `research-corrections`.
- The itinerary check resolves each step by its full identifier, and the references between steps take the full form.
- A new record type declares the number of segments of its identifier with its prefix.
