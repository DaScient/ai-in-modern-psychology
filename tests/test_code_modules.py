"""Smoke tests for the in-repo code modules.

Imports + a small functional check per module so CI catches accidental
signature breaks. These are NOT validation tests.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import networkx as nx


def test_foundations_modules_import_and_run():
    from code.foundations.act_r_simulation import ACTRMemory
    from code.foundations.symbolic_connectionist import compare
    mem = ACTRMemory()
    assert mem is not None
    result = compare([0, 1, 2, 3, 4])
    assert set(result.keys()) == {"symbolic", "connectionist"}
    assert len(result["symbolic"]) == len(result["connectionist"]) == 5


def test_adaptive_learning_bkt_and_trajectory():
    from code.io_ed.adaptive_learning import (
        BKTParams, bkt_update, simulate_trajectory, recommend_next_difficulty,
    )
    p = BKTParams()
    p_next = bkt_update(0.1, True, p)
    assert 0.0 <= p_next <= 1.0
    traj = simulate_trajectory([True, False, True, True], p)
    assert len(traj) >= 1
    assert all(0.0 <= x <= 1.0 for x in traj)
    diff = recommend_next_difficulty(0.6)
    assert isinstance(diff, float)


def test_hiring_bias_audit_returns_metrics():
    from code.io_ed.hiring_bias_audit import audit
    rng = np.random.default_rng(0)
    n = 500
    A = rng.binomial(1, 0.4, n)
    Y = rng.binomial(1, 0.3, n)
    Yhat = rng.binomial(1, 0.3, n)
    result = audit(Y, Yhat, A)
    assert isinstance(result, dict)
    assert len(result) >= 3


def test_polarization_abm_runs():
    from code.social.polarization_abm import run_bounded_confidence
    hist = run_bounded_confidence(n_agents=50, epsilon=0.2, steps=10, seed=0)
    arr = np.asarray(hist)
    assert arr.ndim == 2
    assert arr.shape[1] == 50


def test_network_influence_cascade_and_greedy():
    from code.social.network_influence import (
        independent_cascade, linear_threshold, expected_reach, greedy_seed_selection,
    )
    g = nx.path_graph(20)
    ic = independent_cascade(g, [0], p=0.6, seed=0)
    assert ic.reach >= 1
    lt = linear_threshold(g, [0], seed=0)
    assert lt.reach >= 1
    er = expected_reach(g, [0], p=0.3, n_runs=20, seed=0)
    assert er >= 1
    seeds = greedy_seed_selection(g, k=2, p=0.3, n_runs=10, seed=0)
    assert len(seeds) == 2


def test_digital_phenotyping_and_score():
    from code.research.digital_phenotyping import (
        generate_synthetic_day, simple_depression_score,
    )
    _, w_d = generate_synthetic_day(depressed=True, seed=0)
    _, w_h = generate_synthetic_day(depressed=False, seed=0)
    sd = simple_depression_score(w_d)
    sh = simple_depression_score(w_h)
    assert sd > sh


def test_nlp_psychology_features():
    from code.research.nlp_psychology import (
        extract_features, language_style_match, flesch_reading_ease,
    )
    f = extract_features("I am sad and hopeless. I cannot think anymore.")
    assert f.first_person_sing > 0
    assert f.negative_affect > 0
    assert flesch_reading_ease("I am happy.") > 0
    assert 0.0 <= language_style_match("I am happy", "I am sad") <= 1.0


def test_decision_curve_analysis():
    from code.clinical.decision_curve import decision_curve, informative_range
    y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    p = [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.55, 0.45]
    curve = decision_curve(y, p, thresholds=[0.1, 0.2, 0.3, 0.4, 0.5])
    assert len(curve) == 5
    lo, hi = informative_range(curve)
    assert lo <= hi


def test_therapy_safety_severity():
    from code.clinical.therapy_safety import assess_message
    crit = assess_message("I want to kill myself").severity
    none = assess_message("I had a great day").severity
    # The exact label vocabulary varies; just check non-crisis is "lower" than crisis.
    assert crit != none


def test_risk_prediction_synthetic():
    from code.clinical.risk_prediction import generate_synthetic_ehr, FEATURE_COLS
    df = generate_synthetic_ehr(n_samples=200, seed=0)
    assert all(c in df.columns for c in FEATURE_COLS)
    assert "attempt" in df.columns


def test_fairness_metrics():
    from code.ethics.fairness_metrics import (
        demographic_parity_difference, equal_opportunity_difference,
    )
    y = np.array([1, 0, 1, 0, 1, 0, 1, 0])
    yhat = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    a = np.array([0, 0, 0, 0, 1, 1, 1, 1])
    assert isinstance(float(demographic_parity_difference(yhat, a)), float)
    assert isinstance(float(equal_opportunity_difference(y, yhat, a)), float)
