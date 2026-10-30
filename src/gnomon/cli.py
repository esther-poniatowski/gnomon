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

from pathlib import Path
from typing import Any, Mapping

import typer
import yaml

from . import info as pkg_info, __version__
from .itineraries import itinerary_problems
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


@app.command("itinerary")
def cli_itinerary(
    directory: str = typer.Argument(..., help="Directory holding the filled records of one problem."),
) -> None:
    """Check every itinerary of one problem against the registries and the records it names."""
    source = Path(directory)
    if not source.is_dir():
        typer.echo(f"no such directory: {source}", err=True)
        raise typer.Exit(code=1)
    loaded = [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted(source.glob("*.yml"))]
    records: dict[str, Mapping[str, Any]] = {
        str(record["id"]): record for record in loaded if isinstance(record, Mapping) and "id" in record
    }
    itineraries = [record for record in records.values() if record.get("type") == "itinerary"]
    problems = [f"{itinerary['id']}: {problem}" for itinerary in itineraries for problem in itinerary_problems(itinerary, records)]
    for line in problems:
        typer.echo(line)
    typer.echo(f"{len(itineraries)} itineraries checked, {len(problems)} problems found")
    if problems:
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
