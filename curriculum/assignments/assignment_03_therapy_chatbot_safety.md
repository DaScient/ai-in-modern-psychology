# Assignment 3 — Design a Safety Protocol for a Therapy Chatbot

> Aligned with Chapter 10 of *AI in Modern Psychology*.

## Learning Goals

- Identify failure modes of conversational mental-health agents.
- Design rule-based and ML-based safeguards.
- Specify escalation paths and document them in a model card.

## Task

1. Extend `code/clinical/therapy_safety.py` with **at least three** new safety
   patterns (with citations to the literature for each).
2. Add unit tests for true-positive and false-positive cases.
3. Write an `model_card.md` for your safety classifier following the
   [model-card template](../../ethics_toolkit/model_card_template.md).
4. Describe an escalation pathway in a flow diagram (any format) that connects
   user message → classifier verdict → resources / human review.

## Deliverables

- A pull-request-style branch with edits to `therapy_safety.py`.
- A folder `assignment_03_<your_name>/` containing tests, model card, and flow diagram.

## Rubric

| Criterion | Points |
|-----------|-------:|
| Quality and justification of new patterns | 25 |
| Test coverage including false-positive cases | 20 |
| Model-card completeness | 25 |
| Escalation diagram clarity | 20 |
| Reflection on remaining limitations | 10 |
