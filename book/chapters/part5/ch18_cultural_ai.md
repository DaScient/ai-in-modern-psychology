# Chapter 18: Cultural AI

## Learning Objectives

By the end of this chapter, you should be able to:

- Describe the WEIRD-sample problem and how it propagates into ML.
- Diagnose at least three concrete mechanisms by which AI models encode the cultural assumptions of their training data.
- Apply Henrich's tight–loose, individualist–collectivist, and analytic–holistic distinctions when auditing an AI deployment.
- Propose a feasible *cultural validity* protocol for a new AI mental-health product.

## Overview

Most psychology is WEIRD — Western, Educated, Industrialised, Rich, Democratic (Henrich, Heine & Norenzayan, 2010). Most AI training data is *also* WEIRD, plus heavily English-language and US-coastal. This double layering of bias is the central concern of this chapter.

## 18.1 The WEIRD Problem in Two Layers

- **Sample layer**: psychology's empirical findings come from a small slice of humanity.
- **Tool layer**: the AI tools we apply to those findings carry their own cultural fingerprint.

A culturally insensitive AI tool tested on a culturally biased dataset can *appear* to validate findings that hold nowhere except in the training distribution.

## 18.2 Where Culture Enters AI

- **Tokenisation** — non-Latin scripts and morphologically rich languages are systematically under-supported.
- **Pre-training corpora** — Common Crawl is heavily English and US.
- **Annotator demographics** — emotion and toxicity labels reflect annotator culture.
- **Benchmarks** — most NLP benchmarks were authored by US graduate students.
- **Deployment defaults** — chatbots default to direct, individualistic communication styles.

## 18.3 Concrete Cross-Cultural Findings That AI Often Misses

- **Self-construal** — independent vs. interdependent (Markus & Kitayama, 1991).
- **Tight vs. loose cultures** (Gelfand, 2018).
- **Holistic vs. analytic cognition** (Nisbett, 2003).
- **Display rules** for emotion (Ekman; Matsumoto).
- **Stigma profiles** in mental health (especially around family disclosure).

## 18.4 Cultural Validity Protocols

For any mental-health AI product:

1. **Inclusion list** — which cultural contexts are *in* the validation set?
2. **Exclusion list** — which contexts are explicitly out of scope, and how is that communicated?
3. **Local linguistic adaptation** — beyond translation: idiom, register, taboo.
4. **Local clinical adaptation** — referrals, helplines, stigma considerations.
5. **Local feedback loop** — channel for users to flag mis-attunement.

```{admonition} Try it
:class: tip
Score the same paragraph in English and a back-translated version with
`code.research.nlp_psychology.lexicon_score`. Compare the I-talk rate.
Is the difference *linguistic* or *cultural*?
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **WEIRD** | Western, Educated, Industrialised, Rich, Democratic. |
| **Tight / loose** | Strength of social norms and tolerance of deviance. |
| **Self-construal** | Independent vs. interdependent view of self. |
| **Display rule** | Cultural prescription about emotion expression. |

## Worked Example: Adapting a Crisis Hotline

Suppose `code.clinical.therapy_safety` is to be deployed in Japan. List the changes needed in: lexicon, severity rules, resource URLs, hand-off scripts, and consent text. Discuss why translation alone is insufficient.

## Hands-on Exercises

1. Audit the educational lexicon in `nlp_psychology.py` for culturally specific terms; replace at least five.
2. Read a recent paper on cross-cultural emotion recognition and identify two assumptions about display rules.
3. Build a "cultural validity card" for any of the in-repo code modules.

## Case Study: Mental Health Apps in Sub-Saharan Africa

Studies on chatbot apps in low- and middle-income countries (Wahbeh et al., 2020) show that *engagement is high but completion rates are low*, with cited reasons including data costs, language mismatch, and family-stigma concerns. The intervention design that works in San Francisco may have to be re-architected, not just translated.

## Common Pitfalls

- Treating language as a proxy for culture.
- Treating translation as adaptation.
- Confusing demographic with cultural diversity.

## Connections to Other Chapters

- Fairness audits → **Chapter 13**, **Chapter 22**.
- NLP construct validity → **Chapter 7**.
- Therapy-bot design → **Chapter 10**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Whose responsibility is cultural adaptation — model developers, vendors, deployers, or users?
2. When is "default to English-language norms" defensible?
3. Could AI itself help debias AI training data? Discuss feasibility and risks.

## Further Reading

- Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33, 61–135.
- Bender, E. M., et al. (2021). On the dangers of stochastic parrots. *FAccT*.
- Sambasivan, N., et al. (2021). Re-imagining algorithmic fairness in India and beyond. *FAccT*.
- Gelfand, M. (2018). *Rule Makers, Rule Breakers*. Scribner.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
