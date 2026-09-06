---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Revision vocabulary
---
# Revision vocabulary

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Instantiates the architectural commitments at [revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback) and its sub-questions: [revision kinds](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-kinds), [revision recording](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-recording), [archival](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-archival), [upstream-change propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation). The architecture commits *that* a closed enum for revision kinds exists and allows multiple tags, *that* each kind has a default propagation priority, *that* revision objects distinguish authored and derived fields, and *that* archival diagnostics name the required action without performing it. This file fixes the contents.

---

## Criteria

### Multi-tag revision episodes supported ^t3-multi-tag-supported

A single revision episode must admit multiple kind tags. The schema cannot force a one-tag-per-episode constraint.

### Cross-aspect vocabulary partition ^t3-vocabulary-partition

The enum for revision kinds, the enum for failure kinds, the [warrant-kind enum](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary), and the gain-kind enum (per [Reasoning-annotation field set](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields)) must partition cleanly rather than overlap. No vocabulary entry may be ambiguous between two enums.

### Authored-vs-derived field classification ^t3-author-derived-split

Each revision-object field must be classified as authored, derived, or author-during-lifecycle. No field is unclassified.

---

## Decisions

### Revision-kind enum ^t3-revision-kind-enum

> [!QUESTION] Which revision kinds does the system recognize, and what default propagation priority does each carry?

Closed enum; a revision episode may carry multiple tags; each kind carries a default propagation priority. When a revision episode carries multiple tags, the episode priority is the max over the default priorities of its tags ([upstream-change propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation) refines this with warrant kind sensitivity).

| Kind                    | Meaning                                                                                                                                                                                                                                                                                                                                                     | Default propagation priority |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `retraction`            | A *canonical, once-active object* (definition, claim, example, question, ...) is no longer pursued. When the object existed, it had a status and possibly accumulated dependents.                                                                                                                                                                          | High                         |
| `scope_narrowing`       | The object's applicability is restricted (e.g., a definition's domain shrinks; a claim's range tightens).                                                                                                                                                                                                                                                   | Medium                       |
| `scope_generalization`  | The object's applicability is extended (existing uses remain valid; new uses become possible).                                                                                                                                                                                                                                                              | Low                          |
| `reorientation`         | The object's content is reframed without strict narrowing or generalizing (e.g., a definition rephrased around a different invariant; a claim reformulated against a different counterfactual; a question reformulated). Reformulation of a question or goal is a *particular case* of `reorientation` applied to question-kind objects; no separate label. | Medium                       |
| `taxonomic_restructure` | The object's classification or its relations to siblings/parents change (renaming, regrouping, splitting, merging).                                                                                                                                                                                                                                         | High                         |
| `correction`            | A non-scope content change (an error in a proof; a wrong example replaced).                                                                                                                                                                                                                                                                                 | Medium                       |

### Rationale failure-kind enum ^t3-failure-kind-enum

> [!QUESTION] Which tags for failure kinds does the rationale field admit, to enable queries across projects about patterns in failed routes?

The revision object's `rationale` field carries one or more tags for failure kinds from a closed enum, plus optional prose.

Initial entries: `derivation_blocked`, `requires_unavailable_object`, `obstructed_by_assumption`, `superseded_by_alternative`.

### Revision-object schema ^t3-revision-object-schema

> [!QUESTION] What field set does a revision object carry, and which fields are authored vs. derived?

Per [revision recording](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-recording), every revision episode is a record at `revisions/{id}.md` with the following fields:

| Field              | Description                                                                                                                                                      | Author                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `revised_objects`  | List of upstream object IDs revised in this episode (multi-target permitted when several objects are revised together as part of one coherent revision process). | Human reviewer at creation                                                          |
| `revision_kinds`   | One or more tags from the enum for revision kinds above.                                                                                                        | Human reviewer at creation                                                          |
| `rationale`        | *Why* the revision was issued, via the enum for failure kinds above plus optional prose.                                                                         | Human reviewer at creation                                                          |
| `priority`         | Urgency for treating the revision.                                                                                                                               | Derived automatically (see [upstream-change propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation)), specified by human reviewer |
| `dependents`       | List of subsequent objects (IDs) requiring revision, identified by traversing the dependency registry from each entry in `revised_objects`.                      | Derived automatically, specified by human reviewer                                  |
| `status`           | `open`, `in_progress`, `resolved`                                                                                                                                | Human reviewer during lifecycle                                                     |
| `dependent.status` | Per-dependent records `pending`, `revised`, `confirmed_unaffected`, `retracted`.                                                                                 | Human reviewer during lifecycle                                                     |

### Archival validator diagnostics ^t3-archival-diagnostics

> [!QUESTION] What diagnostics does the archival validator emit on incomplete tombstone/revision pairings?

Per [archival](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-archival), when the status of a canonical object flips to `retracted`, the author must:

1. Create a revision object in `revisions/` carrying `revision_kinds: [retraction]`, naming the retracted ID in `revised_objects` with `rationale` filled in.
2. Move the file to `archive/{kind}/{id}.md`.

The validator emits diagnostics naming the required action when the pairing is incomplete:

- if a tombstone object exists in `archive/{kind}/` without a corresponding revision object (e.g. "tombstone at `archive/{kind}/{id}.md` requires a corresponding revision object");
- if an object marked `retracted` remains in the active store (e.g. "object at `{kind}/{id}.md` marked `retracted` must be moved to `archive/{kind}/`");
- if an object is in the archive but not marked `retracted` (e.g. "object at `archive/{kind}/{id}.md` must be marked `retracted`").

Similarly, when a revision object flips to `resolved`, the author moves it to `archive/revisions/`; the validator applies analogous checks.

### Propagation parameter examples ^t3-propagation-examples

> [!QUESTION] Which relation kinds transmit revision; which warrant kinds determine sensitivity; how do priority components combine? ([upstream-change propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation))

The examples below draw on the relation vocabulary deferred to [the project TODO](vendor/gnomon/docs/TODO) and the [warrant-kind enum](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary). They illustrate how the three propagation parameters combine; the relation vocabulary work settles the actual transmission set and combination rule.

- **Transmission examples.** `depends_on`, `supports`, `uses` transmit revision; `contrasts_with`, `exemplifies` (in some readings) do not.
- **Sensitivity examples.** Monotonic warrants (deductive) are sensitive only to retraction of premises or invalidation of the inference rule (e.g., `retraction`, `taxonomic_restructure`, `correction`). Defeasible warrants (empirical, abductive, analogical, heuristic) are additionally sensitive to qualifying or counter-evidence introduced upstream (e.g., `scope_narrowing`, `scope_generalization`, `reorientation`).
- **Combination rule (provisional).** Max of the priorities attached to each `revision_kind`, with one notch up if the edge is defeasible and only defeasible support is sensitive to the upstream change.

---

## Open questions

### Transmitting relation set ^t3-transmitting-relation-set

> [!QUESTION] Which exact relation kinds transmit revision?

Deferred to the relation-vocabulary decision in [the project TODO](vendor/gnomon/docs/TODO); see also [upstream-change propagation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-propagation).

### Combination rule for priority ^t3-priority-combination-rule

> [!QUESTION] What is the exact rule combining `revision_kind` priority with `warrant_kind` sensitivity into the per-dependent priority?

Provisional formulation in the Decisions section above; final form deferred.
