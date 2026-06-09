# Chapter 2: Symbolic and Connectionist Approaches

## Learning Objectives

By the end of this chapter, you should be able to:

- Articulate the core representational commitments of symbolic and connectionist AI.
- Identify which psychological phenomena each paradigm models well — and which it models poorly.
- Run a side-by-side comparison using `code.foundations.symbolic_connectionist.compare`.
- Defend a position in the "great divide" debate using empirical, not stylistic, criteria.

## Overview

For four decades the philosophy of AI has been organised around a dichotomy: are minds symbol-manipulators or pattern-matchers? Modern systems are usually hybrids, but the contrast remains the cleanest lens for understanding *why* a particular psychological task is hard.

## 2.1 The Symbolic Tradition

Symbolic AI represents knowledge as discrete tokens — *concepts*, *propositions*, *production rules* — composed via formal logic. Newell and Simon's **physical-symbol-system hypothesis** {cite}`newell1976computer` claims that symbol manipulation is necessary and sufficient for general intelligent action.

Strengths:

- **Compositionality**: combine known atoms into new structures (Fodor & Pylyshyn, 1988).
- **Transparency**: every step can be inspected and audited.
- **Sample efficiency**: a well-designed rule base needs zero training examples.

Weaknesses:

- **Brittleness**: small surface changes can defeat the system.
- **Knowledge bottleneck**: somebody has to author the rules.
- **Poor handling of perceptual noise**.

## 2.2 The Connectionist Tradition

Connectionist models represent knowledge as patterns of activation distributed over many simple units. Backpropagation lets the network *learn* the representations from data {cite}`rumelhart1986learning`. The PDP volumes argued that this gracefully accounts for graded categories, prototype effects, and language acquisition.

Strengths:

- **Perceptual robustness**: noise and partial input degrade gracefully.
- **Learnability**: representations emerge from the task and the data.
- **Continuous similarity**: nearby inputs yield nearby outputs.

Weaknesses:

- **Opacity**: hidden-layer features may not map onto human-interpretable concepts.
- **Data hunger**.
- **Systematic generalisation**: classic challenge from Marcus (1998) onward.

## 2.3 Hybrid Architectures (Neuro-Symbolic AI)

Modern systems increasingly combine both paradigms:

- **Differentiable theorem provers** (e.g., NTPs, DeepProbLog) embed logic in a differentiable substrate.
- **Tool-augmented LLMs** route deterministic computation (calculators, SQL, retrieval) outside the neural net.
- **ACT-R + reinforcement learning** mixes symbolic chunks with sub-symbolic activation (revisit in Chapter 6).

For psychology, hybrid systems matter because human cognition itself is hybrid: rule-following in arithmetic and grammar, statistical induction in perception and motor control (Marcus, 2018).

## 2.4 What Each Paradigm Says About the Mind

| Question | Symbolic answer | Connectionist answer |
|----------|-----------------|----------------------|
| Origin of concepts | Innate primitives + composition | Statistical regularities in input |
| Nature of learning | Rule discovery | Weight adjustment |
| Locus of cognition | Propositional working memory | Distributed activation |
| Failure mode | Brittle, all-or-nothing | Graceful but inscrutable |

```{admonition} Try it
:class: tip
Run `compare([2, 3, 16, 33, 100, 200])` from `code.foundations.symbolic_connectionist`.
The connectionist model — trained on 0–63 — will *interpolate* gracefully but
*extrapolate* poorly to 100 and 200. Discuss: which psychological tasks expect
the kind of generalisation it fails at?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Production rule** | Condition → Action pair; the unit of symbolic computation. |
| **Distributed representation** | Concept encoded across many units, no single unit "is" the concept. |
| **Compositionality** | Meaning of the whole determined by meanings of parts and how combined. |
| **Catastrophic forgetting** | Connectionist nets overwriting old skills when learning new ones. |
| **Neuro-symbolic** | Architectures combining differentiable and symbolic components. |

## Worked Example: The Past-Tense Debate

Rumelhart & McClelland (1986) trained a connectionist model on English past tenses and reproduced the U-shaped learning curve: *went → goed → went*. Pinker & Prince (1988) replied that explicit symbolic rules ("add *-ed*") plus an exception list explain the same data with sharper predictions. Forty years on, behavioural and neural data support both: regular and irregular morphology recruit partially distinct neural systems (Ullman, 2004).

This is the prototype debate for the entire chapter: both paradigms fit the data; the empirical test must come from *predictions they make differently*.

## Hands-on Exercises

1. Implement an *exception* in the symbolic side of `symbolic_connectionist.py` (e.g., "treat 7 as a special case"). Then retrain the MLP on the same exception. Which paradigm captures it more cleanly?
2. Run the MLP on numbers `0..63` (training range) and `100..150` (extrapolation). Plot accuracy. Why does it degrade?
3. Pick a psychological phenomenon you study (e.g., insight learning, prototype categorisation, conjunction errors). Which paradigm would you reach for first, and why?

## Case Study: Vision in the Brain and in CNNs

DiCarlo et al. (2012) and Yamins & DiCarlo (2016) showed that the *internal representations* of large image-trained CNNs predict spike rates in inferotemporal cortex better than any hand-engineered model. This is a connectionist victory — but only if you grant that "predicting spike rates" counts as a theory of vision. Symbolic theorists reply that it predicts *the data*, not *the algorithm*.

## Common Pitfalls

- **Confusing implementation with theory.** Implementing a function in a CNN does not commit you to the claim that brains use the same algorithm.
- **Treating opacity as fatal.** Many *human* cognitive processes are opaque to introspection; opacity per se is not disqualifying.
- **Treating brittleness as fatal.** A brittle but transparent system can be safer than an opaque robust one in high-stakes settings (Chapter 11).

## Connections to Other Chapters

- Cognitive architectures use both paradigms — **Chapter 3**.
- Hybrid clinical decision-support — **Chapter 11**.
- Explainability of opaque models — **Chapter 22**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Defend or refute: "Compositionality is non-negotiable for any theory of language."
2. Which clinical task most demands transparency, and which most demands perceptual robustness? How does that choice select between paradigms?
3. Find a recent neuro-symbolic system (2022+). What does it gain over each pure side?

## Further Reading

- Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28, 3–71.
- Marcus, G. (2003). *The Algebraic Mind*. MIT Press.
- Yamins, D. L. K., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. *Nature Neuroscience*, 19, 356–365.
- Garcez, A., & Lamb, L. (2023). Neurosymbolic AI: The 3rd wave. *Artificial Intelligence Review*.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
