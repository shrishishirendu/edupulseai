"""Data preparation script."""

from __future__ import annotations

from pathlib import Path

from src.edupulse.config import DEFAULT_CONFIG


def prepare() -> None:
    """Placeholder function to showcase data prep entry point."""
    paths = DEFAULT_CONFIG.data
    Path(paths.processed).mkdir(parents=True, exist_ok=True)
    Path(paths.raw).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    prepare()