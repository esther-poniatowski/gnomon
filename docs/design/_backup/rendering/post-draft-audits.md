# Post-Draft Audits

Audits are post-draft verification, separated from rules and specifications
because they operate after the drafting pass rather than during generation. The
audit pass receives the draft note, the integration record, and the pre-draft
specification as its baseline, and produces a separate audit report as its
output artifact.

## Audit checklists

The audit system uses eight dimensions, each with a checklist of binary
questions. The sections correspond one-to-one to the audit report sections.

- **Contract compliance audit.** Verifies that the atomic question was answered
  exactly, the minimal target result was delivered, and the termination
  criterion was respected.
- **Coherence audit.** Verifies local necessity, retention, and deductive
  continuity. Questions: Does the note answer exactly one atomic question? Does
  each major section contribute directly? Could any section be removed without
  loss? Does each section use a specific output from a preceding section? Does
  each section's output-consumer pair remain on the main result path? Does the
  skeleton declare and use an admissible decomposition pattern?
- **Mathematical rigor audit.** Verifies proof strategies and premise
  legitimacy. Questions: Are assumptions explicit? Is the proof strategy stated
  before the proof? Is the proof family named appropriately? Does the
  derivation reveal the committed explanatory target or merely verify the
  result? Does it build forward from the problem in the family-appropriate way?
  Is every non-trivial premise proved locally or declared?
- **Redundancy audit.** Verifies that the note does not rederive prior results,
  restate background that should be linked, or duplicate interpretation written
  elsewhere.
- **Argumentative structure audit.** Verifies claim/derivation/interpretation
  separation. Do result statements perform proof work? Do proof paragraphs
  carry interpretation beyond what the next move requires? Do interpretation
  paragraphs merely restate the claim?
- **Motivation audit.** Verifies functional motivation. Are major constructs
  introduced through genuine obstacles? Does each major construct cite the
  exact later step it enables? Are there rhetorical rather than functional
  motivations?
- **Terminology audit.** Verifies consistent use of defined terms against the
  terminology registry. Does any prose use a forbidden variant? Does any newly
  introduced term lack a registry entry?
- **Integration audit.** Verifies inter-note dependencies. Are dependencies
  correctly cited? Is the output directly usable by downstream notes? Has the
  registry been updated?

## Audit report template

The audit report opens with a metadata block (note audited, contract checked)
followed by nine numbered sections corresponding one-to-one to the checklists:
(1) Contract compliance, (2) Coherence, (3) Mathematical rigor, (4) Redundancy,
(5) Argumentative, (6) Motivation, (7) Terminology, (8) Integration,
(9) Required revisions. Sections 1--8 record findings, each citing the specific
checklist question that was violated. Section 9 collects all required revisions
with severity and recommended action.

## Audit enforcement by note type

The audit pass must verify that the note's declared type matches its actual
content. If a note contains sections that match a forbidden pattern for its
declared type, the audit must flag the violation and recommend one of:

- excise the offending section
- defer it to a new note of the appropriate type
- reclassify the note if the content is legitimate but the type declaration is
  wrong

## Writing-quality dimensions

Four of the eight audit dimensions assess prose quality independently of
mathematical correctness or note governance: coherence, redundancy,
argumentative structure, and motivation. These dimensions are also maintained
as writing-quality audit specifications in hermeneia.
