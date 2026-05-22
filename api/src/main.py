"""FastAPI application entry point for AI in Biological Sciences API."""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events."""
    logger.info("Starting AI Bio API...")
    yield
    logger.info("Shutting down AI Bio API...")


app = FastAPI(
    title="AI in Biological Sciences API",
    description="""
## Welcome to the AI Bio API

This API provides programmatic access to state-of-the-art AI models for
biological research, aligned with the textbook "AI in Biological Sciences"
(DaScient Press, 2025).

### Key Capabilities:

- **Protein Structure**: AlphaFold2-level prediction and design
- **Genomics**: Variant interpretation, regulatory element prediction
- **Single-Cell**: Embeddings, trajectories, cell-type annotation
- **Ecology**: Species distribution, tipping point detection
- **Clinical**: Diagnosis, prognosis, treatment planning
- **Drug Discovery**: Docking, de novo design, ADMET prediction
- **Literature**: Hypothesis generation, knowledge graph mining
- **Ethics**: Bias auditing, fairness metrics

### Authentication

Include your API key in the `X-API-Key` header:
```bash
curl -H "X-API-Key: your_key" https://api.bioai.dascient.com/health
```

### Rate Limits

| Tier | Requests/second | Monthly cap |
|------|----------------|-------------|
| Academic | 10 | 100,000 |
| Commercial | 50 | 1,000,000 |
| Enterprise | 500 | Unlimited |

### Interactive Documentation

- Swagger UI: `/docs`
- ReDoc: `/redoc`

### Versioning

Current version: `v1`. Major versions introduce breaking changes.
""",
    version="1.0.0",
    openapi_tags=[
        {"name": "Protein", "description": "Protein structure and design"},
        {"name": "Genomics", "description": "Genomic sequence analysis"},
        {"name": "Single-Cell", "description": "Single-cell omics"},
        {"name": "Ecology", "description": "Ecological modeling"},
        {"name": "Clinical", "description": "Medical AI"},
        {"name": "Drug", "description": "Drug discovery"},
        {"name": "Literature", "description": "Literature mining"},
        {"name": "Ethics", "description": "Bias auditing"},
        {"name": "System", "description": "System status"},
    ],
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "DaScient Support",
        "url": "https://dascient.com/support",
        "email": "support@dascient.com",
    },
    license_info={
        "name": "CC BY-NC-SA 4.0",
        "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
    },
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from .endpoints import protein_router, single_cell_router  # noqa: E402

app.include_router(protein_router.router, prefix="/api/v1/protein", tags=["Protein"])
app.include_router(single_cell_router.router, prefix="/api/v1/scell", tags=["Single-Cell"])


@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


def custom_openapi():
    """Custom OpenAPI schema with examples."""
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema.setdefault("components", {})
    openapi_schema["components"]["examples"] = {
        "ProteinSequence": {
            "value": {
                "sequence": "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDP"
            }
        },
        "SingleCellMatrix": {
            "value": {
                "counts": [[0, 1, 2], [3, 0, 1], [2, 3, 0]],
                "genes": ["GAPDH", "TP53", "BRCA1"],
                "cells": ["cell_1", "cell_2", "cell_3"],
            }
        },
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
