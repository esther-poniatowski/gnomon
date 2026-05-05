# Semantic relations

To improve query precision, the graph use typed relations (edges between objects).

_Examples_: ==TODO: select the minimal set that is simultaneously expressive enough and non overlapping, and define each relation precisely.==

- `defines`
- `uses` / `uses_in_proof` / `requires`
- `assumes`
- `answers`
- `proves`
- `refutes` / `contradicts`
- `specializes` / `refines`
- `generalizes`
- `compares_with` / `contrasts_with`
- `motivates` / `motivated_by`
- `requires_for_interpretation` / `interprets_via`
- `illustrates` / `instantiates` / `exemplifies`
- `excluded_by`

Specifically, justificatory dependence and semantic dependence are different edges. For instance:

- A theorem **semantically depends** on a definition because its statement cannot be interpreted without it.
- A proof may **justificatorily depend** on several lemmas and assumptions.

**WARNING: Relational inflation**

If every object is linked to many others with vague relation names, the graph becomes unreadable. Therefore:

- restrict relation vocabulary
- make edge types precise
- distinguish strong and weak dependencies


## 5. Relation ontology should be split into two strata

The proposal will become much cleaner if relation types are divided into:

### A. Canonically declared relations

These are asserted at the level of epistemic content itself.

|Relation|Typical source → target|
|---|---|
|`defines`|Definition → Concept|
|`uses`|Proof / Claim / Definition → Concept / Assumption / Claim|
|`proves`|Proof → Claim|
|`assumes`|Proof / Claim / Construction → Assumption|
|`specializes`|Concept / Claim → Concept / Claim|
|`generalizes`|Concept / Claim → Concept / Claim|
|`contradicts`|Claim / Counterexample → Claim|
|`exemplifies`|Example → Concept / Claim|
|`refutes`|Counterexample / Claim → Claim|
|`addresses`|Claim / Definition / Construction → Question|

### B. Inquiry-relative relations

These should exist only inside argument bundles.

|Relation|Meaning|
|---|---|
|`selected_for`|chosen for a target inquiry|
|`load_bearing_for`|indispensable in a particular answer path|
|`bridge_for`|connects two otherwise disconnected parts of the answer|
|`deferred_in`|intentionally omitted at current granularity|
|`ordered_before_in`|local presentation or reasoning order within one bundle|

This distinction is important because a relation such as “this object answers question `Q`” may be too strong as a canonical global statement. Often the safer canonical relation is only `addresses`, while the stronger role “is used here as part of the minimal answer” belongs to the inquiry layer.
