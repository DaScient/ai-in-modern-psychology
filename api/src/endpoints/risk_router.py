"""Clinical risk-prediction endpoints (Chapters 8 & 11).

The route exposes the educational gradient-boosting workflow that powers
``notebooks/02_suicide_risk_SHAP.ipynb`` so that learners can score one
or several synthetic EHR records via HTTP.

.. warning::

    Output is **educational** — never use it for triage or clinical
    decision-making. Real deployments need IRB approval, prospective
    validation, calibration on the deployment population, and ongoing
    monitoring (see Chapter 23).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from code.clinical.risk_prediction import FEATURE_COLS, generate_synthetic_ehr, split_xy  # noqa: E402

router = APIRouter()


class PatientRecord(BaseModel):
    """A single synthetic patient record used for educational scoring."""

    age: float = Field(..., ge=0, le=120, examples=[45.0])
    gender: int = Field(..., ge=0, le=1, description="0 = baseline, 1 = comparison group")
    prior_self_harm: int = Field(..., ge=0, le=1)
    ed_visits: int = Field(..., ge=0, le=20)
    nighttime_ed: int = Field(..., ge=0, le=1)
    antidepressant_discontinued: int = Field(..., ge=0, le=1)
    sleep_disorder: int = Field(..., ge=0, le=1)
    location_entropy_high: int = Field(..., ge=0, le=1)


class ScoreResponse(BaseModel):
    risk_score: float = Field(..., ge=0.0, le=1.0)
    threshold: float
    flagged: bool
    explanation: List[str] = Field(default_factory=list)


@router.get("/features", summary="List the synthetic EHR feature columns")
async def list_features() -> List[str]:
    """Return the column names of the educational EHR feature set."""
    return list(FEATURE_COLS)


@router.post(
    "/score",
    response_model=ScoreResponse,
    summary="Score a single synthetic EHR record (educational only)",
)
async def score(record: PatientRecord, threshold: float = 0.5) -> ScoreResponse:
    """Return a calibrated educational risk score using the closed-form
    log-odds model used to *generate* the synthetic data.

    Using the generator's own log-odds equation is intentionally simple —
    it lets students reason about feature contributions without first
    training a model. Replace with a real classifier when serving from a
    notebook.
    """
    if not 0.0 < threshold < 1.0:
        raise HTTPException(status_code=422, detail="threshold must be in (0, 1)")

    import math

    log_odds = (
        -4.5
        + 0.05 * record.age
        + 1.2 * record.prior_self_harm
        + 0.4 * record.ed_visits
        + 1.5 * record.nighttime_ed
        + 1.3 * record.antidepressant_discontinued
        + 0.8 * record.sleep_disorder
        + 0.6 * record.location_entropy_high
    )
    p = 1.0 / (1.0 + math.exp(-log_odds))

    contributions = {
        "age": 0.05 * record.age,
        "prior_self_harm": 1.2 * record.prior_self_harm,
        "ed_visits": 0.4 * record.ed_visits,
        "nighttime_ed": 1.5 * record.nighttime_ed,
        "antidepressant_discontinued": 1.3 * record.antidepressant_discontinued,
        "sleep_disorder": 0.8 * record.sleep_disorder,
        "location_entropy_high": 0.6 * record.location_entropy_high,
    }
    top = sorted(contributions.items(), key=lambda kv: kv[1], reverse=True)[:3]
    explanation = [f"{k} contributed {v:+.2f} to log-odds" for k, v in top]

    return ScoreResponse(
        risk_score=float(p),
        threshold=float(threshold),
        flagged=bool(p >= threshold),
        explanation=explanation,
    )


class SyntheticRequest(BaseModel):
    n_samples: int = Field(20, ge=1, le=1000)
    seed: Optional[int] = 42


@router.post(
    "/synthetic",
    summary="Generate a small synthetic EHR sample (educational)",
)
async def synthetic(req: SyntheticRequest) -> List[dict]:
    """Return ``n_samples`` synthetic records using the same generator that
    feeds the SHAP notebook."""
    df = generate_synthetic_ehr(n_samples=req.n_samples, seed=req.seed)
    X, _ = split_xy(df)
    X = X.copy()
    X["attempt"] = df["attempt"]
    return X.to_dict(orient="records")
