# View schemas

The schemas of this folder declare the views that `gnomon views` generates from the records of a workspace, so that a renderer such as Ekphrasis displays each view as a read-only form. Each schema binds the logical identifier `gnomon:view.<name>@<version>`, which the schema registry of the renderer maps to its file.

- [State of each problem](problem-state.schema.yml): to read whether each problem is solved, which answers it holds, and which obstacles remain
- [Open conditions and ready acts](next-act.schema.yml): to read which act comes next for each question
- [Exposure of each answer](exposure.schema.yml): to read to which revisable laws each answer stays exposed
- [Progress of each itinerary](itinerary-progress.schema.yml): to read how far each itinerary has advanced, and which steps a failed norm impeaches
- [Maturity of each record](maturity.schema.yml): to read which parts of the research are settled
- [Question tree](question-tree.schema.yml): to read the problems, questions and answers of a project as one tree
- [Statement of each question](question-statements.schema.yml): to compare the authored statement of each question with the statement composed from its fields
