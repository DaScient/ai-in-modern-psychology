# Chapter 1: The History of AI in Psychology

```{epigraph}
"Each new tool of psychology has been imported from a neighbouring discipline —
the telescope, the chronoscope, the statistical regression, and now the
neural network."

— paraphrased from Hilgard, *Psychology in America*
```

## Learning Objectives

By the end of this chapter, you should be able to:

- Trace the four overlapping eras that connect AI and psychology: cybernetics, symbolic AI, connectionism, and deep learning.
- Place key milestone systems (ELIZA, SHRDLU, ACT-R, AlphaGo, GPT) on a timeline and identify which psychological constructs each was designed to model.
- Distinguish *AI as a metaphor for cognition* from *AI as a tool for psychological research*.
- Articulate why explainability becomes a first-class concern in the deep-learning era.

## Overview

The relationship between artificial intelligence and psychology has always been bidirectional. Psychology has handed AI its vocabulary — *attention*, *memory*, *reinforcement* — while AI has handed psychology its computational metaphors and, more recently, its measurement instruments. This chapter traces that exchange across roughly eighty years, then sets up the rest of the book as a series of concrete encounters between the two fields.

## 1.1 Origins: Cybernetics and Early AI (1940s–1960s)

The relationship between artificial intelligence and psychology begins not with modern machine learning, but with **cybernetics** — the study of regulatory systems, feedback loops, and control mechanisms. Norbert Wiener's foundational work {cite}`wiener1948cybernetics` drew direct parallels between neural systems and mechanical control systems, laying the groundwork for what would become cognitive science. The McCulloch–Pitts (1943) neuron formalised this analogy in arithmetic: any logical proposition computable by a finite automaton can also be computed by an idealised neural network.

Alan Turing's 1950 paper *Computing Machinery and Intelligence* introduced the famous **Turing Test** as a criterion for machine intelligence — a thought experiment with profound psychological implications. It reframed intelligence as behavioural, observable, and potentially computable {cite}`turing1950computing`.

```{admonition} What the Turing Test does and doesn't claim
:class: tip
Turing's proposal is often misread as a definition of intelligence. It is better
read as a *methodological move*: shift the question from "what is thinking?" —
a question without an agreed operationalisation — to "what behaviour would we
accept as evidence of thinking?". This move is the same one Skinner urged on
psychology in the 1930s. Whether you find it satisfying depends on whether you
are a functionalist about the mind.
```

## 1.2 The Cognitive Revolution and Symbolic AI (1960s–1980s)

The cognitive revolution in psychology coincided with the rise of **symbolic AI**. The **General Problem Solver** (Newell & Simon, 1957) modelled human problem-solving as search through a problem space — a theoretical framework that continues to influence both AI and cognitive psychology {cite}`newell1976computer`. Simon's *bounded rationality* and Tversky and Kahneman's *heuristics and biases* programme can both be read as critiques and refinements of the GPS paradigm.

Key developments of this era:

- **ELIZA (1966)** — first chatbot demonstrating that humans project psychological meaning onto simple pattern-matching. The "ELIZA effect" — humans attributing understanding to systems that merely echo — remains the single most relevant historical lesson for the LLM era.
- **SHRDLU (1970)** — natural-language understanding in constrained domains; demonstrated that situated language is tractable when the world is small.
- **Production-rule systems** — basis for expert systems in clinical psychology (e.g., MYCIN-style differential-diagnosis tools).
- **ACT-R (Adaptive Control of Thought–Rational)** — Anderson's integrated cognitive architecture, still the most widely used computational model of human cognition. We rebuild a fragment of it in Chapter 6.

## 1.3 The Connectionist Revolution (1980s–1990s)

The rediscovery of **backpropagation** {cite}`rumelhart1986learning` shifted AI toward distributed, sub-symbolic representations. The PDP (Parallel Distributed Processing) volumes argued that representation is *emergent*, not designed — a thesis that resonated with cognitive psychologists working on category learning, reading, and language acquisition. Elman's recurrent network for sentence processing (1990) and Rumelhart & McClelland's past-tense model (1986) became foundational case studies.

The trade-off this era exposed — interpretability vs. expressiveness — is the central tension of Chapter 2.

## 1.4 The Deep Learning Era (2010s–Present)

The success of deep neural networks on perceptual tasks {cite}`lecun2015deep` has created both tools and challenges for psychological science. Three milestones bear directly on psychology:

- **2012 — AlexNet** demonstrated that deep convolutional networks can match human accuracy on natural-image classification, sparking a wave of *neural-network-as-model-of-vision* research (e.g., DiCarlo lab; see Chapter 3).
- **2016 — AlphaGo** showed that reinforcement learning combined with self-play could reach super-human performance in a domain long thought to require intuition.
- **2022–present — Large Language Models** opened the door to fully conversational chatbots in mental health (Chapter 10), at the same time exposing serious safety and equity challenges (Part VI).

Where symbolic AI offered theories of cognition, modern deep learning offers tools whose internal workings are themselves difficult to interpret — making **explainability** (Chapters 8, 22) a first-class concern.

```{admonition} Try it
:class: tip
Run `python -m code.foundations.symbolic_connectionist` to see a one-screen
comparison between a symbolic and a connectionist solver on the same toy task.
Then ask yourself: *for which psychological constructs do you want the
symbolic guarantees, and for which is the connectionist flexibility worth the
opacity?*
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Cybernetics** | Study of regulation through feedback in animals and machines. |
| **Cognitive architecture** | Computational theory of the fixed structures and processes of cognition (e.g., ACT-R, SOAR). |
| **Production rule** | A condition-action pair forming the unit of symbolic computation. |
| **Connectionism** | Modelling cognition as patterns of activation in networks of simple processing units. |
| **Deep learning** | Connectionist models with many layers, trained end-to-end by gradient descent. |
| **ELIZA effect** | Tendency of humans to over-attribute understanding to a responsive system. |

## Worked Example: Reading a Timeline Like a Psychologist

Pick three milestones from §1.1–§1.4 and, for each, fill out:

1. **Psychological construct invoked** (e.g., problem-solving, language comprehension).
2. **Operationalisation** chosen by the system.
3. **What psychology adopted in return** (e.g., the search-space metaphor of GPS reshaped how cognitive psychologists thought about insight).

This is the core analytical move of the book.

## Hands-on Exercises

1. **Replay ELIZA.** Implement a 30-line regex-only DOCTOR script. Run it on a friend; ask them to rate how "understood" they felt on a 1–5 scale. Discuss the ELIZA effect in light of their score.
2. **Compare paradigms.** Use `code.foundations.symbolic_connectionist.compare` to predict parity for `[2, 3, 16, 33, 100, 200]`. Where does the connectionist model fail, and why?
3. **Map a 21st-century system.** Pick any 2020+ AI system used in psychology (e.g., a Woebot variant, a GPT-driven coding assistant for qualitative analysis). Place it on the timeline and justify the placement.

## Case Study: ELIZA, Woebot, and the Persistence of Projection

ELIZA (1966) used 200 lines of LISP and pattern substitution. Woebot (2018) uses an LLM-backed CBT-inspired script. Users of both have reported feeling "understood" {cite}`fitzpatrick2017woebot`. The continuity is more striking than the technical leap: humans evaluate conversational systems primarily on *responsiveness and relational warmth*, not on accuracy. This is a feature when the goal is supportive listening; it is a serious safety hazard when users mistake LLM fluency for clinical competence (see Chapter 10).

## Common Pitfalls

- **Mistaking metaphor for theory.** A neural network may *implement* a process without *modelling* it; whether a CNN is a theory of V1 depends on what predictions it makes that V1 also makes.
- **Anchoring on a single era.** Symbolic and connectionist tools are complementary; the chapter-by-chapter case studies in this book use both.
- **Treating AI history as monolithic.** AI winters were not failures of the field — they were failures of specific overclaims (e.g., machine translation by 1965). Each era is best read alongside the funding-and-promises cycle.

## Connections to Other Chapters

- Symbolic vs. connectionist representation choices → **Chapter 2**.
- Cognitive architectures → **Chapter 3**, deepened in **Chapter 6**.
- LLM-era clinical applications → **Chapters 9, 10**.
- Historical lessons for safe deployment → **Chapters 22, 24**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Which historical era's intellectual style is closest to your own area of psychology, and why?
2. Which ethical considerations from Part VI apply most directly here? Pick two and trace them backwards to the milestone where they could first have been raised.
3. What would you need to validate before deploying a system descended from the deep-learning era in a clinical setting?
4. Is the "ELIZA effect" a bug or a feature for supportive mental-health chatbots? Defend your answer.

## Further Reading

- Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433–460.
- Newell, A., & Simon, H. A. (1976). Computer science as empirical inquiry. *Communications of the ACM*, 19(3), 113–126.
- Rumelhart, D. E., McClelland, J. L., & the PDP Research Group. (1986). *Parallel Distributed Processing*. MIT Press.
- LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, 521, 436–444.
- Boden, M. A. (2006). *Mind as Machine: A History of Cognitive Science*. Oxford University Press.
- Marcus, G., & Davis, E. (2019). *Rebooting AI: Building Artificial Intelligence We Can Trust*. Pantheon.


---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
