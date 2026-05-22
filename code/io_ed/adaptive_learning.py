"""Adaptive-learning stub: Bayesian knowledge tracing.

Placeholder for Chapter 14. Implements a minimal BKT update step.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BKTParams:
    """Parameters of a Bayesian Knowledge Tracing model."""

    p_init: float = 0.1    # prior probability of mastery
    p_transit: float = 0.1  # learn rate
    p_slip: float = 0.1    # P(incorrect | mastered)
    p_guess: float = 0.2   # P(correct  | not mastered)


def bkt_update(p_mastery: float, correct: bool, params: BKTParams) -> float:
    """Update posterior probability of mastery after one observation."""
    if correct:
        num = p_mastery * (1 - params.p_slip)
        den = num + (1 - p_mastery) * params.p_guess
    else:
        num = p_mastery * params.p_slip
        den = num + (1 - p_mastery) * (1 - params.p_guess)
    p_post = num / den if den > 0 else p_mastery
    return p_post + (1 - p_post) * params.p_transit
