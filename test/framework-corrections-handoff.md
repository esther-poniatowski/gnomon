---
tags:
  - handoff
index: "[Theoretical modeling tests](test/_index.md)"
aliases:
  - Framework correction handoff
---
# Handoff — framework corrections

The inquiry records form a small modeling language: each declared quantity carries a symbol, and every formula is an expression over those symbols. Two ratified stages brought the records there, and both are complete across the seven filled problems. The [expression language](../docs/epistemology/symbols-and-expressions.md) owns their contract. ^stages

> [!TIP] Next action
> Repair the answer and assessment templates, closing the [validation and representation gaps](answer-assessment-template-issues.md) that the six trials exposed.

## Task state

Seven theoretical inquiries each fill the three inquiry records, and six of them also carry a candidate answer and its assessment. `git log` holds the stages that brought the records there. Each proposed change rests on the [diagnosis of reported problems](framework-issues-synthesis.md).

| State | Stage | Action | Approval gate |
| --- | --- | --- | --- |
| `pending` | **Answer and assessment templates** | Repair the validation and representation gaps that the six trials exposed. | Every gap is closed, or the designer declines it on the record. |
| `pending` | **Remaining candidates** | Review the candidates that the classification record still holds as pending. | Each carries one review state and one owner. |

## Classification record

Each candidate carries one review state, assigned by the designer. The candidates already absorbed, approved or rejected are settled, and `git log` holds them. Only the candidates still awaiting review remain here.

| Candidate | Owner | Review state | Disposition |
| --- | --- | --- | --- |
| Scoped virtues | Shared schema | `pending` | Reduced: a virtue can now name a symbol and a scope entry, both declared. |
| Provenance | Shared schema | `pending` | Not addressed. |
| Domain moved beside the selection criteria | Shared schema | `pending` | Proposed: the domain restricts the same specification that the criteria select on, so both belong to the target. |
| Contrast moved into the phenomenon | Shared schema | `pending` | Proposed: the foils are values of an explanandum variable that the phenomenon declares. |
| Option cells of the notes checked against the registry | Shared schema | `pending` | Still blocked: a note cell carries a gloss and the template writes a token, so `class of actual systems` and `class-actual` compare only once the note cells carry both. |
| The five choices local to the cases | Local case | `pending` | Unchanged. Each requires a decision from the designer. |

## Active constraints

- The designer controls each approval gate. Prepare a proposal and a targeted diff, but do not begin an unreviewed stage.
- Unknown scientific conclusions remain `open`. A protocol choice not yet made stays pending and never becomes `open`.
- Every stage changes its semantic source together with all dependent implementation and verification artifacts.
- The worktree contains unrelated changes under `.obsidian/` and `docs/methods-taxonomies/`. Do not modify or discard those changes.
- Changes under `docs/design/` require an explicit dependency and designer approval.
- No new package may be installed without approval. The documented `gnomon` conda environment is absent, so the read-only checks to date ran in `dev`.

## Open questions

| Decision | Why it matters | Blocked stage |
| --- | --- | --- |
| Which of the remaining candidates are approved? | The review states define the authorized scope. | Remaining candidates |
| Which concrete values resolve the five choices local to the cases? | Without those values, a fixture cannot distinguish an author choice from a scientific unknown. | Local repair |
| Does `scope_over_instances` nest inside each manifestation? | `scope_over_instances` qualifies a claim, and in the current schema a manifestation is the unit of assertion. The case on delayed generalization now forces the question. In that case, the ordering holds for every run, whereas the delay is an ensemble claim over initialization draws. One scope for the whole record therefore cannot qualify both claims. A gloss holds the distinction until the nesting is ratified. | Phenomenon schema |
| Should the expression grammar be enforced by a parser? | The current check is lexical: it resolves identifiers without parsing binders. Signatures are therefore declared by authors and not derived. | Stage B completion |
| Which schema technology is authorized? | The repository declares a schema directory but has no validator for inquiry records. | Provenance and validation |

## Provenance

- The owner of each contract, and the checks that a change must pass, are stated in the [contribution guidelines](../CONTRIBUTING.md).
- The [diagnosis of reported problems](framework-issues-synthesis.md) warrants each proposed change, and the case logs support that diagnosis.
- The six answer and assessment trials exposed [validation and representation gaps](answer-assessment-template-issues.md).
- The [architecture decisions](../docs/adr/_index.md) record what later work must respect, and the decision log holds the choices local to one stage.

## Decision log

Decisions that later work must respect are recorded apart, in the [architecture decisions](../docs/adr/_index.md). This log holds the remaining choices, each local to one stage of this work.

| Date | Decision | Rationale |
| --- | --- | --- |
| 2026-09-21 | Keep local author choices separate from unresolved scientific results. | Only scientific results warrant `open`. |
| 2026-09-22 | Reorient the records toward a modeling language, through the two [ratified stages](#^stages). | The records already depended on references, yet those links were unreliable, because a prose name carried a symbol, a gloss, a signature and sometimes a definition at once. |
| 2026-09-22 | Fold symbols into the fixture migration. | Symbols added after the migration would have required a further pass over every record. |
| 2026-09-22 | Split the operator vocabulary by writer, per the [division by author and reach](../docs/adr/registries-as-source.md). | Of 26 operators in the canonical set, four were used by three or more problems and eight by none, since the set had grown one case at a time. |
| 2026-09-22 | Name a law's third role `constraint` rather than `coexistence`. | The records already labelled those laws an incompressibility constraint and an invariance of the state space, so the working term matched that usage. |
| 2026-09-23 | Keep the infix surface and define it over an S-expression core, per the [syntax decision](../docs/adr/expression-syntax.md). | A parser becomes available while records keep their current surface, and an operator stays a declared symbol, never a reserved word. |
| 2026-09-23 | Write a LaTeX form in single quotes. | A serializer reads the backslash of `\nu` inside double quotes as an escape, so the form arrives as a newline and a letter. The defect is of the same class as the symbol that a serializer read as a boolean. |
| 2026-09-23 | Write a deliberately invalid value as `no-such-role`, a string that no single edit turns into an admitted token. | A string close to an admitted value reads as a typo awaiting correction. Once corrected, such a string leaves the check unable to fail. |
| 2026-09-22 | Treat `status` as one concept whose states vary with the record kind, not as a generic slot. | Where `kind` named seven unrelated distinctions, `status` names the lifecycle of a record everywhere it appears. Only the admissible states depend on the content of the record. |
| 2026-09-22 | Admit a gloss beside an expression, bounded by the rule that it carries no commitment. | The language became formal enough that a reader must reconstruct a condition such as `d_t(N) = 0`. A gloss in words costs less than that reconstruction or a guess. |
| 2026-09-22, revised 2026-09-24 | Keep the constraints of an external system in its entry, outside the laws, and give each one the form of a law. | Two of the three reasons for keeping the constraints bare have expired. `granularity` is retired, and a role applies: of the three constraints written, two are `state-constraint` and one is an admissibility. The third reason, the object that a claim governs, was contestable from the start, and a constraint ranges over places as a law does. The constraints nevertheless stay with the external systems, because their block exists to state the boundary and no law of the target concerns an external system. |
| 2026-09-22 | Declare a variable set outside the system that varies during the dynamics as exogenous. | The rule that an interface variable is a state variable or a parameter forced a false choice. A driving force, a prescribed trajectory and a noise process are determined outside the system, yet none is held fixed. |
| 2026-09-22 | Type operators with `signature` and `values` rather than `takes` and `gives`. | A quantity indexed by a set and an operator taking an argument in that set have the same shape. Moreover, quantities and the method notes already relied on the two keywords. |
| 2026-09-22 | Move the overparameterization restriction from the question's domain to the selection criteria of the reference class. | Membership depends on a joint property of the architecture and the sample that no other specification fixes. A selection criterion records exactly such a property. Moreover, all five problems had left the field empty, while one of them carried its criterion as prose elsewhere. |
| 2026-09-23 | Open every entry with its name and its statement, before its symbol and its notation. | A reader identifies an entry by its name, and the symbol serves afterwards as the handle for the checker and for other expressions. |
| 2026-09-23 | Remove a definition that restates a law that the same record states. | A law can be false of the system and a definition cannot, so one formula carried under both hid which commitment the record makes. |
| 2026-09-23 | Divide the three identifiers of an entry. The name labels the entry, formulas use the symbol as a handle, and the gloss states the content that neither of them carries. | A gloss that paraphrases its name reads as content and states nothing, so it survives review while the entry stays unexplained. |
| 2026-09-23 | Collect the operators of a problem in one file, read against all its records. | An operator was typed over sets declared in the target and used in the phenomenon, so neither record could both own it and hold every set that its type names. |
| 2026-09-23 | Carry the reason for a requirement in a gloss beside it, and no longer in the case description. | Each restriction states the cases that it excludes. No field stated the reason, so a later reader could not tell a scientific commitment from an arbitrary narrowing. |
| 2026-09-23 | Retire `task.level.aggregation` without a replacement. | Every proposed replacement carried a presupposition that the level must not make: that an explanans uses aggregates, and that each of them relates a single variable to another. A satisfaction test already checks the admissibility of an aggregate. The [declaration of the aggregate](../docs/epistemology/target-system.md#^aggregate-admissibility) carries the commitment. |
| 2026-09-23 | Let a requirement path traverse a list, where it formerly read a block of tokens. | A field whose entries carry a reason is a list of mappings. An aim that requires a value in every entry therefore needs a path that traverses the list. |
| 2026-09-23 | Write a modulating condition as a relation over declared symbols, no longer as a direction in words. | `increasing` and `decreasing` were already canonical, since a manifestation may take the form of a dependence. The direction of a modulation therefore needed no vocabulary of its own. |
| 2026-09-23 | Admit no `open` in an external constraint, and mark a genuine unknown with `maturity` instead. | The value `open` carried two meanings that a reader cannot tell apart. One of the two meanings silently hides the quantities that a constraint would have named. |
| 2026-09-23 | Require every carrier of an interaction to be indexed by both its endpoints. | With this requirement, the record reads as a graph. A quantity indexed by the source alone is excluded, because it states a property of that endpoint and carries no influence on another part. |
| 2026-09-23 | Generate the interaction graph over kinds, not over members. | The ordered pairs that are joined are fixed by a parameter of a member model. A target record leaves that parameter unvalued, so it states where to read the edges and lists no edge. |
| 2026-09-23 | Keep at the root a quantity that every member has, and let the laws differ. | A growth law renamed per variant broke the microbial phenomenon that takes its Jacobian. Every member has a growth law, and these laws differ only in their arguments. The law itself states those arguments. |
| 2026-09-23 | Return the overparameterization restriction to the question, reversing the move of 2026-09-22. | The domain had held one parameter to a set, a form that no joint proposition fits, and that limitation forced the earlier move. The domain now carries a joint restriction, so the constraint sits with the inquiry that imposes it and another question may be put below the same line. |
| 2026-09-23 | Read the endpoints of an influence from the order of its pairs. | Separate names for the endpoints restated `applies_to` on one side and the pair order on the other. For an influence between two parts of one kind, the pair of names carried no information. |
| 2026-09-23 | Rebuild a vocabulary from the assertions of the records, not from the needs of the first cases. | `constraint` had absorbed three fifths of the laws, as `distribution-statistics` had the aggregations. A value that draws no distinction hides the claims of the entries that it labels. |
| 2026-09-23 | Admit an influence of more than two places. | A binary product presupposed that every influence has one source. The phenomenon records were corrected for exactly that fixed arity: a higher-order term has an effect that neither of its two sources carries alone. |
| 2026-09-23 | Read which members carry a symbol from the target, in the phenomenon as in the laws. | A phenomenon declares no variant of its own. The rule that an unmarked claim must be readable by every member that it ranges over therefore needs a fact held one record upstream, in the target. |
| 2026-09-23 | Let a maturity marker license a gap that a check would otherwise report. | The marker had no consumer, so a record could admit a gap and no check would read the admission. A check that consults the marker distinguishes an omission from a decision. |
| 2026-09-23 | Give an operator type variables before elevating any. | An operator typed at its one call site carries that site into every inheriting record. An elevated adjoint would thus have imported the state space of one problem into all those records. |
| 2026-09-23 | Replace `pow` with a vector constructor, and keep no second spelling for the same shape. | Every use of `pow` in the corpus was a vector, so keeping both would have left two spellings for one shape. |
| 2026-09-23 | Name the derivative `diff` rather than `d`. | Operators and quantities share one namespace, and two problems declare `d` as a dimension. A canonical `d` would therefore leave `d(u, t)` ambiguous to a reader and to the parser that the syntax decision anticipates. |
| 2026-09-23 | Name a field after the distinction that it decides. Within one record, give no two fields the same name. | `level` suggested a position in a hierarchy while bounding a vocabulary, and a reader of the registry could not tell which of the two fields its key named. |
| 2026-09-24 | Let an explanans appeal to an external system, and not to one of its quantities. | An owned quantity is already reachable as a term under its own symbol, so admitting both would write one appeal two ways. |
| 2026-09-24 | Refine a constraint by the vocabulary that laws *already* use. | The three constraints written fall inside the roles rebuilt from the 29 laws, so a second vocabulary would have named the same distinctions twice. |
| 2026-09-24 | Give a law of the target the warrant that its counterpart in the answer layer already carried. | Every law of a target is admitted, but not on equal grounds. A law derived from other laws stands or falls with its premises. A law posited, fitted or measured rests on a choice, a fit or an instrument, and new evidence revises it first. Every result resting on such a law inherits that exposure, up to the answer. The laws on which a result depends can therefore be read only once each law states why it is admitted. Of the 30 laws written, 26 are posited by the model class, 3 are derived and 1 is measured. |
| 2026-09-24 | Declare the answer's model with the target's blocks, not with a vocabulary of its own. | A candidate answer proposes a model of the target system. A separate vocabulary for that model drew its own distinctions. Those distinctions duplicated the divisions that the value sets already drew. |
| 2026-09-24 | Make the organization one block, not a key on each law. | In the literature on mechanisms, organization is a family of typed relations over components and activities. A key on a law can carry only the single relation that its law states. One block holds the family, and a relation realized by several laws takes one entry. |
| 2026-09-24 | Name the block `organization` and its key `relates`, retiring `influence`. | `influence` named the causal reading of one relation. The block holds relations that need not be causal: adjacency and sameness are organizational, and neither influences another part. |
| 2026-09-24 | Split the prose field by the job that it does, since renaming one key does not suffice. | The word `gloss` suggested a superficial remark, yet the field holds mandatory content. No single word covered its five jobs. For example, of all prose values, 108 render an expression in words, whereas another 35 sit beside no formal field and therefore have no expression to translate. |
| 2026-09-24 | Keep the vocabulary of factors, and let each bear on several elements. | The earlier reading that the vocabulary restates `bears_on` was mistaken. A `law-property` is a property of a law, such as invariance, additivity or factorization. No record names a law property before an answer uncovers one. Each kind names the object that carries the factor, and a property of a family bears on each of its members. |
| 2026-09-24 | Check the warrant that a law claims, beyond recording it in a field. | The decision that a warrant propagates to every result resting on it has no force unless a check confirms that each law marked derived follows from its premises. Without that check, the field would record only an intention. |
| 2026-09-25 | Rename the opaque option values and the reference keys of an assessment. | Each value now names what it selects: `class-actual` and `class-possible` became `actual-systems` and `possible-systems`, `parameter-draw` and `structure-draw` became `random-parameters` and `random-structure`, `link` became `mapping`, and `function` became `functional`, the only noun among the adjectives of the requested relation. The keys `assesses` and `against` became `answer` and `question`, like the reference keys of the other records. |

## Synchronization debt

- `realizations` remains unexercised. The candidate answer on grokking, by contrast, now uses `among`, but that use is unchecked, because the validation pipeline excludes answer records.
- `preferred` is now exercised by the grokking question and assessment. The candidate fails the filtering tiers, and that failure exposes a missing structured state: appraisal withheld, as distinct from a ranked answer supplied.
- A constitutive virtue is settled by the product test and a preferred virtue by appraisal, each exactly once. Filled assessments exercise this rule, and no check enforces it yet.

- The signature of a derived observable is declared, not computed. Until a parser derives it, a record can declare a signature that its definition contradicts. The resolution test checks references and leaves arity unchecked.
- The canonical operator set is closed by no grammar. The [operator groups](../docs/epistemology/symbols-and-expressions.md#^operator-groups) list the set, and a problem needing more operators declares them in its own `operators.yml`.
- The package is not installed in any environment, so the test suite reaches it through `pythonpath` and the command through `PYTHONPATH=src`. An installed `gnomon vocabulary` script requires an authorized project environment.
- The Markdown view of a vocabulary is built, but the view of a filled inquiry record is not, and neither typesets an expression as LaTeX. The inputs of both views, however, exist: the records carry the syntax already, and the registry and the `operators.yml` of each problem already hold the notation that the renderer needs for each operator.
- Of the six constraints written for external systems, half are expressions. Each of the other three is empty, with an adjacent statement of why the system imposes no constraint. For the measurement system, coverage and uncertainty bear on the detection criterion and not on the target, so no record declares the two quantities. A detection test that used them would declare them among its inputs.
- `status` carries a different vocabulary in each record kind. Unlike `kind`, `status` names one concept: the lifecycle of a record, whose admissible states depend on its content. Its repetition across kinds is therefore admitted, with no generic slot in its place.
- Only the rows reading `always` are checked, because the other conditions in the same column are semantic, such as an index set required when no constituent kind or parameter supplies the set.
- A tolerance separates the metric from the bound, so an inquiry can state how it compares candidates without stating how close they must come. In the fixtures, one case specifies a metric, and another fixes neither. A qualitative accuracy carries no tolerance at all.
- A renderer that composes the question statement from the fields remains to be built, together with a LaTeX typesetter for a filled record. The [syntax decision](../docs/adr/expression-syntax.md), an infix surface over an S-expression core, fixes the input notation of such a renderer.
- All six detection tests read `expression: open`, since each would test the pattern that its inquiry seeks. Until the diagnostic exists, the glosses of these tests state the check that each test performs.
- The key order within an entry is stated in the [representation contract](../src/gnomon/data/templates/_index.md) and enforced by no check. A record whose keys run in another order passes every test.
- The lattice realization in the case on active matter is named, and its schema is not written. The check now reports such a variant unless the record marks it open. This record marks the variant open, so the gap is declared, not closed. No lattice member can be generated, and the `continuum` marks on the target and the phenomenon carry information only because a second variant is named.
- The optimizer update of the record on delayed generalization states how the parameters change and not how its auxiliary state does. The former call `d_t(theta, z)` passed two quantities to a derivative, a call that no reading admits. The call now reads `diff(theta, step)`, and the law for `z` remains unwritten.
- `grad`, `div` and `lap` are typed with a free variable for the dimension, and the type language cannot bind it to the domain over which the operators run. The types state the shape correctly and leave the dimension unconstrained.
- The arity of a relation of the organization is stated and only partly checked, since the check requires only that every place index the carrier. A relation may therefore name fewer places than its carrier has and still pass every check. A relation that names a place outside every carrier is reported.
- The direction of a relation of the organization is stated and cannot be checked. An edge with its pairs reversed passes every check, since both endpoints index the carrier either way. The defect belongs to the same class as the declared signature, but lies beyond the reach of a parser.
- The limit once recorded for `applies_to` predates the retirement of that key and of the interaction laws. Whether the `signature` check shares its blind spot, a quantity applied at a literal index, remains to be verified.
- The command is `python -m gnomon`, never `python -m gnomon.cli`: the latter has no `__main__` guard, so it imports the module, exits 0 and performs no action. Invoked that way, a regeneration reports success and writes nothing.
- The Earth-system and microbial answers now use appeals by an explanans, but the checker still reads that record kind only through synthetic unit fixtures.
- Six answer and assessment pairs now exercise the rewritten templates. Their shared [validation and representation gaps](answer-assessment-template-issues.md) supersede the former absence of instances.
- A detection test carries a name and no symbol, since no field references a test. A symbol becomes warranted as soon as an assessment reports a verdict per test.
- The rule that a gloss must not reformulate its name is checked by hand. The supporting check is a heuristic counting shared words, so it reports entries that a reader must triage, and for that reason it is not in the suite.
- A gloss is authored prose beside a formula, and no check ties the two together. A gloss that contradicts its expression passes every check. Only the style keys and a reader detect such a conflict.
- Unused quantities are detected lexically, as undeclared operators are, so a symbol named only inside a gloss counts as reached. A structural count would read the expression and reference fields alone.
- A domain limit is one string pairing a quantity with a value, `Re -> infinity`. Both ends resolve, and the arrow between them is punctuation that no operator defines, so no check verifies that the left side is a declared quantity of the target.
- The corpus fills three precipitating conditions and two modulating ones, but no inhibiting one, no nonstandard circumstance and no byproduct. Each block left empty carries a comment giving the cause specific to its case. The three kinds with no instance need quantities that no case declares: a dissipation rate for the turbulent anomaly, an intervention scale for a nonstandard preparation. The gap lies in the fixtures: the schema now expresses all five kinds.
- Nineteen value sets read `open` because the case fixes no set. Their identifying content sits in the gloss, the place where a name in words belongs. A set that is genuinely constrained and not yet expressible has no other home.
- The option cells of the notes remain unchecked against the registry, because a note states a gloss where a template holds a token. A cell carrying both the gloss and the token would close the last unchecked alignment.
- The schema index lists registry files that its directory lacks. Work on inquiry schemas must update the index without claiming that those unrelated registry files were restored.
- The [assessment record](../src/gnomon/data/templates/_index.md) carries no symbol and no expression. Filled answer records now exercise the expression language under manual inspection, but the loader still excludes them from automated resolution.
