# Note Template

This file defines the structural requirements for all notes in the repository. These are architectural rules, not stylistic preferences. Every note must satisfy them before output.

---

## Opening callout block

Every note opens with the following callouts in the fixed order shown. Each is optional except `[!QUESTION]`.

```
> [!QUOTE] Originality
> [!QUESTION] <inline title>?
> [!TIP] Roadmap
> [!WARNING] Applicability
> [!INFO] See also
---
```

### `[!QUOTE] Originality`

Two subsections, in order:

**Established results** (optional). Each bullet names a result, specifies the domain or literature where it is established, and ends with a period. Unanchored claims ("X is established", "X is standard") without a named domain are forbidden. Every link text in an established-results bullet must pass Operator 5: it names a result or mathematical object, not a note title.

**Contributions of this note** (mandatory). Each bullet must:
- name the mathematical object and the operation performed on it
- state the key result or implication
- be self-contained: a reader must understand what the note achieves without reading further
- end with a period

Forbidden in contribution bullets:
- the note as grammatical subject ("this note derives …", "this note establishes …")
- organizational descriptions that name the note's structure rather than its results ("five questions organize …", "a table collects …", "collected in a summary table") — a contribution states the insight the reader takes away, not the artifact that delivers it
- display-level formulas or `:=` definitions (contribution bullets must be readable without parsing notation; short symbol identifiers are permitted only when necessary for precision)
- numbered section references ("Sections 0–3", "Section 5") — name the content, not the number
- lists of assumptions (assumptions belong in `[!WARNING] Applicability`)
- results the note does not prove (unproven extensions belong in `[!WARNING]` or the body)
- descriptions of proof techniques without stating the result

Apply Operator 2 (concrete subject) to every contribution bullet without exception.

[mathematical object] + [active verb] + [result or implication]
The note is never the grammatical subject of a contribution bullet. The derivation procedure is never the grammatical object.

**Index notes (`_index.md`).** Contribution bullets must synthesize the module’s role in the parent project, using the parent project’s goals and sibling modules as context. They must not restate per-note contribution bullets or describe navigation/grouping ("this index organizes …", "the module groups notes …", "the index points to …"); that content belongs in the Roadmap. Omit **Established results** in index notes unless a module-level claim genuinely requires external context.

### `[!QUESTION] <inline title>?`

The inline title is a short central question ending with `?`. It frames the gap or tension that motivates the note. It does not state results.

The body is permitted only when the inline title alone cannot convey a necessary subquestion or success criterion. At most one such subquestion. The body must not describe what the note derives, establishes, or characterizes — those belong in `[!QUOTE] Contributions`.

### `[!TIP] Roadmap`

Include in notes with structured arguments across several sections. Omit in brief notes where the reasoning path is evident from the headings.

The Roadmap describes how the answer is obtained, not what the answer is.

Structure: one or two sentences stating the main mechanism or approach, then an optional numbered list where each item describes the role of one section — what it feeds to the next, what dependency it resolves, what intermediate result it establishes.

Roadmap opener rules:
- Do not start with "The roadmap …". Use a direct mechanism sentence (e.g., "To …, [object] is [operation] …"). Make it pedagogical and insight-level, not a list.
- Do not use an enumerative preview ("first …, then …, finally …") that repeats the numbered list or section overview.

Each item must:
- name its referent explicitly (section title or descriptive phrase)
- describe the section's logical function in the chain, not its result
- avoid novelty claims (all novelty belongs in `[!QUOTE] Contributions`)

Forbidden opener: a bare "It …" whose antecedent is ambiguous. Use the section title as the subject ("The [section title] …"), not a numbered reference ("Section 0/1/…").

### `[!WARNING] Applicability`

State note-level assumptions here, as bulleted items with **bold labels**. Each bullet: **Label.** sentence stating the assumption and its role or motivation.

Each bullet must state a constraint that the note actively imposes. Do not list features the note lacks or analyses it defers — the absence of an assumption is not itself an assumption. Non-requirements ("no equivariance is assumed", "no symmetry group is required") are vacuous and must be deleted. Do not reference sections by number.

For section-level assumptions, place a `[!WARNING]` callout at the top of that section, beginning with "In this section, …".

Do not use `[!IMPORTANT]` to wrap formal results or lemmas serving as assumptions.

### `[!INFO] See also`

**Purpose.** The See also callout flags external notes whose scope overlaps with the current note, so that a reader can distinguish the two. It is *not* a general navigation aid — the module index and frontmatter metadata already serve that role.

**Regular notes.** Include an entry only when an external note covers sufficiently similar material that a reader might confuse the two notes' responsibilities, or might look for content in the wrong note. Each entry is a Markdown link followed by a dash and a sentence stating how the external note's focus differs from the current note's. If no external note poses an overlap risk, omit the callout entirely.

Forbidden:

- Entries that list upstream dependencies or downstream consumers without overlap risk (these belong in body cross-references)
- Entries that describe an external note's content without stating its distinction from the current note
- Entries whose removal would leave the reader equally well oriented (the entry adds no disambiguation value)

Link-text rules: the link text must name a result, object, or mathematical property — not a note title. Apply Operator 5 to every link text.

**Index notes (`_index.md`).** The See also callout distinguishes sibling modules within the parent project: each entry names a sibling module and states how its scope differs from the current module's. Entries may also reference supporting materials (shared notations, registries, briefings) that serve the current module.

---

## Callout types

All Obsidian callout types are permitted. Type selection guide:

- `[!IMPORTANT]`: interpretive conclusions and key observations. Forbidden as a wrapper for formal results, theorems, or lemmas. Formal results belong in the note body as display statements with anchors.
- `[!EXAMPLE]`: concise worked examples. Long worked examples must not live inside a callout.
- `[!WARNING]`: scope limitations that are assumptions; boundary conditions after derivations
- `[!NOTE]`, `[!INFO]`, `[!TIP]`, `[!CHECK]`, `[!FAIL]`, `[!DANGER]`, `[!QUOTE]`: use the type that matches the semantic role

Multiple consecutive callouts are acceptable when each serves a distinct semantic role. Do not merge unrelated callouts to reduce their count. Do not restate the same applicability limitation in multiple callouts — state it once and cross-link.

---

## Section and heading rules

- Do not begin headings with the definite article "The". Exception: proper names, titles, and headings using "vs." or "&".
- Do not name document artifacts in headings. Headings like "Five questions", "Comparative table", or "Architecture-specific notes" name parts of the document, not the mathematical content. Use headings that name what the section delivers: "Analytic dimensions", "Comparative summary", "Population-structure hierarchy".
- Do not use numbered steps as headings ("Step 1:", "Step 2a:"). Use semantic, descriptive headings.
- Do not reference numbered steps in running text ("Step 3", "Steps 3–6"). Reference sections by semantic content or by link.
- Do not use numbered step outlines as a table of contents for the immediately following paragraphs. Either state the strategy in a single prose sentence or use the list as the actual content.
- Do not enumerate anonymous cases ("Case 1", "Case 2"). Use named cases with semantic labels.

---

## Body structure

Draft each section in dependency order:

1. Purpose and problem statement
2. Setup and definitions
3. General derivation
4. Result statement
5. Interpretation
6. Specializations and examples
7. Failure modes and boundary cases

A specialization must never precede the general result it instantiates. An interpretation must never precede the derivation it interprets. When a note treats multiple cases, the shared setup and general result must precede all case-specific sections.

---

## Non-redundancy requirements

Each interpretive point, result, or takeaway must appear exactly once.

Forbidden redundancy patterns:
- a preview paragraph at the start of a section restates what the section's conclusion will say
- a callout restates a consequence already stated in the surrounding prose
- a "Conclusions" paragraph paraphrases a result already stated in a display equation within the same section
- two sections make the same observation in different technical language
- the body restates a `[!QUOTE] Contributions` bullet without adding new interpretive content

A takeaway paragraph at the end of a section is justified only if it adds interpretive content (mechanistic implications, limiting cases, connections to other results) beyond the formal result. A takeaway that restates the result in words without adding insight must be deleted.

---

## Cross-reference and anchor rules

- Use block anchors (`^anchor-name`) for all cross-references. Heading-slug fragments (`#heading-name`) are forbidden.
- Place anchors on the first content line of the target, not on the heading.
- The `^anchor-name` token defines an anchor. It is not a reference. Do not use it as a reference in running text.
- Verify that every anchor name matches the content it targets semantically.
- If the target note lacks an anchor for the intended content, add one before linking.
- Do not use standalone "See [link]" sentences. Integrate references at the point of use with descriptive anchor text.
- Generic link texts such as "[Result (…)]" are forbidden. Every link text must pass Operator 5.
- Do not wrap a reference in a category word (`[the X result](…)`, `[the Y conditions](…)`, `[the Z theorem](…)`). Instead, integrate the reference as a descriptive sentence whose link text states what the referenced content says, not what kind of thing it is.

---

## Note modularity

- Maintain a single source note for each definition, lemma, proof, or derivation.
- Never duplicate derivations across notes.
- When content is needed elsewhere, add a cross-link to the source note.
- When content is moved to improve modularity, delete the duplicate and leave a pointer at the old location.
- Before drafting, decide: does the full derivation belong here, or does only a pointer belong here? Do not mix both.
- If a section recalls results from other notes, recall only the minimal formula or lemma needed for the next step, then derive a conclusion specific to the current question. Do not write survey-style compilations inside an analytic note.

---

## Summary tables

When a note derives results across multiple cases, include a summary table collecting the key formulas or scalings. A summary table is not redundant with the derivation; it enables synthetic comparison.

---

## Index-entry descriptions (`_index.md`)

Each item in an index file has a dash-separated description after the link. Requirements:

- Open with a functional subject that names what is at stake (a process, a functional role, a structural distinction), not the technical object that implements it.
- Use a count noun before enumerations: "Three network structures produce …", not "Single population, commutative multi-population, … produce …".
- Two sentences maximum: the first states the primary functional effect or structural insight; the optional second states the key consequence or differentiating features.
