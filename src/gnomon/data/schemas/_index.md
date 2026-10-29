---
tags:
  - index
aliases:
  - Record schema files
---
# Record schemas

The schemas of this folder declare the shape of each record type, so that a program validates a record and Ekphrasis renders it as a form, as the [decision on record schemas](../../../../docs/adr/record-schemas.md) states.

> [!IMPORTANT] One entry per schema
> Each entry gives the logical identifier `gnomon:<type>@<version>` of its schema, and is added in the edit that writes the schema.
