"""Social / opinion-dynamics endpoints (Chapter 16).

Wrap :func:`code.social.polarization_abm.run_bounded_confidence` to
deliver classroom-ready agent-based simulation snapshots.
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

from code.social.polarization_abm import run_bounded_confidence  # noqa: E402

router = APIRouter()


class ABMRequest(BaseModel):
    n_agents: int = Field(200, ge=10, le=2000)
    epsilon: float = Field(0.15, gt=0.0, le=1.0, description="Confidence radius")
    steps: int = Field(50, ge=1, le=500)
    seed: Optional[int] = 42


class ABMResponse(BaseModel):
    final_opinions: List[float]
    n_clusters: int
    history_snapshots: List[List[float]] = Field(
        ..., description="A short series of opinion snapshots — initial, midpoint, final."
    )


@router.post(
    "/abm/run",
    response_model=ABMResponse,
    summary="Run a Hegselmann–Krause bounded-confidence simulation",
)
async def run_abm(req: ABMRequest) -> ABMResponse:
    """Return final opinions and a small set of snapshots for plotting.

    ``epsilon`` smaller than ~0.20 typically produces polarization;
    values above ~0.30 produce consensus. This is one of the cleanest
    demonstrations that *micro* assumptions (confidence radius) drive
    *macro* outcomes (consensus vs. fragmentation).
    """
    import numpy as np

    history = run_bounded_confidence(
        n_agents=req.n_agents, epsilon=req.epsilon, steps=req.steps, seed=req.seed
    )
    final = history[-1]
    clusters = len(set(np.round(final, 2)))
    mid = history.shape[0] // 2
    snapshots = [history[0].tolist(), history[mid].tolist(), final.tolist()]
    return ABMResponse(
        final_opinions=final.tolist(),
        n_clusters=int(clusters),
        history_snapshots=snapshots,
    )
