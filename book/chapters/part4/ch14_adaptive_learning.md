# Chapter 14: Adaptive Learning

## Learning Objectives

By the end of this chapter, you should be able to:

- Derive the Bayesian Knowledge Tracing (BKT) update from prior, slip, guess, and transit.
- Implement a one-skill BKT loop with `code.io_ed.adaptive_learning`.
- Compare BKT, IRT, and Deep Knowledge Tracing (DKT) on identifiability and interpretability.
- Design a *zone-of-proximal-development* item selector and discuss its limits.

## Overview

Adaptive learning systems adjust difficulty and feedback to each learner. Their two long-standing model families — knowledge tracing (KT) and item-response theory (IRT) — meet psychology's two long-standing concerns: *what the learner knows* and *what each item measures*.

## 14.1 Bayesian Knowledge Tracing

BKT models each skill as a single latent variable $L$ (mastered / not) with four parameters:

- $P_{\text{init}}$ — prior on mastery before the first item.
- $P_{\text{transit}}$ — probability of moving from un-mastered to mastered after an attempt.
- $P_{\text{slip}}$ — $P(\text{wrong} \mid \text{mastered})$.
- $P_{\text{guess}}$ — $P(\text{correct} \mid \text{not mastered})$.

The update is implemented in `bkt_update()` and the curve in `simulate_trajectory()`. Beck & Chang (2007) showed BKT is *unidentifiable* when $P_{\text{slip}} + P_{\text{guess}} \geq 1$; the helper enforces this constraint.

## 14.2 Item-Response Theory

IRT models each item's difficulty (and optionally discrimination and guess parameters). The 2PL model:

$$P(\text{correct} \mid \theta, b, a) = \frac{1}{1 + e^{-a(\theta - b)}}$$

Used for: test design (SAT, GRE), measurement invariance, and adaptive testing (CAT).

## 14.3 Deep Knowledge Tracing

Piech et al. (2015) replaced the BKT latent with a recurrent neural network over the entire item history. DKT improves predictive accuracy on benchmarks but its outputs are harder to interpret. Recent hybrid work re-imposes constraints (knowledge structure, monotonicity) to recover interpretability.

## 14.4 The Zone of Proximal Development

Vygotsky's ZPD suggests choosing items that the learner can solve *with help* but not alone. Operationalised in adaptive learning as targeting $P(\text{correct}) \approx 0.75$; see `recommend_next_difficulty` in `adaptive_learning.py`.

```{admonition} Try it
:class: tip
```python
from code.io_ed.adaptive_learning import (
    BKTParams, simulate_trajectory, recommend_next_difficulty
)
params = BKTParams()
curve = simulate_trajectory([True]*5 + [False] + [True]*4, params)
print(curve)
print("Next difficulty:", recommend_next_difficulty(curve[-1]))
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Mastery** | Latent binary variable in BKT. |
| **Slip / guess** | Noise parameters that decouple performance from mastery. |
| **CAT** | Computerised adaptive testing. |
| **DKT** | RNN-based knowledge tracing. |
| **ZPD** | Zone of proximal development. |

## Worked Example: Identifiability

Pick $P_{\text{slip}}=0.4, P_{\text{guess}}=0.4$ and confirm BKT raises an error in our implementation. Discuss why two different parameter sets can produce identical likelihoods.

## Hands-on Exercises

1. Fit BKT to a small synthetic learner with 50 attempts. How accurately do you recover the parameters?
2. Implement KT-IDEM (item-difficulty effect model) by extending `bkt_update` to take an item-difficulty argument.
3. Use the *next-difficulty* recommender for a 30-item learning session; compare retention to a uniform-difficulty session.

## Case Study: Carnegie Learning's Cognitive Tutor

The Cognitive Tutor (Anderson et al., 1995) — based on ACT-R — has been deployed in tens of thousands of US classrooms. A US Department of Education-funded RCT (Pane et al., 2014) showed positive effects in the second year of use. The lesson: adaptive systems require time to fit teachers' workflows.

## Common Pitfalls

- Treating $P_{\text{transit}}$ as fixed across items.
- Equating "high mastery probability" with "ready for next skill".
- Optimising for engagement instead of learning.

## Connections to Other Chapters

- Cognitive architectures (ACT-R basis of Cognitive Tutor) → **Chapter 3**.
- Memory models → **Chapter 6**.
- Fairness across learner subgroups → **Chapter 13**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Does BKT's interpretability still matter if DKT predicts better?
2. Should adaptive learning systems share students' mastery estimates with the students themselves?
3. What is the failure mode of recommending items that the student answers correctly 75 % of the time?

## Further Reading

- Corbett, A. T., & Anderson, J. R. (1995). Knowledge tracing. *User Modeling and User-Adapted Interaction*, 4, 253–278.
- Piech, C., et al. (2015). Deep knowledge tracing. *NeurIPS*.
- Beck, J. E., & Chang, K.-min (2007). Identifiability: A fundamental problem of student modeling. *UMAP*.
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*.
