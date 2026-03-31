# Usage

Gnomon organizes mathematical research into a traceable graph of results,
dependencies, and open questions. The tool scaffolds workspaces, validates
registry files, and reports the inferential position of a research project.

## Scaffolding a Research Workspace

The `init` command creates a structured workspace from the standard template:

```sh
gnomon init --target ./my-research
```

The generated workspace follows the hierarchical organization documented in
[Workspace Architecture](../design/methods/workspace-architecture.md): project
and module scales, each with its own registries and frontier tracking.

## Writing Notes with Contracts

Every note begins with a binding contract that fixes its scope, dependencies,
and expected contribution. The contract must be completed before drafting
begins.

The note type determines the structural constraints. Available types include
problem, result, definition, tool, synthesis, comparison, and frontier. See
[Note Types](../design/methods/note-types.md) for the full specification of
each type.

## Maintaining Registries

Machine-readable YAML registries track reasoning graphs, dependency maps, open
questions, and terminology. Validate all registry files against their schemas:

```sh
gnomon validate registries/
```

## Reporting the Inferential Position

The `status` command reports the current state of the workspace: established
results, open questions, in-progress notes, and blocked entries:

```sh
gnomon status
```

The report helps identify where gaps remain in the reasoning graph and which
results are blocked by unresolved dependencies.

## Tracking Upstream Revisions

When an upstream result is revised, downstream consumers may become unstable.
Gnomon propagates instability warnings through the dependency graph:

```sh
gnomon check-stability
```

## Next Steps

- [Formal Contracts](../design/methods/formal-contracts.md) — Per-note
  inferential specifications.
- [Registries](../design/methods/registries.md) — Machine-readable project
  state and reasoning graphs.
- [Procedural Workflows](../design/methods/procedural-workflows.md) — Staged
  pipelines and pass model.
