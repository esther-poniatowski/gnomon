"""Record schemas: the generated files match their sources, and the schemas are valid and complete.

The base schemas are the source of the fields, and the vocabulary registry the source of the closed
vocabularies, so the contracts and the templates are generated copies. These tests check that each
copy equals its generated form, that every schema is valid under draft 2020-12, and that each
contract writes the vocabularies of the registry.
"""

from __future__ import annotations

from typing import Any, Mapping

import pytest
import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from gnomon import schemas
from gnomon.generated import stale_files

KINDS = schemas.kinds()


def registry() -> Registry:
    """Return the resources of every base schema, keyed by its absolute identifier."""
    resources = [
        (schemas.load_base(kind)["$id"], Resource.from_contents(schemas.load_base(kind)))
        for kind in KINDS
    ]
    return Registry().with_resources(resources)


def test_every_generated_file_equals_its_generated_form() -> None:
    assert stale_files() == []


@pytest.mark.parametrize("kind", KINDS)
def test_the_base_schema_and_the_contract_are_valid(kind: str) -> None:
    Draft202012Validator.check_schema(schemas.load_base(kind))
    Draft202012Validator.check_schema(
        yaml.safe_load(schemas.contract_path(kind).read_text(encoding="utf-8"))
    )


def enums(node: Mapping[str, Any], path: str = "") -> dict[str, list[Any]]:
    """Return every vocabulary that a contract writes, keyed by the path of its field."""
    found = {path: list(node["enum"])} if "enum" in node else {}
    for key, child in (node.get("properties") or {}).items():
        found.update(enums(child, f"{path}.{key}" if path else key))
    for key in ("items", "additionalProperties"):
        if isinstance(node.get(key), Mapping):
            found.update(enums(node[key], f"{path}[]"))
    return found


@pytest.mark.parametrize("kind", KINDS)
def test_each_vocabulary_of_the_registry_is_bound_by_a_field_of_its_schema(kind: str) -> None:
    """A vocabulary that no field binds is checked nowhere, since a field selects its vocabulary by
    path."""
    record_type = schemas.load_base(kind)["properties"]["type"]["x-template"]
    bound = set(schemas.vocabulary_paths(schemas.load_base(kind)).values())
    assert set(schemas.vocabulary_options(record_type)) - bound == set()


@pytest.mark.parametrize("kind", KINDS)
def test_each_vocabulary_of_the_contract_is_its_registry_entry(kind: str) -> None:
    """Every field that names a registry key receives exactly the values of that key, and null."""
    base = schemas.load_base(kind)
    record_type = base["properties"]["type"]["x-template"]
    options = schemas.vocabulary_options(record_type)
    linked: dict[str, list[Any]] = {}

    def walk(node: Mapping[str, Any], path: str) -> None:
        if node.get("x-vocabulary"):
            linked[path] = [value for value, _ in options[node["x-vocabulary"]]] + [None]
        for key, child in (node.get("properties") or {}).items():
            walk(child, f"{path}.{key}" if path else key)
        for key in ("items", "additionalProperties"):
            if isinstance(node.get(key), Mapping):
                walk(node[key], f"{path}[]")

    walk(base, "")
    contract = yaml.safe_load(schemas.contract_path(kind).read_text(encoding="utf-8"))
    assert enums(contract) == linked
    assert contract["properties"]["_schema"]["const"] == schemas.identifier(kind, base["x-version"])


ROOT = schemas.DATA.parents[2]
RECORDS = sorted(
    (path, record)
    for path in (ROOT / "examples").glob("*/*.yml")
    if isinstance(record := yaml.safe_load(path.read_text(encoding="utf-8")), dict)
    and record.get("type") in schemas.record_kinds()
)


CASES = [
    pytest.param(path, record, id=f"{path.parent.name}/{path.name}") for path, record in RECORDS
]


@pytest.mark.parametrize("path, record", CASES)
def test_every_worked_record_follows_its_contract(path: Any, record: dict[str, Any]) -> None:
    assert record.get("_schema"), f"{path} names no contract"
    assert schemas.record_errors(record) == []


def test_a_record_that_breaks_its_contract_is_reported() -> None:
    record = {"_schema": "gnomon:problem@1", "type": "problem", "id": "prob.a.b", "status": "posed"}
    assert schemas.record_errors(record) == []
    assert schemas.record_errors({**record, "status": "pending"})[0].startswith(
        "status: 'pending' is not one of"
    )
    assert schemas.record_errors({**record, "type": "question"}) == ["type: 'problem' was expected"]
    assert schemas.record_errors({**record, "statement": 3}) == [
        "statement: 3 is not of type 'string', 'null'"
    ]
    assert schemas.record_errors({"type": "problem"}) == ["_schema: the record names no contract"]
    assert schemas.record_errors({**record, "_schema": "gnomon:problem@9"}) == [
        "_schema: gnomon:problem@9 is no contract of gnomon"
    ]


def test_a_key_that_the_contract_does_not_declare_is_reported() -> None:
    """A misspelled key would otherwise pass as an unknown field, at the root and at any depth."""
    record = {"_schema": "gnomon:concept@1", "type": "concept", "id": "concept.a.b"}
    assert schemas.record_errors({**record, "glos": "x"})[0].startswith(
        "(record): 'glos' is not one of"
    )
    nested = {**record, "confusions": [{"with": "fixed point"}]}
    assert schemas.record_errors(nested)[0].startswith("confusions.0: 'with' is not one of")
    assert schemas.record_errors({**record, "confusions": [{"other": "fixed point"}]}) == []
