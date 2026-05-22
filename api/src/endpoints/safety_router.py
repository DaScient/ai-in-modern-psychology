"""Therapy-chatbot safety endpoints (Chapter 10).

Wraps :mod:`code.clinical.therapy_safety` so callers can check a single
user message for crisis language and obtain a recommended escalation.

These endpoints are **educational**. They must not be used for triage
or as a substitute for clinical judgement.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Allow `import code.*` when the API is launched from the repo root.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from code.clinical.therapy_safety import (  # noqa: E402  (path set above)
    ACUTE_ESCALATION_RESOURCES,
    assess_message,
    build_safety_response,
)

router = APIRouter()


class SafetyRequest(BaseModel):
    """A single message to scan for crisis content."""

    message: str = Field(..., min_length=1, max_length=4000, examples=["I had a tough day."])
    region: Literal["US", "UK", "INTL"] = Field(
        "US",
        description="Region whose helpline appears in the recommended response.",
    )


class SafetyResponse(BaseModel):
    """Outcome of a safety check."""

    triggered: bool
    severity: Literal["none", "elevated", "acute"]
    matched_patterns: List[str]
    recommended_action: str
    user_facing_response: str
    helpline: str


@router.post(
    "/check",
    response_model=SafetyResponse,
    summary="Scan a single message for crisis language",
)
async def check_message(req: SafetyRequest) -> SafetyResponse:
    """Run the conservative regex-based crisis detector on ``message``."""
    result = assess_message(req.message)
    return SafetyResponse(
        triggered=result.triggered,
        severity=result.severity,  # type: ignore[arg-type]
        matched_patterns=result.matched_patterns,
        recommended_action=result.recommended_action,
        user_facing_response=build_safety_response(result, region=req.region),
        helpline=ACUTE_ESCALATION_RESOURCES.get(req.region, ACUTE_ESCALATION_RESOURCES["INTL"]),
    )


@router.get("/resources", summary="List crisis helpline resources by region")
async def list_resources() -> dict:
    """Return the (educational) registry of crisis helplines."""
    return ACUTE_ESCALATION_RESOURCES


class BatchSafetyRequest(BaseModel):
    """Batch endpoint for offline evaluation on transcripts."""

    messages: List[str] = Field(..., min_length=1, max_length=500)
    region: Literal["US", "UK", "INTL"] = "US"


@router.post(
    "/check_batch",
    summary="Scan a batch of messages (max 500) — useful for offline eval",
)
async def check_batch(req: BatchSafetyRequest) -> List[SafetyResponse]:
    """Vectorised wrapper around :func:`check_message`."""
    if len(req.messages) > 500:
        raise HTTPException(status_code=413, detail="Batch limit is 500 messages.")
    out: List[SafetyResponse] = []
    for msg in req.messages:
        result = assess_message(msg)
        out.append(
            SafetyResponse(
                triggered=result.triggered,
                severity=result.severity,  # type: ignore[arg-type]
                matched_patterns=result.matched_patterns,
                recommended_action=result.recommended_action,
                user_facing_response=build_safety_response(result, region=req.region),
                helpline=ACUTE_ESCALATION_RESOURCES.get(
                    req.region, ACUTE_ESCALATION_RESOURCES["INTL"]
                ),
            )
        )
    return out
