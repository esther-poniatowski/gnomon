---
tags:
  - decision
status: proposed
created: 2026-11-01
revised: 2026-11-01
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Findings output
---
# Findings output

> [!QUESTION] Goal: in which form does a check of `gnomon` report a defect, so that the gate Elenchos can build a stable identity for it?

The gate Elenchos reads the findings of each domain tool as a SARIF 2.1.0 log in its findings profile, version 1. It builds the identity of a finding from the tool, the rule, the resource and the locus, and from a discriminator written by the producer. Before this decision, every check returned a list of strings assembled by hand, such as `steps.derive: intuition is no registered activity`. A string of that form names neither a rule nor a field path that a reader can recover. Moreover, several formats drop levels of the path: `inadmissible_values` keeps only the top-level block, and `misnamed_variant` keeps only the keys above the mark.

## Decision

The decision has five parts: a type of finding, a catalogue of rules, the resource and the locus of each finding, the completeness that each run declares, and the output of the command `itinerary`.

### Finding

Every check returns a list of `Finding`, a frozen dataclass of `src/gnomon/findings.py` holding four values: its `rule`, its `path`, its `text` and its `discriminator`. The text is the string that the check returned before this decision, unchanged, so the text output keeps every line. The path is the sequence of segments of the locus, keys and indices; the empty path denotes the whole record. A check never names a file: the caller pairs each finding with the record and the file that it read. ^finding-type

One check spans several records, `unused_declarations`, so it returns each finding with the identifier of the record that declares the quantity.

### Rules

Each message format has one stable `ruleId` of the form `<area>/<kind>`, whose components match `[a-z0-9][a-z0-9._-]*`. The four areas are `itinerary`, `registry`, `completeness` and `vocabulary`, one per family of checks. The catalogue lives in `src/gnomon/findings.py`, together with a one-line description of each rule, and the driver of every log lists all of its rules. Every rule has level `error`, since every finding fails its check. Two formats that differ only by the block named in their prefix share one rule, such as the unselected condition of a quantity and of a feature. ^rule-catalogue

### Resource and locus

The resource of a finding on a record is `id:<identifier>`, the field `id` that the record schemas designate by the keyword `x-identifier`. A finding on a file that holds no record, such as the activity registry, takes `path:<path>`, relative to the root of the repository. In the resource, `%` is written `%25` and `#` is written `%23`. ^resource

The locus is the JSON Pointer of the path, converted as section 4.5 of the profile states: each `~` of a key becomes `~0` before each `/` becomes `~1`, and an index takes its decimal form. The path names the field that the check read, which follows the code where the code and a template differ. For instance, `unrealized_link` reads the list `realizations` at the top of the answer. Three rules place an entry of a list: ^locus

- **Keyed list.** An entry of a list keyed by an identifier takes the pointer of the list, and its identifier opens the discriminator. A step is keyed by `id`, a restriction by `name` or else `of`, an activity of the registry by `id`, and every other entry by `symbol` or else `name`. Every segment below the entry follows the identifier in the discriminator, each part escaped as a pointer token and the parts joined by `/`. For instance, an unresolved identifier `f` in the expression of the law `g` lies at `/laws` with the discriminator `g/expression/f`. Reordering the list therefore keeps every identity. ^keyed-lists
- **Unkeyed list.** An entry of `links`, `realizations` or `virtues` keeps its index as a segment of its path, as do an entry of a keyed list that carries no identifier and an item of a list of strings. The index enters the pointer, or the discriminator when a keyed entry lies above it. ^unkeyed-lists
- **Recovered path.** A format whose message drops levels keeps its message, and its path holds every level: a closed field lies at its full path in `inadmissible_values`, a variant mark at its own position in `misnamed_variant`, and a restriction under `subject.domain.restrictions`. ^recovered-paths

A format without a locus prefix in its message still lies at the field that it concerns: `task.required_accuracy.<key>` for `contradictory_accuracy`, `realizations` for `unrealized_link`, `task.admissible_explanans.justification` for `unjustified_explanans_bound`. A requirement of an aim lies at `task.epistemic_aim` of the question, with the required path as discriminator, whichever record that path reaches. The aim of the question imposes the requirement, and the caller of `unmet_by_aim` holds the question as its resource.

The discriminator is derived from the finding alone: the identifier of its entry, the segments below it, and the offending content, such as an unresolved identifier, a repeated step or the steps of a cycle. It never depends on another finding, and it is empty when the locus suffices. Two steps sharing one identifier yield findings of one identity, which the gate numbers as identical occurrences. ^discriminator

### Completeness of a run

A run is complete when every record of the folder was read and every itinerary was checked. A complete run declares one invocation with `executionSuccessful` set to `true`, whether or not it found a defect. A run in which a record file cannot be read or parsed checks the remaining records, and declares a failed invocation with one notification of level `error`. The same holds when the check stops on an error, such as an unreadable registry. The log then holds every finding detected before the stop. The results are always written, since the analysis begins once the records are listed. ^run-completeness

### Output of the command

The command `gnomon itinerary` accepts `--format text|sarif`, `--output PATH` and `--root PATH`. The default `--format text` keeps the text output byte for byte, and a record that cannot be read still raises its error. With `--format sarif`, the command writes one log on standard output, or at `--output`, creating the missing folders. Every path of the log is relative to `--root`, the current directory by default, and a folder outside the root is refused. When the log takes standard output, the text lines go to standard error. The exit status is 1 when a defect is found or a record cannot be read, and 2 when the log cannot be written. ^command-output

The log holds no `suppressions`, no `fingerprints` and no `baselineState`. The profile reserves the first two for the gate, and excludes the third from version 1. No result holds a region, since the checks track no line, so each physical location denotes the whole record file.

## Constraints that decide the form

- **The identity depends on the field path.** The profile builds the locus from the segments of a path, not from its printed form, since a printed form need not quote a key holding `.` or `[`.
- **The text output is relied on.** Readers and tests compare the messages, so a typed finding must carry the message unchanged.
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
