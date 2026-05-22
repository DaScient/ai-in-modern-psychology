# Chapter 22: Ethics of AI in Psychology

## Learning Objectives

By the end of this chapter, you should be able to:

- Frame applied ethics for AI in psychology around four lenses: *fairness*, *autonomy*, *welfare*, and *accountability*.
- Distinguish bias-in-data, bias-in-model, and bias-in-deployment.
- Run a complete fairness audit with `code.ethics.fairness_metrics` and the `/api/v1/fairness/audit` endpoint.
- Articulate the impossibility theorem and pick a metric *with* a normative justification.
- Combine fairness with calibration in a clinical risk pipeline.

## Overview

Ethics in AI psychology is rarely settled by a single principle. This chapter treats *fairness* as the most operational entry point — the place where principles must become metrics — and shows how the other lenses (autonomy in Chapter 19, welfare in Chapter 9, accountability in Chapter 23) cohere around it. Bias is not a single technical problem; it is a family of problems with distinct origins and distinct mitigations. The aim of an audit is not to eliminate bias (impossible) but to make trade-offs visible and accountable.

## 22.1 Three Sources

- **Bias in data** — historical, sampling, measurement, label bias.
- **Bias in model** — inductive biases, feature selection, objective choice.
- **Bias in deployment** — different thresholds, different populations, different downstream uses.

Mitigation must match source: re-weighting fixes (1), constraint-based training fixes (2), threshold/contextual policy fixes (3).

## 22.2 The Metrics Zoo

| Metric | Equation | Best when |
|--------|----------|-----------|
| Demographic parity | $P(\hat Y \mid A)$ equal | Allocation tasks, low base-rate diff |
| Equal opportunity | $TPR$ equal | True positives matter most (e.g., screening) |
| Equalized odds | $TPR$ and $FPR$ equal | Both errors matter (e.g., bail) |
| Calibration | $P(Y \mid \hat Y, A) = P(Y \mid \hat Y)$ | Risk scores given to humans |
| Counterfactual fairness | Decision invariant to $A$ | Causal interpretation available |

The **impossibility theorem** says you cannot have *all* of these at once when base rates differ.

## 22.3 Calibration vs. Fairness

A clinically calibrated risk model and a demographically parity-fair model can be the *same* model only if base rates are equal. In any other case, the choice is normative. This chapter argues that, for clinical risk, **calibration within group** is the right default — but the choice must be documented in the model card.

## 22.4 Beyond Group Fairness

- **Subgroup fairness** — Kearns et al., 2018: fairness across *combinations* of attributes.
- **Individual fairness** — similar individuals receive similar predictions (Dwork et al., 2012).
- **Procedural fairness** — fairness *of the process*, not just outputs.

The richest deployments combine group, subgroup, and procedural views.

```{admonition} Try it
:class: tip
Run the in-repo API:

    curl -X POST localhost:8000/api/v1/fairness/audit -H 'Content-Type: application/json' \
        -d '{"y_true":[1,0,1,0,1,1,0,0],"y_pred":[1,0,1,1,0,1,0,0],"sensitive":[0,0,0,0,1,1,1,1]}'

and read the per-group disparities. Repeat with `n=200` synthetic rows from
`code/io_ed/hiring_bias_audit.py`.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **TPR / FPR** | True / false positive rate. |
| **PPV / NPV** | Positive / negative predictive value. |
| **Subgroup fairness** | Across intersections of attributes. |
| **Individual fairness** | Similar individuals, similar outputs. |
| **Procedural fairness** | Fair process, not just outcome. |

## Worked Example: A Three-Metric Audit

Compute DP, EO, and EOdds on the same data. Show that the three rank models differently. Justify a choice for: (a) hiring, (b) suicide-risk screening, (c) targeted advertising.

## Hands-on Exercises

1. Reproduce the impossibility theorem on synthetic data with base rates 0.1 vs. 0.3.
2. Use threshold post-processing to equalise TPR. Report calibration loss.
3. Add an *intersectional* attribute (e.g., gender × age band) and re-audit.

## Case Study: Optum's Care-Management Algorithm

Obermeyer et al. (2019) showed that a widely deployed care-management algorithm produced equal *cost predictions* across racial groups — but *under-predicted illness* for Black patients because past healthcare spending was lower in that group. Lesson: bias-in-label is hardest to fix and hardest to see.

## Common Pitfalls

- Picking the metric to fit the conclusion.
- Auditing only at the model layer.
- Forgetting calibration when reporting fairness.

## Connections to Other Chapters

- Hiring fairness → **Chapter 13**.
- Clinical decision support → **Chapter 11**.
- Cultural validity → **Chapter 18**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Which metric should be the default for clinical risk scoring? Defend.
2. Can a fair model be unfair in deployment? Give an example.
3. Should fairness audits be public?

## Further Reading

- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*.
- Chouldechova, A. (2017). Fair prediction with disparate impact. *Big Data*.
- Obermeyer, Z., et al. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366, 447–453.
- Mitchell, S., Potash, E., Barocas, S., D'Amour, A., & Lum, K. (2021). Algorithmic fairness: Choices, assumptions, and definitions. *Annual Review of Statistics*.
