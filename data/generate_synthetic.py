"""Generate synthetic datasets used by the book's notebooks.

Usage:
    python data/generate_synthetic.py --all --seed 42
    python data/generate_synthetic.py --ehr --seed 0
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent


def generate_ehr(n: int = 10_000, seed: int = 42) -> pd.DataFrame:
    """Synthetic EHR for suicide-risk prediction (mirrors notebook 02)."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "age": rng.normal(45, 15, n).clip(18, 90),
            "gender": rng.choice([0, 1], size=n, p=[0.5, 0.5]),
            "prior_self_harm": rng.binomial(1, 0.05, n),
            "ed_visits": rng.poisson(0.5, n).clip(0, 10),
            "nighttime_ed": rng.binomial(1, 0.1, n),
            "antidepressant_discontinued": rng.binomial(1, 0.08, n),
            "sleep_disorder": rng.binomial(1, 0.15, n),
            "location_entropy_high": (rng.gamma(2, 0.5, n) > 2.5).astype(int),
        }
    )
    log_odds = (
        -4.5
        + 0.05 * df["age"]
        + 1.2 * df["prior_self_harm"]
        + 0.4 * df["ed_visits"]
        + 1.5 * df["nighttime_ed"]
        + 1.3 * df["antidepressant_discontinued"]
        + 0.8 * df["sleep_disorder"]
        + 0.6 * df["location_entropy_high"]
    )
    prob = 1 / (1 + np.exp(-log_odds))
    df["attempt"] = rng.binomial(1, prob)
    return df


def generate_hiring(n: int = 5_000, seed: int = 42) -> pd.DataFrame:
    """Synthetic hiring dataset for bias-audit lab."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "years_experience": rng.gamma(2, 3, n).clip(0, 30),
            "education_years": rng.normal(15, 3, n).clip(8, 22),
            "test_score": rng.normal(70, 12, n).clip(0, 100),
            "interview_score": rng.normal(70, 15, n).clip(0, 100),
            "protected_group": rng.binomial(1, 0.4, n),
        }
    )
    # qualified is mostly merit-driven, but historic bias depresses the
    # interview score of the protected group
    df.loc[df["protected_group"] == 1, "interview_score"] -= 5
    score = (
        0.3 * df["years_experience"] / 30
        + 0.3 * df["education_years"] / 22
        + 0.2 * df["test_score"] / 100
        + 0.2 * df["interview_score"] / 100
    )
    df["qualified"] = (score > 0.55).astype(int)
    df["hired"] = (score + rng.normal(0, 0.05, n) - 0.05 * df["protected_group"] > 0.55).astype(int)
    return df


def generate_depression_sensors(n: int = 1_000, seed: int = 42) -> pd.DataFrame:
    """Synthetic smartphone-sensor features for depression detection (Ch 4)."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "sleep_hours_mean": rng.normal(7, 1.5, n).clip(3, 11),
            "sleep_variability": rng.gamma(2, 0.4, n),
            "steps_per_day": rng.normal(7000, 3000, n).clip(0, 25000),
            "screen_time_hours": rng.normal(4, 2, n).clip(0, 16),
            "location_entropy": rng.gamma(2, 0.5, n),
            "social_interactions": rng.poisson(5, n),
        }
    )
    z = (
        -0.4 * (df["sleep_hours_mean"] - 7) ** 2 / 4
        + 1.0 * df["sleep_variability"]
        - 0.0002 * df["steps_per_day"]
        + 0.2 * df["screen_time_hours"]
        - 0.5 * df["location_entropy"]
        - 0.2 * df["social_interactions"]
    )
    df["depressed"] = (1 / (1 + np.exp(-z)) > 0.5).astype(int)
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Generate all datasets")
    parser.add_argument("--ehr", action="store_true")
    parser.add_argument("--hiring", action="store_true")
    parser.add_argument("--depression", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.all or args.ehr:
        path = HERE / "ehr_suicide_risk.csv"
        generate_ehr(seed=args.seed).to_csv(path, index=False)
        print(f"wrote {path}")
    if args.all or args.hiring:
        path = HERE / "hiring_sample.csv"
        generate_hiring(seed=args.seed).to_csv(path, index=False)
        print(f"wrote {path}")
    if args.all or args.depression:
        path = HERE / "depression_synthetic.csv"
        generate_depression_sensors(seed=args.seed).to_csv(path, index=False)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
