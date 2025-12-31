"""Train dropout model placeholder."""

from __future__ import annotations

from src.edupulse.models.dropout import DropoutRiskModel


def train() -> DropoutRiskModel:
    """Return an untrained but initialized model object."""
    return DropoutRiskModel()


if __name__ == "__main__":
    train()