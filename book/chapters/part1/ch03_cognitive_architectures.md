# Chapter 3: Cognitive Architectures

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Cognitive Architectures*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Survey major cognitive architectures — ACT-R, SOAR, global workspace theory, predictive processing — as unified theories of mind.

## 3.1 What Is a Cognitive Architecture?

A cognitive architecture is a fixed set of mechanisms that, together, account for a wide range of cognitive phenomena. It specifies *what stays constant* across tasks (memory systems, perception, motor control) and what is learned or programmed.

## 3.2 ACT-R: Adaptive Control of Thought – Rational

ACT-R {cite}`anderson2004integrated` partitions cognition into modules (declarative memory, procedural memory, perceptual–motor) coordinated by a central production system. The base-level activation equation governs which memories are retrievable at any given time — see [Chapter 6](../part2/ch06_memory_models) and the [ACT-R notebook](../../../notebooks/01_ACT_R_memory_simulation.ipynb).

## 3.3 SOAR and Universal Subgoaling

SOAR treats all goal-directed behaviour as problem-space search, with universal subgoaling when impasses are reached. Its emphasis on chunking offers a mechanism for skill acquisition.

## 3.4 Global Workspace and Predictive Processing

Global Workspace Theory models consciousness as a broadcast over specialised modules. Predictive processing recasts perception as hierarchical Bayesian inference. Both have implications for clinical disorders (e.g., schizophrenia as aberrant precision-weighting).

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of cognitive architectures are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060.
- Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press.
