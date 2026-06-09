# Chapter 6: Memory Models

## Learning Objectives

By the end of this chapter, you should be able to:

- Derive the ACT-R base-level activation equation from first principles.
- Simulate the power-law forgetting curve using `code.foundations.act_r_simulation`.
- Compare ACT-R, exponential decay, SAM, and the temporal context model on their empirical commitments.
- Apply memory-model predictions to a real classroom or clinical scheduling problem.

## Overview

Memory is the original test bed for computational psychology. From Ebbinghaus (1885) onward, the field has insisted that *forgetting follows a law*. What law, and what mechanism, is the central question.

## 6.1 The ACT-R Base-Level Equation

For chunk $i$ retrieved at times $t_{j}$, current time $t$, decay $d$:

$$A_i = \ln \left( \sum_{j} (t - t_j)^{-d} \right) + \beta_i + \epsilon$$

- The log of a sum of $t^{-d}$ terms is the *natural* generalisation of a single power-law decay to multiple retrievals.
- $d \approx 0.5$ across most published fits — a strong cross-task constraint.
- $\epsilon$ is logistic noise with scale $s \pi / \sqrt{3}$.

The exact equation is implemented in `code/foundations/act_r_simulation.py` as `simulate_forgetting_curve`.

## 6.2 Why a Power Law, Not an Exponential?

Empirical retention curves are well fit by power-law decay across decades of experiments (Wixted & Ebbesen, 1991). ACT-R derives the power law as the *aggregate* of many exponentials with different rate constants — the *log-normal distribution of difficulty* assumption. This is one of the few places in psychology where a parameter's value is genuinely cross-task constrained.

## 6.3 Other Memory Models

| Model | Core mechanism | Best at |
|-------|----------------|---------|
| **SAM** (Raaijmakers & Shiffrin) | Context-cue associations | Free recall |
| **TCM** (Howard & Kahana) | Drifting context vector | Serial position effects |
| **REM** (Shiffrin & Steyvers) | Bayesian likelihood | Recognition memory |
| **MINERVA-2** | Trace activation by similarity | Categorisation |

ACT-R subsumes much of SAM and TCM as parameter choices.

## 6.4 Spaced Repetition and Education

The 17-th-century insight that distributed practice beats massed practice is recovered cleanly in any retention-based model: spreading retrievals over wider $t_j$ flattens the activation curve. Modern adaptive flashcard systems (Anki, SuperMemo) implement essentially this prediction.

```{admonition} Try it
:class: tip
Run `notebooks/01_ACT_R_memory_simulation.ipynb`. Modify the retrieval
schedule to be massed (all in the first hour) or spaced (one per day for a
week). Plot the activation at $t = 30$ days. Which schedule yields higher
expected retention?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Base-level activation** | Sum of decayed prior retrievals, in log space. |
| **Retrieval threshold** | Minimum activation needed to recover a chunk. |
| **Spacing effect** | Distributed practice outperforms massed practice. |
| **Power law of forgetting** | Retention falls as $t^{-d}$, not $e^{-kt}$. |
| **Reconsolidation** | Re-storage of a retrieved memory; opens an editing window. |

## Worked Example: Optimal Review Schedule

Treat review scheduling as an optimisation: given a study budget of $n$ reviews and a target retention level $\rho$ at deadline $T$, choose the schedule $\{t_1, \dots, t_n\}$ that maximises $A_i(T)$. The textbook answer — exponentially expanding intervals — is the Pimsleur / Leitner schedule. Derive it from the activation equation.

## Hands-on Exercises

1. Fit $d$ to a published Ebbinghaus dataset (e.g., Murre & Dros, 2015). How close to 0.5 do you get?
2. Add a *retrieval-induced strengthening* term and re-simulate.
3. Connect ACT-R memory to BKT (Chapter 14): treat mastery as a threshold-crossing probability and discuss what each model gets right.

## Case Study: Memory Models in PTSD Treatment

Reconsolidation-based treatments for PTSD (Brunet et al., 2008) explicitly exploit the reactivation window in memory models. Computational simulations have been used to predict optimal timing for propranolol administration after trauma-cue exposure — a striking case of memory theory shaping clinical protocol.

## Common Pitfalls

- Treating the noise term as nuisance rather than as a *prediction* about retrieval latency variability.
- Fitting per-subject $d$ values that explain everything and predict nothing.
- Ignoring encoding strength variability (the $\beta_i$ term).

## Connections to Other Chapters

- Cognitive architectures → **Chapter 3**.
- Adaptive learning scheduling → **Chapter 14**.
- Memory bias in trauma → **Chapter 12**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Why does the field keep rediscovering the power law of forgetting?
2. Should educational software *optimise* retention or *human-readable* schedules?
3. What is the strongest argument that ACT-R is wrong about memory? Defend it.

## Further Reading

- Anderson, J. R. (1990). *The Adaptive Character of Thought*. Erlbaum.
- Wixted, J. T. (2004). The psychology and neuroscience of forgetting. *Annual Review of Psychology*, 55, 235–269.
- Murre, J. M. J., & Dros, J. (2015). Replication and analysis of Ebbinghaus' forgetting curve. *PLoS ONE*, 10(7), e0120644.
- Pavlik, P. I., & Anderson, J. R. (2005). Practice and forgetting effects on vocabulary memory. *Cognitive Science*, 29(4), 559–586.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
