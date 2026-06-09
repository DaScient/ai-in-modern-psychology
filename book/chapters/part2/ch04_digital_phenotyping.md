# Chapter 4: Digital Phenotyping

## Learning Objectives

By the end of this chapter, you should be able to:

- Define **digital phenotyping** and contrast passive vs. active sensing.
- List the main sensor modalities and the psychological constructs they have been used to infer.
- Build a feature-extraction pipeline from a raw GPS / accelerometer trace using `code.research.digital_phenotyping`.
- Identify the specific validity, privacy, and reactivity threats unique to ambulatory sensing.

## Overview

**Digital phenotyping** {cite}`onnela2016harnessing` uses smartphone sensors, wearables, and ecological momentary assessment (EMA) to measure mental health in everyday life. It promises *moment-to-moment* resolution where traditional questionnaires offer only snapshots. The cost is a thicket of new methodological and ethical problems.

## 4.1 Passive vs. Active Sensing

| | Passive | Active (EMA) |
|---|---------|----|
| User effort | None | Multiple prompts per day |
| Reactivity | Low | High |
| Construct validity | Indirect | Direct (self-report) |
| Missingness pattern | Non-random (battery, location) | Diurnal / weekly |

Best practice combines the two: passive streams to fill gaps, EMA to anchor labels.

## 4.2 Common Sensor Modalities

- **Actigraphy** — sleep / activity / circadian disruption (Sleep Regularity Index in `code/research/digital_phenotyping.py`).
- **GPS & Wi-Fi** — *location entropy*, *mobility radius*, time-at-home (Saeb et al., 2015).
- **Keystroke dynamics** — psychomotor slowing, sometimes prodromal to depressive episodes.
- **Voice** — prosody, jitter, shimmer; promising for mania and Parkinson's (Mundt et al., 2012).
- **Heart-rate variability** — autonomic regulation; vagal tone correlates with emotion regulation.
- **Screen events** — phantom checking ("burst fraction") as anxiety marker.

## 4.3 Inferring Affect and Cognition

Machine-learning models map raw sensor streams to constructs such as depression severity, anxiety, and cognitive load. The notebook in `/code/clinical/` shows a depression-detection pipeline with missing-data handling. The headline empirical result: short-horizon (1–7 day) prediction is feasible at population level, but person-specific models often do not transfer (Cohen et al., 2019).

## 4.4 Validity, Privacy, and Reactivity

```{warning}
Digital phenotyping raises acute privacy concerns. GPS traces are re-identifiable
with as few as four points (de Montjoye et al., 2013). Always pair deployment
with the [data governance policy](../../../ethics_toolkit/data_governance_policy.md)
and informed-consent procedures.
```

Validity threats specific to ambulatory data:

- **Selection bias** — early adopters of sensing apps are not representative.
- **Compliance decay** — EMA response rates drop ~10 % per week.
- **Reactivity** — being measured changes the behaviour being measured.

## Key Terms

| Term | Working definition |
|------|---------------------|
| **EMA** | Ecological Momentary Assessment — repeated self-report in situ. |
| **Location entropy** | Shannon entropy of cluster visits — depression correlate. |
| **Gyration radius** | RMS distance from one's daily centroid. |
| **Reactivity** | Change in behaviour caused by measurement. |
| **Idiographic model** | Model trained per-person, not population. |

## Worked Example: From GPS to a Depression Indicator

```python
from code.research.digital_phenotyping import (
    generate_synthetic_day, simple_depression_score
)
raw, window = generate_synthetic_day(depressed=True, seed=0)
print(window.to_dict())
print("Score:", simple_depression_score(window))
```

Compare with `depressed=False`. Which feature drives the score most? Adjust the
weights in `simple_depression_score` and discuss how this connects to feature
engineering choices in Chapter 5.

## Hands-on Exercises

1. **Sleep regularity.** Implement the SRI on two synthetic weeks and show how a single shifted bedtime moves the index.
2. **Missingness pattern.** Drop 30 % of nighttime GPS points and re-compute entropy. By how much do you over- or under-estimate?
3. **Reactivity check.** Design an EMA schedule that minimises reactivity for a 2-week study in college students. Justify your choices using §4.4.

## Case Study: The StudentLife Study

The Dartmouth StudentLife study (Wang et al., 2014) tracked 48 undergraduates with passive sensing and EMA for one term. It established the now-canonical relationship between *reduced co-presence* (proximity sensors) and increased depressive symptoms. The study's biggest contribution, however, is methodological: a publicly available, ethically pre-cleared dataset.

## Common Pitfalls

- **Confusing correlation with construct.** Low location entropy correlates with depression *and* with chronic illness, retirement, and disability.
- **Population-only validation.** A model that works in college students rarely works in older adults.
- **Re-identification.** "Anonymous" mobility traces are not anonymous; treat them as PHI.

## Connections to Other Chapters

- ML pipeline design → **Chapter 5**.
- Diagnostic deployment → **Chapter 8**.
- Privacy and surveillance → **Chapters 20, 23**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Whose data is a GPS trace — the user's, the device manufacturer's, or the platform's?
2. Would you join a 1-year phenotyping study run by your own employer? What would change your answer?
3. Design a *minimum-viable* phenotype: which sensors would you keep, and which would you discard, for a depression-relapse early-warning system?

## Further Reading

- Onnela, J.-P., & Rauch, S. L. (2016). Harnessing smartphone-based digital phenotyping. *Neuropsychopharmacology*, 41, 1691–1696.
- Mohr, D. C., Zhang, M., & Schueller, S. M. (2017). Personal sensing: Understanding mental health using ubiquitous sensors and machine learning. *Annual Review of Clinical Psychology*, 13, 23–47.
- Phillips, A. J. K., et al. (2017). Irregular sleep/wake patterns are associated with poorer academic performance. *Scientific Reports*, 7, 3216.
- Torous, J., et al. (2020). The growing field of digital psychiatry: Current evidence and the future of apps, social media, chatbots, and virtual reality. *World Psychiatry*, 19(3), 318–319.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
