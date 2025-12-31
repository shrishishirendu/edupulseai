"""Dropout risk estimator stubs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import pandas as pd


@dataclass
class DropoutRiskModel:
    """Placeholder dropout risk estimator providing interpretable scores."""

    band_thresholds: Dict[str, float] | None = None

    def predict(self, features: pd.DataFrame) -> pd.Series:
        """Return dummy dropout probabilities for each student."""
        scores = np.linspace(0.1, 0.9, num=len(features), endpoint=True)
        return pd.Series(scores, index=features.index, name="dropout_risk")

    def explain(self, features: pd.DataFrame) -> List[Dict[str, float]]:
        """Produce placeholder explanations for each prediction."""
        return [
            {"attendance": 0.5, "engagement": 0.5}
            for _ in range(len(features))
        ]