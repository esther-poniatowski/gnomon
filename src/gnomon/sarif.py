"""
Write findings as a log of the findings profile of Elenchos, a subset of SARIF 2.1.0.

The log holds one run of the driver ``gnomon``, whose driver lists every rule of the catalogue.
Each result names its rule, its level and its message, the file holding the record as a physical
location relative to ``SRCROOT``, and one logical location ``<resource>#<locus>``. The checks know
no line or column, so no result holds a region, and a physical location denotes the whole file.
The gate builds the identity of each result and writes its suppressions; a producer writes
neither.

The run holds one invocation, which states whether the analysis ran to its end. A run that could
not read every record, or stopped on an error, declares a failed invocation with one notification
of level ``error`` stating why.

See Also
--------
gnomon.findings : the findings and the catalogue of their rules.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, Sequence
from urllib.parse import quote

from .findings import RULES, Finding

SARIF_VERSION = "2.1.0"
SARIF_SCHEMA = (
    "https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/schemas/sarif-schema-2.1.0.json"
)
TOOL_NAME = "gnomon"
URI_BASE_ID = "SRCROOT"
DISCRIMINATOR_KEY = "discriminator/v1"
LEVEL = "error"
"""Every finding of gnomon fails its check, so every rule and result has level error."""

# The characters of an RFC 3986 path segment kept as written, besides unreserved characters: the
# sub-delimiters and ``@``. A colon is encoded, so that a first segment never reads as a scheme.
_URI_SAFE = "/!$&'()*+,;=@"


@dataclass(frozen=True)
class Located:
    """A finding placed in the file and the record that hold it.

    Attributes
    ----------
    finding : Finding
        The defect, located inside its record.
    file : PurePosixPath
        The path of the file, relative to the root of the repository.
    record : str or None
        The identifier of the record, or None for a file that holds no record, such as a registry.
    """

    finding: Finding
    file: PurePosixPath
    record: str | None = None

    def __post_init__(self) -> None:
        if self.file.is_absolute() or ".." in self.file.parts or not self.file.parts:
            raise ValueError(f"not a repository-relative path: {self.file}")


def _escape(name: str) -> str:
    """Write ``%`` as ``%25`` and ``#`` as ``%23``, so that a name splits at its first ``#``."""
    return name.replace("%", "%25").replace("#", "%23")


def resource(located: Located) -> str:
    """Return ``id:<record>`` for a record, and ``path:<file>`` for any other file."""
    if located.record is not None:
        return f"id:{located.record}"
    return f"path:{located.file.as_posix()}"


def logical_name(located: Located) -> str:
    """Return the escaped resource, followed by ``#<locus>`` when the locus is not empty.

    >>> from gnomon.findings import ITINERARY_CYCLE, Finding
    >>> found = Finding(ITINERARY_CYCLE, ("steps",), "steps: a -> a forms a cycle")
    >>> logical_name(Located(found, PurePosixPath("p/itinerary.yml"), "itin.50%#a"))
    'id:itin.50%25%23a#/steps'
    """
    name = _escape(resource(located))
    locus = located.finding.locus
    return f"{name}#{locus}" if locus else name


def artifact_uri(located: Located) -> str:
    """Return the path of the file percent-encoded as a relative URI reference.

    >>> from gnomon.findings import ITINERARY_CYCLE, Finding
    >>> artifact_uri(Located(Finding(ITINERARY_CYCLE, (), ""), PurePosixPath("a b/c:d#.yml")))
    'a%20b/c%3Ad%23.yml'
    """
    return quote(located.file.as_posix(), safe=_URI_SAFE)


def _result(located: Located) -> dict[str, Any]:
    found = located.finding
    result: dict[str, Any] = {
        "ruleId": found.rule.id,
        "level": LEVEL,
        "message": {"text": found.text},
        "locations": [
            {
                "physicalLocation": {
                    "artifactLocation": {"uri": artifact_uri(located), "uriBaseId": URI_BASE_ID}
                },
                "logicalLocations": [{"name": logical_name(located)}],
            }
        ],
    }
    if found.discriminator:
        result["partialFingerprints"] = {DISCRIMINATOR_KEY: found.discriminator}
    return result


def invocation(stopped: str | None) -> dict[str, Any]:
    """Return the invocation of a run, failed with the reason ``stopped`` when it is given."""
    if stopped is None:
        return {"executionSuccessful": True}
    return {
        "executionSuccessful": False,
        "toolExecutionNotifications": [{"level": "error", "message": {"text": stopped}}],
    }


def sarif_log(
    findings: Sequence[Located], version: str, stopped: str | None = None
) -> dict[str, Any]:
    """Return the log of one run of gnomon of ``version``, with one result per finding.

    ``stopped`` states why the analysis did not run to its end, and is None for a complete run. The
    analysis begins once the records are listed, so ``results`` is always written: it holds every
    finding detected before the stop, and is empty when there is none.
    """
    rules = [
        {
            "id": rule.id,
            "shortDescription": {"text": rule.description},
            "defaultConfiguration": {"level": LEVEL},
        }
        for rule in RULES
    ]
    return {
        "version": SARIF_VERSION,
        "$schema": SARIF_SCHEMA,
        "runs": [
            {
                "tool": {"driver": {"name": TOOL_NAME, "version": version, "rules": rules}},
                "invocations": [invocation(stopped)],
                "columnKind": "unicodeCodePoints",
                "results": [_result(located) for located in findings],
            }
        ],
    }
