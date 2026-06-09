# Chapter 12: Crisis Intervention

## Learning Objectives

By the end of this chapter, you should be able to:

- Describe the standard crisis-line workflow and where AI can plug in.
- Use `code.clinical.therapy_safety` to triage volunteer-routed messages.
- Reason about the trade-off between recall and counsellor burden.
- Apply a *minimum-viable-evidence* standard for deploying AI in crisis contexts.

## Overview

Crisis-line services (988 in the US, Samaritans in the UK, Crisis Text Line internationally) sit at the safety net of mental-health care. AI tools have been deployed here for nearly a decade — for queue prioritisation, real-time counsellor support, and quality assurance.

## 12.1 Triage and Routing

The clearest win for AI is **risk-based triage**: prioritising the queue so the highest-acuity messages reach a counsellor first. Crisis Text Line piloted this at scale (Pisani et al., 2019) and reported reduced time-to-response for high-acuity messages.

Design principles:

1. **Recall-favouring threshold** — false positives are cheap, false negatives potentially fatal.
2. **No silent triage** — counsellors should see *that* a triage decision was made and why.
3. **Conservative coverage** — never *deprioritise* a message because the model is uncertain.

## 12.2 Real-Time Counsellor Support

LLM-based assistants can suggest validating phrases, surface clinical resources, and flag risk indicators (Sharma et al., 2023). The evidence base is small but encouraging: counsellor-rated quality improves modestly with the assistant on. Risks include over-reliance and de-skilling.

## 12.3 Quality Assurance and Training

Transcript-level NLP can:

- Identify counsellor adherence to motivational-interviewing techniques.
- Detect cultural mis-attunement.
- Power supervisor caseload review.

Each use is *organisational*; deploying NLP on transcripts requires explicit consent and a clearly defined retention window.

## 12.4 A Minimum-Viable-Evidence Standard

For crisis settings, this book proposes a minimum-viable evidence (MVE) bar:

1. Prospective, multi-site validation.
2. Calibration *and* net-benefit reporting.
3. Documented harm-reporting pathway.
4. Equity audit across at least two protected attributes.
5. Pre-defined retirement criteria.

```{warning}
The detector in `code/clinical/therapy_safety.py` does **not** meet the MVE
bar. It is illustrative — never deploy it.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Acuity** | Severity / urgency of the presenting concern. |
| **Queue triage** | Reordering of pending interactions by predicted acuity. |
| **De-skilling** | Counsellor capability decline due to automation reliance. |
| **Equity audit** | Stratified performance check across protected attributes. |

## Worked Example: From Detector to Queue Order

Given 20 incoming texts, score with `assess_message`, sort by severity, and route. Document what the counsellor sees (the message + a yellow/red banner) and what they do not see (raw model probabilities). Discuss why the latter design choice may *increase* counsellor calibration.

## Hands-on Exercises

1. Construct an adversarial test set: messages a clinician would flag but the regex would miss (e.g., "I have a plan for Saturday"). Quantify recall.
2. Implement a two-stage triage: regex + sBERT classifier. Compare false-positive rates.
3. Write a retrospective harm-analysis template suitable for monthly review meetings.

## Case Study: 988 Lifeline Launch

The July 2022 transition to a three-digit US suicide & crisis lifeline (988) increased call volume by > 50 %. AI-assisted triage has been one ingredient of the system's capacity expansion. Public evaluations are pending; community trust is fragile.

## Common Pitfalls

- Optimising for high precision at the cost of recall in a crisis setting.
- Deploying QA NLP without counsellor and supervisor consent.
- Lacking a documented escalation path when the model disagrees with the counsellor.

## Connections to Other Chapters

- Safety detector implementation → **Chapter 10**.
- Diagnostic risk modelling → **Chapter 8**.
- Equity audits → **Chapter 13**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is a 10 % miss rate acceptable if the alternative is a 30-minute wait?
2. Whose data is a crisis-line transcript?
3. Could AI ever *replace* a counsellor for low-acuity contacts? Defend either side.

## Further Reading

- Pisani, A. R., Kanuri, N., Filbin, B., Gallo, C., Gould, M., Lehmann, L. S., et al. (2019). Protecting user privacy and rights in academic data-sharing partnerships. *JMIR Mental Health*.
- Sharma, A., et al. (2023). Human–AI collaboration enables more empathic conversations in text-based peer-to-peer mental health support. *Nature Machine Intelligence*.
- Gould, M. S., et al. (2022). Helpful and harmful experiences with telephone crisis services. *Suicide and Life-Threatening Behavior*.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
