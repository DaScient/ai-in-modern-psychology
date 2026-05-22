# Chapter 2: Symbolic vs. Connectionist AI

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Symbolic vs. Connectionist AI*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Compare rule-based, symbolic systems with sub-symbolic neural-network approaches and the modern hybrid synthesis.

## 2.1 Symbolic AI: Rules, Logic, and Knowledge

Symbolic AI represents knowledge using discrete, human-readable symbols and manipulates them via formal rules. Production-rule systems, semantic networks, and frames have all shaped cognitive theories such as ACT-R and SOAR.

Strengths: interpretability, compositional reasoning, ease of injecting prior knowledge.
Weaknesses: brittleness, knowledge-engineering bottleneck, poor handling of noise.

## 2.2 Connectionism: Neural Networks and Distributed Representations

Connectionist models encode knowledge in the weights of many simple interconnected units. Distributed representations enable graceful degradation, similarity-based generalization, and learning from data {cite}`rumelhart1986learning`.

## 2.3 Hybrid and Neuro-symbolic Approaches

Modern systems increasingly combine the two: neural perception feeds symbolic planners; differentiable programming embeds logic in gradient descent; large language models exhibit emergent reasoning that blurs the line.

## 2.4 Implications for Psychological Theory

The symbolic-vs-connectionist debate maps onto the dual-process distinction (System 1 / System 2) and the question of whether human cognition is fundamentally rule-based, statistical, or both.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of symbolic vs. connectionist ai are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Marcus, G. (2020). The next decade in AI: four steps toward robust artificial intelligence.
- Smolensky, P. (1988). On the proper treatment of connectionism. *Behavioral and Brain Sciences*, 11(1), 1–23.
