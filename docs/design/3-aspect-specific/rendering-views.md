---
tags:
  - aspect
index: "[Aspect-specific decisions](_index.md)"
aliases:
  - Rendering and views
---
# Rendering and views

> [!INFO] Tier and source
> **Tier 3 (aspect-specific).** Stub file. Holds criteria for the rendering layer and view specifications. Traces to [activity access rights](../1-framework/research-activities-workflows#^t1-activity-access-rights), [single source of truth](../1-framework/research-activities-workflows#^t1-single-source-of-truth), [t1-dual-usability](../1-framework/cost-ergonomics#^t1-read-side-automation), and the rendered-vs-canonical distinction fixed at [derived artifacts](vendor/gnomon/docs/design/2-architecture/layering#^t2-derived-artifacts) and [view specifications](vendor/gnomon/docs/design/2-architecture/layering#^t2-view-specifications).

---

## Criteria

### Declarative note manifests ^t3-declarative-note-manifests

A note manifest declaratively specifies which canonical objects and assemblies feed the note. Manifests are versioned schema objects, not free-form scripts.

### No manual edits in rendered artifacts ^t3-no-manual-edits-rendered

Rendered artifacts are read-only outputs. Manual edits in the rendered artifact are forbidden; corrections happen at the canonical source and propagate through re-rendering.

### Multiple projections from one source ^t3-multiple-projections

A single canonical source supports multiple projections: formal, pedagogical, audit, automation. Each projection is a view spec; none is privileged as the canonical form.

---

## Decisions

*To be drafted at the rendering work.*

---

## Open questions

*To be drafted at the rendering work.*
