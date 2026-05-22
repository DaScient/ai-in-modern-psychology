# Assignment 06 — Polarization ABM and Network Influence

> Companion to **Chapters 16 & 17**.

## Learning Objectives

- Simulate opinion dynamics under bounded confidence.
- Implement and compare random / degree / greedy seed-selection strategies.
- Reason about the policy implications of cascade models.

## Deliverables

1. A notebook extending `notebooks/05_polarization_and_network_influence.ipynb`.
2. A 1500-word reflection on the *policy* implications.

## Tasks

1. **Polarization sweep.** Run `run_bounded_confidence` for $\varepsilon \in \{0.05, 0.10, 0.15, 0.20, 0.30\}$ with 200 agents, 100 steps. Plot final-opinion histograms.
2. **Cascade comparison.** On a 300-node Barabási–Albert graph, compare expected reach for $k=5$ seeds picked by random, degree, and `greedy_seed_selection`.
3. **Stubborn nodes.** Add a 10 % "stubborn-truthful" fraction (immune nodes); rerun task 2. Report the reach reduction.
4. **Reflection.** Address:
   - Could *targeted* prebunking reduce real-world misinformation cascades?
   - When is high-degree node *removal* ethically defensible, and when not?
   - What measurement do you not currently have access to that would change your answer?

## Rubric

| Criterion | Excellent | Adequate | Insufficient |
|-----------|-----------|----------|--------------|
| Polarization sweep | Clear, interpretable plots | Plots present | Errors |
| Cascade comparison | Lazy CELF or runtime analysis | Three strategies compared | Only one |
| Stubborn-node experiment | Sensitivity analysis | Single setting | Not attempted |
| Reflection | Integrates Chs 16 & 17 | Touches both | One-sided |

## Suggested timing: 8 hours.
