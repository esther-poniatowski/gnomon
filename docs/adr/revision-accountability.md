---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Revision accountability
---
# Revision accountability

> [!QUESTION] Goal: which requirements must any mechanism meet when a record of an inquiry is revised?

An inquiry revises records already written: a refuted condition, a failed verdict or a corrective answer sends the researcher back to them. Two mechanisms exist. An answer names an earlier answer by the relation `revises`, under the [decision on answers, models and bindings](answers-models-bindings.md). A revised binding becomes a [new version](../epistemology/model-and-binding.md#^binding-version), and the comparisons computed from earlier versions stay unchanged. No decision stated the aim that these mechanisms serve, nor the limits within which a general mechanism may serve it.

## Decision

Each revision is traceable to its origin. The records state which unit was revised, and the finding or the act that caused the revision, in fields or relations that a tool can read. ^traceable-revision

Each revision propagates to its dependents. A tool follows the authored relations backward from the revised unit, and reports every record resting on it. ^propagated-revision

Propagation flags the dependents and never edits them. The researcher decides, for each dependent, whether it holds unchanged, needs an adjustment, or is retracted in turn. ^flag-not-edit

The mechanism that realizes these requirements remains open. The goal `status-propagation` of the [project goals](../../TODO.md) decides which changes of status mark the dependents, and the goal `relation-registry` decides which relations transmit a revision. ^mechanism-open

## Constraints that decide the requirements

- **A silent overwrite breaks the record of an inquiry.** The records that rest on a withdrawn premise keep resting on it, and no reader can reconstruct why the revised form replaced the earlier one.
- **The history of git records which lines changed.** A commit names neither the reason of a revision in terms of the inquiry nor the records in other files that rest on the revised unit.
- **A tool never edits an authored record.** The [decision against inference at run time](no-run-time-inference.md#^excluded-inference) leaves every judgment to the researcher, and the judgment that a dependent still holds is one of them.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Leave revisions to the history of git | No field records a revision | A dependent keeps resting on a withdrawn premise, and nothing reports it |
| Record each episode of revision as a record of its own, and move retired records to an archive, as the retired design notes (commit 9e138e2) proposed | One record gathers the reason, the priority and the progress of an episode | Deferred to the goal `status-propagation`, which first decides which changes mark the dependents. An archive of earlier records must not become the store of past versions that the [decision on versions](versions-and-history.md#^git-keeps-history) excludes |
| Write the provenance of each revision in the data model of W3C PROV [moreau2013] | A standard model separates the revised entity, the activity and the agent, and names a revision `wasRevisionOf` | A second record of provenance would restate the steps of the itinerary and the relation `revises`, which the [rule of one source](one-source-per-unit.md#^one-source) excludes. PROV serves as a reference model for the mechanism, not as its format |
| Type each revision by the operations of belief revision: expansion, contraction and revision [agm1985] | Each revision carries a kind with a defined effect | The postulates assume a theory closed under logical consequence, which the records never form, since no tool infers. The operations stay candidate kinds of revision under the goal `status-propagation` |
| Expire a unit at a fixed date | Staleness requires no relation | A unit becomes stale when a unit upstream of it is revised, as the [decision on the knowledge interchange format](knowledge-interchange-format.md#^not-transferred) states for the field `stale_after` of the Open Knowledge Format |
| Traceability and flagged propagation, as requirements on a mechanism decided later | Each later mechanism meets fixed requirements | Until the mechanism exists, the requirements hold for answers and for bindings only |

## Consequences

- The relation `revises` and the versions of a binding meet the requirement of traceability for answers and bindings.
- The agent that produced a revision belongs to its origin. The trust fields of the Open Knowledge Format await a decision, as the [decision on the knowledge interchange format](knowledge-interchange-format.md#^trust-fields-open) states.
- A lookup of the records resting on a unit reads the [graph of relations](closed-typed-relations.md#^relation-graph), and its result is a report.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the bibliographic record.

- [agm1985] ◐ Alchourrón, Gärdenfors & Makinson, "On the logic of theory change: partial meet contraction and revision functions", *Journal of Symbolic Logic* 50(2), 510–530, 1985
- [moreau2013] ◐ Moreau & Missier (eds.), *PROV-DM: The PROV Data Model*, W3C Recommendation, 30 April 2013
