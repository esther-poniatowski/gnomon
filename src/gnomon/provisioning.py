"""Provision the complete schema closure used by Gnomon records and views.

The package owns the installed bytes.  A vault receives copies under caller-selected,
vault-relative paths and a registry whose paths refer only to those copies.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urldefrag, urlsplit

import yaml

from . import data_path


class ProvisioningError(ValueError):
    """A requested vault layout is unsafe or conflicts with an existing file."""


@dataclass(frozen=True)
class ProvisioningResult:
    """Summary of one completed provisioning operation."""

    registry: PurePosixPath
    schema_directory: PurePosixPath
    schema_count: int
    written_count: int
    unchanged_count: int


def _relative_vault_path(value: str, *, label: str) -> PurePosixPath:
    """Return a normalized path that cannot leave the vault."""
    if not value or "\\" in value:
        raise ProvisioningError(f"{label} must be a non-empty vault-relative POSIX path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path == PurePosixPath("."):
        raise ProvisioningError(f"{label} must stay inside the vault: {value}")
    return path


def _read_schema(path: Path) -> tuple[bytes, dict[str, Any]]:
    """Return the exact bytes and parsed mapping of one packaged schema."""
    content = path.read_bytes()
    parsed = yaml.safe_load(content)
    if not isinstance(parsed, dict):
        raise ProvisioningError(f"packaged schema is not a mapping: {path}")
    return content, parsed


def _contract_identifier(schema: dict[str, Any]) -> str | None:
    """Return the logical contract fixed by a schema, when it fixes one."""
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return None
    binding = properties.get("_schema")
    if not isinstance(binding, dict):
        return None
    identifier = binding.get("const")
    return identifier if isinstance(identifier, str) else None


def _absolute_references(value: Any) -> set[str]:
    """Return the document identities named by absolute references below ``value``."""
    if isinstance(value, dict):
        references = set()
        reference = value.get("$ref")
        if isinstance(reference, str) and urlsplit(reference).scheme:
            references.add(urldefrag(reference).url)
        for child in value.values():
            references.update(_absolute_references(child))
        return references
    if isinstance(value, list):
        references = set()
        for child in value:
            references.update(_absolute_references(child))
        return references
    return set()


def _register_unique(mapping: dict[str, str], key: str, path: PurePosixPath) -> None:
    """Register one identity and reject two packaged files that claim it."""
    rendered = path.as_posix()
    previous = mapping.setdefault(key, rendered)
    if previous != rendered:
        raise ProvisioningError(
            f"packaged identity {key!r} is duplicated by {previous} and {rendered}"
        )


def _schema_sources(package_data: Path) -> list[tuple[Path, PurePosixPath]]:
    """Return each packaged schema with its provider-qualified destination."""
    owned_root = package_data / "schemas"
    dependency = package_data / "resources" / "ekthesis-export.schema.yaml"
    if not owned_root.is_dir() or not dependency.is_file():
        raise ProvisioningError("the installed Gnomon package does not contain its schema closure")
    owned = sorted(
        source
        for source in owned_root.rglob("*")
        if source.name.endswith((".schema.yml", ".schema.yaml", ".schema.json"))
    )
    sources = [
        (source, PurePosixPath("gnomon") / source.relative_to(owned_root).as_posix())
        for source in owned
    ]
    sources.append((dependency, PurePosixPath("ekthesis/export.schema.yaml")))
    return sources


def _provisioned_files(
    schema_directory: PurePosixPath,
) -> tuple[dict[PurePosixPath, bytes], dict[str, str], dict[str, str]]:
    """Build the vault files and registry mappings from installed package data."""
    outputs: dict[PurePosixPath, bytes] = {}
    contracts: dict[str, str] = {}
    resources: dict[str, str] = {}
    references: set[str] = set()
    for source, relative in _schema_sources(data_path()):
        destination = schema_directory / relative
        content, schema = _read_schema(source)
        outputs[destination] = content
        contract = _contract_identifier(schema)
        if contract is not None:
            _register_unique(contracts, contract, destination)
        identity = schema.get("$id")
        if isinstance(identity, str) and urlsplit(identity).scheme:
            _register_unique(resources, identity, destination)
        references.update(_absolute_references(schema))

    missing = sorted(references - resources.keys())
    if missing:
        raise ProvisioningError(
            "the installed schema closure leaves absolute references unresolved: "
            + ", ".join(missing)
        )

    return outputs, dict(sorted(contracts.items())), dict(sorted(resources.items()))


def _registry_bytes(contracts: dict[str, str], resources: dict[str, str]) -> bytes:
    """Serialize a registry accepted by Ekphrasis and independent of a checkout."""
    registry = {
        "_schema": "kleisis:schema-registry@2",
        "schemas": contracts,
        "resources": resources,
    }
    return yaml.safe_dump(registry, sort_keys=False, allow_unicode=True, width=100).encode()


def _target_path(vault: Path, relative: PurePosixPath) -> Path:
    """Return a target whose existing path components do not escape through a symlink."""
    target = vault.joinpath(*relative.parts)
    ancestor = target.parent
    while not ancestor.exists():
        ancestor = ancestor.parent
    if not ancestor.resolve().is_relative_to(vault):
        raise ProvisioningError(f"configured path leaves the vault through a symlink: {relative}")
    if target.is_symlink() and not target.resolve().is_relative_to(vault):
        raise ProvisioningError(f"configured path leaves the vault through a symlink: {relative}")
    return target


def _write_files(vault: Path, files: dict[PurePosixPath, bytes], *, force: bool) -> tuple[int, int]:
    """Preflight conflicts, then write changed outputs and count retained outputs."""
    targets = {path: _target_path(vault, path) for path in files}
    conflicts = [
        path
        for path, content in files.items()
        if targets[path].exists() and targets[path].read_bytes() != content
    ]
    if conflicts and not force:
        rendered = ", ".join(path.as_posix() for path in sorted(conflicts))
        raise ProvisioningError(
            f"existing files differ; rerun with --force to replace them: {rendered}"
        )

    written = 0
    unchanged = 0
    for relative, content in files.items():
        target = targets[relative]
        if target.exists() and target.read_bytes() == content:
            unchanged += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        written += 1
    return written, unchanged


def provision_schemas(
    vault: Path,
    *,
    registry: str = ".gnomon/schema-registry.yml",
    schema_directory: str = ".gnomon/schemas",
    force: bool = False,
) -> ProvisioningResult:
    """Install a relocatable registry and its complete schema closure in ``vault``.

    Existing identical files are retained.  A differing file stops the operation before any
    write unless ``force`` is true, because the requested paths may contain user-owned content.
    """
    vault = vault.resolve()
    if not vault.is_dir():
        raise ProvisioningError(f"vault is not an existing directory: {vault}")
    registry_path = _relative_vault_path(registry, label="registry path")
    schema_path = _relative_vault_path(schema_directory, label="schema directory")
    if schema_path.is_relative_to(registry_path):
        raise ProvisioningError("registry path cannot be an ancestor of the schema directory")
    files, contracts, resources = _provisioned_files(schema_path)
    if registry_path in files:
        raise ProvisioningError("registry path overlaps a provisioned schema")
    files[registry_path] = _registry_bytes(contracts, resources)
    written, unchanged = _write_files(vault, files, force=force)

    return ProvisioningResult(
        registry=registry_path,
        schema_directory=schema_path,
        schema_count=len(files) - 1,
        written_count=written,
        unchanged_count=unchanged,
    )
