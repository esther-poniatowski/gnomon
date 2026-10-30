---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the second round of inquiry records
---
# Proposals for the second round of inquiry records

The goal [`inquiry-records-round-2`](../../TODO.md) makes the inquiry records checkable, and closes the gaps of the type graph of activities, among them the recording of a negative detection.

## Four statuses of a detection

A claim of detection takes one of four values, which a record must not conflate:

- **no stored result:** nothing is asserted about whether a result exists;
- **known absence:** a search context, explicitly closed, records that no result exists;
- **disproved:** a counterexample or a contradiction is established;
- **undecided:** the question is open and tracked.

The case that motivated the distinction is the status of a proof, but it holds for any detection. A representation without a clean axis of context does not establish that context is absent: it may show only that no marker shaped like an axis was found, while context deforms the whole space ([example 28](../../examples/adversarial-statements.md#^example-statement-using-absence-as-evidence)). Reading "no stored result" as "known absence" is the false negative that the distinction blocks. The [choice of the next act](../procedures/inquiry/next-act.md) states that no activity records a negative detection, and the four values state what such a record distinguishes.

**Literature.** None cited; the candidate arose from the contrast between open-world and closed-world reading in Description Logics.

**Bears on.** [`inquiry-records-round-2`](../../TODO.md).

## Record of a technique

The act of developing a proof technique or an algorithm that gives access to a quantity yields a product that no record holds. A record of a technique would state the local problem, the need for a new technique, its construction, the properties that the inquiry needs from it, an example of use, and its boundary of applicability.

**Literature.** None cited.

**Bears on.** [`inquiry-records-round-2`](../../TODO.md), whose gaps of the type graph of activities include this act.

**Retired source.** `docs/design/_backup/rendering/note-types.md`, at commit 9e138e2.
