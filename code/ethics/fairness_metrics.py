"""
Fairness Metrics for AI in Psychology.

Based on: *AI in Modern Psychology*, Chapters 22–23.

Implements core fairness metrics used in algorithmic auditing:

- Demographic parity
- Equal opportunity
- Equalized odds
- A per-group disparity report
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def demographic_parity_difference(y_pred: np.ndarray, sensitive_attr: np.ndarray) -> float:
    """Compute the absolute demographic-parity difference between two groups.

    Demographic parity requires ``P(Y_hat=1 | A=0) == P(Y_hat=1 | A=1)``.
    Returns ``0.0`` for perfect parity; larger values indicate greater disparity.
    """
    y_pred = np.asarray(y_pred)
    sensitive_attr = np.asarray(sensitive_attr)
    groups = np.unique(sensitive_attr)
    if len(groups) != 2:
        raise ValueError("sensitive_attr must be binary (two unique values)")
    rate_0 = y_pred[sensitive_attr == groups[0]].mean()
    rate_1 = y_pred[sensitive_attr == groups[1]].mean()
    return float(abs(rate_1 - rate_0))


def equal_opportunity_difference(
    y_true: np.ndarray, y_pred: np.ndarray, sensitive_attr: np.ndarray
) -> float:
    """Absolute difference in true-positive rates across two groups."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    sensitive_attr = np.asarray(sensitive_attr)
    groups = np.unique(sensitive_attr)
    tprs = []
    for g in groups:
        mask = (sensitive_attr == g) & (y_true == 1)
        tprs.append(float(y_pred[mask].mean()) if mask.sum() > 0 else 0.0)
    return float(abs(tprs[0] - tprs[1]))


def equalized_odds_difference(
    y_true: np.ndarray, y_pred: np.ndarray, sensitive_attr: np.ndarray
) -> float:
    """Max of TPR-gap and FPR-gap across two groups."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    sensitive_attr = np.asarray(sensitive_attr)
    groups = np.unique(sensitive_attr)
    tprs, fprs = [], []
    for g in groups:
        pos = (sensitive_attr == g) & (y_true == 1)
        neg = (sensitive_attr == g) & (y_true == 0)
        tprs.append(float(y_pred[pos].mean()) if pos.sum() > 0 else 0.0)
        fprs.append(float(y_pred[neg].mean()) if neg.sum() > 0 else 0.0)
    return float(max(abs(tprs[0] - tprs[1]), abs(fprs[0] - fprs[1])))


def fairness_report(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    sensitive_attr: np.ndarray,
    group_names: list | None = None,
) -> pd.DataFrame:
    """Build a per-group fairness report with disparity row."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    sensitive_attr = np.asarray(sensitive_attr)
    groups = np.unique(sensitive_attr)
    if group_names is None:
        group_names = [f"Group {g}" for g in groups]

    rows = []
    for g, name in zip(groups, group_names):
        mask = sensitive_attr == g
        pos = mask & (y_true == 1)
        neg = mask & (y_true == 0)
        n = int(mask.sum())
        rows.append(
            {
                "Group": name,
                "N": n,
                "Positive Rate": round(float(y_pred[mask].mean()) if n else 0.0, 4),
                "TPR (Recall)": round(float(y_pred[pos].mean()) if pos.sum() else 0.0, 4),
                "FPR": round(float(y_pred[neg].mean()) if neg.sum() else 0.0, 4),
                "Accuracy": round(float((y_pred[mask] == y_true[mask]).mean()) if n else 0.0, 4),
            }
        )

    disparity = {
        "Group": "| Disparity |",
        "N": "-",
        "Positive Rate": round(demographic_parity_difference(y_pred, sensitive_attr), 4),
        "TPR (Recall)": round(equal_opportunity_difference(y_true, y_pred, sensitive_attr), 4),
        "FPR": "-",
        "Accuracy": "-",
    }
    return pd.concat([pd.DataFrame(rows), pd.DataFrame([disparity])], ignore_index=True)


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    n = 1000
    protected = rng.binomial(1, 0.4, n)
    y_true = rng.binomial(1, 0.3, n)
    score = 0.3 * y_true - 0.2 * protected + rng.normal(0, 0.1, n)
    y_pred = (score > 0).astype(int)

    print("Fairness Report for Simulated Hiring Algorithm:")
    print("=" * 60)
    print(fairness_report(y_true, y_pred, protected, ["Majority", "Protected"]).to_string(index=False))
    print()
    print(f"DPD: {demographic_parity_difference(y_pred, protected):.4f}")
    print(f"EOD: {equal_opportunity_difference(y_true, y_pred, protected):.4f}")
    print(f"EOdds: {equalized_odds_difference(y_true, y_pred, protected):.4f}")
