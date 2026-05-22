# Chapter 3: Cognitive Architectures

## Learning Objectives

By the end of this chapter, you should be able to:

- Define a cognitive architecture and distinguish it from a domain model.
- Compare ACT-R, SOAR, EPIC, and CLARION on representation, learning, and biological plausibility.
- Identify which architectural commitment matches a given empirical phenomenon.
- Read and modify the ACT-R fragment in `code/foundations/act_r_simulation.py`.

## Overview

A **cognitive architecture** specifies the fixed structures and mechanisms of cognition — the parts that *do not change* across tasks — and lets you populate them with task-specific knowledge. Done well, an architecture is a *unified theory of cognition* in Newell's (1990) sense: a single substrate that, in principle, explains perception, memory, decision-making, and motor control with one set of mechanisms.

## 3.1 Why Architectures?

Modular psychological models proliferate (one for memory, one for reading, one for choice). Architectures discipline the field: any new domain model must be *implementable* in the architecture, which both falsifies models that quietly assume unlimited working memory and reveals empirical predictions that single-domain models hide.

## 3.2 ACT-R (Anderson)

- **Declarative memory** holds chunks; activation follows the base-level learning equation $A_i = \ln \sum_j t_j^{-d} + \epsilon$ (Chapter 6).
- **Procedural memory** holds production rules; firing is gated by utility values learned by reinforcement.
- **Buffers** (goal, retrieval, visual, manual) are the only loci through which modules communicate — a strong claim about working memory.
- **Empirical reach**: skill acquisition, list memory, multitasking, fMRI prediction.

See `code/foundations/act_r_simulation.py` for a minimal implementation of the declarative-memory subsystem.

## 3.3 SOAR (Laird, Newell, Rosenbloom)

SOAR commits to **chunking** — a *single* learning mechanism that compiles all problem-solving experience into new production rules. The trade-off vs. ACT-R is sharper learning theory at the cost of less direct mapping to behavioural latencies.

## 3.4 EPIC (Meyer & Kieras)

EPIC takes perception and motor control seriously by modelling them as parallel processes with realistic time constants. It is the architecture of choice for multitasking and human factors (Chapter 15).

## 3.5 CLARION (Sun)

CLARION integrates explicit (symbolic) and implicit (connectionist) knowledge in parallel, paralleling the dual-process literature in social and cognitive psychology.

## 3.6 Choosing an Architecture

| Phenomenon you care about | Architecture that handles it most natively |
|---------------------------|---------------------------------------------|
| Skill acquisition curves | ACT-R |
| Chunking and problem-space search | SOAR |
| Dual-task interference, motor timing | EPIC |
| Implicit vs. explicit learning | CLARION |
| Neural plausibility | LEABRA / Spaun |

```{admonition} Try it
:class: tip
The fragment in `act_r_simulation.py` is < 200 lines. Add a *goal* buffer
that pushes chunks back into declarative memory at retrieval, and you have
modelled rehearsal. Plot the resulting forgetting curve.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Architecture** | Fixed structure + mechanisms shared across all tasks. |
| **Chunk** | Atom of declarative memory in ACT-R. |
| **Buffer** | A slot through which a module communicates with others. |
| **Production utility** | Reinforcement-learned value attached to a rule. |
| **Unified theory of cognition** | Newell's (1990) target for an architecture. |

## Worked Example: Predicting List-Memory Errors

Anderson's classic demonstration: feed an ACT-R model a serial-position list; predict the U-shape of recall accuracy. Without changing any free parameters, the base-level learning equation predicts both primacy (more rehearsal) and recency (recent retrievals). Try reproducing this with the in-repo simulator.

## Hands-on Exercises

1. Extend `ACTRMemory.add_chunk` to accept a *partial match* tolerance and demonstrate stimulus generalisation.
2. Implement utility-based production selection. Show how reward shifts behaviour over 100 trials.
3. Compare ACT-R's predictions to a simple exponential forgetting model. Why does ACT-R win?

## Case Study: Architectures in Human-Centred Design

NASA, the FAA, and Volvo have all used ACT-R/PM and EPIC to predict pilot and driver error before fielding new interfaces. The lesson for psychology: an architecture that fits a single experiment may not fit *task switching with realistic timing constants* — yet that is precisely where safety hinges.

## Common Pitfalls

- **Fitting a single experiment with infinite knobs.** Architectures must be evaluated across multiple tasks with one parameter set.
- **Confusing the architecture with the task model.** A bad task model in ACT-R is not evidence against ACT-R.
- **Ignoring scale.** A 6-rule production system is not a model of cognition; it is an example.

## Connections to Other Chapters

- ACT-R memory equation → **Chapter 6**.
- Architectures vs. deep nets as models of brain → **Chapter 2**.
- Workload and burnout modelling → **Chapter 15**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is the choice of architecture an empirical question, an aesthetic one, or a tooling decision?
2. Which architecture most plausibly scales to *social* cognition, and which to *perceptual* cognition?
3. How would you falsify ACT-R? Be specific about what data would force you to reject it.

## Further Reading

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060.
- Newell, A. (1990). *Unified Theories of Cognition*. Harvard University Press.
- Sun, R. (2016). *Anatomy of the Mind: Exploring Psychological Mechanisms and Processes with the Clarion Cognitive Architecture*. Oxford University Press.
- Laird, J. (2012). *The Soar Cognitive Architecture*. MIT Press.
