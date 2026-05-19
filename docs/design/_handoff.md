# Handoff — gnomon design

This file gives the project-level state for a new agent. Read this file first, then read the focused handoff for the work you are about to do:

- [Refactor handoff](_handoff-refactor.md) — Step A through Step D for the design-folder refactor, and the current refactor state.
- [Cleanup handoff](_handoff-cleanup.md) — Step A.4 source-file cleanup only.
- [Design index](_index.md) — current folder layout and tier scheme.

Do not use the backup proposals as live design state unless an active file or the [classification table](_classification-table.md) points to a specific backup passage.

---

## What gnomon is

`gnomon` is a design for an object-centered knowledge architecture for research notes, definitions, arguments, proofs, and derived views. The [design index](_index.md) holds the current folder layout and tier scheme.

Two object levels must stay distinct:

- **Framework objects** are the representation units in the architecture: `Claim`, `Definition`, `Proof`, and related epistemic objects.
- **Content objects** are the things the research talks about: concepts, systems, properties, relations, and examples.

A criterion about framework objects does not automatically decide a content taxonomy, and a content taxonomy does not automatically change the framework object model.

---

## Current work

The design-folder refactor is mid-flight. The [refactor handoff](_handoff-refactor.md) owns the per-step status and the next action; the [cleanup handoff](_handoff-cleanup.md) owns the Step A.4 file mechanics. Read those for the current task — the immediate work is the Step A.4 backup-source cleanup, and parts of Steps C and D have been brought forward under user ratification.

Open Tier-2 decisions can proceed in parallel only if they do not invalidate [classification-table](_classification-table.md) targets without updating the table before Step B.

---

## Work discipline

- Read the current files before acting. The handoffs point to state; they do not replace the source files.
- Preserve anchors until a step explicitly redirects or removes them — unless the user directs an extended action that redirects them earlier (see *Opportunistic scope* below).
- Use Obsidian block-anchor links, such as `#^anchor-name`. MD051 warnings on those links are expected false positives.
- Ratify substantive design changes with the user before applying them. Source cleanup has its own stricter approval rule in the [cleanup handoff](_handoff-cleanup.md).
- Replace duplicate recalls with links to the owning source. Do not keep parallel prose that says the same thing in different words.
- Frame rejected routes by the active constraint that excludes them, not by the history of who wrote them or when.

### Opportunistic scope ^opportunistic-scope

The step sequence (A → B → C → D, and the batch order within each) is the **default** order, not a hard barrier. Any step may perform actions that the sequence assigns to a later step — reformulating content, creating or deleting entries, deleting files, renaming labels and anchors, redirecting cross-references — **when the user explicitly directs that action**. No extra confirmation step is required beyond the explicit request; the agent performs it directly.

The purpose of allowing this is **visibility**: applying a migration when its outcome is already settled surfaces the remaining work in the folders and files, rather than letting historical records accumulate and obscure what still needs attention. A cleaned, current file is more legible to the next agent than a stale one wrapped in migration callouts.

Extended actions are bounded by two rules:

- **Explicit user direction only.** An agent does not exceed its step's scope on its own initiative. It may *propose* an extended action, but applies it only on the user's explicit request.
- **No silent breakage.** An extended action must not leave dangling links, orphaned anchors, or contradicted handoffs. If a redirect target does not yet exist, either create it or route to an interim home — never leave a dead reference.

### Deferred synchronization debt ^deferred-synchronization-debt

An extended action moves the project ahead of the step sequence, so three artefacts can fall out of date: the [classification table](_classification-table.md), cross-references across the design files, and the handoffs. The agent keeps a running **synchronization-debt list** of what each extended action changed and what it implies for those three artefacts, and surfaces that list to the user at any stopping point — when a task completes, when the user asks for status, or before a new phase of work. The debt is recalled, not silently carried: the user decides when to settle it.

---

## Handoff maintenance rules

Future agents must keep the handoffs small and current.

- Separate concerns between handoffs: project-level orientation belongs to the main handoff, Step A-D state belongs in the [refactor handoff](_handoff-refactor.md), and Step A.4 mechanics belong in the [cleanup handoff](_handoff-cleanup.md).
- Delete completed task details once the next agent no longer needs them. Keep the current state, relevant result if any, the next dependency, and any warning that prevents reproducing past errors.
- Do not restate file contents that a new agent can recover by reading the file itself. Link to the file and state why it matters.
- Do not duplicate the same instruction across handoffs. Put it in the narrowest handoff that needs it, and link from the broader handoff.
- When a task completes, change the status and remove obsolete warnings, obsolete TODOs, and superseded route descriptions in the same edit.
- When a route is discarded, keep only the active constraint or decision that rules it out.
- When new pending work appears, record the owner file, the prerequisite, and the next action. Avoid adding an audit log unless the exact past mistake is likely to be repeated.
- Keep handoff links stable and anchor-based where possible.
- Use *dynamic links* instead of static path references where possible (Obsidian detects these and updates them when files move). Correct pattern: `[alt-text](path/to/file.md)`. A bare backticked path is not a link and is not updated. Do not restate the raw path in the alt-text; use descriptive alt-text that does not need to be updated when the file moves. 
