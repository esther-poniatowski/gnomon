---
tags:
  - tasks
aliases:
  - Usability improvement plan
---
# Usability improvement plan

This plan makes `gnomon` operationally usable for domain-competent researchers new to its epistemic framework. The integrated workflow supports both new and existing inquiries. Each researcher must author every scientific and epistemic claim and distinguish software conformance from epistemic validity.

## Task state

The user ratified the product model, entry routes and ownership boundary on 2026-11-09. Gnomon's canonical documents now state these decisions. The corresponding Ekphrasis synchronization remains open. Every unchecked item inherits the pending date 2026-11-09 until its state changes.

The default order follows the dependencies among the phases. A phase may start out of sequence when its prerequisites hold. Then, the project must record the resulting synchronization debt.

Gnomon has finished Phase 0. In Phase 1, Gnomon versioned the contracts of the sentence-valued view fields. Therefore, freshly generated views now pass the Ekphrasis corpus test. Ekphrasis also runs Gnomon, places a real issue at its field through the generic checker interface and diagnoses the dependencies of this route. The desktop diagnostic route passed in Obsidian: the report separates simultaneous registry and interpreter failures, advances to a missing checker package after the interpreter is repaired, and measures a configured Gnomon checker. Mobile verification is deferred outside the basic-version milestone. Forced runner stops terminate checker process trees through a process group on macOS and Linux, with integration evidence on macOS. Linux execution, Windows failure handling, both setup-probe timeout layers and queued calls for superseded text remain open. Ekphrasis now compares each displayed view with the current authored-record state and identifies a stale view at its source-state field.

The portable setup and initial greenfield authoring routes of Phase 2 are operational. The command `gnomon setup` installs a relocatable registry and its complete schema closure in an arbitrary vault. The Obsidian diagnostic passes the registry, schema, form, file-indexing and write-permission checks. By default, `gnomon init` writes only identifying and first-stage required fields; Ekphrasis displays those fields immediately and keeps optional branches behind *+ Add a field*. The complete commented source templates remain available through `--full-template`. A generic Ekphrasis creation can now invoke `gnomon register`, so Gnomon retains the stage order and Markdown rules of its inquiry index. The combined creation-and-registration route passed inside Obsidian. The adoption tutorial now starts from one active question, retains external sources as pointers, promotes only its target and phenomenon, and reaches an authored choice of the next act. The tutorials link reusable meanings to their specification or epistemology owners, while one inquiry procedure owns selective promotion, external-unit classification and pointer placement.

Phase 4 separates missing fields, invalid values, warnings and epistemically unresolved research state. Openable documentation targets remain deferred while users consult GitHub, and displaying a finding's general rule remains open. Phase 5 is complete. The next-act view keeps every ready act unranked, shows its operative consequences, and compares valid appraisals only through ordinal dominance. Ekphrasis identifies current and stale generated views through the producer's source-state command. Gnomon selects one primary view for each explicit completion target, and each selected view states its coverage. Ekphrasis now opens that view without copying Gnomon's routing rules. Phase 6 publishes an operational inquiry graph that opens on a starting problem and connects products through typed research activities. Its layered mode exposes the primary route, while its network mode exposes the complete graph. Node facets, provenance layers and individual edge kinds can reduce either projection. Keyboard navigation follows and announces visible research relations from one graph Tab stop. The user accepted the basic rendered views. The integrated greenfield tutorial now documents the portable-vault workflow across both products. The first novice walkthrough has passed setup, progressive disclosure, first-stage entry, contextual identifier guidance and invalid-identifier recovery on both entry routes. Gnomon's generated question contract now publishes its same-record aim requirements, so the checker-free form also reveals each conditional first-stage field from the selected aim. The integrated recovery walkthrough has also passed. Its five verified desktop procedures are now published in the user guide.

## Phase 0 — Fix the product contract

**Owner:** Gnomon. Ekphrasis contributes to the shared boundary.

- [x] **Define the primary user.** The primary persona is a domain-competent researcher who is new to Gnomon and its epistemic vocabulary. The user need not be a novice at research. (2026-11-09)
- [x] **Declare two required entry routes.** The *greenfield route* begins a new inquiry in Gnomon. The *adoption route* represents an active part of existing research in Gnomon. (2026-11-09)
- [x] **Adopt the [Gnomon–Ekphrasis ownership boundary](docs/adr/research-scope.md#^ekphrasis-boundary).** (2026-11-09)
- [x] **Define the [four result classes](docs/adr/findings-output.md#^interface-result-classes) used by every interface.** (2026-11-09)
- [ ] **Synchronize the ratified product contract.** Gnomon's canonical scope, interface and integration documents state the four completed decisions. Ekphrasis must add the same boundary and result classes to its canonical product and interface documents. (Gnomon completed 2026-11-09; Ekphrasis pending)
- [x] **Reconcile published capability states.** The [capability-status guide](docs/guide/capabilities.md) marks each published outcome `planned`, `experimental`, `supported` or `deprecated`; the README now links to that canonical inventory. (2026-11-09)
- [x] **Correct immediate credibility defects.** Make `gnomon --version` functional and test it through the CLI. (2026-11-09)

**Exit criterion.** The canonical Gnomon and Ekphrasis product and interface documents state the ratified contract without a conflicting capability statement.

## Phase 1 — Stabilize the Gnomon–Ekphrasis contract

Each action below names its accountable owner. The other project contributes through the ownership boundary where required.

Ekphrasis already provides schema-derived authoring and inspection. This plan uses that interface. Therefore, Gnomon adds no forms or presentation dashboard.

- [x] **Gnomon — Publish generated form contracts as the Gnomon-owned integration source.** The registry exports each record contract with its referenced base schema and every view schema. Contract tests require canonical field guidance, determinate interaction data, exact vocabulary bindings and resolvable logical and physical identities. The shared maturity vocabulary is bound by version 2 of each affected record contract, while version 1 remains readable. Conditional epistemic requirements remain in Gnomon findings. (2026-11-09)
- [x] **Ekphrasis — Close current contract drift and remove copied guidance.** Every editable Gnomon contract is loaded through the current registry and checked against its generated template. Synthetic fixtures retain generic schema constructs without copying Gnomon's field descriptions or examples. (2026-11-10)
- [x] **Ekphrasis — Complete schema-registry support required by the basic workflow.** Registry version 2 resources and absolute `$ref` entries resolve locally, Gnomon contracts compose through `allOf`, and changes to indexed schema files reopen dependent forms. A generated schema inside a hidden folder requires an Obsidian restart after its admitted closure changes. (2026-11-11)
- [ ] **Ekphrasis — Reload hidden generated schemas without restarting Obsidian.** Make Ekphrasis reload a changed registry closure explicitly. This post-basic task must preserve the exact-closure boundary and must not restore a configurable resource directory.
- [x] **Ekphrasis — Run Gnomon through a configured checker.** Ekphrasis selects a checker when the schema identifier matches its configured pattern. The checker runs the configured interpreter command and consumes Gnomon's machine-readable findings report. The bridge preserves the issue metadata, and its runtime source names no consumer. (2026-11-10)
- [x] **Gnomon — Standardize the issue transport.** YAML issues carry the source file, record identifier, field path, result class, rule, severity, explanation, repair condition and documentation target; missing guidance remains `null`. Static Analysis Results Interchange Format (SARIF) issues carry the required fields and include the optional guidance properties when authored. Existing YAML keys remain compatibility aliases. (2026-11-09)
- [x] **Gnomon — Author canonical repair guidance.** Every published rule receives a repair condition and a documentation target from its authoritative documentation. Catalogue loading rejects a missing or unknown guidance entry, and tests require every target to resolve. (2026-11-10)
- [x] **Ekphrasis — Test current Gnomon views through registry discovery.** The optional corpus test reads every exported view contract and generated view from the current Gnomon checkout, without copying them into Ekphrasis. (2026-11-10)
- [x] **Gnomon — Render the three multiword fields with their content kinds.** The exposure contract binds `reason` to `text`. The question-statements contract binds `authored` and `composed` to `markdown-line`. Gnomon now emits exposure `@4` and question-statements `@3`, while their predecessors remain immutable. Exposure `@4` also admits `commitment` when an itinerary decides or generates a product. Tests cover both current and retained contracts. (2026-11-10)
- [x] **Ekphrasis — Pass the corpus gate with the current Gnomon contracts.** Freshly generated views resolve and validate without schema issues. Their rendered forms contain no editable control, and scalar lists occupy compact cells. (2026-11-10)
- [x] **Ekphrasis — Implement the setup diagnostic.** The read-only command and settings button verify the registry and schema closure, the active record and its write permission, and the configured checker route. A live Gnomon run covered 56 contracts, 88 resources, 33 references and 252 data files. (2026-11-10)
- [x] **Ekphrasis — Finish the desktop setup-diagnostic protocol inside Obsidian.** The report distinguishes simultaneous registry and interpreter failures and advances to the missing package after the interpreter is repaired. A configured Gnomon checker produced a valid report in 6.1 seconds; its duration check compared that measurement with the timeout and recommended 12.3 seconds. Mobile verification is deferred outside the basic-version milestone. (2026-11-13)
- [x] **Ekphrasis — Implement the macOS and Linux process-tree stop.** A timeout, restart or forced close terminates the runner's process group, including the configured findings command and its descendants. Integration tests cover all three triggers and recovery on macOS. Pure tests cover the Linux plan. (2026-11-10)
- [ ] **Ekphrasis — Complete cross-platform process-tree verification.** Run the forced-stop integration on Linux. Handle a non-zero Windows `taskkill` exit through a tested fallback that lets `close()` finish, then run the integration on Windows.
- [ ] **Ekphrasis — Stop every process tree started by the setup probe.** Cover the outer TypeScript timeout and the embedded Python command timeout for both `runCommand` and `callChecker`. Await termination and test a descendant at each boundary.
- [ ] **Ekphrasis — Discard superseded queued checks.** Remove a queued checker call before it starts when newer source text has replaced the text that requested it.

**Exit criterion.** The corpus integration check opens every supported Gnomon record contract and view schema correctly in Ekphrasis. Every editable contract receives canonical field guidance. The check also demonstrates at least one field-level Gnomon finding at the correct Ekphrasis control. The desktop setup-diagnostic protocol passes inside Obsidian. Stopping or superseding a check leaves no command in its managed process tree running or queued.

## Phase 2 — Implement the two onboarding routes

Each action below names its accountable owner. The other project contributes through the ownership boundary where required.

### Greenfield route

- [x] **Gnomon — Create the workspace.** The command `gnomon init` creates only the folder, index, initial problem record and itinerary required from the first act. Additional YAML records remain available on demand through the option `--with`. (2026-11-10)
- [x] **Ekphrasis — Create later records on demand.** The command *Create instance* selects a writable contract from the configured registry, creates a non-overwriting skeleton bound by `_schema`, and opens its form. The read-only corpus test creates and opens a current Gnomon question without modifying Gnomon. The Obsidian interaction protocol passed on macOS in Obsidian 1.15.0. (2026-11-10)
- [x] **Ekphrasis — Exclude absent optional branches.** Required and present fields appear immediately. Other optional properties remain behind *+ Add a field*, which creates a source-free draft until its first edit. Synthetic tests, a read-only Gnomon corpus check and an Obsidian 1.15.0 protocol passed. (2026-11-10)
- [x] **Ekphrasis — Expose conditional fields from authored choices.** A current conditional rule or missing-field issue reveals its absent target and marks it required. Clearing the condition hides only an uncommitted target; an authored value remains visible. Gnomon locates same-record aim, commitment and selected-value requirements at their repair fields. A real explanatory-question finding, synthetic interaction tests and the Obsidian 1.15.0 protocol pass. (2026-11-10)
- [x] **Gnomon–Ekphrasis — Reveal first-stage conditional fields on the documented route.** Gnomon generates local `required-when` rules from its canonical aim-requirement registry into the question contract. Ekphrasis consumes those generic rules without a configured custom checker. In Obsidian 1.15.0, selecting `explanation` revealed `task.requested_relation`, marked it required and stated its condition; selecting `description` again removed the uncommitted field. (2026-11-11)
- [x] **Gnomon — Preserve a CLI fallback.** Researchers can add any additional generated template through the option `--with` and use the existing commands `gnomon validate` and `gnomon check`. (2026-11-10)
- [x] **Gnomon — Scaffold sparse authored records.** The default initializer projects identifying and first-stage required fields from the canonical template and requirement registry. The option `--full-template` preserves the complete commented source template. In Obsidian 1.15.0, the generated problem form showed only its nine working fields, while *+ Add a field* exposed the absent optional branches. (2026-11-11)
- [x] **Gnomon — Provision contracts into an arbitrary vault.** The command `gnomon setup` copies every packaged Gnomon and dependency schema into configurable vault-relative locations and writes an Ekphrasis registry that names only those copies. The command requires no Gnomon checkout in the vault, retains identical files and refuses changed targets unless replacement is explicit. The greenfield tutorial uses this portable route. (2026-11-11)
- [x] **Gnomon–Ekphrasis — Preserve the inquiry index after generic instance creation.** Gnomon publishes the idempotent command `gnomon register <record>`, which derives the stage, label and purpose from its canonical template index. Ekphrasis exposes an optional generic post-creation command with `{vault}`, `{path}` and `{schema}` placeholders; a failed command leaves the created record open, reports the cause and offers a retry that does not create the record again. Automated tests cover both boundaries, and the tutorial configures `["-m", "gnomon", "register", "{vault}/{path}"]`. In Obsidian 1.15.0, creating a current question record added its canonical entry under stage 2 of the existing inquiry index. A deliberately failed registration then recovered the same record and added exactly one entry after its command was corrected. (2026-11-11)

### Adoption route

- [x] **Gnomon — Begin from one active problem or question.** The option `gnomon init --start-with problem|question` creates an itinerary and only the selected sparse record. The adoption guide leaves the surrounding project unconverted. (2026-11-10)
- [x] **Gnomon — Record provenance before formalization.** The `sources` field of a problem or question records existing notes, publications, models and data as external pointers without copying or classifying their content. (2026-11-10)
- [x] **Gnomon — Promote only operationally required units.** Selected source content becomes a structured Gnomon unit only when Gnomon must inspect its fields or resolve its identifier for the active question or a chosen act. After the researcher applies this rule, the option `--with` adds the requested missing template without adding unrelated kinds; a law or content used as a ground enters its owning record instead. (2026-11-10)
- [x] **Gnomon — Require explicit classification.** The researcher classifies each selected source unit as a standalone record or a nested law before placement, then assigns any answer-ground role separately. Gnomon and Ekphrasis do not infer these decisions, and the CLI rejects `law` and `warrant` as record kinds. (2026-11-10)
- [x] **Gnomon — Preserve source relations.** The guide maps each of the eight supported kinds to a canonical pointer field. New non-empty source lists cover model and answer records. Existing source fields cover target systems, phenomena and laws. Other kinds remain external until the guide states where they belong and which field stores their source. No field distinguishes the route, so Gnomon cannot make `sources` mandatory only when the route starts from existing research. (2026-11-10)

Both routes use the same downstream checks and views after the active starting record is filled. No later checker or view may depend on the route that created the record.

**Exit criterion.** The greenfield route creates later records only on demand and retains the CLI fallback. The adoption route preserves source pointers and researcher-authored classifications. Both routes reach states that pass the same checks and produce the same downstream views.

## Phase 3 — Support partial work without normalizing invalid records

**Owner:** Gnomon defines the scopes and requirements; Ekphrasis presents their state.

- [x] **Define named validation scopes from the existing specification stages.** The ordered identifiers are `problem-posed`, `question-typed`, `subject-identified`, `subject-specified`, `candidate-proposed` and `candidate-assessed`. The first five correspond to the five specification stages; the last names the subsequent assessment endpoint. The requested scope is explicit rather than inferred from workspace contents. (2026-11-10) ^named-validation-scopes
- [x] **Declare the requirement set of each scope.** The requirement registry states the incremental records, paths, commitments and completion conditions added at each scope. It preserves aim-dependent, on-demand and candidate-dependent requirements, and it defines no generic `draft` status. (2026-11-10)
- [x] **Retain global integrity checks.** The scoped check context keeps contract, identifier and reference checks unconditional. Regression tests plant all three defects and require their findings at each named scope. (2026-11-10)
- [x] **Separate expected omissions from defects.** A field required only at a later scope appears as future work rather than a current failure. (2026-11-10)
- [x] **Display the active scope in Ekphrasis.** A scoped SARIF run publishes its completion target as non-issue run context. Ekphrasis displays that target above the validation findings without changing their counts. Synthetic tests, the current Gnomon corpus and the Obsidian 1.15.0 protocol pass. (2026-11-10)
- [x] **Allow resumption.** Reopening a record reconstructs its completion target, current findings and issue-only outline from the saved YAML and checker configuration. Ekphrasis stores no duplicate progress state. A fresh-session corpus test and the Obsidian 1.15.0 close-and-reopen protocol preserve the missing-field route without changing the YAML. (2026-11-10)

**Exit criterion.** A partially authored record has a defined completion target. Later-scope omissions do not appear as current findings. After reopening the record, its current omissions and their form routes are reconstructed.

## Phase 4 — Make findings operational

**Owner:** Gnomon publishes findings; Ekphrasis locates and presents them.

- [x] **Ekphrasis — Reach an identified collection entry at its exact field.** The locator combines the issue's pointer with its discriminator to resolve `laws[0].expression`. A click in the validation summary unfolds the containing groups and focuses that field. The corpus test plants an undeclared symbol in a model law and requires this route. (2026-11-10)
- [x] **Ekphrasis — Resolve the remaining issue paths.** A returned field path reaches its exact field. A pointer and discriminator reach a uniquely identified entry and consume every declared field component, including a component whose name also occurs as offending content. A duplicated identifier stays at the collection instead of selecting an arbitrary entry. A typed non-field locus or unmatched path stays in the root report. Focused domain and application regressions cover these boundaries. (2026-11-10)
- [x] **Group findings by their controlling decision.** Gnomon publishes the field whose authored value or presence activates each dependent finding. Ekphrasis groups those findings across issue marks, retains their field-level copies and routes both the controller and each repair target. Invalid controller metadata remains ungrouped. Synthetic tests, the current Gnomon corpus and an Obsidian 1.15.0 protocol pass. (2026-11-10)
- [x] **Order findings by dependency.** Ekphrasis presents controlling choices before their dependent findings. Within each controlling group and among the remaining findings, missing fields precede invalid values, including cross-record inconsistencies, and warnings come last. The order supplied by each checker remains stable within one class. An adversarial component test, the current Gnomon corpus and the Obsidian 1.15.0 protocol pass. (2026-11-10)
- [x] **Preserve the complete report.** Grouping adds a decision-oriented route without removing ordinary mark counts, field issues or unplaced independent findings. A component regression and the Obsidian protocol cover the combined report. (2026-11-10)
- [x] **Gnomon — Provide canonical explanations for CLI users.** The command `gnomon explain <rule-id>` prints the rule's level, meaning, repair condition and documentation target from Gnomon's canonical rule catalogue; `--list` exposes the known identifiers, and an unknown identifier fails without a traceback. (2026-11-10) ^finding-explanations
- [x] **Gnomon — Make every finding lead to its explanation.** The text outputs of `gnomon check` and `gnomon itinerary` share one formatter that prints the warning mark when applicable, the rule identifier and the unchanged finding message. A researcher can pass either command's identifier to `gnomon explain`. The itinerary text and SARIF-output routes have focused regressions, and the existing warning regression protects the check route. (2026-11-10)
- [ ] **Gnomon — Publish openable documentation targets.** Deferred while users consult the documentation on GitHub. A later implementation must open a catalogue target without assuming a repository checkout or an Obsidian-only block anchor.
- [x] **Ekphrasis — Show the details carried by each issue.** The field issue shows its message and rule identifier. The same issue also shows its result class, repair condition and documentation target from Gnomon's SARIF report. (2026-11-10)
- [ ] **Ekphrasis — Show the general rule.** Ask a Gnomon-owned interface for the rule text, then show it with the issue details. Do not copy Gnomon's rule catalogue into Ekphrasis.
- [x] **Distinguish issue states.** Gnomon marks each canonical `pending` verdict with the schema rule `unresolved-value`. Ekphrasis presents that valid authored value under *Research state*, apart from missing, invalid and warning findings, and routes it to its exact field. Synthetic tests, the current Gnomon corpus and an Obsidian 1.15.0 protocol pass. (2026-11-10)
- [x] **State the scope of a clean result.** A complete Gnomon run without an error or warning publishes non-issue context stating that the records satisfy the checked structural and method rules, but the check establishes no truth, warrant or acceptance. A stopped run cannot publish this claim. Ekphrasis displays the context even when the issue list is empty. Producer, adapter, component and current Gnomon-corpus regressions pass. (2026-11-10)

**Exit criterion.** A researcher can move from each finding to the responsible judgment, edit the correct field, and explain what the repaired check establishes and leaves undecided.

## Phase 5 — Improve next-act guidance without making research decisions

**Owner:** Gnomon.

- [x] **Retain every ready act.** Gnomon retains every registered activity mapped to an open condition, then marks it ready or waiting for an input. Readiness applies no preference filter. A regression compares every listed activity with the answerability registry while several ready and waiting activities coexist. (2026-11-10)
- [x] **Group acts by the open condition that they address.** The generated next-act view keeps each open condition with its complete acts table. Its schema renders the conditions as separate records through Ekphrasis's generic collection behavior. The earlier flat contract remains available as `gnomon:view.next-act@3`. (2026-11-11)
- [x] **Show deterministic ordering separately.** Each waiting activity appears under *Required predecessors* with the input types that an unimpeached record must hold before it can run. Available acts remain separate and unranked. Gnomon does not choose whether the researcher creates, repairs or replaces a record to satisfy the requirement. The combined `gnomon:view.next-act@4` contract remains available for existing generated views. (2026-11-11)
- [x] **State the operative consequence of each act.** Each available or waiting act names its condition, required inputs, output type, possible record or field, and waiting acts that may accept its output. The relation remains conditional on the norm passing and does not imply that the act will succeed. The earlier `gnomon:view.next-act@5` contract remains available for existing generated views. (2026-11-11)
- [x] **Let the researcher author comparison criteria.** The itinerary records each appraisal before an act becomes a step. The researcher declares each criterion, its ordered scale and preferred direction, then states each act's available means, value and basis. Gnomon validates the structure but supplies no judgment. Version 2 retains this appraisal contract for existing records. (2026-11-11)
- [x] **Compute only transparent comparisons.** The itinerary declares `ordinal-dominance` and gives every act a local identifier. The next-act view shows the rule, the supplied criteria and judgments, every pairwise relation and the undominated acts. Gnomon assigns no weights or values. The current itinerary contract is `gnomon:itinerary@3`, and the current next-act contract is `gnomon:view.next-act@7`. Their predecessors remain available. (2026-11-11) ^ready-act-comparison
- [x] **Label unresolved choices.** The view labels its section *Comparisons from supplied criteria*. One undominated act yields `determined`; several yield `unresolved`. The separate *Ready acts* table remains unranked. (2026-11-11)

**Exit criterion.** The researcher can use a bounded comparison to select the next act. The researcher remains responsible for every judgment unless supplied criteria and declared rules determine its result.

## Phase 6 — Deliver benefits through Ekphrasis views

**Owner:** Gnomon publishes view data and schemas; Ekphrasis renders them.

Gnomon adds no second presentation system. Until a canonical integration specification exists, this plan owns the Gnomon–Ekphrasis integration requirements. Those requirements derive from the tracked [view-schema index](src/gnomon/data/schemas/views/_index.md) and the [Ekphrasis handoff](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/handoff.md).

- [x] **Ekphrasis — Honor `readOnly: true`.** Ekphrasis reads `readOnly: true` from every schema layer applied by `allOf`. The read-only state locks that field and its descendants. The commit planner refuses an edit of any locked field, and generated views expose no editing control. (2026-11-10)
- [x] **Ekphrasis — Condense scalar lists in table cells.** Each scalar appears as one token, in file order. Read-only generated views offer no list control. (2026-11-10)
- [x] **Ekphrasis — Complete the remaining view-table constructs.** Read-only labels remain intact, LaTeX renders inline, and large tables retain their headings inside a keyboard-scrollable region. Synthetic and Gnomon corpus tests pass, and the 79-row expression view passed in Obsidian. (2026-11-11)
- [x] **Retire the question tree as the operational view.** The Obsidian trial showed that indentation cannot expose activities, typed edges or a long inquiry. The published contract `gnomon:view.question-tree@3` remains available only from the compatibility registry, and the command `gnomon tree` retains the textual hierarchy. (2026-11-11)
- [x] **Gnomon — Publish the operational inquiry graph.** The contract `gnomon:view.inquiry-graph@1` gives every product, activity instance and external source one canonical node. It identifies starting problems explicitly, names each status axis, gives each activity its registered family and type, and connects nodes through typed input, output and inquiry relations. Repeated sources and products remain single nodes. (2026-11-11) ^inquiry-graph
- [x] **Ekphrasis — Render the generic operational graph.** The field kind `graph` reads only schema-declared roles. The producer supplies category captions, shapes, markers, root captions, status axes and directed edge labels. The renderer supplies a topological canvas, zoom, scrolling, bounded relation focus and complete-route tracing. Synthetic tests and the current Gnomon view corpus pass. (2026-11-11)
- [x] **Verify the corrected operational graph in Obsidian.** The first desktop appraisal rejected the view: nominal titles hid the problem and question statements; activity cards repeated identifiers; activity-purpose edges competed with activity nodes; focus changes relocated surviving nodes; and card details lacked a compact form. The corrected producer emits natural-language product statements, verbal activity outcomes, direct input/output edges and node links. The corrected renderer preserves complete-graph positions, switches between compact and expanded cards, and traverses the declared starting problem before independent components. Successive research stages now run from top to bottom, so the problem, question, answer and assessment occupy one chronological column while parallel activities occupy neighboring columns. An implementation-level Obsidian protocol showed the starting problem and product route at readable zoom, with status at one fixed card location. The researcher accepted the basic rendering on 2026-11-11 and corrected its orientation on 2026-11-12. ^inquiry-graph-reappraisal
- [x] **Add a network mode for large inquiries.** Ekphrasis now computes a deterministic network over the complete typed graph. Dragging changes only the current view, and the layered route remains the default. The [Ekphrasis handoff](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/handoff.md) lists passing checks. Obsidian's native file graph remains complementary. A Gnomon activity can exist without a file, and native edges lack operational relation types. (2026-11-11)
- [x] **Appraise the network mode in Obsidian.** The complete 38-node graph did not expose a recognizable topology at 60% overview zoom: cards remained distinguishable, but edge labels and routes crossed too densely to trace. Switching layouts also discarded the selected starting problem. Ekphrasis now preserves the selected node and the 16-node focused route across layouts; *Show whole graph* explicitly adds the independent components. The corrected transition passed its component tests and an Obsidian check. The complete overview is now provided by the accepted map as typed points, short labels and directed unlabelled edges. (2026-11-13)
- [x] **Separate graph semantics from presentation defaults.** The [graph-presentation handoff](.agent-work/graph-presentation/HANDOFF.md) records the assessed configuration, manipulation and view-topology gaps. Gnomon declares category, node-kind and edge-kind defaults in a dedicated, validated registry, and each operational graph embeds one portable profile with safe icons, titles, styles, relation layers and layout compatibility. Ekphrasis consumes this profile through a generic presentation role and retains legacy values and renderer defaults as fallbacks. Problems, questions, answers and assessments keep a common product shape while receiving distinct semantic icons. Synthetic tests contain no Gnomon vocabulary, and the current profile passed corpus and Obsidian checks. (2026-11-12)
- [x] **Extend graph navigation.** Generic relation layers, individual edge kinds and node facets report visible and hidden nodes and edges, constrain route tracing, and preserve the selected node and stable coordinates across layouts. Values combine by OR within each facet or relation group and by AND across groups. Visible cards form one Tab stop; arrow keys prioritize incident relations, Home and End reach the reading-order boundaries, and a live region announces the traversed edge. Synthetic tests, the current Gnomon corpus and Obsidian checks pass without introducing Gnomon vocabulary in Ekphrasis. (2026-11-12)
- [x] **Register graph layout strategies.** Ekphrasis owns the trusted layout implementations and their structural requirements. A graph profile selects compatible identifiers, while a generic *Layout* selector admits any registered strategy that the graph can support. The layered chronology, card network and condensed map passed synthetic tests, the current Gnomon corpus and an Obsidian check. (2026-11-13)
- [x] **Determine whether a recorded output remains usable.** When the selected step names an output, the graph must give one of three answers. The state `sound` transmits no failed or unsettled norm to a consuming step. The state `conditional` keeps every consuming step conditional until all upstream norms leave `pending` or `inconclusive`. The state `impeached` forbids a consuming step from using the output until the failed route is repaired, replaced or bypassed. The three states report only whether a failed or unsettled norm reaches the output; truth and warrant remain undecided. The graph must show every displayed step-dependency path that enters or leaves the selected step. Each step appears once even when more than one path reaches the step. When the cause of a state lies outside the displayed steps, the graph must mark the state as external. The graph does not rank repairs. Researchers compare future acts in the next-act view and inspect products and activities in the operational inquiry graph. (2026-11-11) ^itinerary-graph-decision
- [x] **Gnomon — Publish the itinerary dependency graph data.** The itinerary-progress contract `@4` publishes every step dependency without imposing an acyclic order, while the retained contract `@3` preserves the tabular view. For a recorded output, the graph assigns one of three states: `sound`, `conditional` or `impeached`. The state `not-produced` marks an expected output without a record. The graph identifies every displayed origin and adds an explicit external origin when required. The complete graph preserves the authored topology, including multiple predecessors, independent steps and cycles. (2026-11-12) ^itinerary-graph-model
- [x] **Gnomon — Publish exposure reachability.** The exposure contract `@6` presents one answer-to-exposing-unit graph before the detailed findings table. The graph lets a researcher start from an answer or from a shared exposing unit. Each table row retains the unit kind, exact reason and recorded route. The graph collapses those rows by answer–unit pair and does not reconstruct the intermediate dependency walk. The retained contract `@5` preserves the table-only view. (2026-11-12) ^exposure-graph-model
- [x] **Gnomon — Publish assembly topology.** The assembly contract `@3` connects each level to its components and each component to its parts before the detailed tables. Each record appears once and retains every assembly role. Each component edge names its level. The tables retain citation provenance, counts and gaps. The tables also list limits and exclusions. In a complex Obsidian fixture, every citation obscured the component hierarchy. Ekphrasis cannot declare that layer hidden initially. The retained contract `@2` preserves the table-only view. (2026-11-13) ^assembly-graph-model
- [x] **Retain tables for next-act and vocabulary guidance.** The next-act view groups ready and waiting activities under the open condition that makes each choice relevant. Its `may_unblock` values state possible type compatibility, not an actual dependency. The current example contains 151 act occurrences, so one graph would obscure the decision context. The vocabulary view primarily supports collision-free symbol choice. Its directed target-system relations may contain joint or repeated source positions, which require an incidence or hypergraph presentation rather than the operational research graph. The existing tables preserve these distinctions without misclassifying target-system relations as research activities. (2026-11-13)
- [x] **Ekphrasis — Override graph presentation locally.** Ekphrasis reads a profile-and-version-keyed list from vault-local plugin data. The list may replace safe titles, icons, markers and style tokens without changing generated views. It may also register missing visual recipes and narrow compatible layouts. Producer-owned node categories, relation layers and layout bounds remain unchanged because they encode semantics. The settings editor reports invalid units before saving, and damaged stored data falls back safely. Automated checks and the live setting, persistence, refresh, diagnostic and visible-fallback route pass. (2026-11-13)
- [x] **Ekphrasis — Render a generic directed graph.** The schema declares every graph role. Selection first isolates the incident relations and can expand to every displayed route that enters or leaves the node. The producer defines each node, visual semantic marker and status axis, and it declares the endpoints and label of each edge. (2026-11-11) ^generic-graph-renderer
- [x] **Define the primary view for each research stage.** The six named completion targets select `problem-state`, `next-act` or `exposure` according to the research task that becomes operative at that stage. Other generated views remain available without displacing that primary route. (2026-11-11)
- [x] **Gnomon — Publish view source state.** All ten generated view contracts require a deterministic `source_state` digest of their canonical authored records. The contracts advance one version, and their predecessors remain exported for existing artifacts. (2026-11-09)
- [x] **Gnomon — Preserve safe-YAML values in source-state hashing.** Encode every safe-YAML value with a deterministic type tag, so dates, binary values, sets and non-finite numbers remain distinct and an invalid record receives its contract finding instead of terminating `gnomon check` during digest generation. (2026-11-09)
- [x] **Ekphrasis — Determine view freshness.** The generic instance checker `ekphrasis_commands.source_state` runs a configured producer command. It compares the command's one-line result with the generated file's value at a configured RFC 6901 pointer. Equal values display *Source state: current*. Differing values warn at `source_state` and require the researcher to regenerate the view. Ekphrasis neither chooses Gnomon records nor serializes them. Synthetic form tests pass, the checker recognized all nine current Gnomon views, and the current and stale presentations passed in Obsidian. (2026-11-11)
- [x] **Gnomon — Select one primary view after every stage.** The explicit `--scope` option writes only the view that supports the research task associated with that completion target and states why the researcher should open it. Gnomon does not infer or assert that the inquiry has reached the selected completion target. (2026-11-11)
- [x] **Gnomon — State the coverage of an incomplete selected view.** The selected view lists the started authored records read by Gnomon. The second table lists the absent record kinds due after the selected target, in inquiry order, with their expected files. The scoped checker computes those rows from the validation-scope registry. (2026-11-11)
- [x] **Ekphrasis — Open the primary view selected by Gnomon.** A researcher supplies the explicit completion target. Ekphrasis invokes a configured command and opens the generated YAML path returned in its JSON result. Gnomon owns the target-to-view route, and Ekphrasis contains no copy of that mapping. Automated producer-boundary tests pass. (2026-11-11)
- [x] **Verify primary-view opening in Obsidian.** The Ekphrasis protocol opened `exposure.yml` for `candidate-proposed`, opened `next-act.yml` for `question-typed`, and refused a producer path outside the vault while keeping the current view open. (2026-11-11)
- [x] **Retain the generated YAML view as the sole data source.** Ekphrasis keeps the completion target only in the open modal. After the producer returns, the generated YAML file supplies the form state and the target is not stored as view state. (2026-11-11)

**Exit criterion.** After each inquiry stage, the researcher can inspect a current read-only view. The view reveals a relation, open condition or revision consequence not apparent from one record alone.

## Phase 7 — Protect accumulated research

**Owner:** Gnomon owns contracts and migrations; Ekphrasis enforces the presentation boundary.

- [x] **Make `gnomon init --force` recoverable.** The command supports a write-free dry run, enumerates affected files, requires confirmation and preserves exact prior bytes under `.gnomon-backup` without overwriting an existing backup. (2026-11-09)
- [x] **Define contract compatibility.** A validation or rendering change advances the logical contract version. Published predecessors remain exported until an accepted retirement decision establishes regeneration or migration and downstream compatibility. (2026-11-09)
- [x] **Add `gnomon migrate --check`.** The command reports binding-only diffs, fields that fail the current contract and unreadable files. The preview returns a nonzero status when work remains and writes no file. (2026-11-11)
- [x] **Review records before migrating them.** Apply mode displays the complete diff and refuses a batch with blockers. The researcher must approve a clean plan. Then, the command preserves exact source bytes in a versioned recovery path before changing any record. (2026-11-12) ^record-migration
- [x] **Distinguish generated and authored files in both products.** Canonical templates remain package resources, while `gnomon init` places editable copies inside the inquiry. Setup copies contracts only into the configured resource directory. Every generated view contract declares `readOnly: true`, so Ekphrasis locks the view. Every authored record contract remains editable. A boundary test checks every provisioned contract. (2026-11-12)
- [x] **Ekphrasis — State capabilities on desktop and mobile.** Forms and built-in checks operate on mobile. Python custom checkers require desktop. When the interpreter is missing, Ekphrasis tells the researcher which setting to fill. (2026-11-10)

**Exit criterion.** Scaffolding and upgrades cannot silently overwrite authored research. Every incompatible contract change has a visible migration route.

## Phase 8 — Publish one end-to-end user journey ^integrated-greenfield-tutorial

Each action below names its accountable owner. The other project contributes instructions for its product where required.

- [x] **Gnomon — Write one greenfield tutorial across both products.** The portable-vault tutorial installs the schema closure, begins with workspace creation, configures and diagnoses Ekphrasis, fills records through its forms, runs Gnomon checks and reads the primary views at four completion targets. (2026-11-11)
- [x] **Gnomon — Write one adoption tutorial.** The [question-led tutorial](docs/guide/adopting-existing-research.md) preserves the surrounding project, checks the question at `question-typed`, promotes only the target and phenomenon selected from the first view, and reaches the choice of abduction at `subject-identified`. (2026-11-11)
- [x] **Gnomon — Keep definitions canonical.** The greenfield and completed-inquiry tutorials link reusable meanings to Gnomon's specification and epistemology. The [external-research promotion procedure](docs/procedures/inquiry/promoting-external-research.md) now owns selective promotion, source-unit classification, record placement and source-pointer destinations, while the adoption tutorial retains only the worked application. (2026-11-11)
- [x] **Gnomon — Generate contextual guidance from schemas.** Base schemas describe each field and provide examples. Vocabulary registries define the admitted values. Generated contracts use the field-index map to link each documented field to its defining canonical GitHub note. (2026-11-11)
- [ ] **Gnomon — Publish the documentation site after the integrated workflow stabilizes.**
- [x] **Gnomon–Ekphrasis — Run the integrated recovery walkthrough.** The desktop protocols cover invalid YAML, recoverable registry and schema-closure failures, an unavailable configured Python runtime, a stale primary view and failed post-creation registration. Each case preserved authored records, named the failed capability, stated one repair step and resumed after repair. (2026-11-11)
- [x] **Gnomon — Add integrated recovery procedures.** The [recovery guide](docs/guide/recovery.md) preserves authored records when five verified desktop failures stop the workflow. This outcome remains experimental because conflicting generated targets, mobile Python commands and missing custom-checker packages are outside the verified procedures. (2026-11-11) ^integrated-recovery
- [x] **Gnomon — Add migration recovery.** The recovery procedure preserves every current source outside the inquiry before restoring the exact backup bytes. After a failed apply, the procedure restores every recovery pair because an incomplete write may alter a source before Gnomon reports it as migrated. The command `gnomon validate` reads the restored contracts. The write-free preview reports each restored source and writes no file. Tests cover successful and partial recovery. (2026-11-12)
- [ ] **Ekphrasis — Add accessibility acceptance tests.** Test keyboard operation, screen-reader labels, issue association, colour independence, focus movement and rendered mathematics.

**Exit criterion.** A researcher can complete either onboarding route from one guide. The guide organizes its instructions by researcher task, so the researcher need not reconstruct the workflow from architecture notes.

## Phase 9 — Validate usability and research benefit

**Owner:** Gnomon product evaluation, using the integrated Gnomon–Ekphrasis workflow.

### Baseline study

- [x] Prepare a baseline session protocol with separate fields for every determinant in the session record. The measured ranges from the first participants, not the protocol, will set the acceptance thresholds. (2026-11-11)
- [ ] Observe representative domain researchers using the current combined workflow.
- [ ] Record a case whenever a participant consults external documentation, misclassifies a field, misreads output or asks the facilitator for help.
- [ ] Set quantitative acceptance thresholds only after the baseline measures realistic ranges.

Eligible participants are domain-competent researchers who have not used Gnomon. Each participant brings one current problem or question. New research must follow the greenfield route. Active research must follow the adoption route. Therefore, participants need not reconstruct work merely to exercise another route. The facilitator must supply installed current builds of Gnomon, Ekphrasis and Obsidian but must not configure the test vault. The participant may browse the GitHub documentation.

Before participating, the researcher approves the research content that may enter the test vault. The researcher separately permits or refuses screen and audio capture. The observer assigns a study code and records no excluded research content.

The participant performs five tasks without semantic help from the facilitator:

1. Find the applicable onboarding route and obtain a passing setup diagnosis.
2. Create or adopt an inquiry and complete its first declared validation scope.
3. Interpret one reported issue, locate its field and repair the record. When the authored record produces no issue, the facilitator preserves the current identifier and replaces it with `not an identifier`. The participant runs the same check. After the task, the facilitator restores the preserved value, and the observer marks the issue as a supplied fixture.
4. Identify the acts available now, select one and create the record required by that act.
5. Open the primary operational view and state one dependency shown in the view.

For each task, the observer records:

- the elapsed time;
- the outcome as *independent*, *assisted* or *not completed*;
- each documentation page consulted and its purpose;
- each field choice or output explanation that conflicts with the canonical documentation;
- each software failure; and
- each action by the facilitator, using one of these classes:
  - repeated task statement;
  - navigation cue;
  - procedural instruction;
  - conceptual explanation; or
  - interface operation.

Across all five tasks, the observer records the benefit stated by the participant. The observer also records the added authoring or maintenance effort. Finally, the participant compares Gnomon with the method already used for the research.

After each task, the observer checks the participant's field choices and output explanations against the canonical Gnomon documentation. The observer attributes a software failure to the software rather than to the participant's concepts. The observer also records every help request. A request remains in the record when the facilitator responds only by repeating the task. The study aggregates measured ranges and concrete failure classes. However, the study assigns no pass or fail verdict to an individual participant.

### Formative tests

- [x] Evaluate setup, first-stage completion, field guidance and recovery from invalid values on both entry routes. Both forms saved their complete first-stage records, displayed valid identifier examples, located malformed identifiers and removed their issues immediately after repair. The adoption form represented unresolved subject slots as typed placeholders and added an external source as a pointer. Independent validation and the corresponding scoped checks passed with no findings. Aim-dependent fields now appear directly from the generated question contract. (2026-11-11)
- [ ] Evaluate the interpretation of conformance, selection of a next act, and retrieval of a dependency or revision consequence.

### Longitudinal evaluation

- [ ] Compare Gnomon-assisted work with the researcher's previous method on retrieval, defect detection, side-question control and revision impact.
- [ ] Compare the traceability of answers and the authoring and maintenance costs of both methods.
- [ ] Ask independent domain reviewers to judge research quality. Gnomon completion and checker success must not serve as proxies for scientific validity.

**Exit criterion.** For a declared target persona and inquiry class, the integrated workflow demonstrates a benefit that exceeds its authoring and maintenance cost.

## Dependencies

```text
Product contract
    ↓
Cross-repository schema and checker integration
    ↓
Greenfield and adoption workflows
    ↓
Partial-stage validation and operational findings
    ↓
Next-act comparison
    ↓
Rendered and freshness-aware views
    ↓
Migration safety and end-to-end documentation
    ↓
Longitudinal benefit evaluation
```

The cross-project contract and the greenfield workflow have the highest implementation priority. Adoption of existing research remains a coequal entry route, not the justification for the product.

## Active constraints

- Gnomon owns the semantics of research records, their schemas, the checks across them, computed diagnoses and generated view data.
- Ekphrasis owns schema-derived forms, source-preserving field interaction, issue presentation and rendering of generated views.
- Greenfield and adoption workflows must converge on the same records and checks.
- Every scientific or epistemic classification remains an authored judgment.
- A computation is admitted only when authored values and a declared rule determine its result.
- YAML records and generated YAML views remain the single sources consumed by both products.
- Guidance must derive from canonical schemas, registries, specification notes and theory notes rather than duplicated cross-repository prose.

## Open questions

- Which authored criteria are sufficient for a useful comparison of ready acts without creating an implicit recommendation?
- Which inquiry classes and researcher profiles should enter the baseline and longitudinal studies?

## Provenance

- The usability assessment tested `gnomon --help`, `init`, `check`, `status`, `tree`, a partial problem record and a completed worked inquiry on 2026-11-09.
- The adversarial review challenged the original recommendations and identified omitted concerns: partial drafts, issue navigation, compatibility, overwrite safety, installation diagnosis and accessibility.
- Parallel implementation agents repaired the version option, standardized issue transport and made forced scaffolding recoverable. An independent compatibility review classified the source-state field as an incompatible change to ten view contracts and required retention of their predecessors.
- The user corrected two premises: Gnomon must serve greenfield projects as well as existing projects, and Ekphrasis supplies its forms and views.
- The [Gnomon README](README.md) governs the product's scope and links to its current capability inventory.
- The [guide to filling inquiry records](docs/guide/filling-records.md) governs the current authoring workflow.
- The [procedure for choosing the next act](docs/procedures/inquiry/next-act.md) governs computed readiness and researcher judgment.
- The [Ekphrasis overview](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/overview.md) governs schema-derived forms, source-preserving edits and field-level validation.
- The [Ekphrasis form specification](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/features/form-view.md) governs progressive display, instructions, issue navigation and read-only presentation requirements.
- The [Ekphrasis project handoff](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/handoff.md) records the current implementation state and known drift from Gnomon.
- The tracked [view-schema index](src/gnomon/data/schemas/views/_index.md) records the purpose and contract of each generated view.
- The [capability-status guide](docs/guide/capabilities.md) governs whether a researcher can rely on, trial or await each published outcome.

## Decision log

- **Two entry routes.** Greenfield and adoption workflows are both required. Neither route determines the shared record model.
- **One owner per responsibility.** Gnomon owns semantic content and computed data; Ekphrasis owns forms and view presentation.
- **Minimal greenfield workspace target.** The initializer creates the folder, index, problem record and itinerary. Then, Ekphrasis creates additional records on demand. The command `gnomon init --with <record-kind>` retains the YAML fallback for adding those records.
- **Minimal initialization intentionally changes the pre-alpha default.** The previous default created seven templates. The current default creates only the problem and itinerary templates; existing scripts that require the former set must name the remaining kinds with repeated `--with` options. The published Python constant `CORE_KINDS` follows the current default.
- **First benefit checkpoints.** After the problem is posed, the problem-state view exposes its demand and obstacles. After the question is typed, the question diagnosis exposes its open conditions and ready acts.
- **No automatic research recommendation.** The software may compare ready acts only from authored criteria and declared rules.
- **Named partial scopes.** Intermediate work is checked against explicit stage requirements rather than an undefined draft state.
- **Views expose value.** Gnomon publishes generated YAML views, and Ekphrasis renders them without maintaining another source.
- **View freshness is content-addressed.** Each generated view identifies the complete canonical authored-record mapping through a SHA-256 digest; unchanged mappings retain the digest and a changed authored value replaces it.
- **Published contracts require explicit retirement.** Gnomon retains earlier logical contracts until a separate accepted decision establishes migration or regeneration and downstream compatibility.
- **Issue guidance remains authored.** The issue transport carries explicit guidance fields, but only the owning specification or procedure may supply their content.
- **Capability status has one owner.** The capability guide owns the current label and boundary of each published outcome; the README links to that inventory instead of maintaining a second checklist.
- **Forced scaffolding preserves prior bytes.** A forced initialization writes deterministic backups before replacing any target and refuses to overwrite an existing backup.
- **Evaluation separates usability from scientific validity.** Form completion and clean checks measure interaction and conformance, never research quality.
