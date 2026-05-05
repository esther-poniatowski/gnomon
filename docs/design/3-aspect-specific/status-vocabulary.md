# Status vocabulary

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Instantiates the architectural commitment at [epistemic status as a maturity record](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status), resolved as status enums by object kind that close at design time. The architecture commits *that* each object kind declares its own status enum in the schema. This file fixes the enum entries for each kind and the distinction between maturity and warrant kind.

---

## Criteria

### Terminal value required in every per-kind enum ^t3-status-terminal-value

Every status enum for an object kind must include a `retracted` value or equivalent terminal value, so that the `retraction` kind in [revision machinery](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary) has a target state.

### Status independent of warrant kind ^t3-status-distinct-warrant

Status and [warrant kind](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary) are independent properties; neither implies the other.

---

## Decisions

### Per-kind status enums ^t3-per-kind-status-enums

> [!QUESTION] What status enum does each object kind declare?

Each object kind declares its own enum. The entries below are working proposals, to be ratified by the schema work. The enums are closed at design time.

| Object kind | Status enum (proposal) |
| --- | --- |
| Claim / theorem | `preliminary` \| `hypothesized` \| `informally_backed` \| `formally_proven` \| `accepted` \| `retracted` |
| Question | `open` \| `refined` \| `answered` \| `abandoned` |
| Proof | `sketched` \| `drafted` \| `verified` \| `retracted` |
| Definition | `provisional` \| `stabilized` \| `retracted` |

Other object kinds (example, method, assumption, ...) declare their own enums under the same convention.

### Maturity vs. warrant kind ^t3-maturity-vs-warrant

> [!QUESTION] Are epistemic maturity and warrant kind independent properties, and how do they interact?

Epistemic maturity records the object's *current standing*; [warrant kind](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary) records *how the object is supported*. The two are independent (per [t3-status-distinct-warrant](#^t3-status-distinct-warrant)):

- A *formally proven* claim within a deductive system has maturity `accepted` and warrant kind `deductive`.
- A *hypothesized* empirical claim has maturity `hypothesized` and warrant kind `empirical`.
- A *formally proven* result that depends on an empirical premise has maturity `accepted` and defeasible support.
- A *retracted* claim has maturity `retracted`; its warrant kinds become operationally inert.

Supersession is not a maturity value; it is a git-history phenomenon, per [t1-git-delegation](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-git-delegation). The maturity enum records the in-state standing of the object at HEAD.

---

## Open questions

### Status transitions and revision propagation ^t3-status-transition-propagation

> [!QUESTION] Which status transitions trigger revision propagation for dependents whose support depended on the prior status?

- **Retracting transitions** (any state -> `retracted` or a terminal value for the kind): clearly invoke the [revision machinery](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-kinds) as a `retraction` kind.
- **Strengthening transitions** (e.g., `hypothesized -> formally_proven`): may not require propagation. A downstream argument that flagged its conclusion as tentative because its premise was only `hypothesized` should be re-examined when the premise strengthens, but no stale mark is needed because the support is now stronger, not weaker. Whether to record such transitions as a `correction` kind for queries across projects is open.
- **Lateral transitions** within an enum (e.g., for questions, `open -> refined`): no propagation; the question is being clarified, not retracted.

A precise table that maps transitions to propagation behavior is deferred until the enums by kind are ratified.
