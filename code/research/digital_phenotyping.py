"""Digital-phenotyping feature extraction — Chapter 4.

A teaching toolkit that takes *raw* passive-sensing streams (GPS,
accelerometer, screen events) and converts them into the small set of
behavioural features that recur across the literature:

* **Location entropy** — Shannon entropy of cluster visits.
* **Mobility radius** — gyration radius of GPS trace (km).
* **Circadian disruption** — variance of activity counts in the
  midnight–04:00 window.
* **Sleep regularity index (SRI)** — proxy for sleep stability.
* **Screen-time bursts** — fraction of screen unlocks lasting < 30 s
  (a marker of compulsive checking).

The module ships with a synthetic generator so that learners can study
the pipeline without needing IRB-approved data.

References:
    Onnela & Rauch (2016) *Neuropsychopharmacology*.
    Saeb et al. (2015) *J. Med. Internet Res.*
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Sequence, Tuple

import numpy as np
import pandas as pd

EARTH_RADIUS_KM = 6371.0


# ---------------------------------------------------------------------------
# Feature extractors
# ---------------------------------------------------------------------------


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance between two lat/lon points in kilometres."""
    lat1, lon1, lat2, lon2 = map(np.radians, (lat1, lon1, lat2, lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return float(2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(a)))


def location_entropy(cluster_ids: Sequence[int]) -> float:
    """Shannon entropy (base 2) of cluster visits.

    Low entropy ≈ life confined to few places (a depression marker in
    several studies). High entropy ≈ varied daily life.
    """
    arr = np.asarray(cluster_ids)
    if arr.size == 0:
        return 0.0
    _, counts = np.unique(arr, return_counts=True)
    p = counts / counts.sum()
    return float(-np.sum(p * np.log2(p + 1e-12)))


def mobility_radius_km(lat: Sequence[float], lon: Sequence[float]) -> float:
    """Gyration radius of a GPS trace, in kilometres."""
    lat_arr = np.asarray(lat, dtype=float)
    lon_arr = np.asarray(lon, dtype=float)
    if lat_arr.size < 2:
        return 0.0
    centroid_lat, centroid_lon = lat_arr.mean(), lon_arr.mean()
    dists = np.array(
        [_haversine_km(la, lo, centroid_lat, centroid_lon) for la, lo in zip(lat_arr, lon_arr)]
    )
    return float(np.sqrt(np.mean(dists**2)))


def circadian_disruption(activity: Sequence[float], hours: Sequence[int]) -> float:
    """Variance of activity in the midnight–04:00 nadir window.

    Healthy circadian rhythms produce near-zero activity in this window;
    elevated variance is associated with depression and shift-work
    disorder.
    """
    activity_arr = np.asarray(activity, dtype=float)
    hours_arr = np.asarray(hours, dtype=int)
    mask = (hours_arr >= 0) & (hours_arr < 4)
    if mask.sum() < 2:
        return 0.0
    return float(np.var(activity_arr[mask]))


def sleep_regularity_index(sleep_states: Sequence[Sequence[int]]) -> float:
    """Sleep Regularity Index (Phillips et al., 2017).

    Args:
        sleep_states: Matrix of shape (n_days, n_minutes) with 1=asleep, 0=awake.
            Two consecutive days are compared minute-by-minute; SRI is the mean
            agreement scaled to [-100, 100].

    Returns:
        SRI in [-100, 100]; ``100`` = perfectly regular sleep.
    """
    arr = np.asarray(sleep_states, dtype=int)
    if arr.ndim != 2 or arr.shape[0] < 2:
        return 0.0
    agreement = (arr[:-1] == arr[1:]).mean()
    return float(200.0 * agreement - 100.0)


def screen_burst_fraction(unlock_durations_seconds: Sequence[float], threshold: float = 30.0) -> float:
    """Fraction of phone-unlock events lasting less than ``threshold`` seconds.

    A high burst fraction indicates "phantom checking" behaviour
    correlated with anxiety and adolescent depression.
    """
    arr = np.asarray(unlock_durations_seconds, dtype=float)
    if arr.size == 0:
        return 0.0
    return float((arr < threshold).mean())


# ---------------------------------------------------------------------------
# End-to-end demo pipeline
# ---------------------------------------------------------------------------


@dataclass
class PhenotypeWindow:
    """Aggregated digital-phenotype features for one participant-day."""

    participant_id: str
    day: int
    location_entropy: float = 0.0
    mobility_radius_km: float = 0.0
    circadian_disruption: float = 0.0
    sleep_regularity: float = 0.0
    screen_burst_fraction: float = 0.0
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, float | str | List[str]]:
        return {
            "participant_id": self.participant_id,
            "day": self.day,
            "location_entropy": self.location_entropy,
            "mobility_radius_km": self.mobility_radius_km,
            "circadian_disruption": self.circadian_disruption,
            "sleep_regularity": self.sleep_regularity,
            "screen_burst_fraction": self.screen_burst_fraction,
            "notes": list(self.notes),
        }


def simple_depression_score(window: PhenotypeWindow) -> float:
    """Combine features into a unit-interval educational depression score.

    Weights are *illustrative* — they come from Saeb et al. (2015) but
    are scaled here for didactic clarity. Do not interpret the absolute
    value as a clinical indicator.
    """
    z_loc = max(0.0, 2.5 - window.location_entropy)
    z_mob = max(0.0, 5.0 - window.mobility_radius_km) / 5.0
    z_circ = min(window.circadian_disruption / 4.0, 1.0)
    z_burst = min(window.screen_burst_fraction, 1.0)
    raw = 0.35 * z_loc / 2.5 + 0.25 * z_mob + 0.25 * z_circ + 0.15 * z_burst
    return float(min(max(raw, 0.0), 1.0))


def generate_synthetic_day(
    participant_id: str = "P001",
    day: int = 0,
    depressed: bool = False,
    seed: int | None = None,
) -> Tuple[pd.DataFrame, PhenotypeWindow]:
    """Generate one synthetic participant-day plus its aggregated features.

    Depressed participants get: narrower location distribution, smaller
    mobility radius, noisy night activity, and more screen-checking bursts.
    """
    rng = np.random.default_rng(seed)
    n_clusters = 2 if depressed else 6
    cluster_ids = rng.integers(0, n_clusters, size=288)  # 5-minute bins
    # GPS jitter around home (lat=37.77, lon=-122.41 — San Francisco)
    spread = 0.005 if depressed else 0.04
    lat = 37.77 + rng.normal(0, spread, size=288)
    lon = -122.41 + rng.normal(0, spread, size=288)
    hours = (np.arange(288) // 12) % 24
    activity = rng.gamma(0.5 if depressed else 0.2, 1.0 if depressed else 0.5, size=288)
    sleep_states = np.zeros((2, 480), dtype=int)
    sleep_states[0, : 60 * 7] = 1  # 7 h regular
    if depressed:
        sleep_states[1, 60:60 + 60 * 5] = 1  # offset + short sleep
    else:
        sleep_states[1, : 60 * 7] = 1
    unlocks = rng.gamma(0.5 if depressed else 1.5, 30 if depressed else 60, size=120)

    window = PhenotypeWindow(
        participant_id=participant_id,
        day=day,
        location_entropy=location_entropy(cluster_ids),
        mobility_radius_km=mobility_radius_km(lat, lon),
        circadian_disruption=circadian_disruption(activity, hours),
        sleep_regularity=sleep_regularity_index(sleep_states),
        screen_burst_fraction=screen_burst_fraction(unlocks),
    )
    if depressed:
        window.notes.append("Synthetic: depressive phenotype")

    raw = pd.DataFrame(
        {
            "minute": np.arange(288) * 5,
            "cluster_id": cluster_ids,
            "lat": lat,
            "lon": lon,
            "hour": hours,
            "activity": activity,
        }
    )
    return raw, window


if __name__ == "__main__":  # pragma: no cover
    for tag in (False, True):
        _, win = generate_synthetic_day(depressed=tag, seed=0)
        print(("Healthy" if not tag else "Depressed"), "->", win.to_dict())
        print("  educational depression score:", simple_depression_score(win))
