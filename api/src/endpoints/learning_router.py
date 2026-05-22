"""Adaptive-learning endpoints (Chapter 14).

Expose the Bayesian Knowledge Tracing update used by
``code.io_ed.adaptive_learning`` plus a simple trajectory simulator
suitable for classroom dashboards.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from code.io_ed.adaptive_learning import BKTParams, bkt_update, simulate_trajectory  # noqa: E402

router = APIRouter()


class BKTRequest(BaseModel):
    p_mastery: float = Field(..., ge=0.0, le=1.0, description="Current prior of mastery.")
    correct: bool
    p_init: float = Field(0.1, ge=0.0, le=1.0)
    p_transit: float = Field(0.1, ge=0.0, le=1.0)
    p_slip: float = Field(0.1, ge=0.0, le=0.5)
    p_guess: float = Field(0.2, ge=0.0, le=0.5)


class BKTResponse(BaseModel):
    p_mastery_next: float


@router.post(
    "/bkt/update",
    response_model=BKTResponse,
    summary="Apply one BKT update step",
)
async def bkt_step(req: BKTRequest) -> BKTResponse:
    """Update mastery probability after a single graded response."""
    params = BKTParams(
        p_init=req.p_init,
        p_transit=req.p_transit,
        p_slip=req.p_slip,
        p_guess=req.p_guess,
    )
    return BKTResponse(p_mastery_next=float(bkt_update(req.p_mastery, req.correct, params)))


class TrajectoryRequest(BaseModel):
    responses: List[bool] = Field(..., min_length=1, max_length=200)
    p_init: float = Field(0.1, ge=0.0, le=1.0)
    p_transit: float = Field(0.1, ge=0.0, le=1.0)
    p_slip: float = Field(0.1, ge=0.0, le=0.5)
    p_guess: float = Field(0.2, ge=0.0, le=0.5)


class TrajectoryResponse(BaseModel):
    mastery_curve: List[float]
    final_mastery: float


@router.post(
    "/bkt/trajectory",
    response_model=TrajectoryResponse,
    summary="Replay a sequence of responses through BKT",
)
async def bkt_trajectory(req: TrajectoryRequest) -> TrajectoryResponse:
    """Return the mastery curve produced by walking BKT through a response sequence."""
    params = BKTParams(
        p_init=req.p_init,
        p_transit=req.p_transit,
        p_slip=req.p_slip,
        p_guess=req.p_guess,
    )
    curve = simulate_trajectory(req.responses, params)
    return TrajectoryResponse(mastery_curve=curve, final_mastery=curve[-1])
