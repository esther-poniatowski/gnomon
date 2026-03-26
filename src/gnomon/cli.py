"""
Command-line interface for the `gnomon` package.

Defines commands available via `python -m gnomon` or `gnomon` if installed as a script.

Commands
--------
info : Display diagnostic information.
init : Scaffold research workspace structure into a target directory.
validate : Validate registry files against schemas.
status : Report inferential position in the research workspace.
"""

import typer
from . import info as pkg_info, __version__

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
    paths: list[str] = typer.Argument(..., help="Registry files or directories to validate."),
) -> None:
    """Validate registry files against schemas."""
    typer.echo("Registry validation is not yet implemented.")
    raise typer.Exit(code=0)


@app.command("status")
def cli_status(
    target: str = typer.Option(".", "--target", "-t", help="Research workspace directory."),
) -> None:
    """Report inferential position: established results, open questions, in-progress notes, blocked entries."""
    typer.echo("Workspace status reporting is not yet implemented.")
    raise typer.Exit(code=0)


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
