# Assignment 05 — Decision-Curve Analysis for Clinical Risk

> Companion to **Chapters 8 & 11**.

## Learning Objectives

- Compute *net benefit* across thresholds for a clinical risk model.
- Identify the *informative threshold range* and defend the operating point.
- Argue why discrimination and calibration alone are insufficient evidence for deployment.

## Deliverables

1. A notebook reproducing decision-curve analysis on the synthetic risk dataset.
2. A one-page memo to a fictional medical director recommending an operating point.

## Tasks

1. Use `code.clinical.risk_prediction.generate_synthetic_ehr` to create 5 000 rows.
2. Train a calibrated logistic regression (use `CalibratedClassifierCV`).
3. Compute and plot the decision curve over thresholds 0.005–0.5 using `code.clinical.decision_curve.decision_curve`.
4. Report the **informative threshold range** (use `informative_range`).
5. Pick an operating point and justify it on cost grounds (false positive cost vs. false negative cost) — **not** on Youden's J or any other ROC convenience.
6. In your memo, explain the curve to a non-technical clinician in ≤ 250 words.

## Stretch Goals

- Stratify the analysis by a synthetic protected attribute; do disparities exist within the informative range?
- Resample to halve the base rate and re-run. Does the informative range move? Why?

## Rubric

| Criterion | Excellent | Adequate | Insufficient |
|-----------|-----------|----------|--------------|
| Notebook | Reproducible, calibrated | Runs | Errors |
| Operating point | Cost-justified | Defended | Arbitrary |
| Memo readability | Flesch ≥ 60 | Readable | Jargon-heavy |
| Stretch | Both done | One done | None |

## Suggested timing: 6 hours.
