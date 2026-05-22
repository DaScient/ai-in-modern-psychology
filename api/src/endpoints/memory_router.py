"""ACT-R declarative-memory endpoints (Chapter 6).

Wraps :class:`code.foundations.act_r_simulation.ACTRMemory` so that
classroom demos can hit a stable HTTP endpoint and visualise the
power-law forgetting curve without re-implementing the activation
equation.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import numpy as np  # noqa: E402

from code.foundations.act_r_simulation import ACTRMemory  # noqa: E402

router = APIRouter()


class ChunkSpec(BaseModel):
    """A single declarative-memory chunk to seed the simulation."""

    name: str = Field(..., examples=["paris"])
    content: Dict[str, str] = Field(default_factory=dict, examples=[{"capital_of": "France"}])
    retrieval_times: List[float] = Field(
        default_factory=lambda: [0.0],
        description="Times at which this chunk has been retrieved (>=1 required).",
        min_length=1,
    )


class SimulateRequest(BaseModel):
    """Run a forgetting-curve simulation."""

    chunk: ChunkSpec
    decay: float = Field(0.5, gt=0.0, lt=1.0, description="ACT-R decay parameter (d)")
    threshold: float = Field(-2.0, description="Retrieval threshold (tau)")
    times: List[float] = Field(
        default_factory=lambda: [float(t) for t in range(1, 51)],
        description="Time-points at which to compute activation. Must exceed all retrieval times.",
        min_length=1,
    )


class SimulatePoint(BaseModel):
    time: float
    activation: float
    above_threshold: bool


class SimulateResponse(BaseModel):
    decay: float
    threshold: float
    points: List[SimulatePoint]
    asymptote_time: Optional[float] = Field(
        None, description="First time point at which activation falls below threshold, if any."
    )


@router.post(
    "/simulate",
    response_model=SimulateResponse,
    summary="Simulate the ACT-R forgetting curve for a single chunk",
)
async def simulate(req: SimulateRequest) -> SimulateResponse:
    """Return base-level activation across requested time points.

    The activation is computed *deterministically* (without the logistic noise
    used in :func:`ACTRMemory.compute_activation`) so that classroom outputs are
    reproducible. Compose with :class:`code.foundations.act_r_simulation.ACTRMemory`
    directly when you need stochastic retrieval dynamics.
    """
    memory = ACTRMemory(decay=req.decay, noise=0.0, threshold=req.threshold)
    memory.add_chunk(req.chunk.name, dict(req.chunk.content))
    memory.chunks[req.chunk.name].retrieval_times = list(req.chunk.retrieval_times)

    times = np.array(req.times, dtype=float)
    activations = memory.simulate_forgetting_curve(req.chunk.name, times)

    asymptote: Optional[float] = None
    for t, a in zip(times, activations):
        if a < req.threshold:
            asymptote = float(t)
            break

    return SimulateResponse(
        decay=req.decay,
        threshold=req.threshold,
        points=[
            SimulatePoint(time=float(t), activation=float(a), above_threshold=bool(a >= req.threshold))
            for t, a in zip(times, activations)
        ],
        asymptote_time=asymptote,
    )
