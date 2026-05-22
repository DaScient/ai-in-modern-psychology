# Chapter 17: Network Influence

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish *Independent Cascade* and *Linear Threshold* models of network diffusion.
- Simulate both with `code.social.network_influence` and reason about the predictions each makes.
- Apply Kempe–Kleinberg–Tardos greedy seed selection to a small network.
- Connect cascade dynamics to misinformation, peer-led mental-health interventions, and consumer adoption.

## Overview

Social-psychological phenomena rarely diffuse uniformly; they spread through *networks* whose structure shapes the outcome. This chapter builds the two canonical cascade models and applies them to three psychological problems: misinformation, peer-led suicide prevention, and the spread of help-seeking behaviour.

## 17.1 Independent Cascade (IC)

Each newly activated node attempts to infect each neighbour exactly once with edge probability $p$. The simplest tractable model of viral diffusion:

```python
from code.social.network_influence import independent_cascade
import networkx as nx
g = nx.barabasi_albert_graph(200, 2, seed=0)
print(independent_cascade(g, seeds=[0], p=0.05, seed=0).reach)
```

Properties:

- **Memoryless** — once an edge fails, it cannot fire later.
- **Monotone & submodular** in the seed set — enabling provable greedy approximations.

## 17.2 Linear Threshold (LT)

Each node $v$ has a threshold $\theta_v \sim U(0,1)$. It activates when the sum of weights $w_{uv}$ over active neighbours $u$ exceeds $\theta_v$. Captures *social proof*: needing multiple peers before adopting.

The contrast with IC matters for psychology: behaviours requiring social validation (smoking, vaccine uptake) fit LT better; rumour transmission fits IC.

## 17.3 Influence Maximisation

Kempe, Kleinberg & Tardos (2003) showed that selecting $k$ seeds to maximise expected IC reach is NP-hard, but the *greedy* algorithm — repeatedly add the node with the largest marginal gain — achieves a $(1 - 1/e) \approx 63\%$ approximation. The submodularity of cascade reach makes this possible.

```python
from code.social.network_influence import greedy_seed_selection, expected_reach
seeds = greedy_seed_selection(g, k=3, p=0.05, n_runs=30, seed=0)
print("Greedy seeds:", seeds, "expected reach:", expected_reach(g, seeds, p=0.05, n_runs=100))
```

## 17.4 Applications in Psychology

- **Peer-led mental-health interventions**: the SOS suicide-prevention program in schools uses gatekeeper training that mirrors greedy seed selection in social networks.
- **Misinformation cascades**: IC models capture rumour spread; intervention design can be re-framed as *node deletion* or *threshold raising* (prebunking).
- **Help-seeking adoption**: friends-of-friends effects on therapy uptake follow LT-style social proof.

```{admonition} Try it
:class: tip
Run `notebooks/05_polarization_ABM.ipynb` after the polarization run for a
network-influence cell. Compare *random* vs. *greedy* seed reach on a 200-node
preferential-attachment graph.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Independent cascade** | Per-edge probabilistic infection. |
| **Linear threshold** | Adoption when cumulative neighbour weight ≥ threshold. |
| **Submodularity** | Diminishing returns property enabling greedy bounds. |
| **Influence maximisation** | Select $k$ seeds to maximise expected reach. |
| **Gatekeeper** | High-influence node trained to recognise risk in peers. |

## Worked Example: Misinformation Mitigation via Node Removal

Start from a barabasi-albert graph; run IC with 5 seeds. Now remove the 5 highest-degree nodes (the *centrality-removal* heuristic) and re-run. Quantify the reduction in cascade size and discuss the ethical implication of treating *people* as removable nodes.

## Hands-on Exercises

1. Compare IC and LT on the same graph with matched edge weights. Which gives larger reach when $p \approx \bar w$?
2. Add a 10 % "vaccinated" fraction (immune nodes). Plot reach vs. vaccination fraction.
3. Re-implement greedy seed selection with **lazy evaluation** (CELF, Leskovec et al., 2007). Time the speedup.

## Case Study: Mexican Trauma-Survivor Network Study

Jones et al. (2018) used IC-style modelling to predict the spread of PTSD-help-seeking through an existing social network of trauma survivors. Predicted reach matched 6-month follow-up within 8 %. Lesson: cascade models can guide *positive* network interventions, not only misinformation studies.

## Common Pitfalls

- Treating IC parameters as estimable from cross-sectional data.
- Forgetting that greedy seed selection is *not* optimal.
- Confusing degree centrality with influence.

## Connections to Other Chapters

- Misinformation interventions → **Chapter 16**.
- Cultural variation in social ties → **Chapter 18**.
- Ethics of network-targeted interventions → **Chapter 22**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is targeted peer intervention manipulation or care? Defend either side.
2. When is LT a *better* psychological theory than IC?
3. What is the role of *weak ties* (Granovetter) in either model?

## Further Reading

- Kempe, D., Kleinberg, J., & Tardos, É. (2003). Maximizing the spread of influence through a social network. *KDD*.
- Granovetter, M. (1978). Threshold models of collective behavior. *Am. J. Sociol.*
- Christakis, N. A., & Fowler, J. H. (2007). The spread of obesity in a large social network over 32 years. *NEJM*.
- Leskovec, J., et al. (2007). Cost-effective outbreak detection in networks. *KDD*.
