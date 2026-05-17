
# Rendering and Views

## Rendering specifications

|Component|Role|
|---|---|
|**Note manifests**|Declare which objects and bundles feed a note|
|**Templates**|Define rendering format and ordering logic|
|**Audience profiles**|Technical summary, pedagogical summary, glossary, dashboard|
|**Selection rules**|Include only validated results, or only load-bearing objects, etc|
|**Transformation rules**|Shorten proof bodies, expand definitions, suppress metadata|
|**Ordering rules**|Topological order, pedagogical order, conceptual order|
|**Layout specifications**|Tables, sections, link style, citation format|

## Rendered artifacts

|Artifact|Source|
|---|---|
|**Technical summary note**|note manifest + argument bundle|
|**Audience-facing overview**|note manifest + template + selected objects|
|**Concept glossary**|terminology index + definitions|
|**Dependency map**|graph layer|
|**Open issues dashboard**|issue bundles + status registry|
|**Proof dependency view**|relation registry + justificatory graph|
|**Research branch map**|namespace registry + inquiry graph|
|**Progress report**|status index + unresolved nodes|

## Expository views

To preserve coherence in exposition, the source for "digest notes" should preferably be:

- a selected argument bundle
- not the entire registry
- not arbitrary object collections

To enforces that any note is a reproducible, auditable compilation, the selection of objects for a given note must itself be **declarative and traceable**. A note specification file should enumerate:

- which object IDs it draws from
- in what order
- with what rendering template

Concretely, this means notes become compilable from a manifest:

```yaml
note_id: NOTE-007
audience: peer_researchers
target_question: Q-001
selected_objects:
  - { id: DEF-003, role: background }
  - { id: ASM-001, role: hypothesis }
  - { id: THM-042, role: main_result }
  - { id: EX-005, role: illustration }
template: technical_summary_v2
```