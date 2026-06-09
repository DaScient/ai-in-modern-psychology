# Chapter 9: AI in Psychotherapy

## Learning Objectives

By the end of this chapter, you should be able to:

- Identify the four roles AI now plays in psychotherapy: triage, augmentation, assistance, and replacement.
- Read the evidence on common factors and alliance as they apply to AI-mediated care.
- Apply common-factors theory to evaluate any new AI-therapy claim.
- Articulate what would have to be true for replacement to be ethically defensible.

## Overview

For most therapy outcomes, technique explains a minority of variance; the *therapeutic alliance* and *common factors* (warmth, hope, structure) explain more (Wampold, 2015). This places AI in psychotherapy in an awkward position: the easy parts to automate (technique, exercises) explain less than the hard parts to automate (alliance, attunement).

## 9.1 Four Roles for AI

| Role | Example | Risk profile |
|------|---------|--------------|
| **Triage** | Screen messages for crisis (Ch 10) | Low if non-coercive |
| **Augmentation** | Suggest CBT homework, log mood, prompt between sessions | Low |
| **Assistance to therapist** | Real-time alliance feedback, transcript coding | Medium — clinician oversight required |
| **Replacement** | Standalone "AI therapist" | High — not yet defensible for severe presentations |

## 9.2 Evidence Base

- **Apps and digital CBT.** Meta-analyses show small-to-moderate effects vs. waitlist, smaller vs. active controls (Andersson, 2018).
- **Chatbots.** RCTs of Woebot, Wysa, and Tess show effects on anxiety and depression in non-severe samples; effects fade after engagement drops (Inkster et al., 2018).
- **Therapist-augmenting tools.** Lyssn-style alliance feedback has been shown to improve fidelity to CBT and MI techniques (Imel et al., 2017).

## 9.3 Common Factors and AI

Wampold's contextual model:

1. Real relationship
2. Expectations and credibility
3. Specific ingredients of the treatment

AI can replicate (3) and partially (2) but only weakly (1). The empirical question is whether (3) without (1) is enough for most clients — likely "no" for severe presentations, "maybe" for sub-clinical distress.

## 9.4 Population and Setting

- **Adolescents** report lower stigma with chatbots; effect on engagement is documented.
- **Low-resource settings** are the strongest argument for AI-mediated care: a flawed chatbot may beat no care.
- **Severe presentations** (suicidality, psychosis, substance use): every available study urges caution.

```{admonition} Try it
:class: tip
Pair `notebooks/04_therapy_bot_safety.ipynb` (crisis detection) with the
chapter's common-factors discussion. Which factor is the bot *replacing*,
and which is it *bypassing*?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Therapeutic alliance** | Collaborative bond between client and clinician. |
| **Common factors** | Cross-modality elements that predict outcome. |
| **Allegiance effect** | Researchers' favoured therapy tends to win their trials. |
| **Dose–response** | Effect size as function of engagement / sessions. |
| **Stepped care** | Pathway from low- to high-intensity intervention. |

## Worked Example: Reading a Chatbot RCT

Take a published Woebot trial. Identify: comparison condition, completion rate, effect on PHQ-9, effect on engagement, and *what counts as adherence*. Compute the dose–response curve. Discuss why a "small-but-positive" effect can be either substantively important or substantively trivial depending on cost and access.

## Hands-on Exercises

1. Design a stepped-care protocol that uses an AI chatbot at step 1 and a human therapist at step 3. Specify the escalation criteria.
2. Write a *failure-mode log* for an AI therapy tool: list five plausible failure cases and the mitigation for each.
3. Critique an existing app's privacy policy from a psychotherapy-research perspective.

## Case Study: Replika and Parasocial Risk

Replika's user base reported strong attachment, and the 2023 changes to the romantic features triggered a documented spike in distress posts. Lesson: emotional attachment to AI products is *itself* a clinical signal, and platform changes can be experienced as relational ruptures.

## Common Pitfalls

- Equating engagement metrics with clinical benefit.
- Ignoring the comparator (waitlist ≠ active treatment).
- Designing safety as an after-thought rather than a constraint.

## Connections to Other Chapters

- Crisis detection mechanics → **Chapter 10**.
- Regulatory status → **Chapter 21**.
- Privacy in conversational data → **Chapter 20**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Are AI therapists best framed as *therapy* or as *self-help with conversation*?
2. Under what conditions, if any, would standalone AI therapy be ethically defensible for adolescents?
3. Should outcome metrics for AI therapy differ from those for human therapy?

## Further Reading

- Wampold, B. E., & Imel, Z. E. (2015). *The Great Psychotherapy Debate*. Routledge.
- Inkster, B., Sarda, S., & Subramanian, V. (2018). An empathy-driven, conversational AI agent. *JMIR mHealth & uHealth*.
- Fitzpatrick, K. K., Darcy, A., & Vierhile, M. (2017). Woebot: A randomized controlled trial. *JMIR Mental Health*.
- Torous, J., & Blease, C. (2024). Generative AI in mental health care: Risks and roles. *World Psychiatry*.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
