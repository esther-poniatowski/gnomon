---
tags:
  - decision
status: accepted
created: 2026-10-30
revised: 2026-10-30
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Neutral records on existence
---
# Records neutral on existence

> [!QUESTION] Goal: what may a record presuppose about the existence of the objects that it describes?

The positions of the philosophy of science separate a question of existence, whether the object of an inquiry exists independently of its descriptions, from a question of access, whether the object can be known other than through a description. The [note on existence and access](../epistemology/foundations/existence-and-access.md) states both questions and the positions that answer them. The definitions of the method state the realist sense of each term first, as a [reading aid](../epistemology/foundations/things-and-constructs.md), and no decision stated whether the records themselves take a side.

## Decision

A record states no ontological status. No field records whether an item exists independently of its description, and no check reads such a status. ^no-ontological-field

Every content of a record is a representation of its object. The target specification represents the target, and a model record represents a system studied in place of the target. ^records-represent

A claim of a record is read literally, and it can be false of its object. A declaration makes no claim, and it is assessed for its adequacy only. ^claims-literal

## Constraints that decide the stance

- **Researchers who share a method differ on realism.** A realist and an empiricist can fill the same records for one inquiry, and a record that states a stance would oblige one of them to misreport.
- **No check needs a stance on existence.** Each test of warrant compares a claim with recorded data or with admitted laws, and it returns the same verdict under a realist and an empiricist reading.
- **A tool must not settle a philosophical question.** A field read by a checker produces verdicts, so a field of ontological status would turn a philosophical commitment into a defect report.
- **A claim must be able to fail.** The tests of fidelity and of warrant presuppose that a claim says something about its object that the data can contradict, which instrumentalism denies.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Realist records: a field states that each declared constituent or law exists independently | A reader knows the commitment of each record | An empiricist cannot fill the field truthfully, and no check would use it |
| Empiricist records: claims about unobservables are recorded as instruments of prediction only | No metaphysical commitment enters a record | A claim then cannot be false of its object, and the tests of fidelity and warrant lose their object |
| A status field per item, filled by the author with a stance of their choice | Each author records their own stance | The field yields no verdict and fragments the records of one inquiry across stances, against the [grounds for a shared field](shared-field-grounds.md) |
| Records neutral on existence, literal on claims, and representational in every content | Every reading of the philosophy of science except instrumentalism fits the same records, and every check keeps its object | A reader who needs the stance of an author finds it outside the records, in the prose of the inquiry |

## Consequences

- The realist frame of the definitions stays a reading aid, and each definition keeps its representational sense explicit for an empiricist reader.
- The description of a target and a model system are both representations. The method separates them by their role, the description of the target against a stand-in studied in its place, never as reality against representation.
- A future field that would presuppose a stance on existence reopens this decision.
