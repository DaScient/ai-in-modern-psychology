"""Decision-curve analysis for clinical-utility evaluation — Chapter 11.

Standard ML metrics (AUC, accuracy) tell you whether a model
*discriminates* but not whether it is *useful* at the operating point a
clinician would actually pick. Decision-curve analysis (Vickers &
Elkin, 2006, *Med. Decis. Making*) plots **net benefit** versus
**threshold probability** and compares to the trivial baselines of
"treat all" and "treat none".

Net benefit at threshold :math:`p_t` is::

    NB = TP/N - FP/N * (p_t / (1 - p_t))

Net benefit > the better of the two trivial strategies indicates the
model is clinically informative at that threshold.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

import numpy as np


@dataclass
class DCAPoint:
    threshold: float
    net_benefit_model: float
    net_benefit_treat_all: float
    net_benefit_treat_none: float = 0.0

    @property
    def model_beats_baseline(self) -> bool:
        return self.net_benefit_model > max(self.net_benefit_treat_all, 0.0)


def net_benefit(y_true: Sequence[int], y_pred_prob: Sequence[float], threshold: float) -> float:
    """Net benefit of a probabilistic model at a single decision threshold."""
    y_true_arr = np.asarray(y_true, dtype=int)
    y_pred_arr = (np.asarray(y_pred_prob, dtype=float) >= threshold).astype(int)
    n = len(y_true_arr)
    if n == 0:
        return 0.0
    tp = int(np.sum((y_pred_arr == 1) & (y_true_arr == 1)))
    fp = int(np.sum((y_pred_arr == 1) & (y_true_arr == 0)))
    if threshold >= 1.0:
        return 0.0
    return float(tp / n - fp / n * (threshold / (1 - threshold)))


def treat_all_net_benefit(y_true: Sequence[int], threshold: float) -> float:
    """Net benefit of always-treating at ``threshold``."""
    y = np.asarray(y_true, dtype=int)
    n = len(y)
    if n == 0 or threshold >= 1.0:
        return 0.0
    prev = float(np.mean(y == 1))
    return float(prev - (1 - prev) * (threshold / (1 - threshold)))


def decision_curve(
    y_true: Sequence[int],
    y_pred_prob: Sequence[float],
    thresholds: Sequence[float] | None = None,
) -> List[DCAPoint]:
    """Compute a decision curve over a grid of thresholds."""
    if thresholds is None:
        thresholds = np.linspace(0.01, 0.99, 99)
    out: List[DCAPoint] = []
    for t in thresholds:
        out.append(
            DCAPoint(
                threshold=float(t),
                net_benefit_model=net_benefit(y_true, y_pred_prob, float(t)),
                net_benefit_treat_all=treat_all_net_benefit(y_true, float(t)),
            )
        )
    return out


def informative_range(curve: Sequence[DCAPoint]) -> tuple[float, float] | None:
    """Return ``(min_t, max_t)`` over which the model beats both baselines.

    Returns ``None`` if no threshold range is dominated by the model.
    """
    informative = [pt.threshold for pt in curve if pt.model_beats_baseline]
    if not informative:
        return None
    return float(min(informative)), float(max(informative))


if __name__ == "__main__":  # pragma: no cover
    rng = np.random.default_rng(42)
    n = 1000
    y = rng.binomial(1, 0.05, n)
    score = rng.beta(2, 5, n) + 0.3 * y
    score = (score - score.min()) / (score.max() - score.min())
    curve = decision_curve(y, score)
    print("First / mid / last DCA points:")
    print(curve[0])
    print(curve[len(curve) // 2])
    print(curve[-1])
    print("Informative range:", informative_range(curve))
