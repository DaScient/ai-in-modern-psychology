"""NLP for psychology — Chapter 7.

A compact, dependency-light toolkit for the most common text-analysis
tasks in clinical and social psychology research:

* **Lexicon scoring** — a small LIWC-style affect lexicon plus a
  utility to fit *any* category × word matrix to a corpus.
* **Pronoun usage** — first-person singular pronoun rate (a robust
  depression signal across multiple replications).
* **Linguistic style accommodation** — cosine similarity of function-
  word vectors across two speakers (a marker of therapeutic alliance).
* **Readability** — Flesch reading-ease score for self-report
  instruments.

The lexicon used here is intentionally tiny. It exists so students
understand how lexicons *work*; real research should use validated
resources (LIWC-22, VADER, EmoLex) with appropriate licensing.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Sequence

# ---------------------------------------------------------------------------
# Tiny illustrative lexicon (NOT a substitute for LIWC).
# ---------------------------------------------------------------------------

EDUCATIONAL_LEXICON: Dict[str, List[str]] = {
    "positive_affect": [
        "happy", "joy", "love", "great", "wonderful", "excellent",
        "good", "glad", "kind", "thankful", "grateful",
    ],
    "negative_affect": [
        "sad", "angry", "hate", "terrible", "bad", "awful",
        "hopeless", "worthless", "depressed", "anxious", "afraid",
    ],
    "first_person_sing": ["i", "me", "my", "mine", "myself"],
    "first_person_plural": ["we", "us", "our", "ours", "ourselves"],
    "cognitive_process": [
        "because", "think", "know", "consider", "reason",
        "cause", "should", "ought", "maybe", "perhaps",
    ],
    "function_words": [
        "the", "a", "an", "and", "or", "but", "in", "on", "at",
        "to", "of", "for", "with", "is", "are", "was", "were",
    ],
}


_WORD_RE = re.compile(r"[A-Za-z']+")


def tokenize(text: str) -> List[str]:
    """Lowercase word tokenizer suitable for lexicon scoring."""
    return [m.group(0).lower() for m in _WORD_RE.finditer(text)]


def lexicon_score(text: str, lexicon: Mapping[str, Sequence[str]] | None = None) -> Dict[str, float]:
    """Return the per-category rate of lexicon hits per total tokens.

    Args:
        text: Input string.
        lexicon: Mapping category -> word list. Defaults to
            :data:`EDUCATIONAL_LEXICON`.

    Returns:
        Dict ``{category: rate}`` where ``rate`` is in [0, 1].
    """
    if lexicon is None:
        lexicon = EDUCATIONAL_LEXICON
    tokens = tokenize(text)
    if not tokens:
        return {cat: 0.0 for cat in lexicon}
    counts = Counter(tokens)
    n = len(tokens)
    return {
        cat: float(sum(counts.get(w, 0) for w in words)) / n
        for cat, words in lexicon.items()
    }


def first_person_singular_rate(text: str) -> float:
    """Rate of first-person singular pronouns ("I-talk") per token.

    Elevated I-talk is one of the most consistently replicated linguistic
    markers of depression (Tackman et al., 2019, *J. Pers. Soc. Psychol.*).
    """
    return lexicon_score(text)["first_person_sing"]


# ---------------------------------------------------------------------------
# Linguistic style accommodation (LSA)
# ---------------------------------------------------------------------------


def _function_word_vector(text: str) -> Dict[str, float]:
    tokens = tokenize(text)
    if not tokens:
        return {w: 0.0 for w in EDUCATIONAL_LEXICON["function_words"]}
    counts = Counter(tokens)
    n = len(tokens)
    return {w: counts.get(w, 0) / n for w in EDUCATIONAL_LEXICON["function_words"]}


def _cosine(a: Mapping[str, float], b: Mapping[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return float(dot / (na * nb)) if na and nb else 0.0


def language_style_match(text_a: str, text_b: str) -> float:
    """Cosine similarity of function-word vectors between two speakers.

    Closer to ``1.0`` indicates higher linguistic accommodation, which
    correlates with therapeutic alliance (Niederhoffer & Pennebaker,
    2002, *J. Lang. Soc. Psychol.*).
    """
    return _cosine(_function_word_vector(text_a), _function_word_vector(text_b))


# ---------------------------------------------------------------------------
# Readability
# ---------------------------------------------------------------------------


def _syllable_count(word: str) -> int:
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev = False
    for ch in word:
        is_v = ch in vowels
        if is_v and not prev:
            count += 1
        prev = is_v
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


def flesch_reading_ease(text: str) -> float:
    """Flesch reading-ease score for self-report instruments.

    Returns roughly:

    * 90–100 — Very easy (5th grade)
    * 60–70 — Plain English (8th/9th grade)
    * 0–30 — Very difficult (college graduate)

    Useful when adapting clinical instruments for low-literacy populations.
    """
    sentences = max(len(re.findall(r"[.!?]+", text)), 1)
    words = tokenize(text)
    if not words:
        return 0.0
    syllables = sum(_syllable_count(w) for w in words)
    return float(206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words)))


# ---------------------------------------------------------------------------
# Convenience aggregator
# ---------------------------------------------------------------------------


@dataclass
class TextFeatures:
    """All educational text-analysis features for a single document."""

    n_tokens: int
    positive_affect: float
    negative_affect: float
    first_person_sing: float
    cognitive_process: float
    flesch: float

    def to_dict(self) -> Dict[str, float]:
        return {
            "n_tokens": self.n_tokens,
            "positive_affect": self.positive_affect,
            "negative_affect": self.negative_affect,
            "first_person_sing": self.first_person_sing,
            "cognitive_process": self.cognitive_process,
            "flesch": self.flesch,
        }


def extract_features(text: str) -> TextFeatures:
    """Run every text-analysis function in this module on ``text``."""
    scores = lexicon_score(text)
    return TextFeatures(
        n_tokens=len(tokenize(text)),
        positive_affect=scores["positive_affect"],
        negative_affect=scores["negative_affect"],
        first_person_sing=scores["first_person_sing"],
        cognitive_process=scores["cognitive_process"],
        flesch=flesch_reading_ease(text),
    )


def corpus_summary(texts: Iterable[str]) -> Dict[str, float]:
    """Average each feature across an iterable of documents."""
    rows = [extract_features(t).to_dict() for t in texts]
    if not rows:
        return {}
    keys = rows[0].keys()
    return {k: float(sum(r[k] for r in rows) / len(rows)) for k in keys}


if __name__ == "__main__":  # pragma: no cover
    samples = {
        "Depressive narrative": (
            "I just feel so hopeless. I can't think clearly anymore. I keep "
            "telling myself I'm worthless. I don't know what I'm doing."
        ),
        "Reflective narrative": (
            "We had a difficult week, but we tried to consider what we could "
            "learn. The team felt grateful for the support and chose to think "
            "carefully about next steps."
        ),
    }
    for label, text in samples.items():
        print(f"--- {label} ---")
        print(extract_features(text).to_dict())
        print()
    print("LSM(A, B):", language_style_match(*samples.values()))
