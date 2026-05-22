# Chapter 11: Clinical Decision Support

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish a CDS *tool* from a CDS *system*.
- Compute net benefit and decision-curve analysis using `code.clinical.decision_curve`.
- Design an alert that increases use of evidence-based care without overwhelming clinicians (alert-fatigue trade-off).
- Audit a CDS deployment for transportability and drift.

## Overview

Clinical decision support (CDS) in mental health spans from PHQ-9 cutoff alerts in primary care to ICU-style early-warning scores in inpatient psychiatry. The shift from a *model* to a *system* introduces challenges — workflow, alert fatigue, human-AI handoff — that ML papers rarely confront.

## 11.1 Anatomy of a CDS

| Layer | Question it answers |
|-------|----------------------|
| Trigger | When does the system fire? |
| Inference | What is the underlying risk? |
| Display | How is it shown to the clinician? |
| Action | What concrete option does the clinician have? |
| Logging | What is audited later? |

A CDS failure is almost always a *Display* or *Action* failure, not an *Inference* one.

## 11.2 Net Benefit and Threshold Reasoning

A model's threshold is a *value judgement*: what is the relative cost of a false negative vs. a false positive? Decision-curve analysis (Vickers & Elkin, 2006; `code/clinical/decision_curve.py`) plots net benefit across thresholds and reveals the *range* in which the model beats "treat all" and "treat none". Outside that range, the model is *not* useful.

## 11.3 Alert Fatigue

When alerts fire too often, clinicians ignore them — including the important ones. Two design moves help:

1. **Calibrate thresholds to the clinical pathway**, not to ROC convenience.
2. **Pair every alert with a concrete actionable option** ("Order PHQ-9", "Schedule follow-up").

Empirical baseline: alert systems with > 15 % "override without rationale" rate are widely judged failures.

## 11.4 Transportability and Drift

Models trained on one population, in one EHR, with one documentation style, rarely transport without recalibration:

- **Calibration drift** — risk distributions shift; predicted probabilities lose meaning.
- **Feature drift** — coding practices change (ICD-10 cutover, COVID coding chaos).
- **Outcome drift** — what counts as the target event changes.

Mitigation: continuous calibration monitoring, scheduled recalibration, and pre-defined retirement criteria.

```{admonition} Try it
:class: tip
Take the SHAP notebook's trained model and apply it to a *resampled* synthetic
dataset with halved base rate. Compute net benefit on both. Where does the
clinically useful threshold range move?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Alert fatigue** | Decline in clinician response with overuse. |
| **Recalibration** | Adjusting predicted probabilities to a new population. |
| **Transportability** | Performance preservation across sites. |
| **Override** | Clinician dismissing an alert. |
| **Time-to-event** | Horizon over which the prediction is valid. |

## Worked Example: DCA on the Synthetic Risk Model

Run:

```python
from code.clinical.risk_prediction import generate_synthetic_ehr
from code.clinical.decision_curve import decision_curve, informative_range
import numpy as np

df = generate_synthetic_ehr(5000, seed=0)
# Score each row with the same log-odds equation used by the generator:
import math
log_odds = (-4.5 + 0.05*df.age + 1.2*df.prior_self_harm + 0.4*df.ed_visits
            + 1.5*df.nighttime_ed + 1.3*df.antidepressant_discontinued
            + 0.8*df.sleep_disorder + 0.6*df.location_entropy_high)
prob = 1/(1+np.exp(-log_odds))
curve = decision_curve(df.attempt, prob)
print("Informative threshold range:", informative_range(curve))
```

## Hands-on Exercises

1. Build a synthetic *site-shift* experiment: train on one prevalence, test on another. Plot calibration before / after Platt scaling.
2. Design a one-screen alert UI mock-up for a primary-care PHQ-9 escalation.
3. Write a retirement protocol: what triggers would force you to take a deployed model offline?

## Case Study: Sepsis CDS Generalisation

Although outside psychiatry, the Epic Sepsis Model (Wong et al., 2021) is the canonical cautionary tale: deployed widely, externally validated poorly. The same pattern can repeat in mental-health CDS without active calibration.

## Common Pitfalls

- Choosing thresholds by ROC optimum rather than clinical cost.
- Underestimating the cost of false positives in resource-poor settings.
- Treating drift monitoring as optional.

## Connections to Other Chapters

- ML methodology → **Chapter 5**.
- Diagnostic deployment → **Chapter 8**.
- Crisis-line CDS → **Chapter 12**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Who is responsible when a clinician follows a CDS alert that turns out to be wrong?
2. Should patients know which CDS tools are influencing their care?
3. How would you measure "clinical adoption" without optimising for it?

## Further Reading

- Vickers, A. J., & Elkin, E. B. (2006). Decision-curve analysis. *Med Decis Making*, 26, 565–574.
- Wong, A., et al. (2021). External validation of a widely implemented proprietary sepsis prediction model. *JAMA Internal Medicine*.
- Sittig, D. F., & Singh, H. (2010). A new socio-technical model for studying health information technology. *Quality and Safety in Health Care*.
