## IDs, Versioning and Provenance

Each object carries **stable identifiers**:

- identity of an object
- version of an object
- provenance (from which prior version it was derived, if applicable)
- relation of that object to other objects

This improvement has several benefits:

- retrieval becomes semantic rather than lexical
- the same concept cannot be redescribed multiple times
- variants become distinct objects with explicit relations
- dependencies can be tracked formally
- updates propagate clearly — in particular, a weakened assumption propagates impact to all downstream objects, and the version graph makes this impact computable
- the intellectual trajectory of the framework can be reconstructed, which is itself a research artifact.

**Scoping and namespace hierarchy**: As the framework scales, objects must be scoped. A **namespace hierarchy** — analogous to module systems — allows sub-frameworks to be developed semi-independently, with explicitly declared interfaces (exported objects) and dependencies between namespaces. This prevents the global registry from becoming an undifferentiated flat namespace and supports the management of multiple concurrent research threads.

## Model Versionning

To prevent ontology drift, this layer should be versioned independently.

_Example_:

- ontology version `0.3`
- knowledge base built against ontology version `0.3`