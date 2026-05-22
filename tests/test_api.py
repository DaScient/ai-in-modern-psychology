"""Smoke tests for the FastAPI Psychology API surface."""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from api.src.main import app

client = TestClient(app)


def test_root_and_health():
    r = client.get("/")
    assert r.status_code == 200
    h = client.get("/health")
    assert h.status_code == 200
    assert h.json()["status"] in ("ok", "healthy")


def test_memory_simulate():
    r = client.post("/api/v1/memory/simulate", json={
        "chunks": [{"name": "x", "retrieval_times": [0.0, 60.0]}],
        "end_time": 300.0, "n_points": 10,
    })
    assert r.status_code in (200, 422)


def test_safety_check():
    r = client.post("/api/v1/safety/check", json={"message": "I want to die"})
    assert r.status_code == 200
    assert "severity" in r.json()


def test_risk_score_synthetic():
    r = client.post("/api/v1/risk/score", json={
        "age": 35, "prior_self_harm": 1, "ed_visits": 2, "nighttime_ed": 1,
        "antidepressant_discontinued": 1, "sleep_disorder": 1, "location_entropy_high": 0,
    })
    assert r.status_code in (200, 422)


def test_fairness_audit():
    r = client.post("/api/v1/fairness/audit", json={
        "y_true":  [1, 0, 1, 0, 1, 0, 1, 0],
        "y_pred":  [1, 0, 1, 1, 0, 0, 1, 0],
        "sensitive": [0, 0, 0, 0, 1, 1, 1, 1],
    })
    assert r.status_code == 200


def test_learning_bkt_update():
    r = client.post("/api/v1/learning/bkt/update", json={"p_mastery": 0.2, "correct": True})
    assert r.status_code == 200
    assert "p_mastery_next" in r.json()


def test_social_abm_run():
    r = client.post("/api/v1/social/abm/run", json={"n_agents": 40, "epsilon": 0.2, "steps": 10, "seed": 0})
    assert r.status_code == 200
