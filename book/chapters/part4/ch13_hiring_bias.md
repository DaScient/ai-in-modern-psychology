# Chapter 13: Hiring Bias

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Hiring Bias*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Algorithmic hiring, sources of bias, fairness metrics, and legal frameworks.

## 13.1 Sources of Bias

- Historical bias in training data
- Representation bias in samples
- Measurement bias in proxies (e.g., ZIP code for socio-economic status)
- Aggregation bias across subgroups

## 13.2 Fairness Metrics

Demographic parity, equal opportunity, equalized odds — see [`code/ethics/fairness_metrics.py`](../../../code/ethics/fairness_metrics.py). The metrics are mutually incompatible in general; choice depends on context.

## 13.3 Mitigation Strategies

Pre-, in-, and post-processing approaches. Adversarial debiasing trades off accuracy for fairness.

## 13.4 Legal Landscape

Title VII (US), EEOC technical assistance, NYC Local Law 144, and the EU AI Act all impose disclosure and audit requirements.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of hiring bias are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*.
