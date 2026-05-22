# Assignment 2 — Audit a Hiring Algorithm for Bias

> Aligned with Chapter 13 of *AI in Modern Psychology*.

## Learning Goals

- Apply demographic parity, equal opportunity, and equalized odds.
- Interpret intersectional disparities.
- Recommend mitigation strategies grounded in the literature.

## Task

1. Use `code/clinical/risk_prediction.generate_synthetic_ehr` or the synthetic
   hiring dataset to train a logistic regression and an XGBoost model that
   predict a positive outcome.
2. Add a binary protected attribute and a continuous protected attribute
   (e.g., simulated socio-economic status). Inject historical bias of your own
   choosing into the data-generating process.
3. Compute the full fairness report from `code.ethics.fairness_metrics`.
4. Try **at least one** mitigation technique (pre-, in-, or post-processing).
5. Write a 1000-word report explaining what you found, what trade-offs you observed,
   and what you would recommend to a hiring manager who wants to use the model.

## Deliverables

- A reproducible notebook in `assignment_02_<your_name>.ipynb`.
- A 1000-word report `assignment_02_<your_name>.md`.

## Rubric

| Criterion | Points |
|-----------|-------:|
| Correct data generation and bias injection | 15 |
| Correct computation of fairness metrics | 25 |
| Effective mitigation step and analysis | 25 |
| Quality of report and recommendations | 30 |
| Reproducibility | 5 |
