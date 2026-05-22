# Data Governance Policy

> Template based on *AI in Modern Psychology*, Chapter 23.4.

## 1. Scope

This policy applies to all personal data — including behavioural,
psychometric, sensor, and clinical data — collected, processed, or stored by
projects associated with this repository.

## 2. Principles

| Principle | Operational meaning |
|-----------|---------------------|
| Lawfulness | Processing has a clear legal basis (e.g., consent, contract, legitimate interest). |
| Purpose limitation | Data are used only for the purposes disclosed at collection. |
| Data minimization | Only data strictly necessary for the stated purpose are collected. |
| Accuracy | Data are kept accurate and up-to-date; corrections propagate. |
| Storage limitation | Data are kept no longer than necessary. |
| Integrity & confidentiality | Data are protected against unauthorized access. |
| Accountability | A named steward is responsible for each dataset. |

## 3. Roles

- **Data steward** — accountable for a specific dataset, including access decisions.
- **Data processor** — anyone who handles data on the steward's behalf.
- **Data subject** — the individual whose data are processed.

## 4. Retention Schedule

| Data type | Default retention | Justification |
|-----------|-------------------|---------------|
| Raw sensor streams | 12 months | Re-analysis window. |
| Aggregated features | 5 years | Reproducibility of published findings. |
| Identifiers / link tables | Until study closure | Minimum necessary to manage withdrawals. |
| Audit logs | 7 years | Regulatory requirement. |

Deviations from the default require steward sign-off and ethics review.

## 5. Access Control

- Least-privilege access by default.
- Multi-factor authentication required for any system holding identifiable data.
- Quarterly access reviews.

## 6. Deletion

- On participant request, identifiable data are deleted within 30 days.
- Aggregated derivatives are reviewed for re-identification risk before retention.
- For ML models, machine-unlearning or retraining is required when feasible.

## 7. Incident Response

- Suspected breach is reported to the data steward within 24 hours.
- Notification to data subjects within 72 hours (or per applicable law).
- Post-mortem published internally.

## 8. Review

This policy is reviewed annually and after any significant incident.
