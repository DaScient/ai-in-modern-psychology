# Assignment 04 — Digital Phenotyping Pipeline

> Companion to **Chapter 4** (*Digital Phenotyping*) and **Chapter 5**
> (*Machine Learning in Psychology*).

## Learning Objectives

By the end of this assignment, you should be able to:

- Generate, clean, and feature-engineer passive-sensing data.
- Implement a defensible per-window feature extractor.
- Discuss the construct validity of *every* feature you compute.
- Identify three privacy issues your pipeline raises.

## Deliverables

1. A Jupyter notebook implementing the pipeline.
2. A 2-page write-up using the structure below.
3. A completed [data governance policy](../../ethics_toolkit/data_governance_policy.md)
   for your hypothetical study.

## Part 1 — Pipeline (40 %)

Using `code.research.digital_phenotyping`:

1. Generate 14 simulated days of data (mix of `depressed=True` and `False`).
2. Compute per-day windowed features.
3. Apply `simple_depression_score`; plot the score over days.
4. Add at least **one** new feature of your own design and justify it.

## Part 2 — Validation (30 %)

- Discuss whether your new feature reflects a *construct* or a *correlate*.
- Identify one published validation study you would cite.
- State at least three *anchor measures* (e.g., PHQ-9) you would collect alongside the sensors.

## Part 3 — Ethics (30 %)

Using the data-governance template, document:

1. What is collected, why, where it lives, who can read it, retention horizon.
2. The minimum-data alternative that would still answer the research question.
3. The participant communication script (≤ 200 words, Flesch ≥ 60).

## Rubric

| Criterion | Excellent (90+) | Adequate (70–89) | Insufficient (< 70) |
|-----------|------------------|-------------------|----------------------|
| Pipeline runs | Reproducible, parameterised | Runs end-to-end | Errors on rerun |
| Feature design | Novel, validated, theory-anchored | Reasonable, justified | Ad hoc |
| Validation reasoning | Distinguishes construct vs. correlate | Cites relevant lit | Surface-level |
| Ethics artefact | Covers all 12 sections | Most sections | Skeleton only |

## Suggested timing: 8–10 hours.
