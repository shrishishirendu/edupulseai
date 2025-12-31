"""Dataset loading utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

LoadFormat = Literal["csv", "parquet"]


def load_dataset(path: Path, fmt: LoadFormat = "csv") -> pd.DataFrame:
    """Load a dataset from disk into a DataFrame."""
    if fmt == "csv":
        return pd.read_csv(path)
    if fmt == "parquet":
        return pd.read_parquet(path)
    msg = f"Unsupported format: {fmt}"
    raise ValueError(msg)