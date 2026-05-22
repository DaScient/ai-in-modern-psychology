"""
Therapy chatbot safety: rule-based crisis-language detector.

Based on: *AI in Modern Psychology*, Chapter 10.

Production deployments must combine pattern matching with classifier
ensembles, conservative thresholds, and human-in-the-loop review.
This module is illustrative, not deployment-ready.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Conservative crisis lexicon. Real systems use much larger, vetted lists.
CRISIS_PATTERNS = [
    r"\bkill myself\b",
    r"\bend (?:it|my life)\b",
    r"\bsuicid(?:e|al)\b",
    r"\bself[\s-]?harm\b",
    r"\bcut(?:ting)? myself\b",
    r"\bwant to die\b",
    r"\bno reason to live\b",
    r"\boverdose\b",
]

ACUTE_ESCALATION_RESOURCES = {
    "US": "Call or text 988 (Suicide & Crisis Lifeline)",
    "UK": "Call 116 123 (Samaritans)",
    "INTL": "https://findahelpline.com",
}


@dataclass
class SafetyResult:
    """Result of a single safety check."""

    triggered: bool
    matched_patterns: list
    severity: str  # "none" | "elevated" | "acute"
    recommended_action: str


def assess_message(message: str) -> SafetyResult:
    """Assess a single user message for crisis content.

    Args:
        message: User-supplied text.

    Returns:
        A :class:`SafetyResult` describing whether escalation is warranted.
    """
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    text = message.lower()
    matched = [p for p in CRISIS_PATTERNS if re.search(p, text)]

    if not matched:
        return SafetyResult(
            triggered=False,
            matched_patterns=[],
            severity="none",
            recommended_action="continue_normal_flow",
        )

    severity = "acute" if len(matched) >= 2 else "elevated"
    action = "escalate_to_human" if severity == "acute" else "provide_resources_and_check_in"
    return SafetyResult(
        triggered=True,
        matched_patterns=matched,
        severity=severity,
        recommended_action=action,
    )


def build_safety_response(result: SafetyResult, region: str = "US") -> str:
    """Build a user-facing message based on a :class:`SafetyResult`."""
    if not result.triggered:
        return ""
    resource = ACUTE_ESCALATION_RESOURCES.get(region, ACUTE_ESCALATION_RESOURCES["INTL"])
    return (
        "I'm really concerned about what you just shared. You don't have to face this alone. "
        f"Please reach out right now: {resource}. "
        "If you're in immediate danger, contact local emergency services."
    )


if __name__ == "__main__":
    samples = [
        "I had a tough day at work",
        "I just want to end it all, I can't keep going",
        "Sometimes I think about cutting myself when things get hard",
    ]
    for s in samples:
        r = assess_message(s)
        print(f"INPUT: {s}\n  -> triggered={r.triggered} severity={r.severity}")
        if r.triggered:
            print(f"  -> {build_safety_response(r)}\n")
