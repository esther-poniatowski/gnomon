---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Dotted identifiers
tags: []
source:
---
# Dotted identifiers

> [!QUESTION] Goal: in which form does an identifier name a record or a unit declared inside a record?

The [flat symbol table](flat-symbol-table.md) lets a reference from another record name a record and a symbol, written `system.TOPIC#SYMBOL`. A record identifier is already a sequence of dots, such as `quest.TOPIC.NAME`. Units nest inside a record, such as a law inside an answer or a step inside an itinerary, and consumers cite them from other repositories. The form `#` admits one level only, and it mixes two separators in one identifier.

## Decision

Every identifier is a uniform sequence of dots, from the record to the nested unit. The prefix of a record fixes the number of segments of its identifier: two for `system` and `ops`, three for every other record type. The segments beyond that number name units by their own identifiers, never by field names or list positions. A step of an itinerary is named by the identifier of the itinerary followed by the identifier of the step.

## Constraints that decide the form

- **A reference must separate the record from the unit.** A resolver must locate the record first, then the unit inside it. Since the prefix fixes the number of segments of the record, the split needs no lookup.
- **A unit keeps its identifier when it moves between fields.** An idealization reclassified as an abstraction stays the same unit, so a field name inside an identifier would break every reference to it.
- **Consumers need a subrecord identifier.** The cross-repository resolution of `geonexus` names a unit by a record identifier and an optional subrecord identifier. The segments beyond the record supply that subrecord identifier.
- **A field path is not an identifier.** The key `maturity` names fields by their paths, such as `laws.expression`, and those paths address values, never units.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Keep `system.TOPIC#SYMBOL` | No change to the notes, the checkers or the fixtures | The form admits one level of nesting, and an identifier carries two separators |
| Dots throughout, with the record found by the longest identifier declared | Record identifiers of any length | Each resolution needs a lookup in the declared records, and a record named as the prefix of another one makes the split ambiguous |
| Dots throughout, with the number of record segments fixed by the prefix | One separator, and a split read from the prefix alone | A new record type must declare its number of segments |

## Consequences

- The notes on [symbols and expressions](../epistemology/symbols-and-expressions.md) and the flat symbol table state the dotted form, and the templates, checkers and fixtures follow.
- A new record type declares the number of segments of its identifier with its prefix.
- The itinerary check resolves a step by its full identifier.
