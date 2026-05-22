"""
ACT-R Style Memory Simulation.

Based on: *AI in Modern Psychology*, Chapter 6.

Implements simplified ACT-R base-level activation::

    A_i = ln(sum_j t_j^{-d}) + beta_i + epsilon

Where ``t_j`` is the time since the j-th retrieval, ``d`` is the decay
parameter, ``beta_i`` is base-level learning, and ``epsilon`` is logistic noise.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np


@dataclass
class MemoryChunk:
    """Represents a single memory chunk in ACT-R declarative memory."""

    name: str
    content: dict
    creation_time: float
    retrieval_times: List[float] = field(default_factory=list)
    base_level: float = 0.0


class ACTRMemory:
    """Simplified ACT-R declarative-memory module with base-level learning.

    Reference: Anderson et al. (2004). An integrated theory of the mind.
    *Psychological Review*, 111(4), 1036–1060.
    """

    def __init__(self, decay: float = 0.5, noise: float = 0.25, threshold: float = -2.0):
        """Initialize ACT-R memory.

        Args:
            decay: Decay parameter ``d`` (default 0.5, as in ACT-R 6.0).
            noise: Activation noise ``s`` (default 0.25).
            threshold: Retrieval threshold ``tau`` (default -2.0).
        """
        self.decay = decay
        self.noise = noise
        self.threshold = threshold
        self.chunks: dict = {}
        self.current_time: float = 0.0

    def add_chunk(self, name: str, content: dict) -> MemoryChunk:
        """Add a new memory chunk to declarative memory."""
        chunk = MemoryChunk(
            name=name,
            content=content,
            creation_time=self.current_time,
            retrieval_times=[self.current_time],
        )
        self.chunks[name] = chunk
        return chunk

    def compute_activation(self, chunk: MemoryChunk) -> float:
        """Compute base-level activation for ``chunk`` at the current time."""
        if not chunk.retrieval_times:
            return self.threshold - 1.0

        time_diffs = [self.current_time - t for t in chunk.retrieval_times if self.current_time - t > 0]
        if not time_diffs:
            return chunk.base_level

        bll = float(np.log(sum(td ** (-self.decay) for td in time_diffs)))
        activation_noise = float(np.random.logistic(0, self.noise * np.pi / np.sqrt(3)))
        return bll + activation_noise

    def retrieve(self, query: dict, time_advance: float = 1.0) -> Optional[MemoryChunk]:
        """Attempt to retrieve a chunk matching ``query``.

        Returns the highest-activation matching chunk above threshold, or
        ``None`` if no chunk exceeds threshold.
        """
        self.current_time += time_advance

        matching = []
        for chunk in self.chunks.values():
            if all(chunk.content.get(k) == v for k, v in query.items()):
                activation = self.compute_activation(chunk)
                matching.append((activation, chunk))

        if not matching:
            return None

        best_activation, best_chunk = max(matching, key=lambda x: x[0])
        if best_activation >= self.threshold:
            best_chunk.retrieval_times.append(self.current_time)
            return best_chunk
        return None

    def simulate_forgetting_curve(self, chunk_name: str, time_points: np.ndarray) -> np.ndarray:
        """Simulate activation over time (smooth forgetting curve, noise-free)."""
        if chunk_name not in self.chunks:
            raise ValueError(f"Chunk '{chunk_name}' not found in memory")

        chunk = self.chunks[chunk_name]
        original_time = self.current_time

        activations = []
        for t in time_points:
            time_diffs = [t - rt for rt in chunk.retrieval_times if t - rt > 0]
            if time_diffs:
                bll = float(np.log(sum(td ** (-self.decay) for td in time_diffs)))
            else:
                bll = self.threshold - 1.0
            activations.append(bll)

        self.current_time = original_time
        return np.array(activations)


if __name__ == "__main__":
    np.random.seed(0)
    memory = ACTRMemory(decay=0.5, noise=0.25, threshold=-1.5)
    memory.add_chunk("operant_conditioning", {"type": "concept", "domain": "behaviorism"})
    memory.add_chunk("classical_conditioning", {"type": "concept", "domain": "behaviorism"})

    for _ in range(5):
        result = memory.retrieve({"domain": "behaviorism"}, time_advance=10)
        if result:
            print(f"Retrieved: {result.name} at t={memory.current_time:.1f}")

    times = np.linspace(1, 500, 50)
    activations = memory.simulate_forgetting_curve("operant_conditioning", times)
    print(f"Final activation at t={times[-1]:.0f}: {activations[-1]:.3f}")
