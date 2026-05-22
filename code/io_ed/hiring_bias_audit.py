"""Hiring-bias audit helpers.

Light wrapper around ``code.ethics.fairness_metrics`` for the hiring case
study in Chapter 13.
"""

from __future__ import annotations

import numpy as np

from ..ethics.fairness_metrics import (
    demographic_parity_difference,
    equal_opportunity_difference,
    equalized_odds_difference,
    fairness_report,
)


def audit(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    protected: np.ndarray,
    dpd_threshold: float = 0.10,
    eod_threshold: float = 0.10,
) -> dict:
    """Run a quick fairness audit and return verdicts.

    Thresholds default to 0.10 (the EEOC's "4/5ths-rule" practical cousin).
    """
    dpd = demographic_parity_difference(y_pred, protected)
    eod = equal_opportunity_difference(y_true, y_pred, protected)
    eodds = equalized_odds_difference(y_true, y_pred, protected)
    return {
        "demographic_parity_difference": dpd,
        "equal_opportunity_difference": eod,
        "equalized_odds_difference": eodds,
        "passes_dpd": dpd < dpd_threshold,
        "passes_eod": eod < eod_threshold,
        "report": fairness_report(y_true, y_pred, protected),
    }
