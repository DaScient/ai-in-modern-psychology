"""Algorithmic-fairness endpoints (Chapters 13 & 22).

Wrap :mod:`code.ethics.fairness_metrics` so that classroom audits can hit
the API directly. All metrics here assume a *binary* sensitive attribute.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, model_validator

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from code.ethics.fairness_metrics import (  # noqa: E402
    demographic_parity_difference,
    equal_opportunity_difference,
    equalized_odds_difference,
    fairness_report,
)

router = APIRouter()


class AuditRequest(BaseModel):
    """Inputs for an algorithmic-fairness audit."""

    y_true: List[int] = Field(..., min_length=2, description="Ground-truth labels (0/1).")
    y_pred: List[int] = Field(..., min_length=2, description="Model predictions (0/1).")
    sensitive: List[int] = Field(..., min_length=2, description="Binary sensitive attribute.")
    group_names: Optional[List[str]] = Field(
        None, description="Optional pretty names, ordered to match unique sensitive values."
    )

    @model_validator(mode="after")
    def _check_lengths(self) -> "AuditRequest":
        if not (len(self.y_true) == len(self.y_pred) == len(self.sensitive)):
            raise ValueError("y_true, y_pred, and sensitive must have the same length")
        if self.group_names is not None and len(self.group_names) != 2:
            raise ValueError("group_names must contain exactly two names for a binary attribute")
        return self


class AuditResponse(BaseModel):
    demographic_parity_difference: float
    equal_opportunity_difference: float
    equalized_odds_difference: float
    per_group: List[dict]
    notes: List[str]


@router.post(
    "/audit",
    response_model=AuditResponse,
    summary="Compute parity, opportunity, and odds disparities (binary attribute)",
)
async def audit(req: AuditRequest) -> AuditResponse:
    """Return demographic parity, equal opportunity, equalized odds and a
    per-group table. Useful as a smoke-test for the metrics covered in
    Chapter 13."""
    import numpy as np

    y_true = np.asarray(req.y_true, dtype=int)
    y_pred = np.asarray(req.y_pred, dtype=int)
    s = np.asarray(req.sensitive, dtype=int)
    if len(np.unique(s)) != 2:
        raise HTTPException(status_code=422, detail="sensitive must take exactly two values")

    dpd = demographic_parity_difference(y_pred, s)
    eod = equal_opportunity_difference(y_true, y_pred, s)
    eodds = equalized_odds_difference(y_true, y_pred, s)
    report = fairness_report(y_true, y_pred, s, req.group_names)

    notes: List[str] = []
    if dpd > 0.10:
        notes.append("Demographic parity gap exceeds 10% — investigate before deployment.")
    if eod > 0.10:
        notes.append("Equal-opportunity gap exceeds 10% — review TPR disparity.")
    if not notes:
        notes.append("All gaps within the 10% educational threshold (not a legal standard).")

    return AuditResponse(
        demographic_parity_difference=float(dpd),
        equal_opportunity_difference=float(eod),
        equalized_odds_difference=float(eodds),
        per_group=report.to_dict(orient="records"),
        notes=notes,
    )
