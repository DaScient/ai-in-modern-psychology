# Chapter 4: Digital Phenotyping

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Digital Phenotyping*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Use smartphone sensors, wearables, and ecological momentary assessment (EMA) to measure mental health in everyday life.

## 4.1 Passive vs. Active Sensing

Passive sensing collects data without user effort (GPS, accelerometry, screen-time). Active sensing prompts users via EMA. Combined, they provide a high-frequency window into behaviour at ecological scale.

## 4.2 Common Sensor Modalities

- **Actigraphy** — sleep / activity / circadian disruption
- **GPS & Wi-Fi** — location entropy, mobility radius
- **Keystroke dynamics** — psychomotor slowing
- **Voice** — prosody, jitter, shimmer
- **Heart-rate variability** — autonomic regulation

## 4.3 Inferring Affect and Cognition

Machine-learning models map raw sensor streams to constructs such as depression severity, anxiety, and cognitive load. The notebook in `/code/clinical/` shows a depression-detection pipeline with missing-data handling.

## 4.4 Validity, Privacy, and Reactivity

```{warning}
Digital phenotyping raises acute privacy concerns. Always pair deployment with the [data governance policy](../../../ethics_toolkit/data_governance_policy.md) and informed-consent procedures.
```

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of digital phenotyping are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Onnela, J.-P., & Rauch, S. L. (2016). Harnessing smartphone-based digital phenotyping. *Neuropsychopharmacology*, 41, 1691–1696.
