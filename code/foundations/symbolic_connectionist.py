"""Symbolic vs. connectionist comparison — Chapter 2.

This module pairs two minimal classifiers that solve the *same* toy task
("is this number even?") so that students can compare:

* A **symbolic** production-rule system that performs explicit lookup
  in a hand-authored rule base.
* A **connectionist** feed-forward network that learns the same mapping
  from data.

The point is *not* to claim one paradigm is better — the chapter argues
that both have complementary strengths. The point is to expose every
moving piece so that learners can run the comparison themselves::

    python -m code.foundations.symbolic_connectionist

The neural model is intentionally tiny so it trains in seconds on a CPU
with only ``numpy`` — no PyTorch / TensorFlow required.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Sequence, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Symbolic side: a tiny production-rule system.
# ---------------------------------------------------------------------------


@dataclass
class Rule:
    """A single production rule.

    The ``condition`` is a predicate on the input; the ``action`` returns
    a class label. The ``priority`` field lets us implement conflict
    resolution by *specificity*, the canonical strategy in production
    systems such as OPS5 and ACT-R.
    """

    name: str
    condition: Callable[[int], bool]
    action: Callable[[int], int]
    priority: int = 0


@dataclass
class ProductionSystem:
    """A minimal forward-chaining production-rule classifier."""

    rules: List[Rule] = field(default_factory=list)
    trace: List[str] = field(default_factory=list)

    def add_rule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def classify(self, x: int) -> int:
        """Return the label produced by the highest-priority firing rule."""
        firing = [r for r in self.rules if r.condition(x)]
        if not firing:
            self.trace.append(f"no rule fired for x={x}")
            return -1
        winner = max(firing, key=lambda r: r.priority)
        self.trace.append(f"x={x} fired '{winner.name}'")
        return winner.action(x)


def build_even_odd_classifier() -> ProductionSystem:
    """Build a 2-rule production system that classifies numbers as even/odd."""
    ps = ProductionSystem()
    ps.add_rule(Rule("is_even", condition=lambda x: x % 2 == 0, action=lambda x: 0, priority=1))
    ps.add_rule(Rule("is_odd", condition=lambda x: x % 2 == 1, action=lambda x: 1, priority=1))
    return ps


# ---------------------------------------------------------------------------
# Connectionist side: a tiny MLP trained with numpy SGD.
# ---------------------------------------------------------------------------


def _to_bits(x: int, n_bits: int = 8) -> np.ndarray:
    """Encode a non-negative integer as a fixed-length bit vector."""
    if x < 0 or x >= 2**n_bits:
        raise ValueError(f"x={x} out of range for {n_bits}-bit encoding")
    return np.array([(x >> i) & 1 for i in range(n_bits)], dtype=float)


@dataclass
class MLPClassifier:
    """Tiny single-hidden-layer MLP trained with cross-entropy."""

    n_bits: int = 8
    n_hidden: int = 16
    lr: float = 0.1
    seed: int = 0

    def __post_init__(self) -> None:
        rng = np.random.default_rng(self.seed)
        # Xavier init
        self.W1 = rng.normal(0, 1.0 / np.sqrt(self.n_bits), (self.n_bits, self.n_hidden))
        self.b1 = np.zeros(self.n_hidden)
        self.W2 = rng.normal(0, 1.0 / np.sqrt(self.n_hidden), (self.n_hidden, 2))
        self.b2 = np.zeros(2)

    @staticmethod
    def _softmax(z: np.ndarray) -> np.ndarray:
        z = z - z.max(axis=-1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=-1, keepdims=True)

    def _forward(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        h = np.tanh(X @ self.W1 + self.b1)
        p = self._softmax(h @ self.W2 + self.b2)
        return h, p

    def fit(self, xs: Sequence[int], ys: Sequence[int], epochs: int = 200) -> List[float]:
        X = np.array([_to_bits(x, self.n_bits) for x in xs])
        Y = np.eye(2)[np.array(ys, dtype=int)]
        losses: List[float] = []
        for _ in range(epochs):
            h, p = self._forward(X)
            loss = float(-np.mean(np.sum(Y * np.log(p + 1e-12), axis=1)))
            losses.append(loss)
            # Backprop
            dz2 = (p - Y) / len(X)
            dW2 = h.T @ dz2
            db2 = dz2.sum(axis=0)
            dh = dz2 @ self.W2.T
            dz1 = dh * (1 - h**2)
            dW1 = X.T @ dz1
            db1 = dz1.sum(axis=0)
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1
            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2
        return losses

    def predict(self, x: int) -> int:
        X = _to_bits(x, self.n_bits)[None, :]
        _, p = self._forward(X)
        return int(np.argmax(p, axis=-1)[0])


# ---------------------------------------------------------------------------
# Side-by-side comparison helper.
# ---------------------------------------------------------------------------


def compare(xs: Sequence[int]) -> Dict[str, List[int]]:
    """Run both classifiers on ``xs`` and return their predictions.

    The symbolic system needs *zero* training examples — its rules encode
    the task by construction. The connectionist model must induce the
    parity rule from examples and will get most numbers right after
    a few hundred SGD steps, but it cannot generalise beyond its bit
    width.
    """
    ps = build_even_odd_classifier()
    sym_preds = [ps.classify(int(x)) for x in xs]

    mlp = MLPClassifier(seed=0)
    training = list(range(0, 64))
    labels = [v % 2 for v in training]
    mlp.fit(training, labels, epochs=300)
    nn_preds = [mlp.predict(int(x)) for x in xs]
    return {"symbolic": sym_preds, "connectionist": nn_preds}


def hello() -> str:
    """Backwards-compatible greeting used by older notebooks."""
    return (
        "Symbolic vs. connectionist demo — see compare() and Chapter 2 of "
        "AI in Modern Psychology."
    )


if __name__ == "__main__":  # pragma: no cover - illustrative
    xs = [0, 1, 2, 7, 16, 33, 100, 127]
    preds = compare(xs)
    print(f"{'x':>5} | symbolic | connectionist")
    for x, s, n in zip(xs, preds["symbolic"], preds["connectionist"]):
        print(f"{x:>5} | {s:>8} | {n:>13}")
