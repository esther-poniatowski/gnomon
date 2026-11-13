# View schemas

The schemas of this folder declare the views that `gnomon views` generates from the records of a workspace, and the vocabulary that `gnomon vocabulary` generates for one problem, so that a renderer such as Ekphrasis displays each view as a read-only form. Every computed display is such a YAML view; no command writes a Markdown copy. Each schema binds the logical identifier `gnomon:view.<name>@<version>`, which the schema registry of the renderer maps to its file.

- [Shared view components](components/_index.md): defines fields reused by several generated-view contracts
- [State of each problem](problem-state.schema.yml): to read whether each problem is solved, which answers it holds, and which obstacles remain
- [Open conditions and ready acts](next-act.schema.yml): shows what each act requires and produces, then compares valid appraisals by their declared rule
- [Exposure of each answer](exposure.schema.yml): to read which revisable units each answer rests on
- [Assembly of each level](assembly.schema.yml): to read what each level of an inquiry is assembled from, which parts are settled, and what remains open or left out
- [Progress of each itinerary](itinerary-progress.schema.yml): reports the itinerary-derived state of each named output and traces its suppliers and consumers among displayed steps
- [Maturity of each record](maturity.schema.yml): to read which parts of the research are settled
- [Operational inquiry graph](inquiry-graph.schema.yml): follows research products through the activities that consume and produce them
- [Statement of each question](question-statements.schema.yml): to compare the authored statement of each question with the statement composed from its fields
- [LaTeX form of each expression](expressions.schema.yml): to read each expression of a record as typeset mathematics
- [Vocabulary of a problem](vocabulary.schema.yml): to choose a new symbol without colliding with one that the records of a problem already declare
- [Compatible view contracts](compatibility/_index.md): resolves published view contracts retained for existing artifacts and consumers
