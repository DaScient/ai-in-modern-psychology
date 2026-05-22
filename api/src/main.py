"""FastAPI entry point for the AI in Modern Psychology service.

The API surfaces the educational models that live under ``/code`` so that
learners and contributors can experiment with them from HTTP clients, the
Jupyter Book examples, or simple front-end demos. Every endpoint maps
to a chapter of *AI in Modern Psychology* (DaScient Press, 2026).

Run locally::

    uvicorn api.src.main:app --reload

Then open http://localhost:8000/docs for the interactive Swagger UI.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from . import __version__

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):  # pragma: no cover - trivial lifecycle hook
    """Startup / shutdown lifecycle hook."""
    logger.info("Starting AI in Modern Psychology API v%s", __version__)
    yield
    logger.info("Shutting down AI in Modern Psychology API")


DESCRIPTION = """
## AI in Modern Psychology — Programmatic Workbench

This API exposes the educational models from the
[`ai-in-modern-psychology`](https://github.com/DaScient/ai-in-modern-psychology)
workbench as HTTP endpoints so that learners can experiment with them from
notebooks, web demos, or scripted assignments.

It is a **teaching artefact**: every endpoint is intentionally simple,
fully open source, and explicitly *not* validated for clinical or
high-stakes use. Each route maps to a chapter of the companion book.

| Route prefix | Chapter | Underlying module |
|--------------|---------|-------------------|
| `/api/v1/memory` | Ch 6 — Memory models | `code.foundations.act_r_simulation` |
| `/api/v1/safety` | Ch 10 — Therapy chatbots | `code.clinical.therapy_safety` |
| `/api/v1/risk`   | Ch 8 / 11 — Diagnostic & decision support | `code.clinical.risk_prediction` |
| `/api/v1/fairness` | Ch 13 / 22 — Bias auditing | `code.ethics.fairness_metrics` |
| `/api/v1/learning` | Ch 14 — Adaptive learning | `code.io_ed.adaptive_learning` |
| `/api/v1/social` | Ch 16 — Opinion dynamics | `code.social.polarization_abm` |

### Conventions

* All endpoints accept and return JSON.
* Numeric arrays are passed as plain JSON lists.
* No authentication is required for the educational deployment; productionising
  the service is left as an exercise (see `curriculum/assignments`).

### Safety

Endpoints that touch sensitive scenarios (crisis detection, risk prediction)
always return *educational* output. They must not be used for triage,
diagnosis, or any real-world decision-making.
"""


def create_app() -> FastAPI:
    """Application factory — kept separate so tests can rebuild a clean app."""
    app = FastAPI(
        title="AI in Modern Psychology API",
        description=DESCRIPTION,
        version=__version__,
        openapi_tags=[
            {"name": "Memory", "description": "ACT-R style declarative memory"},
            {"name": "Safety", "description": "Therapy-chatbot crisis escalation"},
            {"name": "Risk", "description": "Clinical risk prediction (educational)"},
            {"name": "Fairness", "description": "Algorithmic-fairness audits"},
            {"name": "Learning", "description": "Bayesian knowledge tracing"},
            {"name": "Social", "description": "Opinion-dynamics agent-based models"},
            {"name": "System", "description": "Health and metadata"},
        ],
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        contact={
            "name": "AI in Modern Psychology — DaScient Press",
            "url": "https://github.com/DaScient/ai-in-modern-psychology",
        },
        license_info={
            "name": "MIT (code) / CC BY-NC-SA 4.0 (text)",
            "url": "https://opensource.org/licenses/MIT",
        },
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )

    # Import routers lazily to keep top-level import light during testing.
    from .endpoints import (
        fairness_router,
        learning_router,
        memory_router,
        risk_router,
        safety_router,
        social_router,
    )

    app.include_router(memory_router.router, prefix="/api/v1/memory", tags=["Memory"])
    app.include_router(safety_router.router, prefix="/api/v1/safety", tags=["Safety"])
    app.include_router(risk_router.router, prefix="/api/v1/risk", tags=["Risk"])
    app.include_router(fairness_router.router, prefix="/api/v1/fairness", tags=["Fairness"])
    app.include_router(learning_router.router, prefix="/api/v1/learning", tags=["Learning"])
    app.include_router(social_router.router, prefix="/api/v1/social", tags=["Social"])

    @app.get("/health", tags=["System"], summary="Liveness probe")
    async def health_check() -> dict:
        """Return service health and version metadata."""
        return {"status": "healthy", "version": __version__}

    @app.get("/", tags=["System"], summary="Service index")
    async def index() -> dict:
        """Top-level metadata document linking to the docs and source."""
        return {
            "name": "AI in Modern Psychology API",
            "version": __version__,
            "docs": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json",
            "source": "https://github.com/DaScient/ai-in-modern-psychology",
        }

    def custom_openapi() -> dict:
        if app.openapi_schema:
            return app.openapi_schema
        schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )
        schema.setdefault("components", {})
        schema["components"]["examples"] = {
            "SafetyMessage": {
                "value": {"message": "I had a tough day at work but I'm OK."}
            },
            "BKTUpdate": {
                "value": {"p_mastery": 0.1, "correct": True},
            },
            "FairnessAudit": {
                "value": {
                    "y_true": [1, 0, 1, 0, 1, 1, 0, 0],
                    "y_pred": [1, 0, 1, 1, 0, 1, 0, 0],
                    "sensitive": [0, 0, 0, 0, 1, 1, 1, 1],
                }
            },
        }
        app.openapi_schema = schema
        return app.openapi_schema

    app.openapi = custom_openapi
    return app


app = create_app()
