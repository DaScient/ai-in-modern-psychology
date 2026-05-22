# Chapter 5: Machine Learning for Psychologists

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Machine Learning for Psychologists*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

A pragmatic introduction to supervised, unsupervised, and reinforcement learning for psychological data.

## 5.1 Supervised vs. Unsupervised Learning

Supervised learning predicts a known target (diagnosis, outcome). Unsupervised learning discovers structure (clusters, latent dimensions). Each addresses different psychological questions.

## 5.2 Model Selection and Overfitting

Psychological data are noisy and high-dimensional. Cross-validation, regularization, and held-out test sets are essential to avoid optimistic estimates that fail to replicate.

## 5.3 Gradient Boosting and Tabular Data

Gradient boosting (XGBoost, LightGBM) remains state-of-the-art for tabular clinical data and is used throughout the clinical chapters.

## 5.4 From Prediction to Explanation

Predictive accuracy is necessary but not sufficient. SHAP {cite}`lundberg2017unified` and LIME provide local explanations that are critical for clinical adoption.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of machine learning for psychologists are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology. *Perspectives on Psychological Science*, 12(6), 1100–1122.
