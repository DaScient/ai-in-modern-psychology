"""Tiny data-loader helpers for sample datasets shipped with the repo."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_csv(name: str) -> pd.DataFrame:
    """Load a CSV from the repository ``data/`` folder by file name."""
    path = DATA_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"{path} not found. Run data/generate_synthetic.py first.")
    return pd.read_csv(path)
