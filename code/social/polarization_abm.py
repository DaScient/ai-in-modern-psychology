"""
Bounded-confidence opinion-dynamics agent-based model.

Based on: *AI in Modern Psychology*, Chapter 16.

Implements a Hegselmann–Krause style model: agents update their opinion to
the mean of neighbours whose opinions differ by less than ``epsilon``.
"""

from __future__ import annotations

import numpy as np


def run_bounded_confidence(
    n_agents: int = 200,
    epsilon: float = 0.15,
    steps: int = 50,
    seed: int | None = 42,
) -> np.ndarray:
    """Run a Hegselmann–Krause opinion-dynamics simulation.

    Args:
        n_agents: Number of agents.
        epsilon: Confidence radius (smaller -> more polarization).
        steps: Number of update steps.
        seed: Random seed.

    Returns:
        Array of shape ``(steps + 1, n_agents)`` containing opinions over time.
    """
    rng = np.random.default_rng(seed)
    opinions = rng.uniform(0.0, 1.0, n_agents)
    history = np.zeros((steps + 1, n_agents))
    history[0] = opinions

    for t in range(1, steps + 1):
        new_opinions = np.empty_like(opinions)
        for i in range(n_agents):
            neighbours = np.abs(opinions - opinions[i]) < epsilon
            new_opinions[i] = opinions[neighbours].mean()
        opinions = new_opinions
        history[t] = opinions

    return history


if __name__ == "__main__":
    hist = run_bounded_confidence(epsilon=0.15)
    final = hist[-1]
    print(f"Final unique opinion clusters (rounded to 2 dp): {len(set(np.round(final, 2)))}")
