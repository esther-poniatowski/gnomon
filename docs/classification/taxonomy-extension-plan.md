---
tags:
  - gaps
index: "[Classification](docs/classification/_index.md)"
aliases:
  - Taxonomy extension plan
---
# Extending the feature system into a taxonomy

> [!QUESTION] Goal: Which additional structures and decisions turn the current qualitative feature system into an explicit taxonomy?

The [current construction procedure](construction-procedure.md) produces a feature system. Its output records the analyzed objects and their operational feature profiles. The output also states dependencies supported by the analyzed table. A taxonomy requires a further representational layer:

- a set of **taxa** $T$;
- a **membership relation** $\mu\subseteq U\times T$, or a single-valued assignment $c:U\to T$ when the taxa form a partition;
- a **hierarchy relation** $\preceq$ on $T$ when the taxonomy orders taxa by a declared criterion.

The feature system describes objects and relations among descriptors. The taxonomy groups or orders objects through taxa. Neither a reduced feature set nor a dependency basis selects the taxa without an additional construction rule. Standard classification methodology likewise selects classifying variables separately from constructing groups ([Bailey, 1994](https://books.google.ca/books/about/Typologies_and_Taxonomies.html?id=1TaYulGjhLYC)).

==FIX: [taxonomy-extension · implemented-review] Review the distinction between the current feature-system output and the proposed taxonomy layer, then select a construction route before the layer is added to the main procedure.==

## Proposed routes

| Route | Taxa | Membership | Hierarchy | Additional commitment |
| --- | --- | --- | --- | --- |
| Exact-profile partition | Equivalence classes of $\operatorname{IND}(R)$ for a retained raw attribute set $R$ | Each object belongs to the unique class with its recorded $R$-profile | A hierarchy requires a documented sequence of coarser attribute sets or partitions | Treating identical retained profiles as one taxon; the rough-set indiscernibility relation supplies the partition for a fixed $R$ ([Pawlak, 1982](https://link.springer.com/article/10.1007/BF01001956)) |
| FCA concept hierarchy | Selected formal concepts, represented by extents and intents | An object belongs to each selected concept whose extent contains it | Extent inclusion supplies a concept lattice; the lattice is generally a partial order rather than a tree | A concept-selection rule, because the full lattice can contain many overlapping candidate taxa ([Ganter and Wille, 1999](https://link.springer.com/book/10.1007/978-3-642-59830-2)) |
| Similarity-based clustering | Clusters induced from object dissimilarities | The clustering rule yields crisp or graded cluster membership | Hierarchical clustering can yield a dendrogram; a cut rule selects operational taxa | A fully specified dissimilarity, including attribute weights and a stopping criterion |
| Purpose-indexed classification | Classes defined relative to an external task | A learned or stipulated classifier assigns objects to taxa | A tree or ordered class system requires a separately justified structure | Training targets plus an objective and an out-of-sample validation design |

The exact-profile route is the narrowest extension of the present Rough Set formalism. The FCA route is the narrowest route to an intensional partial order. The similarity and purpose-indexed routes introduce modeling structure that the present crisp table does not determine.

## Construction contract to add

The extension should add five explicit steps after feature-system validation:

1. Declare the taxonomic function and choose one route.
2. Define the taxon identity criterion and construct $T$.
3. Define $\mu$ or $c$, including the rule for a new object.
4. Define the hierarchy relation and verify its required properties.
5. Validate the taxonomy against the declared function.

The resulting guarantees must name their level. Table-level guarantees concern the finite analyzed objects. Assignment guarantees concern new objects under a stated membership rule. Domain-level claims require sampling or expert assumptions beyond the current procedure.

## Open design decisions

- Must each object belong to exactly one taxon, or may taxa overlap?
- Must the hierarchy be a tree, or is a partial order admissible?
- Which proposed route should construct $T$?
- What rule assigns a previously unseen object, and what evidence validates that rule?
