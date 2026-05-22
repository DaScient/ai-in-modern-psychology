"""Network-influence models — Chapter 17.

Two canonical diffusion models on a contact network:

* **Independent Cascade (IC)** — each newly activated node tries to
  infect each neighbour once with edge-specific probability.
* **Linear Threshold (LT)** — each node activates when the cumulative
  influence of active neighbours exceeds an individual threshold.

These models underlie much of computational social-influence research,
from misinformation cascades to peer-led mental-health interventions
(Kelly et al., 2015, *Soc. Sci. Med.*).

Designed to depend on ``networkx`` only — no heavyweight optional deps.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

import numpy as np

try:  # pragma: no cover - import guarded for environments without networkx
    import networkx as nx
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "code.social.network_influence requires `networkx` — install it via "
        "`pip install networkx`."
    ) from exc


@dataclass
class CascadeRun:
    """Result of a single cascade simulation."""

    seeds: List[int]
    activated: Set[int] = field(default_factory=set)
    history: List[Set[int]] = field(default_factory=list)

    @property
    def reach(self) -> int:
        return len(self.activated)


def independent_cascade(
    graph: "nx.Graph",
    seeds: Sequence[int],
    p: float = 0.05,
    max_steps: int = 50,
    seed: Optional[int] = None,
) -> CascadeRun:
    """Simulate one Independent-Cascade run.

    Args:
        graph: A ``networkx`` graph (directed or undirected).
        seeds: Initially active node ids.
        p: Per-edge propagation probability (uniform).
        max_steps: Hard cap on diffusion rounds.
        seed: RNG seed for reproducibility.
    """
    rng = np.random.default_rng(seed)
    activated: Set[int] = set(seeds)
    frontier: Set[int] = set(seeds)
    history: List[Set[int]] = [set(activated)]

    for _ in range(max_steps):
        new_frontier: Set[int] = set()
        for u in frontier:
            for v in graph.neighbors(u):
                if v in activated:
                    continue
                if rng.random() < p:
                    new_frontier.add(v)
        if not new_frontier:
            break
        activated |= new_frontier
        history.append(set(activated))
        frontier = new_frontier

    return CascadeRun(seeds=list(seeds), activated=activated, history=history)


def linear_threshold(
    graph: "nx.Graph",
    seeds: Sequence[int],
    thresholds: Optional[Dict[int, float]] = None,
    weights: Optional[Dict[Tuple[int, int], float]] = None,
    max_steps: int = 50,
    seed: Optional[int] = None,
) -> CascadeRun:
    """Simulate one Linear-Threshold run.

    Args:
        graph: A ``networkx`` graph.
        seeds: Initially active node ids.
        thresholds: Optional per-node thresholds; sampled from U(0,1) if None.
        weights: Optional per-edge weights; defaults to ``1/deg(v)`` (the
            standard normalisation).
        max_steps: Hard cap on diffusion rounds.
        seed: RNG seed for reproducibility.
    """
    rng = np.random.default_rng(seed)
    nodes = list(graph.nodes)
    if thresholds is None:
        thresholds = {n: float(rng.random()) for n in nodes}
    if weights is None:
        weights = {}
        for v in nodes:
            deg = max(graph.degree(v), 1)
            for u in graph.neighbors(v):
                weights[(u, v)] = 1.0 / deg

    activated: Set[int] = set(seeds)
    history: List[Set[int]] = [set(activated)]

    for _ in range(max_steps):
        new_active: Set[int] = set()
        for v in nodes:
            if v in activated:
                continue
            influence = sum(weights.get((u, v), 0.0) for u in graph.neighbors(v) if u in activated)
            if influence >= thresholds[v]:
                new_active.add(v)
        if not new_active:
            break
        activated |= new_active
        history.append(set(activated))

    return CascadeRun(seeds=list(seeds), activated=activated, history=history)


def expected_reach(
    graph: "nx.Graph",
    seeds: Sequence[int],
    p: float = 0.05,
    n_runs: int = 100,
    seed: Optional[int] = None,
) -> float:
    """Monte-Carlo estimate of expected IC reach for a seed set."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_runs):
        run = independent_cascade(graph, seeds, p=p, seed=int(rng.integers(0, 2**31 - 1)))
        out.append(run.reach)
    return float(np.mean(out))


def greedy_seed_selection(
    graph: "nx.Graph",
    k: int,
    p: float = 0.05,
    n_runs: int = 50,
    seed: Optional[int] = None,
) -> List[int]:
    """Greedy influence-maximisation (Kempe, Kleinberg, Tardos, 2003).

    At each step add the node whose addition maximises Monte-Carlo
    expected reach. The (1 − 1/e) approximation guarantee holds because
    IC reach is monotone and submodular under random edge realisations.
    """
    selected: List[int] = []
    candidates = list(graph.nodes)
    rng = np.random.default_rng(seed)
    for _ in range(k):
        best_node, best_gain = None, -1.0
        for n in candidates:
            if n in selected:
                continue
            gain = expected_reach(
                graph, selected + [n], p=p, n_runs=n_runs, seed=int(rng.integers(0, 2**31 - 1))
            )
            if gain > best_gain:
                best_gain = gain
                best_node = n
        if best_node is None:
            break
        selected.append(best_node)
    return selected


if __name__ == "__main__":  # pragma: no cover
    g = nx.barabasi_albert_graph(50, 2, seed=0)
    seeds = greedy_seed_selection(g, k=3, p=0.1, n_runs=30, seed=0)
    print("Greedy seeds:", seeds)
    print("Expected reach:", round(expected_reach(g, seeds, p=0.1, n_runs=100, seed=0), 2))
