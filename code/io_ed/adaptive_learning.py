"""Adaptive-learning utilities — Bayesian Knowledge Tracing (BKT).

Companion to *AI in Modern Psychology*, Chapter 14.

This module implements:

* A typed :class:`BKTParams` container.
* The single-step :func:`bkt_update` rule.
* A :func:`simulate_trajectory` helper that walks BKT through a sequence
  of graded responses and returns the full mastery curve.
* A minimal Rasch-model item-response :func:`p_correct_irt` helper used
  to *generate* synthetic responses for student-modelling assignments.

The implementation is deliberately compact — every line maps to an
equation discussed in the chapter so that students can extend it (e.g.,
to KT-IDEM or DKT) without untangling production code.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class BKTParams:
    """Parameters of a Bayesian Knowledge Tracing model.

    Attributes:
        p_init: Prior probability of mastery before the first observation.
        p_transit: Probability of transitioning from un-mastered to mastered
            after attempting an item (the "learning rate").
        p_slip: P(incorrect | mastered).
        p_guess: P(correct | not mastered).
    """

    p_init: float = 0.1
    p_transit: float = 0.1
    p_slip: float = 0.1
    p_guess: float = 0.2

    def __post_init__(self) -> None:
        for name in ("p_init", "p_transit", "p_slip", "p_guess"):
            v = getattr(self, name)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"{name} must lie in [0, 1] (got {v!r})")
        if self.p_slip + self.p_guess >= 1.0:
            # Standard BKT identifiability constraint
            raise ValueError(
                "BKT is not identifiable when p_slip + p_guess >= 1.0 "
                "(Beck & Chang, 2007)."
            )


def bkt_update(p_mastery: float, correct: bool, params: BKTParams) -> float:
    """Update the posterior probability of mastery after one observation.

    Args:
        p_mastery: Prior P(mastered) before observing the response.
        correct: Whether the student answered the item correctly.
        params: BKT parameters.

    Returns:
        Posterior P(mastered) after applying the BKT update.
    """
    if not 0.0 <= p_mastery <= 1.0:
        raise ValueError("p_mastery must lie in [0, 1]")

    if correct:
        num = p_mastery * (1 - params.p_slip)
        den = num + (1 - p_mastery) * params.p_guess
    else:
        num = p_mastery * params.p_slip
        den = num + (1 - p_mastery) * (1 - params.p_guess)
    p_post = num / den if den > 0 else p_mastery
    return p_post + (1 - p_post) * params.p_transit


def simulate_trajectory(responses: Iterable[bool], params: BKTParams) -> List[float]:
    """Walk BKT through a sequence of responses and return the mastery curve.

    Args:
        responses: Iterable of booleans — one per item attempt.
        params: BKT parameters; ``params.p_init`` is used as the prior.

    Returns:
        List of posterior P(mastered) values, one per attempt, in order.
    """
    p = params.p_init
    out: List[float] = []
    for correct in responses:
        p = bkt_update(p, bool(correct), params)
        out.append(p)
    return out


def p_correct_irt(theta: float, difficulty: float, discrimination: float = 1.0) -> float:
    """Two-parameter logistic item-response probability.

    Useful for *generating* synthetic responses for BKT assignments where
    learners need a ground-truth ability score (``theta``) to compare
    against the BKT posterior.
    """
    z = discrimination * (theta - difficulty)
    return 1.0 / (1.0 + math.exp(-z))


def recommend_next_difficulty(p_mastery: float, target_p_correct: float = 0.75) -> float:
    """Recommend an item difficulty that hits ``target_p_correct``.

    Treats ``p_mastery`` as a coarse proxy for IRT ``theta``. A common
    heuristic in adaptive learning is to keep the student near a 75%
    success rate to balance challenge and confidence — see Vygotsky's
    zone of proximal development (Chapter 14).
    """
    if not 0.0 < target_p_correct < 1.0:
        raise ValueError("target_p_correct must lie in (0, 1)")
    # Inverse logistic: theta - difficulty = logit(target)
    logit = math.log(target_p_correct / (1.0 - target_p_correct))
    theta = math.log(max(p_mastery, 1e-6) / max(1.0 - p_mastery, 1e-6))
    return theta - logit


if __name__ == "__main__":  # pragma: no cover - illustrative
    params = BKTParams()
    responses = [True, False, True, True, True, False, True, True, True, True]
    curve = simulate_trajectory(responses, params)
    print("Mastery trajectory:")
    for i, p in enumerate(curve, start=1):
        print(f"  step {i:2d} ({'correct' if responses[i - 1] else 'incorrect'}): {p:.3f}")
