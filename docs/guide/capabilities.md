---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Capability status
---
# Capability status

Capability status classifies each Gnomon outcome for the current release. The package remains pre-alpha, so its interfaces may change. The `supported` label applies only to the release being used.

## Status meanings

Four labels determine how a researcher may use an outcome.

- **Supported:** a documented route produces the outcome, and targeted tests or worked inquiries show that it works and detects relevant failures
- **Experimental:** a route exists, but a central contract or part of its operational coverage remains incomplete
- **Planned:** no supported route produces the complete outcome
- **Deprecated:** a route remains available while users migrate; its row names its successor and states when Gnomon will remove the old route

An absent route is removed rather than deprecated. Gnomon currently deprecates no published outcome.

## Current capabilities

Each row states the usable boundary and the first guide or command to use.

| Capability | Status | Current boundary | Entry point |
| --- | --- | --- | --- |
| Create a new inquiry workspace | `supported` | The command creates the problem, its itinerary and their index; repeated `--with` options add additional record kinds when required | [Starting an inquiry](first-inquiry.md) |
| Continue a greenfield inquiry through forms | `experimental` | Portable schema provisioning, generic creation with producer-owned index registration, progressive form disclosure, checks and primary views work in an arbitrary vault. Creation and registration passed together inside Obsidian; portable registry use still lacks a complete manual protocol | [Starting an inquiry](first-inquiry.md) |
| Adopt part of an existing research project | `experimental` | The verified question-led route retains external sources as pointers, promotes only the selected target and phenomenon, and ends with an authored act choice. The problem-led route and the other source-unit classes remain documented but unverified in the integrated tutorial. Researchers must supply every class and source pointer | [Starting from existing research](adopting-existing-research.md) |
| Author core inquiry records | `supported` | Schemas and guidance cover every core record | [Filling inquiry records](filling-records.md) |
| Author models and bindings | `experimental` | Records and checks exist, but open design goals can still change their fields and interpretation | [Record specification](../specification/_index.md) |
| Record concepts | `supported` | Concept records have a schema, template and checks | [Concept fields](../specification/concept.md) |
| Represent a question hierarchy | `supported` | Typed links connect each subquestion to its parent, and exclusions record parts outside the inquiry | [Subquestions and exclusions](../specification/question.md) |
| Record a formal derivation | `supported` | Derivation records have a schema, template and checks | [Moves and posits](../specification/derivation.md) |
| Validate record contracts | `supported` | Validation checks each record against the schema named by its `_schema` field | [Contract validation](cli-reference.md#^cli-validate) |
| Check the research method | `supported` | Checks cover structural, symbolic, epistemic and cross-record rules | [Method checks](cli-reference.md#^cli-check) |
| Check an inquiry itinerary | `supported` | The checker enforces each itinerary's declared structure and registry constraints | [Itinerary checks](cli-reference.md#^cli-itinerary) |
| Generate a problem vocabulary | `supported` | The generated view collects declared symbols, operators and LaTeX forms | [Problem vocabulary](cli-reference.md#^cli-vocabulary) |
| Diagnose open conditions and ready acts | `supported` | The status report derives answerability conditions and acts from the current records | [Inquiry diagnosis](cli-reference.md#^cli-status) |
| Print the question hierarchy | `supported` | The command prints the problem, question, answer and assessment hierarchy as text | [Question tree](cli-reference.md#^cli-tree) |
| Generate the operational inquiry graph | `experimental` | The generated view connects typed research products through typed activity nodes and directed relations; the Obsidian protocol confirms root-focused navigation, while filters and keyboard navigation remain open | [Inquiry views](cli-reference.md#^cli-views) |
| Generate computed inquiry views | `supported` | Nine schema-bound views expose computed state without changing records | [Inquiry views](cli-reference.md#^cli-views) |
| Compute the source identifier of a view | `supported` | Gnomon computes the identifier that a presentation tool can compare with the value stored in a view | [View source identifier](cli-reference.md#^cli-source-state) |
| Typeset record expressions | `supported` | The expressions view derives LaTeX from symbols currently declared in Gnomon | [Inquiry views](cli-reference.md#^cli-views) |
| Export research units and relations | `supported` | The export follows `ekthesis:export@1`, and check mode detects a file that differs from current records | [Research export](cli-reference.md#^cli-export) |
| Inspect the installed package | `supported` | The root flag prints the package release; the info command also prints the operating system and Python release | [Package diagnostics](cli-reference.md#^cli-info) |
| Compare a model with data | `planned` | Binding records hold inputs, but no command compares model outputs with data | [Model-design proposal](../proposals/model-design.md) |
| Generate reusable notation macros | `planned` | The expressions view typesets current symbols, but no command generates reusable macros | [Notation ownership proposal](../proposals/vocabulary-records.md) |
| Define a concept formally | `planned` | Candidate formalisms exist, but no accepted record or checker supports this act | [Definition framework](../proposals/definitions-framework.md) |
| Reduce epistemic acts to primitives | `planned` | The activity registry lists the acts directly | [Research-action proposal](../proposals/research-actions.md) |
| Check a named validation scope | `experimental` | The CLI separates current omissions from work due later and preserves integrity findings. Activation of on-demand commitments from open conditions remains unavailable | [Validation scopes](../specification/validation-scopes.md) |
| Explain a finding by its rule identifier | `supported` | The explain command prints the meaning, repair condition and documentation target of one rule from the catalogue of rules; Ekphrasis does not yet display this explanation | [Finding explanations](cli-reference.md#^cli-explain) |
| Compare ready acts by authored criteria | `supported` | The next-act view applies ordinal dominance and displays its authored inputs, derived relations and unresolved choices | [Ready-act comparison](../../PLAN-usability.md#^ready-act-comparison) |
| Preview schema changes to records | `experimental` | Check mode reports binding-only diffs, blocking fields and unreadable files without writing | [Migration preview](cli-reference.md#^cli-migrate) |
| Apply reviewed schema changes to records | `experimental` | Apply mode displays every binding-only diff, asks the researcher to approve it and preserves exact source bytes before writing. Before restoring those bytes, the recovery procedure copies newer sources outside the inquiry | [Record migration](../../PLAN-usability.md#^record-migration) |
| Recover the integrated workflow from failures | `experimental` | The guide covers five desktop failures and command-line migration recovery. Conflicting generated targets, mobile Python commands and missing custom-checker packages remain outside the verified procedures | [Workflow recovery](recovery.md) |

## Status changes

Gnomon assigns a new label only after all criteria for that label pass. The `supported` label requires current documentation and realistic success coverage. The `supported` label also requires tests of failures that can invalidate or damage a research workspace. A deprecated row must name its successor and state when the old route will be removed.
