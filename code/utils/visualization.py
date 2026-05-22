"""Visualization helpers shared across notebooks."""

from __future__ import annotations

from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np


def plot_forgetting_curve(times: np.ndarray, activations: Iterable[float], threshold: float = -1.5):
    """Plot an ACT-R style forgetting curve."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(times, activations, linewidth=2, label="Base-level activation")
    ax.axhline(threshold, color="r", linestyle="--", label=f"Retrieval threshold ({threshold})")
    ax.set_xlabel("Time since encoding")
    ax.set_ylabel("Activation")
    ax.set_title("Power-Law Forgetting Curve")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    return fig, ax
