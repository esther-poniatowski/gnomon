# Registries

The registries of this folder declare the epistemic activities and the artifacts that they take and produce. The plan check reads both, so that each step of a [plan record](../../../../docs/epistemology/plan.md) can be compared with the activity that it instantiates.

- [Epistemic activities](activities.yml): to find the input and output types, the norm, the mode and the context of an activity before writing a step of a plan.
- [Artifact types](artifact-types.yml): to find which record kind holds an artifact of a given type, and which types no record kind holds yet.

> [!NOTE] Templates of project state
> The folder is also meant to hold templates that a consuming project copies to record its own state: an inferential architecture (`reasoning_graph.yaml`), the current frontier of open questions (`open_questions.yaml`), the terms and their forbidden variants (`terminology.yaml`), and the provenance of each result (`dependencies.yaml`). None of these templates is written yet.
