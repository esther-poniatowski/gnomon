"""
Command-line interface for the `gnomon` package.

Defines commands available via `python -m gnomon` or `gnomon` if installed as a script.

Commands
--------
info : Display diagnostic information.
init : Scaffold research workspace structure into a target directory.
validate : Validate each record against the schema of its type.
status : List the open conditions of the questions of a workspace.
vocabulary : Collect the symbols and operators of one problem into a table.
itinerary : Check every itinerary of one problem against the activity and product-type registries.
"""

import json
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Optional

import typer
import yaml

from . import info as pkg_info, __version__
from .findings import Finding
from .itineraries import itinerary_problems
from .sarif import Located, sarif_log
from .vocabulary import load_problem, render_markdown, render_yaml

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command("info")
def cli_info() -> None:
    """Display version and platform diagnostics."""
    typer.echo(pkg_info())


@app.command("init")
def cli_init(
    target: str = typer.Option(".", "--target", "-t", help="Target workspace directory."),
) -> None:
    """Scaffold research workspace structure into a target directory."""
    typer.echo("Research workspace scaffolding is not yet implemented.")
    raise typer.Exit(code=0)


@app.command("validate")
def cli_validate(
    paths: list[str] = typer.Argument(..., help="Record files or directories to validate."),
) -> None:
    """Validate each record against the schema of its type."""
    typer.echo("Record validation is not yet implemented.")
    raise typer.Exit(code=0)


@app.command("status")
def cli_status(
    target: str = typer.Option(".", "--target", "-t", help="Research workspace directory."),
) -> None:
    """List the open conditions of answerability of each question, and the acts that address them."""
    typer.echo("Workspace status reporting is not yet implemented.")
    raise typer.Exit(code=0)


@app.command("vocabulary")
def cli_vocabulary(
    directory: str = typer.Argument(..., help="Directory holding the filled records of one problem."),
    output: str = typer.Option(
        "vocabulary.yml", "--output", "-o", help="Record written inside that directory."
    ),
    markdown: bool = typer.Option(
        False, "--markdown", "-m", help="Also build the Markdown view beside the record."
    ),
    root: str = typer.Option(
        ".", "--root", "-r", help="Workspace root from which the Markdown view links its index."
    ),
) -> None:
    """Collect the symbols and operators of one problem into a table its author can consult."""
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    try:
        index_path = (source / "_index.md").resolve().relative_to(Path(root).resolve())
    except ValueError:
        typer.echo(f"{source} lies outside the workspace root {root}", err=True)
        raise typer.Exit(code=1)
    problem = load_problem(source)
    target = source / output
    target.write_text(render_yaml(problem), encoding="utf-8")
    if markdown:
        page = render_markdown(problem, index_path=index_path.as_posix())
        (source / f"{target.stem}.md").write_text(page, encoding="utf-8")
    repeated = problem.collisions()
    typer.echo(
        f"{target}: {len(problem.declarations)} symbols, "
        f"{len(problem.local)} operators of the problem, "
        f"{len(repeated)} symbols reused across records"
    )


class OutputFormat(str, Enum):
    """The forms in which a check reports its findings."""

    text = "text"
    sarif = "sarif"


def _read_records(
    source: Path, tolerant: bool
) -> tuple[dict[str, Mapping[str, Any]], dict[str, Path], list[str]]:
    """Return the records of ``source`` keyed by identifier, the file of each, and the read failures.

    A later file carrying an identifier already read replaces the earlier one. When ``tolerant`` is
    false, a file that cannot be read or parsed raises its error; otherwise the failure is returned
    as a line naming the file, and the remaining files are read.
    """
    records: dict[str, Mapping[str, Any]] = {}
    files: dict[str, Path] = {}
    failures: list[str] = []
    for path in sorted(source.glob("*.yml")):
        if tolerant:
            try:
                record = yaml.safe_load(path.read_text(encoding="utf-8"))
            except (OSError, ValueError, yaml.YAMLError) as error:
                failures.append(f"{path}: {error}")
                continue
        else:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, Mapping) and "id" in record:
            records[str(record["id"])] = record
            files[str(record["id"])] = path
    return records, files, failures


def _write_log(log: dict[str, Any], output: Optional[Path]) -> None:
    """Write ``log`` to ``output``, creating its folders, or to standard output when it is None."""
    text = json.dumps(log, indent=2, ensure_ascii=False) + "\n"
    if output is None:
        typer.echo(text, nl=False)
        return
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    except OSError as error:
        typer.echo(f"cannot write the log {output}: {error}", err=True)
        raise typer.Exit(code=2) from error


@app.command("itinerary")
def cli_itinerary(
    directory: str = typer.Argument(..., help="Directory holding the filled records of one problem."),
    output_format: OutputFormat = typer.Option(
        OutputFormat.text, "--format", "-f",
        help="text prints one line per problem; sarif also writes a SARIF 2.1.0 log in the findings "
        "profile of Elenchos, on standard output or at --output.",
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o",
        help="With --format sarif, write the log to this path instead of standard output; "
        "missing folders are created.",
    ),
    root: Path = typer.Option(
        Path("."), "--root", "-r",
        help="With --format sarif, the repository root from which the log states every path.",
    ),
) -> None:
    """Check every itinerary of one problem against the registries and the records it names.

    The text output prints one line per problem and a count. With ``--format sarif`` and no
    ``--output``, the log takes standard output and those lines go to standard error. The command
    exits with status 1 when a problem is found or a record cannot be read, and with status 2 when
    the log cannot be written.
    """
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    sarif = output_format is OutputFormat.sarif
    if output is not None and not sarif:
        raise typer.BadParameter("requires --format sarif", param_hint="--output")
    folder = PurePosixPath(".")
    if sarif:
        try:
            folder = PurePosixPath(source.resolve().relative_to(root.resolve()).as_posix())
        except ValueError:
            typer.echo(f"{source} lies outside the root {root}", err=True)
            raise typer.Exit(code=1) from None
    records, files, unreadable = _read_records(source, tolerant=sarif)
    stopped = (
        f"{len(unreadable)} record files could not be read, so the itineraries naming their records "
        "were not fully checked" if unreadable else None
    )
    itineraries = [record for record in records.values() if record.get("type") == "itinerary"]
    found: list[tuple[str, Finding]] = []
    try:
        for itinerary in itineraries:
            found += [(str(itinerary["id"]), problem) for problem in itinerary_problems(itinerary, records)]
    except (OSError, ValueError, yaml.YAMLError) as error:
        if not sarif:
            raise
        stopped = f"the check stopped on an error: {error}"
    problems = [f"{identifier}: {problem.text}" for identifier, problem in found]
    to_stderr = sarif and output is None
    for line in unreadable:
        typer.echo(line, err=True)
    for line in problems:
        typer.echo(line, err=to_stderr)
    typer.echo(f"{len(itineraries)} itineraries checked, {len(problems)} problems found", err=to_stderr)
    if sarif:
        located = [
            Located(problem, folder / files[identifier].name, identifier) for identifier, problem in found
        ]
        _write_log(sarif_log(located, __version__, stopped), output)
    if problems or stopped:
        raise typer.Exit(code=1)


@app.callback()
def main_callback(
    version: bool = typer.Option(
        False, "--version", "-v", help="Show the package version and exit."
    )
) -> None:
    """Formal epistemic framework for organizing mathematical research."""
    if version:
        typer.echo(__version__)
        raise typer.Exit()
