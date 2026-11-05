"""
Record schemas: the base schema of each record type, its bound contract, and its template.

A base schema declares the fields of one record type under JSON Schema draft 2020-12, written in
YAML, and leaves each closed vocabulary open. Its contract composes the base, fixes the binding
``_schema`` to ``gnomon:<type>@<version>``, and writes each closed vocabulary from the vocabulary
registry. The template of the record type is rendered from the base schema and the registry, so
that each field, each placeholder and each guidance is declared once, as the decision on record
schemas states.

Besides the standard keywords, a base schema carries the keywords that render its template:

- ``x-template``: the placeholder written after the key of a field;
- ``x-comment``: the guidance written in the comment of the line of a field;
- ``x-vocabulary``: the key of the registry that declares the closed vocabulary of a field;
- ``x-blank``: a blank line before the field;
- ``x-template-key``: the placeholder key of a mapping whose keys are free, such as ``maturity``;
- ``x-header``, at the root: the comment lines that open the template.

See Also
--------
gnomon.cli : the command ``schemas``, which writes or checks the generated files.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import Any, Mapping

import yaml

from .identifiers import RECORD_SEGMENTS, identifier_pattern

DATA = Path(__file__).parent / "data"

#: The folder of the base schemas and of their contracts.
SCHEMAS = DATA / "schemas"

#: The folder of the templates, rendered from the base schemas.
TEMPLATES = DATA / "templates"

#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"

#: The namespace of the logical identifiers of the contracts.
NAMESPACE = "gnomon"

#: The prefix of the absolute identifier of each schema file.
BASE_URI = "https://github.com/esther-poniatowski/gnomon/schemas"

#: The column at which the comment of a line opens, unless the line is longer.
COMMENT_COLUMN = 33

#: The width beyond which a line separates its comment by three spaces instead.
COMMENT_WIDTH = 30

#: The keywords that render a template, which a contract does not repeat.
TEMPLATE_KEYWORDS = (
    "x-template",
    "x-comment",
    "x-vocabulary",
    "x-blank",
    "x-template-key",
    "x-header",
)


Options = Mapping[str, list[tuple[str, str]]]


def base_path(kind: str) -> Path:
    """Return the file of the base schema of a record type."""
    return SCHEMAS / f"{kind}.base.schema.yml"


def contract_path(kind: str) -> Path:
    """Return the file of the contract of a record type."""
    return SCHEMAS / f"{kind}.contract.schema.yml"


def kinds() -> list[str]:
    """Return the record types that declare a base schema, in alphabetical order."""
    return sorted(
        path.name.removesuffix(".base.schema.yml") for path in SCHEMAS.glob("*.base.schema.yml")
    )


@cache
def load_base(kind: str) -> dict[str, Any]:
    """Return the base schema of a record type, read once; callers do not modify it."""
    schema: dict[str, Any] = yaml.safe_load(base_path(kind).read_text(encoding="utf-8"))
    return schema


def vocabulary_options(kind: str, source: Path | None = None) -> dict[str, list[tuple[str, str]]]:
    """Return, per field of a record type, its admitted values with their glosses.

    >>> options = vocabulary_options("answer")
    >>> options[".status"][0]
    ('entertained', '')
    """
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    return {
        name: [(str(entry["value"]), str(entry.get("name") or "")) for entry in values]
        for name, values in fields.items()
    }


def comment_of(field: Mapping[str, Any], options: Options) -> str:
    """Return the comment of a field: its admitted values, then its guidance.

    >>> comment_of({"x-vocabulary": "x", "x-comment": "the attitude"},
    ...            {"x": [("a", ""), ("b", "gloss")]})
    'a | b (gloss); the attitude'
    """
    guidance = str(field.get("x-comment") or "")
    vocabulary = field.get("x-vocabulary")
    if not vocabulary:
        return guidance
    listed = " | ".join(
        f"{value} ({name})" if name else value for value, name in options[str(vocabulary)]
    )
    return f"{listed}; {guidance}" if guidance else listed


def line(text: str, comment: str) -> str:
    """Return one line of a template, with its comment aligned at the comment column."""
    if not comment:
        return text
    gap = COMMENT_COLUMN - len(text) if len(text) < COMMENT_WIDTH else 3
    return f"{text}{' ' * gap}# {comment}"


def head(key: str, field: Mapping[str, Any]) -> str:
    """Return the key of a field followed by its placeholder."""
    raw = field.get("x-template")
    return f"{key}: {raw}" if raw not in (None, "") else f"{key}:"


class _TemplateLines:
    """The lines of a template being rendered, and the vocabulary options that its comments list."""

    def __init__(self, options: Options) -> None:
        self.options = options
        self.out: list[str] = []

    def add_field(self, key: str, spec: Mapping[str, Any], indent: int, dash: bool = False) -> None:
        """Append the lines of one field, and of the fields that it holds."""
        if spec.get("x-blank"):
            self.out.append("")
        prefix = " " * indent + ("- " if dash else "")
        inner = indent + 2 if dash else indent
        comment = comment_of(spec, self.options)
        properties = spec.get("properties")
        items = spec.get("items")
        free = spec.get("additionalProperties")
        if isinstance(properties, Mapping) and spec.get("x-template") in (None, ""):
            self.out.append(line(prefix + key + ":", comment))
            for name, child in properties.items():
                self.add_field(name, child, inner + 2)
        elif isinstance(items, Mapping) and spec.get("x-template") in (None, ""):
            self.out.append(line(prefix + key + ":", comment))
            self.add_item(items, inner + 2)
        elif isinstance(free, Mapping) and free.get("x-template-key"):
            self.out.append(line(prefix + key + ":", comment))
            self.out.append(
                line(
                    " " * (inner + 2) + head(str(free["x-template-key"]), free),
                    comment_of(free, self.options),
                )
            )
        else:
            self.out.append(line(prefix + head(key, spec), comment))

    def add_item(self, items: Mapping[str, Any], indent: int) -> None:
        """Append the lines of the one entry that a template list shows."""
        properties = items.get("properties")
        if isinstance(properties, Mapping) and properties:
            for position, (name, child) in enumerate(properties.items()):
                self.add_field(name, child, indent + (2 if position else 0), dash=not position)
        else:
            self.out.append(
                line(
                    " " * indent + f"- {items.get('x-template', '')}",
                    comment_of(items, self.options),
                )
            )


def render_template(kind: str, base: Mapping[str, Any], options: Options) -> str:
    """Return the template of a record type, opened by the binding to its contract and rendered from
    its base schema."""
    lines = _TemplateLines(options)
    lines.out += [f"# {text}" if text else "#" for text in base.get("x-header") or []]
    if lines.out:
        lines.out.append("")
    lines.out.append(f"_schema: {identifier(kind, int(base.get('x-version', 1)))}")
    for name, spec in (base.get("properties") or {}).items():
        lines.add_field(name, spec, 0)
    return "\n".join(lines.out) + "\n"


def overlay(field: Mapping[str, Any], options: Options) -> dict[str, Any] | None:
    """Return the constraints that a contract adds to a field, deep: the values of its vocabulary,
    and the keys that an object may hold.

    The keys are closed by ``propertyNames``, since each subschema of ``allOf`` is validated alone,
    so ``additionalProperties`` in the contract would reject the keys that the base declares.
    """
    added: dict[str, Any] = {}
    vocabulary = field.get("x-vocabulary")
    if vocabulary:
        added["enum"] = [value for value, _ in options[str(vocabulary)]] + [None]
    declared = field.get("properties")
    if isinstance(declared, Mapping) and declared:
        added["propertyNames"] = {"enum": list(declared)}
    nested = {
        name: sub
        for name, child in (field.get("properties") or {}).items()
        if (sub := overlay(child, options))
    }
    if nested:
        added["properties"] = nested
    items = field.get("items")
    if isinstance(items, Mapping) and (sub := overlay(items, options)):
        added["items"] = sub
    free = field.get("additionalProperties")
    if isinstance(free, Mapping) and (sub := overlay(free, options)):
        added["additionalProperties"] = sub
    return added or None


def vocabulary_paths(base: Mapping[str, Any]) -> dict[str, str]:
    """Return the vocabulary bound to each closed field of a base schema, keyed by the path of the
    field.

    The path joins the keys from the root with dots; an entry of a list adds no segment.

    >>> vocabulary_paths({"properties": {"status": {"x-vocabulary": ".status"},
    ...     "laws": {"items": {"properties": {"role": {"x-vocabulary": "laws.role"}}}}}})
    {'status': '.status', 'laws.role': 'laws.role'}
    """
    bound: dict[str, str] = {}

    def walk(node: Mapping[str, Any], path: tuple[str, ...]) -> None:
        for name, child in (node.get("properties") or {}).items():
            if not isinstance(child, Mapping):
                continue
            if child.get("x-vocabulary"):
                bound[".".join((*path, name))] = str(child["x-vocabulary"])
            walk(child, (*path, name))
        items = node.get("items")
        if isinstance(items, Mapping):
            walk(items, path)

    walk(base, ())
    return bound


def identifier(kind: str, version: int) -> str:
    """Return the logical identifier of the contract of a record type."""
    return f"{NAMESPACE}:{kind}@{version}"


def identifier_prefix(base: Mapping[str, Any]) -> str | None:
    """Return the prefix of the identifiers of a record type, read from the placeholder of its
    field ``id``, or None when the type declares no identifier.

    >>> identifier_prefix({"properties": {"id": {"x-template": "quest.TOPIC.NAME"}}})
    'quest'
    """
    template = ((base.get("properties") or {}).get("id") or {}).get("x-template")
    return str(template).split(".", 1)[0] if template else None


def contract(kind: str, base: Mapping[str, Any], options: Options) -> dict[str, Any]:
    """Return the contract of a record type: the base, the binding of ``_schema``, and its
    vocabularies."""
    version = int(base.get("x-version", 1))
    schema: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"{BASE_URI}/{kind}.contract.schema.yml",
        "title": f"{base.get('title', kind)} contract",
        "description": f"The record type `{kind}`, bound to `{identifier(kind, version)}`,"
        " with its closed vocabularies.",
        "allOf": [{"$ref": str(base["$id"])}],
        "required": ["_schema"],
        "properties": {
            "_schema": {
                "const": identifier(kind, version),
                "title": "Schema",
                "description": "The logical identifier of the contract that the record follows.",
            },
            "type": {"const": kind},
        },
        "x-identifier": base.get("x-identifier", "id"),
    }
    prefix = identifier_prefix(base)
    if prefix in RECORD_SEGMENTS:
        schema["properties"]["id"] = {"pattern": identifier_pattern(str(prefix))}
    added = overlay(base, options)
    if added and "properties" in added:
        schema["properties"].update(added["properties"])
    schema["propertyNames"] = {"enum": ["_schema", *(base.get("properties") or {})]}
    return schema


def dump(document: Mapping[str, Any]) -> str:
    """Return a schema written in YAML, keys in their declared order."""
    return yaml.safe_dump(dict(document), sort_keys=False, allow_unicode=True, width=100)


def generated_files() -> dict[Path, str]:
    """Return every file generated from the base schemas and the registry, with its content."""
    files: dict[Path, str] = {}
    for kind in kinds():
        base, options = load_base(kind), vocabulary_options(kind)
        files[contract_path(kind)] = (
            f"# Generated by `gnomon schemas` from `{kind}.base.schema.yml` and the vocabulary"
            " registry. Edit those, not this file.\n" + dump(contract(kind, base, options))
        )
        files[TEMPLATES / f"{kind}.yml"] = render_template(kind, base, options)
    return files


@cache
def identifier_prefixes() -> dict[str, str]:
    """Return the prefix of the identifiers of each record type that declares one, keyed by the
    value of its field ``type``.

    >>> identifier_prefixes()["target-system"], identifier_prefixes()["question"]
    ('system', 'quest')
    """
    found: dict[str, str] = {}
    for kind in kinds():
        base = load_base(kind)
        prefix = identifier_prefix(base)
        if prefix:
            found[str(base["properties"]["type"]["x-template"])] = prefix
    return found


def record_kinds() -> dict[str, str]:
    """Return the base schema of each record type, keyed by the value of the field ``type``."""
    return {str(load_base(kind)["properties"]["type"]["x-template"]): kind for kind in kinds()}


@cache
def contract_validator(kind: str) -> Any:
    """Return the validator of the contract of a record type, which resolves the base schemas."""
    # pylint: disable=import-outside-toplevel  # jsonschema loads only when a record is validated
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource

    resources = [
        (load_base(name)["$id"], Resource.from_contents(load_base(name))) for name in kinds()
    ]
    return Draft202012Validator(
        yaml.safe_load(contract_path(kind).read_text(encoding="utf-8")),
        registry=Registry().with_resources(resources),
    )


def record_errors(record: Mapping[str, Any]) -> list[str]:
    """Return every violation of the contract that a record names in its field ``_schema``.

    A record names no contract, or a contract that `gnomon` does not publish, when its binding is
    missing or unknown; each other error states the path of the field and the violated keyword.
    """
    named = record.get("_schema")
    published = {
        identifier(kind, int(load_base(kind).get("x-version", 1))): kind for kind in kinds()
    }
    if not named:
        return ["_schema: the record names no contract"]
    if named not in published:
        return [f"_schema: {named} is no contract of {NAMESPACE}"]
    validator = contract_validator(published[named])
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '(record)'}: {error.message}"
        for error in sorted(
            validator.iter_errors(dict(record)), key=lambda e: list(map(str, e.absolute_path))
        )
    ]


def stale_files() -> list[Path]:
    """Return every generated file whose content differs from its generated form."""
    return [
        path
        for path, text in generated_files().items()
        if not path.is_file() or path.read_text(encoding="utf-8") != text
    ]
