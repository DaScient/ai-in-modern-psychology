# Algorithmic Recourse Protocol

> Companion to *AI in Modern Psychology*, Chapter 11. Defines how a person
> affected by an AI decision can contest, understand, and change that decision.

## 1. Trigger

Any of the following triggers a recourse pathway:

- A user is denied a service, benefit, or opportunity by an AI-mediated decision.
- A user is flagged for elevated risk in a clinical or workplace context.
- A user disputes the data the model used about them.

## 2. Notification

Within **5 business days** of the decision, the user receives:

1. The fact that an AI system contributed to the decision.
2. A plain-language summary of the most influential factors (e.g., top SHAP features).
3. The contact channel for filing a recourse request.

## 3. Recourse Request

The user may request:

- **Data correction** — submit evidence that the input data are wrong.
- **Counterfactual explanation** — what minimum changes would have produced a different outcome?
- **Human review** — escalate to a human decision-maker.
- **Model audit** — request an independent review of the model.

## 4. Response Time

| Request type | Target response time |
|--------------|----------------------|
| Data correction | 10 business days |
| Counterfactual explanation | 10 business days |
| Human review | 20 business days |
| Model audit | 90 calendar days |

## 5. Outcomes

- If the data were incorrect, the decision is re-made with corrected data.
- If a human reviewer disagrees with the model, the human decision prevails.
- Patterns of overturned decisions trigger model re-training.

## 6. Documentation

- Every recourse request and outcome is logged in an immutable audit table.
- Aggregate statistics (by demographic group) are published quarterly.

## 7. No Retaliation

Filing a recourse request must not negatively affect the user's standing,
treatment quality, or access to services.
