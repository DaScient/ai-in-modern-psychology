# Chapter 6: Memory Models

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Memory Models*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Computational models of memory — from ACT-R base-level activation to modern spreading-activation networks.

## 6.1 Base-Level Activation and the Power Law of Forgetting

$$ A_i = \ln\left(\sum_j t_j^{-d}\right) + \beta_i + \varepsilon $$

The ACT-R base-level learning equation captures the well-attested power-law forgetting curve {cite}`anderson2004integrated`.

## 6.2 Spreading Activation and Semantic Networks

Activation spreads along weighted associative links, modelling priming effects and free recall.

## 6.3 Working Memory and Capacity Limits

Buffer-based architectures (ACT-R, EPIC) instantiate Baddeley's working-memory model with capacity and decay constraints.

## 6.4 Hands-on: simulate forgetting curves

See [`notebooks/01_ACT_R_memory_simulation.ipynb`](../../../notebooks/01_ACT_R_memory_simulation.ipynb) for a runnable simulation of chunk decay.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of memory models are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060.
