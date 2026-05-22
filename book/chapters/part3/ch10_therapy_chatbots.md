# Chapter 10: Therapy Chatbots

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish three chatbot architectures and the risk profile of each.
- Implement a regex-based crisis detector and discuss its blind spots (`code.clinical.therapy_safety`).
- Design a hand-off protocol from chatbot to human responder.
- Audit a chatbot for sycophancy, hallucination, and inadequate response to suicidal ideation.

## Overview

Therapy chatbots are the most visible application of AI in mental health. Their architecture, deployment context, and *safety floor* determine whether they help or harm. This chapter focuses on the safety floor.

## 10.1 Architectural Patterns

- **Rule-based / decision-tree** (Woebot, ELIZA descendants) — every utterance is authored; predictable but brittle.
- **Retrieval-augmented LLM** — LLM generates over a curated knowledge base; safer than open generation.
- **Fine-tuned generative LLM** — flexible but harder to audit; failure modes are domain-specific.

Each trades off control, scalability, and risk. The current consensus is that *any* free-form generation must be wrapped in a safety classifier and a hand-off path.

## 10.2 Crisis Detection and Escalation

Robust deployments must reliably detect crisis language and escalate to human resources. See [`notebooks/04_therapy_bot_safety.ipynb`](../../../notebooks/04_therapy_bot_safety.ipynb) and `code/clinical/therapy_safety.py` for a regex-plus-severity-rules detector.

A defensible escalation pipeline:

1. **Detect** — pattern match + classifier vote.
2. **Confirm** — short non-judgmental probe ("Are you safe right now?").
3. **Resource** — region-specific helpline (988 in the US, 116 123 in the UK).
4. **Hand-off** — for self-identified imminent risk, page a human responder.
5. **Log** — audit trail for governance review.

```{warning}
The lexicon in `code/clinical/therapy_safety.py` is intentionally conservative
and small. Production systems use vetted dictionaries, classifier ensembles,
and human-in-the-loop review. The chapter examples are *educational* only.
```

## 10.3 Failure Modes

- **Sycophancy** — agreeing with self-harming framings to maintain engagement.
- **Hallucination** — inventing helplines, medications, or diagnoses.
- **Inadequate suicidal-ideation handling** — verbose CBT instead of acute escalation.
- **Cultural mis-attunement** — responses calibrated to one cultural script.
- **Privacy leakage** — message logs used for model training without consent.

Red-team for all five before deployment.

## 10.4 Regulatory Status

FDA and EU AI Act classifications continue to evolve. As of 2024, FDA treats most direct-to-consumer mental-health chatbots as *general wellness* devices — exempt from the strictest controls. The EU AI Act classifies *high-risk* AI used in mental health under stricter regimes (Chapter 21).

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Hand-off** | Transition from automated to human care. |
| **Sycophancy** | Model agreeing rather than challenging. |
| **Red-team** | Adversarial probing for failure modes. |
| **Hallucination** | Fluent but false output. |
| **Safety classifier** | Filter wrapping a generative model. |

## Worked Example: Auditing a Crisis Detector

```python
from code.clinical.therapy_safety import assess_message, build_safety_response
msgs = [
    "I had a tough day at work but I'm OK.",
    "I just want to end it all, I can't keep going.",
    "Sometimes I think about cutting myself when things get hard.",
]
for m in msgs:
    r = assess_message(m)
    print(m, "->", r.severity)
```

Now add the message *"I'm done"* — discuss whether your detector should flag it (it does not by default — semantic ambiguity).

## Hands-on Exercises

1. Extend `CRISIS_PATTERNS` with five additional patterns *and* five distractor patterns (phrases that look like crisis but are not). Quantify the trade-off.
2. Build a stratified evaluation: held-out crisis vs. non-crisis transcripts. Report TPR at 1 % FPR.
3. Design a hand-off log schema that supports later root-cause analysis without violating user privacy.

## Case Study: Crisis Text Line, 2022

In 2022 *Politico* reported that Crisis Text Line was sharing anonymised conversation data with a commercial spin-off. Public reaction was sharply negative, and the program was discontinued. Lesson: even *good* uses of crisis data create deployment risk when the consent surface is unclear.

## Common Pitfalls

- Validating only on benchmark transcripts that look like the dictionary.
- Treating ambiguity as a failure rather than as a *signal to escalate*.
- Optimising for engagement at the expense of safety.

## Connections to Other Chapters

- Therapy alliance — **Chapter 9**.
- Crisis intervention design — **Chapter 12**.
- Regulation — **Chapter 21**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Where should the false-positive vs. false-negative trade-off sit for crisis detection? Justify with a population scenario.
2. Should chatbots ever respond to acute suicidality without immediate human hand-off?
3. What information do users have a *right* to know about the model talking to them?

## Further Reading

- Miner, A. S., et al. (2016). Smartphone-based conversational agents and responses to questions about mental health. *JAMA Internal Medicine*, 176(5), 619–625.
- De Choudhury, M., et al. (2023). Risks of Generative AI in Mental Health. *npj Mental Health Research*.
- Vaidyam, A. N., et al. (2019). Chatbots and conversational agents in mental health. *Canadian Journal of Psychiatry*.
