# Chapter 19: Recommender Systems

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish content-based, collaborative-filtering, and reinforcement-learning recommenders.
- Identify the psychological constructs (engagement, well-being, autonomy) that recommender objectives encode.
- Audit a recommender for filter-bubble effects, exposure bias, and adolescent-mental-health risk.
- Propose a *value-aligned* objective function that protects autonomy without sacrificing usefulness.

## Overview

Recommender systems are the single largest deployed AI surface in users' daily lives — from YouTube and TikTok to Spotify and the App Store. Their objectives are typically *engagement* (clicks, watch-time), which is a poor proxy for the psychological constructs they actually influence.

## 19.1 Three Architectures

| Architecture | Signal | Strength | Weakness |
|--------------|--------|----------|----------|
| **Content-based** | Item features | No cold-start for new items | Limited serendipity |
| **Collaborative filtering** | User × item interactions | Captures latent taste | Cold-start, popularity bias |
| **Reinforcement learning** | Sequential reward | Optimises long-term engagement | Hard to audit, encourages addictive loops |

Modern systems (YouTube, TikTok) combine all three.

## 19.2 Objectives Implicitly Encode Psychology

- **Click prediction** treats curiosity as success.
- **Watch-time** treats absorption as success.
- **Return frequency** treats habit as success.

Each is a *proxy* for what users would, on reflection, endorse. The mismatch between revealed and reflective preferences (Sunstein, 2014) is the central ethical problem of the chapter.

## 19.3 Adolescent Mental Health and Recommenders

Internal Facebook/Instagram research (leaked, 2021) showed that algorithmic recommendation amplified body-image content among teen users in a way that worsened well-being for ≥ 13 % of users surveyed. The pattern is now widely replicated. Recommenders are not neutral pipes.

Specific evidence:

- Twenge & Haidt (2022) — correlational, contested.
- Allcott et al. (2020) field experiment — Facebook deactivation improves subjective well-being modestly.
- Algorithmic-feed off vs. on experiments (Guess et al., 2023) — modest short-term effects, large long-term unknowns.

## 19.4 Designing Value-Aligned Recommenders

Practical levers (Stray, 2020; Helberger et al., 2018):

1. **Long-horizon objectives** — predict user-rated well-being after a week, not the next click.
2. **Plural objectives** — diversity, autonomy, accuracy alongside engagement.
3. **User-tunable knobs** — let users dial down a category they regret consuming.
4. **Exposure caps** — daily watch-time, sensitive-topic cool-downs.
5. **Auditable defaults** — public documentation of the objective function.

```{admonition} Try it
:class: tip
Adapt `code.social.network_influence` to model *recommended content* as a
network where edges are user-to-item probabilities. Treat *engagement* and
*regret* as two competing objectives. Which seed-selection policy
maximises engagement minus regret?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Collaborative filtering** | Recommend based on similar users' interactions. |
| **Filter bubble** | Algorithmically narrowed information diet. |
| **Exposure bias** | Skewed training data caused by recommender's own choices. |
| **Reflective preferences** | What users endorse on reflection vs. impulse. |

## Worked Example: Auditing a Recommender's Objective

Take a published objective from a recent recommender paper. Map it onto the psychological constructs it implicitly assumes. Identify two failure modes and the data needed to detect them.

## Hands-on Exercises

1. Implement a popularity-bias mitigation by *inverse-propensity weighting* on a small MovieLens-style dataset.
2. Build a simple "regret-aware" recommender: a small ML model predicts whether the user will hide / mute the content within 24 h. Subtract the regret prediction from the click prediction.
3. Critique TikTok's reported algorithm description from a *contextual integrity* standpoint (Chapter 20).

## Case Study: YouTube Kids and Algorithmic Rabbit Holes

Multiple investigations (Wired, 2017; Tufekci, 2018) documented YouTube's recommender amplifying extreme content for child viewers. The platform responded with curated-only modes and category-based filters. Lesson: defaults matter more than user controls because most users never change defaults.

## Common Pitfalls

- Treating engagement as a value.
- Auditing recommendations as if they were independent of each other.
- Ignoring the difference between *what users click* and *what users want to have clicked*.

## Connections to Other Chapters

- Misinformation amplification → **Chapters 16, 17**.
- Adolescent well-being → **Chapter 4**.
- Regulatory obligations → **Chapter 21**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Should recommender objectives be publicly disclosed?
2. Is "engagement" ever an ethical objective?
3. Design a recommender for a mental-health-app's content library that maximises *recovery progress* rather than time-in-app.

## Further Reading

- Stray, J. (2020). Aligning AI optimization to community well-being. *International Journal of Community Well-Being*.
- Sunstein, C. R. (2014). *Choosing Not to Choose*. Oxford University Press.
- Milli, S., et al. (2023). Engagement, user satisfaction, and the amplification of divisive content on social media. *PNAS*.
- Helberger, N., Karppinen, K., & D'Acunto, L. (2018). Exposure diversity as a design principle for recommender systems.
