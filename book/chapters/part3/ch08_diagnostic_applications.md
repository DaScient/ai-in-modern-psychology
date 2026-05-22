# Chapter 8: Diagnostic Applications

## Learning Objectives

By the end of this chapter, you should be able to:

- Identify the three regimes in which ML changes psychiatric diagnosis: triage, screening, and confirmation.
- Reason about *base rates* and their effect on positive predictive value.
- Use SHAP explanations to communicate risk to a clinician (notebook 02).
- Decide when *not* to deploy a diagnostic model.

## Overview

Machine-learning models for psychiatric diagnosis from EHR, imaging, and behavioural data have proliferated. The shift from research to deployment, however, is governed by tests that ML papers rarely report: *calibration*, *net benefit*, and *transportability*.

## 8.1 Predicting Suicide Attempts

Walsh, Ribeiro, and Franklin's pioneering work {cite}`walsh2017predicting` showed that EHR-trained models can outperform clinician judgement at short-horizon prediction. See [`notebooks/02_suicide_risk_SHAP.ipynb`](../../../notebooks/02_suicide_risk_SHAP.ipynb) for a runnable case study. The headline result — AUC ≈ 0.84 in held-out data — is impressive *and* compatible with very high false-positive rates at clinically useful thresholds.

## 8.2 Base Rates, Calibration, and Clinical Utility

With base rates near 0.5 %, even AUC-0.85 models produce many false positives. **Net benefit** and **decision-curve analysis** (Chapter 11, `code/clinical/decision_curve.py`) become essential because they incorporate the *threshold probability* a clinician would actually use.

| Base rate | AUC | Threshold | Approx. PPV |
|-----------|-----|-----------|--------------|
| 0.5 % | 0.85 | 0.05 | ~5 % |
| 5 % | 0.85 | 0.20 | ~30 % |
| 30 % | 0.85 | 0.40 | ~70 % |

The same model can be useless in one population and useful in another.

## 8.3 Imaging Biomarkers

Structural and functional MRI features have been used to predict transition to psychosis, treatment response, and ADHD subtypes. Replication across scanners and sites remains the central methodological problem (ABCD, ENIGMA consortia).

## 8.4 Explainability for Clinicians

SHAP values turn opaque ensemble models into per-patient explanations that can guide — but should not replace — clinical reasoning. Notebook 02 walks through:

1. Train a calibrated XGBoost.
2. Compute SHAP for a flagged patient.
3. Generate a one-page summary clinicians can act on.

```{admonition} Try it
:class: tip
Modify the SHAP notebook to add a *fairness audit* slice (e.g., separate
SHAP summaries for two simulated subgroups). Discuss what you see and what
the audit *cannot* tell you about deployment risk.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **PPV** | Positive predictive value — P(disease &#124; positive test). |
| **Net benefit** | Decision-theoretic utility at a chosen threshold. |
| **Transportability** | Whether a model trained on one site works on another. |
| **SHAP value** | Shapley-value attribution of a prediction to a feature. |
| **Calibration drift** | Decline in calibration over time / across sites. |

## Worked Example: From AUC to Action

A risk model has AUC 0.85 in derivation, 0.80 in external validation. Population base rate is 1 %. Compute PPV at the 0.05 threshold; compute decision-curve net benefit; report whether you would deploy. The notebook walks through these steps.

## Hands-on Exercises

1. Recompute notebook 02's metrics on a synthetic cohort with base rate halved. Discuss.
2. Use `code.clinical.decision_curve` to find the threshold range where the model is *not* clinically useful.
3. Draft a one-page "clinician card" summarising what the model is and is not validated for.

## Case Study: VHA REACH-VET

The U.S. Veterans Health Administration's REACH-VET program identifies the top 0.1 % of veterans at suicide risk monthly and dispatches outreach. Public evaluation shows reduced hospitalisations among flagged veterans (Kessler et al., 2017). The model is *narrow* and the intervention *non-coercive*; both design choices matter ethically.

## Common Pitfalls

- Reporting AUC without base rate or threshold.
- Confusing high TPR with clinical utility.
- Ignoring the cost of a missed positive vs. a false positive.

## Connections to Other Chapters

- Calibration and decision curves → **Chapter 11**.
- Explainability for non-technical stakeholders → **Chapter 22**.
- Triage in crisis settings → **Chapter 12**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. At what PPV would you support routine deployment of a suicide-risk model?
2. Does an opaque-but-better model ever beat a transparent-but-worse one in clinical settings?
3. What pre-deployment monitoring would you require for a 1-year pilot?

## Further Reading

- Walsh, C. G., Ribeiro, J. D., & Franklin, J. C. (2017). Predicting risk of suicide attempts. *Clinical Psychological Science*.
- Kessler, R. C., et al. (2017). Developing a practical suicide risk prediction model for targeting high-risk patients in the Veterans Health Administration. *International Journal of Methods in Psychiatric Research*.
- Vickers, A. J., & Elkin, E. B. (2006). Decision-curve analysis. *Medical Decision Making*, 26(6), 565–574.
- Char, D. S., et al. (2018). Implementing machine learning in health care — addressing ethical challenges. *NEJM*.
