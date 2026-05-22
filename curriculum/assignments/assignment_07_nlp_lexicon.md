# Assignment 07 — NLP Lexicon Validation

> Companion to **Chapter 7**.

## Learning Objectives

- Construct and validate a small psychological lexicon.
- Distinguish lexicon-based, embedding-based, and LLM-based NLP.
- Report a defensible construct-validity audit.

## Deliverables

1. A new lexicon file (`.json` or `.csv`) of ≥ 60 entries across ≥ 4 categories.
2. A notebook applying the lexicon to a public dataset.
3. A construct-validity audit (1-page).

## Tasks

1. **Build a lexicon.** Pick *one* of: cognitive distortions, moral foundations (replication of MFD-2 subset), gratitude language, anxiety somatic descriptors. Document the source of each word.
2. **Apply it.** Use `code.research.nlp_psychology.lexicon_score` on a public mental-health text dataset of your choice (CLPsych, Reddit r/depression archive subset, or a synthetic generator you write).
3. **Construct validity.** Report:
   - Convergent validity vs. one external measure.
   - Test–retest reliability across two halves of your dataset.
   - One adversarial case where the lexicon fails.
4. **Comparison.** Compare your lexicon score to a sBERT cosine-similarity baseline. Discuss when each wins.

## Rubric

| Criterion | Excellent | Adequate | Insufficient |
|-----------|-----------|----------|--------------|
| Lexicon design | Categories well separated | Reasonable | Ad hoc |
| Convergent validity | Quantified, discussed | Reported | Missing |
| Adversarial case | Insightful | Listed | Trivial |
| Comparison | Both methods run, discussed | One method | None |

## Suggested timing: 8 hours.
