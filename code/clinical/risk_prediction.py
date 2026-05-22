"""Clinical risk-prediction utilities.

This module wraps the SHAP-explained gradient-boosting workflow used in the
notebook ``02_suicide_risk_SHAP.ipynb`` so it can be reused programmatically.
"""

from __future__ import annotations

from typing import Tuple

import numpy as np
import pandas as pd


FEATURE_COLS = [
    "age",
    "gender",
    "prior_self_harm",
    "ed_visits",
    "nighttime_ed",
    "antidepressant_discontinued",
    "sleep_disorder",
    "location_entropy_high",
]


def generate_synthetic_ehr(n_samples: int = 10_000, seed: int | None = 42) -> pd.DataFrame:
    """Generate a synthetic EHR dataset that mimics suicide-risk predictors.

    All data are simulated. **Do not** use for real risk assessment.
    """
    rng = np.random.default_rng(seed)
    age = rng.normal(45, 15, n_samples).clip(18, 90)
    gender = rng.choice([0, 1], size=n_samples, p=[0.5, 0.5])
    prior_self_harm = rng.binomial(1, 0.05, n_samples)
    ed_visits = rng.poisson(0.5, n_samples).clip(0, 10)
    nighttime_ed = rng.binomial(1, 0.1, n_samples)
    antidepressant_discontinued = rng.binomial(1, 0.08, n_samples)
    sleep_disorder = rng.binomial(1, 0.15, n_samples)
    location_entropy = rng.gamma(2, 0.5, n_samples)

    log_odds = (
        -4.5
        + 0.05 * age
        + 1.2 * prior_self_harm
        + 0.4 * ed_visits
        + 1.5 * nighttime_ed
        + 1.3 * antidepressant_discontinued
        + 0.8 * sleep_disorder
        + 0.6 * (location_entropy > 2.5).astype(int)
    )
    prob = 1 / (1 + np.exp(-log_odds))
    attempt = rng.binomial(1, prob, n_samples)

    return pd.DataFrame(
        {
            "age": age,
            "gender": gender,
            "prior_self_harm": prior_self_harm,
            "ed_visits": ed_visits,
            "nighttime_ed": nighttime_ed,
            "antidepressant_discontinued": antidepressant_discontinued,
            "sleep_disorder": sleep_disorder,
            "location_entropy_high": (location_entropy > 2.5).astype(int),
            "attempt": attempt,
        }
    )


def split_xy(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Return feature matrix and target series from a synthetic EHR dataframe."""
    return df[FEATURE_COLS], df["attempt"]
