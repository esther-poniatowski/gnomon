# Handoff — gnomon design

This file gives the project-level state for a new agent. Read this file first, then read the focused handoff for the work you are about to do:

- [Refactor handoff](_handoff-refactor) — Step A through Step D for the design-folder refactor.
- [Cleanup handoff](_handoff-cleanup) — Step A.4 source-file cleanup only.
- [Design index](_index) — current tier layout and file entry points.

Do not use the backup proposals as live design state unless an active file or the classification table points to a specific backup passage.

---

## Current state

`gnomon` is a design for an object-centered knowledge architecture for research notes, definitions, arguments, proofs, and derived views. The design folder uses the tier layout:

```text
design/
  _index.md
  _classification-table.md
  _migration-table.md
  _fleeting-ideas.md
  _worked-examples.md
  1-framework/      — Tier 1, one file per theme
  2-architecture/   — Tier 2
  3-aspect-specific/ — Tier 3
  _backup/
```

The active source of truth is split as follows:

- The **canonical Tier-1 criteria** live in `1-framework/`, one file per conceptual theme — `framework-foundations`, `expressive-depth`, `reasoning-integrity`, `modular-content-organization`, `research-activities-workflows`, `cost-ergonomics`, `external-interfaces` — indexed by `1-framework/_index.md`. The earlier single file `_framework-criteria.md` no longer exists; it was split into these theme files.
- `_classification-table.md` is the ledger for Step B and Step C.
- `_migration-table.md` is still only a header and must be built in Step B.
- `2-architecture/` and `3-aspect-specific/` keep the flat tier layout until Step D reorganizes them by theme (Tier 1 is already theme-organized).
- `_fleeting-ideas.md` is a staged candidate catalogue, not a final theme file.
- `_worked-examples.md` is a reference test suite, not a final theme file.

Two object levels must stay distinct:

- **Framework objects** are the representation units in the architecture: `Claim`, `Definition`, `Proof`, and related epistemic objects.
- **Content objects** are the things the research talks about: concepts, systems, properties, relations, and examples.

A criterion about framework objects does not automatically decide a content taxonomy, and a content taxonomy does not automatically change the framework object model.

---

## Immediate work

The next task is **Step A.4** in the refactor: remove source bodies whose Tier-1 content has already moved into the `1-framework/` theme files. The `1-framework/` portion is done (the four legacy stubs were deleted, their links redirected); Files 5–11 (Tier-2/3 and backup sources) remain. The cleanup handoff owns the current file status and the deletion rules.

After Step A.4:

1. Step A.5 updates `_classification-table.md` for content added after Step A.3 and for later Tier-1 criterion changes.
2. Step B builds `_migration-table.md`.
3. Step C performs batch migration in the order recorded in the refactor handoff.
4. Step D reorganizes the design folder by theme.

Open Tier-2 decisions can proceed in parallel only if they do not invalidate classification-table targets without updating the table before Step B. The main unresolved Tier-2 questions are `^t2-layer-feedback`, `^t2-subtype-discipline`, `^t2-operation-primitiveness`, `^t2-planning-execution-sync`, `^t2-reasoning-record-storage`, `^t2-granularity-strata`, and `^t2-partial-formalization-profiles`.

---

## Work discipline

- Read the current files before acting. The handoffs point to state; they do not replace the source files.
- Preserve anchors until the migration step explicitly redirects or removes them.
- Use Obsidian block-anchor links, such as `#^anchor-name`. MD051 warnings on those links are expected false positives.
- Ratify substantive design changes with the user before applying them. Source cleanup has its own stricter approval rule in the cleanup handoff.
- Replace duplicate recalls with links to the owning source. Do not keep parallel prose that says the same thing in different words.
- Frame rejected routes by the active constraint that excludes them, not by the history of who wrote them or when.

---

## Handoff maintenance rules

Future agents must keep the handoffs small and current.

- Update only the handoff that owns the state: project-level orientation belongs here, Step A-D state belongs in the refactor handoff, and Step A.4 mechanics belong in the cleanup handoff.
- Delete completed task details once the next agent no longer needs them. Keep the result, the next dependency, and any error-preventing warning.
- Do not restate file contents that a new agent can recover by reading the file itself. Link to the file and state why it matters.
- Do not duplicate the same instruction across handoffs. Put it in the narrowest handoff that needs it, and link from the broader handoff.
- When a task completes, change the status and remove obsolete warnings, obsolete TODOs, and superseded route descriptions in the same edit.
- When a route is discarded, keep only the active constraint or decision that rules it out.
- When new pending work appears, record the owner file, the prerequisite, and the next action. Avoid adding an audit log unless the exact past mistake is likely to be repeated.
- Keep handoff links stable and anchor-based where possible.
