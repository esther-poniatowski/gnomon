# Reasoning-annotation field set

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Instantiates the architectural commitments at [reasoning-annotation fields](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-fields) (resolved as fields that vary by profile), [reasoning-annotation attachment](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-attachment) (the grid of locus × content kind), and [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles) (the profile shape). This file fixes what the architecture deferred: the field set and field type for each cell, the named profiles, and the chain of guarantees.

---

## Criteria

### Cell completeness across the locus × content-kind grid ^t3-cell-completeness

Every cell in the locus × content kind grid must declare a field set (possibly empty), a type for each field, and a rule for which fields are mandatory. No cell may remain undefined.

---

## Decisions

### Per-cell field-set proposals ^t3-per-cell-field-set-proposals

> [!QUESTION] Which fields populate each locus × content kind cell, and how is each field typed (free text, controlled enum, structured record, typed reference)?

The architectural choice requires fields to vary by profile. The three alternatives below remain relevant because they spell out candidate field sets; the schema work selects the actual fields from these proposals.

- **Minimal spine with prose defaults.** Each cell has a small mandatory spine of fields and admits a prose body for the rest. The spine fields are mandatory at every formalization profile; nothing else is mandatory. Content by cell:
	- *Canonical, licensing*: `content`, `applied_schema_id` (reference to [operation-schema placement](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-schema-placement)), `support_edges` (each carrying `warrant_kind` per [warrant-kind annotation](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation)).
	- *Assembly, strategic*: prose rationale at each citation site.
	- *Assembly, explanatory*: prose gain after each contribution.
	- *Assembly, process records*: free text or absent.
	- *Assembly, promotable*: prose until promoted; on promotion, the canonical object spine applies.

  *Tradeoffs.* Authors write the least extra structure ([t1-feasibility](../1-framework/cost-ergonomics#^t1-system-scale), [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization)). Queries and validators see little structure; the "five specifications per step" required by [t1-non-arbitrary](../1-framework/reasoning-integrity#^t1-served-goal) cannot be checked mechanically because four specifications live in prose.

- **Structured spine with fields that vary by profile.** Each cell has a mandatory spine *and* a structured optional layer. The formalization profile decides which optional fields become mandatory. Content by cell:
	- *Canonical, licensing*: spine as in the minimal regime, plus optional `preconditions` (typed list) and `derivation` (structured ladder when the profile demands it).
		- *Assembly, strategic*: one structured record per citation — `deficiency_addressed` (prose or controlled tag), `parent_question` (typed reference), `route_chosen` (prose), `rejected_alternatives` (typed list of references or prose labels).
	- *Assembly, explanatory*: a structured record — `gain_kind` (controlled enum, exact vocabulary still open), `gain_statement` (free text).
		- *Assembly, process records*: structure depends on the kind — work metadata as `{schema_id, inputs, output_state}`; applied operations as `{inputs, warrant, action, outputs, success_state}`; state deltas as typed pairs.
		- *Assembly, promotable*: structure depends on the kind — internal lemma as `{statement, support_edges}`; named rejected route as `{label, failure_kind, rationale}` (the `failure_kind` enum comes from the [revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary)); support endpoint inside an assembly as `{statement, warrant_kind}`.
	  A formalization profile (per [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles)) selects which optional fields become mandatory. The spine is mandatory at every profile. The strongest profile makes every optional field mandatory; that is what [t1-intelligibility](../1-framework/reasoning-integrity#^t1-justification-levels) and [t1-non-arbitrary](../1-framework/reasoning-integrity#^t1-served-goal) would impose if read as hard requirements. This profile does not fit informal research practice, so it forms the strict pole of tension [X2](../1-framework/_tensions#^t2-x2).

	  *Tradeoffs.* Queries and validators see enough structure to check [t1-non-arbitrary](../1-framework/reasoning-integrity#^t1-served-goal) when the profile demands it. Authors write more annotations, but profiles keep that burden adjustable. The schema becomes heavier and relies on [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles) to partition mandatory and optional fields.

- **Structured canonical cells with prose assembly cells.** Field requirements differ by locus:
	- *Canonical object cells*: structured spine as in the profile-based regime, mandatory at every profile.
	- *Assembly cells*: prose only, no required structure (strategic, explanatory, process, and promotable kinds all default to prose), with the schema declaring only the *presence* of each kind, not its internal structure. Promotable records become structured at promotion time.

	  *Tradeoffs.* Canonical content is durable and shared, so it gets typed; assembly content belongs to an inquiry, so it stays loose. This preserves [non-redundancy](../1-framework/modular-content-organization#^t1-non-redundancy) for canonical records and [t1-feasibility](../1-framework/cost-ergonomics#^t1-system-scale) for assemblies. It loses query support over assemblies and weakens [t1-intelligibility](../1-framework/reasoning-integrity#^t1-justification-levels) at the strategic and explanatory levels.

---

## Open questions

### Explanatory-gain enum ^t3-gain-kind-enum

> [!QUESTION] Which controlled entries does the `gain_kind` enum admit?

Unspecified. The enum must be drafted and checked against the [revision rationale enum](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary) and the [warrant-kind enum](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary) so that the three vocabularies partition cleanly rather than overlap (per [t3-vocabulary-partition](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary#^t3-vocabulary-partition)).

### Per-cell field-set selection ^t3-per-cell-field-set-selection

> [!QUESTION] Within the structured-spine regime, which fields actually populate each cell?

The schema work picks the field set, drawing on the bodies in the Decisions section above.

### Named profiles and guarantee chain ^t3-named-profiles-guarantees

> [!QUESTION] Which named formalization profiles exist, what does each mandate per cell, and which formal guarantees degrade between profiles?

Settled at [partial-formalization profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles).
