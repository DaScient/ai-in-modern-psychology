# Chapter 7: Natural Language Processing in Psychology

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish lexicon, embedding, and LLM approaches to psychological text analysis.
- Use `code.research.nlp_psychology` to extract LIWC-style features, *I-talk*, language style match, and Flesch readability.
- Identify the construct-validity threats specific to text-as-data.
- Pre-register an NLP study of clinical narratives that respects sample-size, base-rate, and validation requirements.

## Overview

Language is the most evidence-rich psychological signal we routinely produce. NLP turns transcripts, social-media posts, and clinical notes into measurements. The discipline of this chapter is to keep that turn *measurable* — to anchor every feature to a psychological construct and to validate that anchor.

## 7.1 The Three NLP Generations in Psychology

| Generation | Tool | Strength | Weakness |
|------------|------|----------|----------|
| Lexicon | LIWC, VADER, EmoLex | Transparent, audit-friendly | Misses context, sarcasm |
| Embedding | word2vec, GloVe, sBERT | Captures graded similarity | Opaque, training-data biased |
| LLM | GPT-4, Llama, Med-LLM | Zero-shot, fluent | Hallucination, opacity, cost |

Use lexicons when *transparency* is required (any audited deployment). Use embeddings when *similarity* is the construct. Use LLMs when *flexibility* is needed and outputs will be reviewed.

## 7.2 Lexicons Worth Knowing

- **LIWC** (Pennebaker) — 80+ categories, validated against affect and personality.
- **VADER** — sentiment with social-media normalising (capitals, emoji).
- **EmoLex / NRC** — fine-grained discrete emotions; multilingual.
- **MFD-2** — Moral Foundations Dictionary for political-psychology research.

The educational lexicon in `code/research/nlp_psychology.py` ships ~50 words; it is *only* a teaching artefact.

## 7.3 Replicated Findings

- **I-talk and depression.** First-person singular pronoun rate is a small but robust depression correlate (Tackman et al., 2019), replicated across samples and languages.
- **Linguistic Style Matching.** Cosine similarity of function-word vectors predicts therapeutic alliance (Niederhoffer & Pennebaker, 2002).
- **Cognitive distortions in CBT.** All-or-nothing phrasing, mental filtering, and personalisation can be reliably tagged by classifiers trained on transcripts.

## 7.4 Construct Validity in Text-as-Data

Three questions every NLP-driven study must answer:

1. **What construct?** Define what *negative affect* means before counting "sad" words.
2. **What anchor?** Validate against an independent rating (e.g., PHQ-9), not against itself.
3. **What window?** Sentence, paragraph, post, person? Choice changes everything.

```{admonition} Try it
:class: tip
Run `code.research.nlp_psychology.extract_features` on three texts of your
own choosing. Discuss whether the I-talk feature alone is enough to
distinguish them — and which feature you would add next.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Lexicon** | Hand-curated list of words tagged by category. |
| **Embedding** | Dense vector representation of words / sentences. |
| **I-talk** | First-person singular pronoun rate. |
| **LSM** | Language Style Matching across speakers. |
| **Flesch reading ease** | Readability score for self-report instruments. |

## Worked Example: Validating Depression Inferences from Tweets

A defensible pipeline:

1. Pre-register the operationalisation (e.g., "high I-talk = top decile").
2. Sample tweets with PHQ-9 self-report (e.g., De Choudhury et al., 2013).
3. Train *and* evaluate on disjoint users.
4. Report both AUC and *clinical* metrics (false-positive rate at top decile).

## Hands-on Exercises

1. Extend the educational lexicon with 20 *cognitive-distortion* phrases and measure their rate in a transcript dataset of your choice.
2. Replicate the I-talk effect on a public dataset (e.g., CLPsych shared task).
3. Compare lexicon scores to a sBERT embedding regression on the same outcome — when does each win?

## Case Study: CLPsych Shared Task

The annual Computational Linguistics + Clinical Psychology shared task has tracked the *real* progress of clinical NLP for a decade. Top systems for suicide-risk classification now combine LLM features with structured clinical metadata; *pure* text models stalled around AUC 0.7 in 2018 and have moved only modestly since.

## Common Pitfalls

- **Frequency-as-meaning.** "Death" appears in mortuary records and in goth poetry; counts mean nothing without context.
- **Sample-leak.** Twitter users post repeatedly; subject-level CV is mandatory.
- **Anchor drift.** Self-report instruments are themselves imperfect; report their reliability.

## Connections to Other Chapters

- Therapy-bot deployment → **Chapter 10**.
- Bias in language models → **Chapter 18**, **Chapter 22**.
- Crisis-line classification → **Chapter 12**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is text data "passive" if the person produced it for an audience?
2. Defend a position on LLM use for qualitative thematic analysis.
3. Which NLP feature would you trust enough to act on in a clinical setting?

## Further Reading

- Pennebaker, J. W., Boyd, R. L., Jordan, K., & Blackburn, K. (2015). The development and psychometric properties of LIWC2015.
- Tackman, A. M., et al. (2019). Depression, negative emotionality, and self-referential language. *J. Pers. Soc. Psychol.*, 116(5), 817–834.
- Coppersmith, G., et al. (2018). Natural language processing of social media as screening for suicide risk. *Biomedical Informatics Insights*.
- Boyd, R. L., & Schwartz, H. A. (2021). Natural language analysis and the psychology of verbal behavior. *Journal of Language and Social Psychology*.
