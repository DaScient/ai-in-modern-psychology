# Chapter 8: Diagnostic Applications

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Diagnostic Applications*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Machine-learning models for psychiatric diagnosis from EHR, imaging, and behavioural data.

## 8.1 Predicting Suicide Attempts

Walsh, Ribeiro, and Franklin's pioneering work {cite}`walsh2017predicting` showed that EHR-trained models can outperform clinician judgement at short-horizon prediction. See [`notebooks/02_suicide_risk_SHAP.ipynb`](../../../notebooks/02_suicide_risk_SHAP.ipynb) for a runnable case study.

## 8.2 Base Rates, Calibration, and Clinical Utility

With base rates near 0.5 %, even high-AUC models produce many false positives. Net benefit and decision-curve analysis become essential.

## 8.3 Imaging Biomarkers

Structural and functional MRI features have been used to predict transition to psychosis, treatment response, and ADHD subtypes.

## 8.4 Explainability for Clinicians

SHAP values turn opaque ensemble models into per-patient explanations that can guide — but should not replace — clinical reasoning.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of diagnostic applications are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Walsh, C. G., Ribeiro, J. D., & Franklin, J. C. (2017). Predicting risk of suicide attempts.
