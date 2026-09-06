---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Status vocabulary
---
# Status vocabulary

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Instantiates the architectural commitment at [epistemic status as a maturity record](../2-architecture/object-kinds.md#^t2-epistemic-status): maturity is recorded in a schema-declared status field, closed at design time. The architecture commits *that* maturity is enum-recorded; the *grain* of the enum — one per object kind, or one uniform enum — is an open question in this file. This file carries the candidate enum entries, the open grain question, and the distinction between maturity and warrant kind.

---

## Criteria

### Terminal value required in every per-kind enum ^t3-status-terminal-value

Every status enum for an object kind must include a `retracted` value or equivalent terminal value, so that the `retraction` kind in [revision machinery](revision-vocabulary.md) has a target state.

### Status independent of warrant kind ^t3-status-distinct-warrant

Status and [warrant kind](warrant-vocabulary.md) are independent properties; neither implies the other.

---

## Decisions

### Maturity vs. warrant kind ^t3-maturity-vs-warrant

> [!QUESTION] Are epistemic maturity and warrant kind independent properties, and how do they interact?

Epistemic maturity records the object's *current standing*; [warrant kind](warrant-vocabulary.md) records *how the object is supported*. The two are independent (per [t3-status-distinct-warrant](#^t3-status-distinct-warrant)):

- A *formally proven* claim within a deductive system has maturity `accepted` and warrant kind `deductive`.
- A *hypothesized* empirical claim has maturity `hypothesized` and warrant kind `empirical`.
- A *formally proven* result that depends on an empirical premise has maturity `accepted` and defeasible support.
- A *retracted* claim has maturity `retracted`; its warrant kinds become operationally inert.

Supersession is not a maturity value; it is a version-history phenomenon, outside the frameworks scope per [no version history](../1-framework/framework-foundations.md#^t1-no-version-history). The maturity enum records only the objects current in-state standing.

---

## Open questions

### Per-kind status enums ^t3-per-kind-status-enums

> [!QUESTION] Does each object kind declare its own status enum, or do all kinds share one uniform maturity enum?

[Epistemic status as a maturity record](../2-architecture/object-kinds.md#^t2-epistemic-status) commits *that* maturity is recorded in a schema-declared enum, but the grain of that enum is unsettled.

- **Per-kind enums** — each object kind declares its own enum, closed at design time. This fits each kind's lifecycle precisely: a `Proof` matures through `sketched | drafted | verified`, a `Question` through `open | refined | answered | abandoned`, which a shared enum cannot express.
- **Uniform enum** — all kinds share one maturity enum. This keeps the framework smaller: maturity status is not a central concern, and per-kind enums multiply the vocabulary the schema declares, the validators check, and the reader learns.

The tension is between **lifecycle fidelity** and **framework economy**. The per-kind enum was the earlier working answer; its kind-specific entries are the candidate for that alternative:

| Object kind | Status enum (per-kind candidate) |
| --- | --- |
| Claim / theorem | `preliminary` \| `hypothesized` \| `informally_backed` \| `formally_proven` \| `accepted` \| `retracted` |
| Question | `open` \| `refined` \| `answered` \| `abandoned` |
| Proof | `sketched` \| `drafted` \| `verified` \| `retracted` |
| Definition | `provisional` \| `stabilized` \| `retracted` |

Resolution must hold whichever grain it picks against [object-kind set smallness](../2-architecture/object-kinds.md#^t2-ontology-small) and the terminal-value requirement at [t3-status-terminal-value](#^t3-status-terminal-value): every enum, per-kind or uniform, must carry a `retracted` or equivalent terminal value.

Bearing criteria: [terminal value required in every per-kind enum](#^t3-status-terminal-value), [object-kind set smallness](../2-architecture/object-kinds.md#^t2-ontology-small).

### Status transitions and revision propagation ^t3-status-transition-propagation

> [!QUESTION] Which status transitions trigger revision propagation for dependents whose support depended on the prior status?

- **Retracting transitions** (any state -> `retracted` or a terminal value for the kind): clearly invoke the [revision machinery](../2-architecture/validity-revision.md#^t2-revision-kinds) as a `retraction` kind.
- **Strengthening transitions** (e.g., `hypothesized -> formally_proven`): may not require propagation. A downstream argument that flagged its conclusion as tentative because its premise was only `hypothesized` should be re-examined when the premise strengthens, but no stale mark is needed because the support is now stronger, not weaker. Whether to record such transitions as a `correction` kind for queries across projects is open.
- **Lateral transitions** within an enum (e.g., for questions, `open -> refined`): no propagation; the question is being clarified, not retracted.

A precise table that maps transitions to propagation behavior is deferred until [the status-enum grain](#^t3-per-kind-status-enums) is settled.

An earlier draft proposed a single closed transition table over a generic four-state workflow vocabulary, with any unlisted transition rejected as a validation error:

| From | Allowed transitions |
| --- | --- |
| `pending` | `in-progress` |
| `in-progress` | `done`, `pending` (with justification) |
| `done` | `revised` |
| `revised` | `done` |

This is a **candidate**, not a settled table. Its states predate the per-kind framing and do not transcribe onto the kind-specific enums; resolution must restate the permitted transitions over whichever enum grain wins. The candidate's transferable commitment is the **closed-table rule** — transition legality is schema-declared and a transition outside the table is a validation error — which the [catalogue of structural validators](../2-architecture/validation-views.md#^t2-validator-catalogue) checks under its status-transitions entry.
