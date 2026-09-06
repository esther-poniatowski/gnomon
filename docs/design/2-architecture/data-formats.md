---
tags:
  - architecture
index: "[Architectural commitments](_index.md)"
aliases:
  - Source languages and metadata
---
# Source languages, metadata, and grammar

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file fixes the source languages, file metadata contract, declaration wrappers, rich content blocks, and parser rules used by framework files. It instantiates [t1-dual-usability](../1-framework/cost-ergonomics#^t1-read-side-automation), [no version history](vendor/gnomon/docs/design/1-framework/framework-foundations#^t1-no-version-history), the meta-schema rule [field-typing discipline](object-kinds#^t2-field-typing), [read-side automation](../1-framework/cost-ergonomics#^t1-read-side-automation), and [single source of truth](../1-framework/research-activities-workflows#^t1-single-source-of-truth).

---

## Criteria ^t2-data-format-criteria

> [!INFO] The *prose+formulas+math* sub-claim is migrated to [rich prose expressivity](../1-framework/expressive-depth#^t1-rich-prose-expressivity) (promoted T2 → T1). The remaining sub-claims redirect to the cost-axis cluster, field typing, and write-side automation.

The format must:

- remain readable and editable for researchers;
- let programs parse every object and rich content block;
- let schemas check typed fields and cross-object constraints;
- support controlled fields (for example `type`, `status`, and relation labels);
- support Markdown fields with prose, formulas, and Obsidian-rendered math;
- produce stable Git diffs at the file level.

## Decisions

### Source languages ^t2-source-languages

> [!QUESTION] Which source languages does gnomon use for editable files that must also be parsed and validated?

`gnomon` uses a two-level Markdown format with a frontmatter–body split:

| Layer | Format | Content |
| --- | --- | --- |
| File identity | YAML frontmatter | File role, exported identifiers, namespace, and Obsidian-side fields (for example `tags`, `aliases`, and `cssclasses`) |
| Framework content | Markdown with `gnomon:` tags | Declaration scopes (objects, reasonings, rejections, views) and the typed content blocks they contain (statements, proofs, goals, examples, commentary) |

Tying the frontmatter to one object type would either pollute the schema with fields irrelevant to non-object files or push such files into a second-class shape. A file-role contract generalizes across all file types the framework hosts.

### File metadata contract ^t2-file-metadata-contract

> [!QUESTION] Which file-level fields identify a source file and expose its addressable declarations?

Frontmatter declares the file's identity through these fields:

- `role`: the file's function in the framework (for example `object-definitions`, `reasoning`, `rejection`, `schema`, `view`, `exposition`). The project schema enumerates the permitted values.
- `exports`: the identifiers of the objects, reasonings, rejections, or other declarations the file exposes for cross-file reference. Parsers use this list as an entry-point hint when building registries.
- `namespace`: an optional namespace under which the file's exports are addressed.
- Obsidian-side fields (for example `tags`, `aliases`, and `cssclasses`).

The body holds every declaration through `gnomon:decl:<role>` wrappers. For object-definition files, each wrapper is a `gnomon:decl:object` whose first direct-child fenced YAML block carries the object's metadata under the project schema's object key set (for example `id`, `type`, `title`, `status`, `scope`, `depends_on`, `answers`, `relations`, `sources`, and `version`). Other file roles use analogous declaration tags so the body grammar stays uniform across roles.

```yaml
---
role: object-definitions
exports:
  - claim.task_relevance.invariance_criterion
namespace: claims.task_relevance
tags: [claim, task-relevance]
---
```

**Single-export convention for object-definition files.** A file with `role: object-definitions` should expose exactly one object — that is, `len(exports) == 1` — unless the file explicitly opts into a multi-object form. This preserves the "one canonical object per file" invariant where it matters: it discourages sprawling files, gives every object a canonical home, and keeps the file path a stable identifier proxy. The schema enforces this softly through a linter warning rather than a hard syntactic constraint, so a file may still bundle auxiliary objects tightly bound to a lead object when warranted.

**Inference and validation.** Since no files exist yet, no migration is required. Going forward, a validator examines each file mechanically:

- if `role` is missing, the validator infers it from the body's declaration tags (a body containing only `gnomon:decl:object` wrappers infers `role: object-definitions`) and either fills the field or flags the file for review;
- if `exports` is missing, the validator scans the body for declaration wrappers, extracts each declaration's identifier, and fills the list;
- the validator rejects any file whose body declarations are incompatible with its declared `role`.

### Gnomon block grammar ^t2-gnomon-block-grammar

> [!QUESTION] How does the body encode rich content blocks and declaration scopes while remaining valid Markdown?

Rich fields use HTML comments whose names begin with `gnomon:`. Each opening tag has a matching closing tag. JSON after the tag name stores block metadata.

```markdown
<!--gnomon:statement-->
Markdown content.
<!--gnomon:/statement-->

<!--gnomon:proof-step {"id":"p1","parent":null}-->
Markdown content.
<!--gnomon:/proof-step-->
```

The parser rejects unclosed tags, unexpected closing tags, malformed JSON attributes, and overlapping blocks. A block may contain nested blocks only when the outer block schema permits them.

Content blocks may use multiline or inline form. These two blocks have the same syntax-level meaning:

```markdown
<!--gnomon:goal-->
Solve the equation.
<!--gnomon:/goal-->

<!--gnomon:goal-->Solve the equation.<!--gnomon:/goal-->
```

The tag namespace has two roles:

- **Content tags** (`gnomon:<name>`, such as `gnomon:statement`, `gnomon:proof`, and `gnomon:proof-step`) mark rich fields of an object.
- **Declaration tags** (`gnomon:decl:<name>`, such as `gnomon:decl:object`) mark object scopes and other structural regions.

The `decl:` prefix belongs only to declaration-level tags. Content-tag names must not begin with `decl:`.

*Example for a single object*:

````markdown
---
role: object-definitions
exports:
  - claim.task_relevance.invariance_criterion
namespace: claims.task_relevance
---

<!--gnomon:decl:object-->
```yaml
id: claim.task_relevance.invariance_criterion
type: claim
title: "Invariance criterion for task relevance"
status: provisional
depends_on:
  - id: def.task
    relation: requires
  - id: def.representation
    relation: requires
  - id: crit.invariance
    relation: requires
answers:
  - quest.task_relevance.main
scope:
  architectures: [feedforward]
  tasks: [classification]
```

<!--gnomon:proof-->
<!--gnomon:goal-->Solve the **equation** $f(x) = y$ for $x$.<!--gnomon:/goal-->

<!--gnomon:proof-step {"id":"p1", "parent":null}-->
Rearrange the equation to isolate the unknown $x$:
$$
ax = bx + c \implies ax - bx = c
$$
<!--gnomon:/proof-step-->

<!--gnomon:proof-step {"id":"p2","parent":"p1"}-->
Factor out $x$:
$$
x(a - b) = c
$$
<!--gnomon:/proof-step-->

<!--gnomon:proof-step {"id":"p3","parent":"p2"}-->
Divide both sides by the coefficient of $x$:
$$
x = \frac{c}{a - b}
$$
<!--gnomon:/proof-step-->
<!--gnomon:/proof-->
<!--gnomon:/decl:object-->
````

Anchoring works with the built-in Obsidian syntax, which the parser translates into a `gnomon:ref` block with the anchor's name as metadata. The anchor's name must be unique across the vault. The parser rejects duplicate anchors and references to missing anchors.

<!--gnomon:ref-->
^anchor
<!--gnomon:/ref-->

[Dynamic link to anchor](#^anchor)

> [!FAIL]
> The anchor must be on an single line to be addressable by the parser. This is an Obsidian syntax constraint, not a gnomon design choice.

### Multiple objects in one file ^t2-multiple-objects-per-file

> [!QUESTION] May one file contain several objects, and when must an object move to its own file?

A file may contain several objects when those objects remain tightly bound — for example a definition together with auxiliary claims, immediate corollaries, or local examples that serve it. The file remains the storage unit; the object identifier remains the addressable unit.

When multiple objects coexist in one file:

- An auxiliary object should link to the lead object through a schema-valid relation (for example `depends_on`, `derived_from`, or `illustrates`).
- An object with unrelated downstream users must move to its own file.
- The linter warns when a file with `role: object-definitions` lists more than one entry in `exports`, on the convention that object-definition files expose one canonical object unless the multi-object form is justified.

````markdown
---
role: object-definitions
exports:
  - def.task_relevance
  - claim.task_relevance.invariance_criterion
namespace: defs.task_relevance
---

<!--gnomon:decl:object-->
```yaml
id: def.task_relevance
type: definition
title: "Task relevance of a representation"
```

<!--gnomon:statement-->
Statement for the lead object.
<!--gnomon:/statement-->
<!--gnomon:/decl:object-->

<!--gnomon:decl:object-->
```yaml
id: claim.task_relevance.invariance_criterion
type: claim
title: "Invariance criterion for task relevance"
depends_on:
  - id: def.task_relevance
    relation: requires
```

<!--gnomon:statement-->
Statement for the auxiliary object.
<!--gnomon:/statement-->
<!--gnomon:/decl:object-->
````

---

## Rejected formats

### Uniform Markdown XML ^t2-reject-uniform-markdown-xml

**Proposal.** Custom XML-like comment tags encode both file-level fields and object metadata, so one parser reads the whole file with no YAML at any layer.

**Why reject it.**

- File-level fields (`role`, `exports`, `namespace`) stored only in custom tags disappear from Obsidian frontmatter, so browsing, filtering by role, and editor schema checks on the file's identity all need custom tooling for what YAML frontmatter already exposes.
- XML-style metadata adds syntax without expressive gain over YAML, which already supports nested records, lists, and typed relations inside the in-body object declarations.
- The chosen format already uses Markdown declaration tags for object scopes; replacing the YAML payload inside those tags with XML attributes would burden hand-editing without changing the parser's responsibilities.

### Frontmatter-only file identity omitted ^t2-reject-frontmatter-identity-omitted

**Proposal.** Frontmatter stores only Obsidian fields (`tags`, `aliases`, `cssclasses`). The body's `gnomon:decl:object` wrappers carry every object's metadata, but the file declares no `role` or `exports`. Parsers infer everything from the body.

**Why reject it.**

- The file no longer declares its function at the top, so a reader scanning a folder cannot tell an object-definition file from a reasoning file, a rejection record, or a view specification without opening it. Dispatching on body inspection alone becomes fragile when a file's body is partial or in transition, and the single-export convention has no surface to attach to.
- Without an `exports` list, the parser has no entry-point hint into the body and must treat every declaration wrapper as equally addressable, which prevents files from holding internal scaffolding distinct from exposed declarations.

### YAML only ^t2-reject-yaml-only

**Proposal.** YAML stores both structured fields and prose fields.

**Why reject it.**

- Obsidian renders math in Markdown, not in YAML block scalars.
- Long prose inside YAML needs indentation and escaping discipline that makes manual edits worse.
- Proofs and examples become less readable because content structure competes with YAML structure.

```yaml
proof:
  - goal: "Solve the **equation** $f(x) = y$ for $x$."
  - id: p1
    parent: null
    content: |
      Rearrange the equation to isolate the unknown $x$:
      $$
      ax = bx + c \implies ax - bx = c
      $$
  - id: p2
    parent: p1
    content: |
      Factor out $x$:
      $$
      x(a - b) = c
      $$
  - id: p3
    parent: p2
    content: |
      Divide both sides by the coefficient of $x$:
      $$
      x = \frac{c}{a - b}
      $$
```

### Admonitions ^t2-reject-admonitions

**Proposal.** Custom admonitions such as `ad-goal` and `ad-proof-step` mark content fields.

**Why reject it.**

- Step metadata must live in ad hoc YAML fragments inside each admonition.
- Each proof step becomes a separate rendered block, which fragments the source file.
- Nested proof structure becomes harder to express than with explicit `gnomon:` tags.

```ad-todo
Solve the **equation** $f(x) = y$ for $x$.
```

```ad-done
id: p1
parent: null
---
Rearrange the equation to isolate the unknown $x$:
$$
ax = bx + c \implies ax - bx = c
$$
```

```ad-done
id: p2
parent: p1
---
Factor out $x$:
$$
x(a - b) = c
$$
```

```ad-done
id: p3
parent: p2
---
Divide both sides by the coefficient of $x$:
$$
x = \frac{c}{a - b}
$$
```
