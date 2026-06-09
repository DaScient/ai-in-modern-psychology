# Chapter 13: Hiring Bias

## Learning Objectives

By the end of this chapter, you should be able to:

- Identify five sources of bias in algorithmic hiring.
- Compute demographic parity, equal opportunity, and equalized odds with `code.ethics.fairness_metrics`.
- Discuss the *impossibility theorem* and what it implies for tool choice.
- Audit a candidate-screening pipeline against US (EEOC), NYC Local Law 144, and EU AI Act requirements.

## Overview

Algorithmic hiring is the longest-running large-scale deployment of AI in industrial-organisational psychology. It is also the area with the most mature legal scaffolding. The chapter reviews where bias enters, how to measure it, and what to do about it.

## 13.1 Sources of Bias

- **Historical bias** in training data (past hiring reflects past discrimination).
- **Representation bias** in samples (entry-level vs. promoted populations differ).
- **Measurement bias** in proxies (e.g., ZIP code for socio-economic status).
- **Aggregation bias** across subgroups (one model for everyone hides subgroup effects).
- **Evaluation bias** (benchmarks themselves are skewed).

The single most important practical lesson: *if the training labels were biased, the model will reproduce that bias*. No fancy method magically removes it.

## 13.2 Fairness Metrics

Three metrics dominate practice (see `code/ethics/fairness_metrics.py`):

- **Demographic parity** — $P(\hat Y = 1 \mid A=0) = P(\hat Y = 1 \mid A=1)$.
- **Equal opportunity** — equal TPR across groups.
- **Equalized odds** — equal TPR *and* FPR.

The Kleinberg–Chouldechova **impossibility theorem** {cite}`chouldechova2017fair` shows that, when base rates differ across groups, calibration, equal opportunity, and predictive parity cannot all hold simultaneously. The choice between metrics is therefore *normative*, not technical.

## 13.3 Mitigation Strategies

Three families:

- **Pre-processing** — reweighting / re-sampling the training data.
- **In-processing** — adversarial debiasing, fairness-constrained optimisation.
- **Post-processing** — group-specific thresholds (legal status varies by jurisdiction).

Adversarial debiasing trades off accuracy for fairness. Whether the trade-off is acceptable is again a normative question.

## 13.4 Legal Landscape

- **Title VII (US)** prohibits disparate impact in employment decisions.
- **EEOC** uses the 4/5ths rule as a practical screen.
- **NYC Local Law 144** (effective 2023) mandates annual bias audits for *automated employment decision tools* used on NYC candidates.
- **EU AI Act** (effective 2025) classifies employment-decision AI as *high-risk*, imposing data-quality, transparency, and human-oversight obligations.

A defensible audit must report the audited model, audited population, metrics chosen, and the auditor.

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Disparate impact** | Differential effect on a protected group regardless of intent. |
| **4/5ths rule** | EEOC practical screen: selection ratio < 80 % of majority. |
| **Calibration within groups** | P(Y=1 &#124; score, A) does not depend on A. |
| **Counterfactual fairness** | Decision unchanged if A had been different. |

## Worked Example: A Full Audit

```python
from code.io_ed.hiring_bias_audit import audit
import numpy as np
rng = np.random.default_rng(0)
n = 2000
A = rng.binomial(1, 0.4, n)
Y = rng.binomial(1, 0.3, n)
score = 0.3 * Y - 0.2 * A + rng.normal(0, 0.1, n)
Yhat = (score > 0).astype(int)
result = audit(Y, Yhat, A)
print(result)
```

The `audit` helper returns DPD, EOD, EOdds, threshold-passing booleans, and the per-group disparity table. Notebook 03 walks through the audit step-by-step with synthetic resume data.

## Hands-on Exercises

1. Use post-processing to *equalise* TPR across the two synthetic groups in notebook 03. Report the cost in overall accuracy.
2. Simulate the *impossibility theorem*: pick base rates 10 % vs. 30 % and show that calibration and equal opportunity cannot both hold.
3. Draft a one-page NYC Local Law 144 disclosure for a fictional company.

## Case Study: Amazon's Resume Screener

Amazon (Dastin, 2018) trained a resume screener on 10 years of historical hiring and discovered it penalised resumes containing the word *women's* (as in "women's chess club"). The system was discarded. Lesson: when labels encode prior bias, *removing the protected variable does not remove the bias*.

## Common Pitfalls

- Auditing on the training distribution only.
- Picking the metric *after* seeing the audit.
- Treating an audit as a one-time event rather than continuous monitoring.

## Connections to Other Chapters

- Fairness metric internals → **Chapter 22**.
- Adaptive learning fairness → **Chapter 14**.
- Privacy in candidate data → **Chapter 23**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Which fairness metric is right for your hiring context? Defend the choice as a normative argument, not a technical one.
2. Should companies be required to disclose the score a candidate received?
3. Is there a fair way to use historical hiring data at all?

## Further Reading

- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning* (open access).
- Chouldechova, A. (2017). Fair prediction with disparate impact. *Big Data*, 5(2).
- Raghavan, M., et al. (2020). Mitigating bias in algorithmic hiring. *FAT* '20.
- Selbst, A. D., et al. (2019). Fairness and abstraction in sociotechnical systems. *FAT* '19.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
