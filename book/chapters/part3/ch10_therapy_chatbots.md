# Chapter 10: Therapy Chatbots

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Therapy Chatbots*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Architecture, safety escalation, and limitations of conversational mental-health agents.

## 10.1 Architectural Patterns

- Rule-based / decision-tree (Woebot)
- Retrieval-augmented LLM
- Fine-tuned generative LLM

Each trades off control, scalability, and risk.

## 10.2 Crisis Detection and Escalation

Robust deployments must reliably detect crisis language and escalate to human resources. See [`notebooks/04_therapy_bot_safety.ipynb`](../../../notebooks/04_therapy_bot_safety.ipynb) for a worked example.

## 10.3 Failure Modes

Sycophancy, hallucination, and inadequate handling of suicidal ideation are documented failure modes that demand monitoring and red-teaming.

## 10.4 Regulatory Status

FDA and EU AI Act classifications continue to evolve. See Chapter 21.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of therapy chatbots are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Inkster, B., Sarda, S., & Subramanian, V. (2018). An empathy-driven, conversational AI agent for digital mental wellbeing.
