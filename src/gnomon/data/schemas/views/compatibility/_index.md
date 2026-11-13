# Compatible view contracts

Preserves published view contracts while maintained artifacts or consumers require them.

- [Assembly, version 1](assembly.v1.schema.yml): validates an assembly without `source_state`
- [Assembly, version 2](assembly.v2.schema.yml): preserves the tabular assembly view for existing generated views
- [Exposure, version 2](exposure.v2.schema.yml): validates an exposure view without `source_state`
- [Exposure, version 3](exposure.v3.schema.yml): validates an exposure view whose reasons are declared as labels
- [Exposure, version 4](exposure.v4.schema.yml): validates an exposure view without selected-target coverage
- [Exposure, version 5](exposure.v5.schema.yml): preserves the tabular exposure view for existing generated views
- [Expressions, version 1](expressions.v1.schema.yml): validates an expression view without `source_state`
- [Itinerary progress, version 2](itinerary-progress.v2.schema.yml): validates itinerary progress without `source_state`
- [Itinerary progress, version 3](itinerary-progress.v3.schema.yml): preserves the tabular step dependencies for existing generated views
- [Maturity, version 1](maturity.v1.schema.yml): validates a maturity view without `source_state`
- [Next act, version 2](next-act.v2.schema.yml): validates a next-act view without `source_state`
- [Next act, version 3](next-act.v3.schema.yml): validates a next-act view that lists every act in one table
- [Next act, version 4](next-act.v4.schema.yml): validates a grouped next-act view before required predecessors and ready acts were separated
- [Next act, version 5](next-act.v5.schema.yml): validates a next-act view before each activity stated its inputs, output location and possible downstream acts
- [Next act, version 6](next-act.v6.schema.yml): validates a next-act view before it displayed comparisons from authored appraisals
- [Next act, version 7](next-act.v7.schema.yml): validates a next-act view without selected-target coverage
- [Problem state, version 1](problem-state.v1.schema.yml): validates a problem-state view without `source_state`
- [Problem state, version 2](problem-state.v2.schema.yml): validates a problem-state view without selected-target coverage
- [Question statements, version 1](question-statements.v1.schema.yml): validates question statements without `source_state`
- [Question statements, version 2](question-statements.v2.schema.yml): validates question statements whose statements are declared as labels
- [Question tree, version 1](question-tree.v1.schema.yml): validates a question tree without `source_state`
- [Question tree, version 2](question-tree.v2.schema.yml): preserves the tabular presentation of question-tree nodes
- [Question tree, version 3](question-tree.v3.schema.yml): preserves the generic nested-tree presentation for existing consumers
- [Vocabulary, version 2](vocabulary.v2.schema.yml): validates a vocabulary without `source_state`
