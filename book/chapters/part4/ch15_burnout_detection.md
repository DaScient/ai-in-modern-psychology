# Chapter 15: Burnout Detection

## Learning Objectives

By the end of this chapter, you should be able to:

- Map the workplace-sensing landscape onto specific psychological constructs (burnout, engagement, workload).
- Articulate the surveillance trade-offs each construct measurement introduces.
- Design a wellbeing dashboard that respects worker agency and minimises chilling effects.
- Evaluate AI-driven workload prediction tools against established I/O frameworks (JD-R, Effort-Reward Imbalance).

## Overview

The same passive-sensing methods that power digital phenotyping (Chapter 4) have entered the workplace as *wellbeing tools*: keystroke analytics, meeting-load dashboards, sentiment monitors. Whether these tools serve workers or surveil them depends almost entirely on *who controls the data*.

## 15.1 The Workplace Sensing Landscape

- **Keystroke and mouse dynamics** — proxy for engagement and cognitive load.
- **Calendar and email metadata** — meeting load, after-hours communication ("always on").
- **Email-tone sentiment** — affect at work.
- **Wearable biosignals** — HRV, sleep, recovery.
- **Survey integration** — daily-diary or pulse surveys (EMA in the workplace).

Each modality reproduces all the digital-phenotyping methodological hazards *plus* the power asymmetry between employer and worker.

## 15.2 Constructs Worth Measuring

The two most reliable predictors of burnout in I/O psychology (Maslach & Leiter, 2016) are *workload* and *control*. AI can measure the first; it cannot, by itself, restore the second.

- **Burnout** (MBI subscales): exhaustion, cynicism, reduced efficacy.
- **Engagement** (UWES): vigour, dedication, absorption.
- **Recovery** (Sonnentag's framework): psychological detachment, relaxation, mastery, control.
- **Job demands–resources (JD-R)** balance.

## 15.3 Worker-Centric Design Principles

A wellbeing tool is *worker-centric* if and only if:

1. Workers control the granularity of disclosure to managers.
2. Aggregate dashboards never identify individuals.
3. Opt-out is genuinely costless (no career penalty).
4. Workers can audit what is collected and inferred.
5. The vendor's business model does not depend on selling that data.

Any single failure shifts the tool from wellbeing to surveillance.

## 15.4 Chilling Effects

When workers know they are being monitored, they change their behaviour — and the *measurement* changes the *thing measured*. This is not a bug to engineer around; it is a fundamental property of measurement in social systems.

```{admonition} Try it
:class: tip
Re-purpose `code/research/digital_phenotyping.py` for a *workplace* phenotype:
replace location entropy with calendar-cluster entropy, mobility radius with
inter-meeting interval. What does the depressive-phenotype proxy look like
for a knowledge worker after a "no-meeting Tuesday"?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **JD-R** | Job Demands–Resources model of strain and motivation. |
| **Recovery** | Post-work psychological replenishment. |
| **Chilling effect** | Behaviour change induced by surveillance. |
| **Pulse survey** | Short, frequent self-report. |
| **Quantified self** | Voluntary self-tracking. |

## Worked Example: A Worker-Owned Wellbeing Dashboard

Design a dashboard that shows the *worker* their meeting load, after-hours email, and recovery proxy, *but* shares with the manager only an opt-in, aggregated, week-level rollup. Argue why each design decision satisfies one of §15.3.

## Hands-on Exercises

1. Survey three commercial workplace-wellbeing products against the §15.3 checklist. Which (if any) pass?
2. Build a synthetic dataset of two teams with identical workload but different control; show how the JD-R framework predicts different burnout trajectories.
3. Write the data-collection consent script you would want shown to you.

## Case Study: Microsoft Productivity Score and Reversal

In 2020 Microsoft launched *Productivity Score* with per-employee analytics; after public backlash, the company removed the individual identifiers within a week. Lesson: even technically successful tools can fail the social-licence test.

## Common Pitfalls

- Treating engagement metrics as goals.
- Confusing aggregate insight with individual diagnosis.
- Ignoring that the most fragile workers are also the most monitored.

## Connections to Other Chapters

- Sensing methodology → **Chapter 4**.
- Fairness audits in IO contexts → **Chapter 13**.
- Surveillance and privacy → **Chapter 20**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Where is the line between a wellbeing tool and a surveillance tool?
2. Should employers ever be allowed to use HRV data?
3. How would you design a wellbeing tool that *increases* worker control?

## Further Reading

- Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience. *World Psychiatry*, 15(2), 103–111.
- Demerouti, E., et al. (2001). The Job Demands–Resources model of burnout. *J. Appl. Psychol.*
- Ajunwa, I., Crawford, K., & Schultz, J. (2017). Limitless worker surveillance. *California Law Review*.
- Bernstein, E. S. (2017). Making transparency transparent. *Academy of Management Annals*.
