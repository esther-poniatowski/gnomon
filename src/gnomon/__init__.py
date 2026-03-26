"""
Initialization logic and public interface for the `gnomon` package.

Gnomon is a formal epistemic framework for organizing mathematical research.
It defines the objects, contracts, and registries that make a research workspace
explicit and machine-verifiable: what has been established, what is in progress,
what is blocked, and where each claim fits in the inferential architecture.

Variables
---------
__version__ : str, default "0.0.0+unknown"
    Version of the package. If the package metadata is unavailable (e.g. in editable or source-only
    environments), a fallback value is provided (PEP 440 compliant).
__all__ : list
    Public objects exposed by this package.

Functions
---------
info() -> str
    Format diagnostic information about the package and platform.
data_path() -> Path
    Return the absolute path to the package data directory.
"""
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path
import platform

try:
    if __package__ is None:  # erroneous script execution
        raise PackageNotFoundError
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = ["info", "data_path", "__version__"]


def info() -> str:
    """Format diagnostic information on package and platform."""
    return f"{__package__} {__version__} | Platform: {platform.system()} Python {platform.python_version()}"


def data_path() -> Path:
    """Return the absolute path to the package data directory.

    This path can be used both when gnomon is installed as a package
    and when it is included as a Git submodule.
    """
    return Path(__file__).parent / "data"
