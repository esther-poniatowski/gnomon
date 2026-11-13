---
tags:
  - decision
status: accepted
created: 2026-11-01
revised: 2026-11-10
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Findings output
---
# Findings output

> [!QUESTION] Goal: in which form does a check of `gnomon` report a defect, so that the gate Elenchos can build a stable identity for it?

The gate Elenchos reads the findings of each domain tool as a SARIF 2.1.0 log in its findings profile, version 1. It builds the identity of a finding from the tool, the rule, the resource and the locus, and from a discriminator written by the producer. Before this decision, every check returned a list of strings assembled by hand, such as `steps.derive: intuition is no registered activity`. A string of that form names neither a rule nor a field path that a reader can recover. Moreover, several formats drop levels of the path: `inadmissible_values` keeps only the top-level block, and `misnamed_variant` keeps only the keys above the mark.

## Decision

### Interface result classes

Every interface result about an inquiry distinguishes its source and authority through one of four classes: ^interface-result-classes

| Result class | Source | Authority |
| --- | --- | --- |
| `contract validation` | the record and the JSON Schema named by its field `_schema` | establishes only whether the record follows that contract |
| `method-conformance finding` | authored records, package registries or another declared checker input, evaluated under a declared rule | identifies a rule that the checked inputs do not satisfy; it does not establish whether a scientific claim is true |
| `computed inquiry diagnosis` | deterministic inquiry state or view data derived from authored records by a declared rule | reports derived state without adding a judgment to the records |
| `researcher-authored verdict` | a judgment written by the researcher with its evidence | records the judgment; software may validate its form and references but must not infer its outcome |

The classes `contract validation` and `method-conformance finding` report defects through the finding transport. A `computed inquiry diagnosis` follows the [boundary of admitted computation](no-run-time-inference.md#^admitted-computation). A `researcher-authored verdict` follows the [prohibition on inferred judgments](no-run-time-inference.md#^excluded-inference).

A verdict whose value is `pending` is valid authored content and remains outside the finding transport. The schemas of assessment and itinerary records declare `x-rules: [{check: unresolved-value, value: pending}]` on their verdict fields. A form client can therefore present that value as unresolved research state without treating it as a defect or inferring which other authored values carry the same meaning.

For a scoped check, an omission due later is future work with the class `computed inquiry diagnosis`. Future work stays outside the finding transport because it has no defect rule, severity, repair condition or stable finding identity. Therefore, text and YAML reports can present future work separately, whereas SARIF contains only current findings.

The SARIF run property `gnomon/validationScope` carries a list of non-issue context objects. A selected scope adds its completion target, description, result class and documentation target. A complete run without an error or warning adds a clean-result context. This context states that the records satisfy the checked structural and method rules, but the check establishes no truth, warrant or acceptance for their claims. A stopped run never adds that context. Run context remains outside `results`, so an interface can explain a clean check without inventing an issue.

### Finding

A check represents each defect as `Finding`, a frozen dataclass in `src/gnomon/findings.py`. Each finding holds its `rule`, `path`, `text`, `discriminator` and optional `controlled_by` path. The associated rule supplies the result class, severity and canonical guidance. The text supplies the explanation printed by the text output. The path supplies the segments of the repair locus; an empty path denotes the whole record. The optional controlling path names the field whose authored value or presence activated the finding. The caller pairs each finding with its record and source file. ^finding-type

The internal issue contract and the YAML report group ten fields by their function:

- **Source:** source file, record identifier and field path
- **Classification:** result class, rule and severity
- **Guidance:** explanation, repair condition and documentation target
- **Dependency:** controlling decision, when one field of the same record activates the finding

Every published rule supplies a repair condition and a documentation target. A standalone rule may omit either optional value. For an omitted value, the YAML report writes `null`. The SARIF log omits the absent property. A dependent finding writes its controlling field as the JSON Pointer `controlled_by` in the YAML contract and as the tool property `gnomon/controllingDecision` in SARIF. An independent finding omits the controlling field in both formats.

One check spans several records, `unused_declarations`, so it returns each finding with the identifier of the record that declares the quantity.

### Rules

Each message format has one stable `ruleId` of the form `<area>/<kind>`, whose components match `[a-z0-9][a-z0-9._-]*`. The first component identifies one family of checks:

- `itinerary`
- `registry`
- `completeness`
- `vocabulary`
- `derivation`
- `dimension`
- `contract`
- `relation`
- `check`, for a check that stopped on an error

The catalogue in `src/gnomon/findings.py` supplies the description, severity and result class of each rule. The [repair-guidance registry](../../src/gnomon/data/rule-guidance.yml) supplies its repair condition and documentation target. Catalogue loading requires the two sources to name exactly the same rules.

A rule of severity `error` fails its check. A rule of severity `warning` reports a specification usually expected for the checked records without failing the check. Two formats that differ only by the block named in their prefix share one rule, such as the unselected condition of a quantity and of a feature. ^rule-catalogue

### Resource and locus

The resource of a finding on a record is `id:<identifier>`, the field `id` that the record schemas designate by the keyword `x-identifier`. A finding on a file that holds no record, such as the activity registry, takes `path:<path>`, relative to the root of the repository. In the resource, `%` is written `%25` and `#` is written `%23`. ^resource

The locus is the JSON Pointer of the path, converted as section 4.5 of the profile states: each `~` of a key becomes `~0` before each `/` becomes `~1`, and an index takes its decimal form. The path names the field that the check read, which follows the code where the code and a template differ. For instance, `unrealized_link` reads the list `realizations` at the top of the answer. Three rules place an entry of a list: ^locus

- **Keyed list.** An entry of a list keyed by an identifier takes the pointer of the list, and its identifier opens the discriminator. A step is keyed by `id`, a restriction by `name` or else `of`, an activity of the registry by `id`, and every other entry by `symbol` or else `name`. Every segment below the entry follows the identifier in the discriminator, each part escaped as a pointer token and the parts joined by `/`. For instance, an unresolved identifier `f` in the expression of the law `g` lies at `/laws` with the discriminator `g/expression/f`. Reordering the list therefore keeps every identity. ^keyed-lists
- **Unkeyed list.** An entry of `links`, `realizations` or `virtues` keeps its index as a segment of its path, as do an entry of a keyed list that carries no identifier and an item of a list of strings. The index enters the pointer, or the discriminator when a keyed entry lies above it. ^unkeyed-lists
- **Recovered path.** A format whose message drops levels keeps its message, and its path holds every level: a closed field lies at its full path in `inadmissible_values`, a variant mark at its own position in `misnamed_variant`, and a restriction under `subject.domain.restrictions`. ^recovered-paths

A finding whose message omits a locus prefix still lies at the field concerned: `task.required_accuracy.<key>` for `contradictory_accuracy`, `realizations` for `unrealized_link`, and `task.admissible_explanans.justification` for `unjustified_explanans_bound`. When an aim requires another field of the question, the finding lies at the missing field. This locus lets an editor reveal the repair target. When the aim requires a field of another record, the finding lies at `task.epistemic_aim` of the question. The required cross-record path becomes its discriminator because the caller of `unmet_by_aim` holds the question as its resource.

The discriminator is derived from the finding alone: the identifier of its entry, the segments below it, and the offending content, such as an unresolved identifier, a repeated step or the steps of a cycle. It never depends on another finding, and it is empty when the locus suffices. Two steps sharing one identifier yield findings of one identity, which the gate numbers as identical occurrences. ^discriminator

### Completeness of a run

A run is complete when every record of the folder was read and every itinerary was checked. A complete run declares one invocation with `executionSuccessful` set to `true`, whether or not it found a defect. A run in which a record file cannot be read or parsed checks the remaining records, and declares a failed invocation with one notification of level `error`. The same holds when the check stops on an error, such as an unreadable registry. The log then holds every finding detected before the stop. The results are always written, since the analysis begins once the records are listed. ^run-completeness

### Output of the command

The command `gnomon itinerary` accepts `--format text|sarif`, `--output PATH` and `--root PATH`. The default text format prints one line per defect. Each line states the itinerary identifier, rule identifier and message. A warning inserts the mark `warning:` before the rule identifier. A record that cannot be read still raises its error.

With the format `sarif`, the command writes one log on standard output or at the selected output path. The command creates missing parent folders. Every path of the log is relative to the selected root, which defaults to the current directory. The command refuses a folder outside that root. When the log takes standard output, the text lines go to standard error. The exit status is 1 for a defect or an unreadable record, and 2 when the log cannot be written. ^command-output

The log holds no `suppressions`, no `fingerprints` and no `baselineState`. The profile reserves the first two for the gate, and excludes the third from version 1. No result holds a region, since the checks track no line, so each physical location denotes the whole record file.

## Constraints that decide the form

- **The identity depends on the field path.** The profile builds the locus from the segments of a path, not from its printed form, since a printed form need not quote a key holding `.` or `[`.
- **The text output leads to the rule catalogue.** Every human-readable finding names its rule identifier, so a researcher can pass that identifier to `gnomon explain`. Readers and tests compare the messages, so a typed finding carries the message unchanged after the identifier.
- **A producer imports no package of Elenchos.** The profile and the conversion of a path to a pointer are implemented again in `gnomon`, after the writer of Kleisis.
- **An entry of a record moves.** An author reorders the steps of an itinerary or the declarations of a block without changing their content, and a baseline entry of the gate must keep matching.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Parse the existing strings into a rule and a path | No check changes | The segments cannot be recovered: several formats drop levels, and a message such as `restrictions.<name>` prints a name in words where the record holds a list |
| Locate every entry of a list by its index | One rule for every list, and the pointer names the exact node | Reordering a keyed list changes the identity of every finding below the moved entries, so a tolerated finding reappears as new |
| Locate a keyed entry by the pointer of its list, and leave the segments below it out of the discriminator | A shorter discriminator | Two findings of one rule in two fields of one entry share an identity, such as an unresolved `f` in the expression and in the signature of one law |
| Locate a keyed entry by the pointer of its list, with its identifier and the segments below it in the discriminator | Identities survive reordering, and every field below the entry stays distinct | Selected. Its cost: a discriminator holds part of the path, so a reader learns the exact field from the message or the discriminator rather than from the pointer alone |

The selected option would lose to index pointers if the gate located a finding by its pointer alone, for instance to highlight a node in an editor. The profile uses the discriminator only in the identity.

## Consequences

- A new message format takes a new rule in `src/gnomon/findings.py`. Renaming a rule changes the identity of its findings, so it requires a rename map in the gate.
- A list that gains an identifier key, or loses one, takes its entry in the table of identifier keys of `src/gnomon/findings.py`. Every finding below its entries then changes identity once.
- The tests of `tests/test_gnomon/test_findings.py` check the loci and the discriminators, and those of `tests/test_gnomon/test_sarif.py` check the log and the command.
- The command `itinerary` does not check the activity registry, so no finding of the rules `registry/*` reaches its log. The writer supports the resource `path:` that such findings take.
