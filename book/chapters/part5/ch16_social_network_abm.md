# Chapter 16: Social Network ABMs

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish ideological, affective, and false polarization.
- Simulate opinion dynamics with `code.social.polarization_abm.run_bounded_confidence`.
- Identify which platform mechanisms (recommendation, virality scaling, default settings) plausibly amplify polarization.
- Read field-experiment evidence sceptically: what does an "echo-chamber" study actually claim?

## Overview

Polarization on social media is one of the most contested topics in computational social psychology. Three claims must be kept apart: that polarization has *increased*, that *social media caused* it, and that *algorithms within social media* caused it. The evidence supports the first more clearly than the second, and the second more clearly than the third.

## 16.1 What Polarization Is (and Isn't)

- **Ideological polarization** — distributions of policy positions become more bimodal.
- **Affective polarization** — feelings toward the other party warm/cool — currently the strongest US trend (Iyengar et al., 2019).
- **False polarization** — *perceived* extremity of the out-group exceeds the actual.

Algorithmic feeds plausibly affect each differently.

## 16.2 Bounded-Confidence Models

The Hegselmann–Krause model (`code/social/polarization_abm.py`): each agent updates its opinion to the *mean of neighbours within $\varepsilon$*. Small $\varepsilon$ → polarization clusters; large $\varepsilon$ → consensus. The runnable demo in `notebooks/05_polarization_ABM.ipynb` reproduces both regimes.

## 16.3 Network Effects

Network-influence models (independent cascade, linear threshold; `code/social/network_influence.py`) show how *who is connected to whom* can dominate *what each person thinks*. Seed selection (Kempe, Kleinberg & Tardos, 2003) becomes a question with both marketing and public-health relevance.

## 16.4 Algorithmic Amplification: What the Evidence Says

The Facebook Open Project (Nyhan et al., Guess et al., 2023) provides the largest existing causal evidence. The headline finding from the 2020 US election: changing the *News Feed* away from algorithmic ranking *did* alter exposure but had small short-run effects on attitudes. This is consistent with two readings — algorithms matter less than thought, or they have already shaped the priors against which the experiments were run.

```{admonition} Try it
:class: tip
Run `notebooks/05_polarization_ABM.ipynb` for $\varepsilon \in \{0.10, 0.20, 0.35\}$.
Discuss which regime your social-media feed resembles.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Affective polarization** | Liking own party more, opposing party less. |
| **Bounded confidence** | Update only on opinions within $\varepsilon$. |
| **Filter bubble** | Algorithmically narrowed information diet. |
| **Selective exposure** | User-driven narrowing of information diet. |
| **Cascade** | Diffusion of behaviour or belief across a network. |

## Worked Example: Two Regimes from One Model

Run the ABM with $\varepsilon=0.15$ and $\varepsilon=0.30$ for 50 steps. Plot the opinion histograms. Why does a single parameter switch the system between *polarization* and *consensus*? What does that tell you about *what* matters most about platform design?

## Hands-on Exercises

1. Add a *stubborn-agent* parameter (fraction of agents who never update). What's the smallest stubborn-fraction needed to prevent consensus?
2. Replace the global mean with a network-weighted mean using `networkx`. Compare polarization on Erdős–Rényi vs. Barabási–Albert graphs.
3. Use `greedy_seed_selection` to find the *most influential* 5 agents in a small network. Discuss the misinformation-mitigation implication.

## Case Study: The Facebook Open Project

In 2023, Facebook released several large-N pre-registered experiments. The 2020 election results showed that *removing algorithmic ranking* reduced political content but had small attitudinal effects in the 3-month window. Lesson: causal estimates are smaller than headlines suggest, *and* one election cycle is a small window.

## Common Pitfalls

- Reading correlational network studies as causal claims.
- Treating "the algorithm" as monolithic; there are many.
- Ignoring the possibility that humans select platforms that suit them.

## Connections to Other Chapters

- Network-influence implementation → **Chapter 17**.
- Misinformation cascades → **Chapter 17**.
- Cultural psychology and AI → **Chapter 18**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is affective polarization a problem AI can fix, or one only institutions can?
2. Should platforms be required to publish their recommendation algorithms?
3. Design an experiment to disentangle *algorithmic* from *human-driven* polarization.

## Further Reading

- Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., & Westwood, S. J. (2019). The origins and consequences of affective polarization. *Annual Review of Political Science*, 22, 129–146.
- Hegselmann, R., & Krause, U. (2002). Opinion dynamics and bounded confidence. *JASSS*.
- Bakshy, E., Messing, S., & Adamic, L. A. (2015). Exposure to ideologically diverse news on Facebook. *Science*, 348, 1130–1132.
- Guess, A., et al. (2023). How do social media feed algorithms affect attitudes and behavior? *Science*, 381, 398–404.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
