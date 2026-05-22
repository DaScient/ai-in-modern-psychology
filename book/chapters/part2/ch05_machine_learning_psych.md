# Chapter 5: Machine Learning in Psychology

## Learning Objectives

By the end of this chapter, you should be able to:

- Choose between supervised, unsupervised, and reinforcement learning for a given psychological question.
- Diagnose the most common methodological pitfalls (leakage, p-hacking via hyperparameters, base-rate neglect).
- Build a defensible **pre-registered ML pipeline** for psychological data.
- Read calibration plots, ROC, PR, and decision curves with equal fluency.

## Overview

Machine learning enters psychology in three modes: as a *prediction tool* (Can we forecast relapse?), as a *measurement instrument* (Can we estimate depression from voice?), and as a *theory* (Does the network's structure tell us something about the mind?). The methodological hazards differ across modes.

## 5.1 Prediction vs. Explanation

Yarkoni & Westfall (2017) argue that psychology has confused *fit* with *prediction*. A model with high in-sample $R^2$ may have *no* out-of-sample predictive value. ML reverses the convention: report held-out performance first, then ask which features mattered.

## 5.2 Choosing a Learner

| Construct | Sensible default |
|-----------|-------------------|
| Linear, low-dimensional EHR | Logistic regression with L2 |
| Tabular with interactions | Gradient boosting (XGBoost, LightGBM) |
| Text | Transformer encoder + linear head |
| Time-series sensor | 1-D CNN or temporal convolutional network |
| Network data | Graph neural net or node2vec + classifier |

Always benchmark against a *trivial* baseline (predict the majority class, predict the mean).

## 5.3 The Five Most Common Pitfalls

1. **Data leakage.** Subject-level data appearing in both train and test sets — particularly common in within-subject sensor studies.
2. **Look-ahead bias.** Using features computed from data that postdates the target time.
3. **Class-imbalance illusions.** A 95 %-accuracy model on a 5 % base rate may be useless.
4. **Hyperparameter p-hacking.** Tuning on the test set is statistically indistinguishable from running 1000 t-tests.
5. **Overinterpreted feature importance.** Permutation importance differs from causal importance.

## 5.4 Defensible Reporting

Adopt the **TRIPOD-AI** {cite}`collins2024tripod` checklist for prognostic models. At minimum, report:

- Source population, inclusion criteria, missingness pattern.
- Train/validation/test splits *with rationale*.
- Calibration in addition to discrimination.
- Decision-curve analysis (see `code/clinical/decision_curve.py`).

## 5.5 From Model to Measurement

When a model is used to *measure* a construct (e.g., depression from speech), classical measurement validity criteria apply: test–retest reliability, convergent validity, discriminant validity. ML practitioners rarely report these. Psychologists must.

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Calibration** | Predicted probabilities matching empirical frequencies. |
| **Net benefit** | Decision-theoretic measure of clinical usefulness at a threshold. |
| **Leakage** | Information from the future or the test set contaminating training. |
| **Shrinkage / regularisation** | Penalising model complexity to combat over-fit. |
| **Calibration plot** | Predicted vs. observed probability decile plot. |

## Worked Example: A Defensible Pipeline

```python
from code.clinical.risk_prediction import generate_synthetic_ehr, FEATURE_COLS
from sklearn.model_selection import GroupKFold
from sklearn.linear_model import LogisticRegressionCV

df = generate_synthetic_ehr(n_samples=5000, seed=0)
X, y = df[FEATURE_COLS], df["attempt"]
# Pretend each row is one visit; group by patient id (here a row index proxy).
cv = GroupKFold(n_splits=5).split(X, y, groups=df.index // 10)
```

Now add: nested CV for hyperparameter selection, isotonic recalibration on the
inner fold, and a decision-curve analysis using `code/clinical/decision_curve.py`.

## Hands-on Exercises

1. Re-run the SHAP notebook with a deliberately introduced leakage feature ("future ED visit") and observe the inflated AUC. Then remove it.
2. Plot a calibration curve before and after isotonic regression.
3. Use `code.clinical.decision_curve.decision_curve` to compute net benefit and discuss whether the model is *clinically* useful at the threshold a clinician would actually choose.

## Case Study: The Limits of Behavioural Prediction

The Fragile Families Challenge {cite}`salganik2020measuring` had 160 teams predict six life outcomes from a rich longitudinal dataset. *No* team meaningfully beat a linear regression baseline. The lesson is humbling: in messy social data, signal can be very small and *no architectural sophistication recovers it*.

## Common Pitfalls

- Treating AUC as the only metric.
- Comparing models trained on different splits.
- Reporting "external validity" without actually testing on external data.

## Connections to Other Chapters

- Calibration and decision curves → **Chapter 11**.
- Feature engineering on sensor data → **Chapter 4**.
- Fairness audits during the ML pipeline → **Chapter 13**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. When does explanation matter more than prediction in your subfield, and when not?
2. Is a model that predicts well but reveals nothing about mechanism still useful for psychology?
3. Pre-register an ML study you have done or could do. What would the protocol fix?

## Further Reading

- Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology. *Perspectives on Psychological Science*, 12(6), 1100–1122.
- Collins, G. S., et al. (2024). TRIPOD+AI statement. *BMJ*.
- Bzdok, D., & Yeo, B. T. (2017). Inference in the age of big data. *NeuroImage*, 155, 549–564.
- Steyerberg, E. W. (2019). *Clinical Prediction Models* (2nd ed.). Springer.
