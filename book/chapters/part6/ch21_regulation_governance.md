# Chapter 21: Regulation and Governance

## Learning Objectives

By the end of this chapter, you should be able to:

- Map the FDA SaMD, EU AI Act, and EU MDR classifications onto common AI mental-health products.
- Read a Model Card and a Datasheet for Datasets with a critical eye.
- Apply the NIST AI Risk Management Framework to a deployment plan.
- Distinguish *governance* from *compliance*.

## Overview

A decade ago AI in psychology was governed by little more than IRB review. Today, multiple overlapping regimes apply — and the cost of ignoring them is escalating. This chapter teaches the structure of the regimes without trying to be a legal manual.

## 21.1 The FDA and Software as a Medical Device (SaMD)

- **Enforcement discretion** for low-risk general-wellness software.
- **510(k)** clearance for substantially equivalent moderate-risk devices.
- **De Novo** pathway for novel low-to-moderate-risk devices.
- **PMA** for high-risk devices.

The FDA's *Predetermined Change Control Plan* (PCCP) accommodates ML models that update post-clearance — a fix for the "frozen model" problem.

## 21.2 The EU AI Act

Risk-based classification (effective 2025–2026):

- **Prohibited** — manipulative systems, real-time biometric scoring.
- **High-risk** — employment, education, essential services — includes most mental-health AI.
- **Limited risk** — disclosure requirements (e.g., users must know they are talking to AI).
- **Minimal risk** — recommender systems.

High-risk obligations: data quality, technical documentation, human oversight, post-market monitoring.

## 21.3 The NIST AI Risk Management Framework

Four functions: **Govern, Map, Measure, Manage**. Each maps to concrete artefacts:

- *Govern* — roles, accountabilities, ethics policy.
- *Map* — system characterisation, context-of-use.
- *Measure* — fairness, robustness, privacy, security.
- *Manage* — risk treatment, incident response.

The framework is non-binding in the US but is the most useful checklist available.

## 21.4 Documentation Artefacts

- **Model cards** (Mitchell et al., 2019) — purpose, scope, training data, evaluation, ethical considerations.
- **Datasheets for datasets** (Gebru et al., 2021) — provenance, composition, collection, labelling, recommended uses.
- **Risk register** — internal log of known risks, status, owner.

Templates: see `ethics_toolkit/model_card_template.md` (and the new deployment-readiness checklist added in this PR).

## Key Terms

| Term | Working definition |
|------|---------------------|
| **SaMD** | Software as a Medical Device. |
| **PCCP** | Predetermined Change Control Plan. |
| **CE marking** | EU declaration of conformity. |
| **GMLP** | Good Machine Learning Practice (FDA/MHRA/HC). |
| **AIA** | AI Act (EU). |

## Worked Example: Classifying a Therapy Chatbot

Decide where Woebot, Wysa, and a hypothetical GPT-driven CBT homework helper sit under (a) FDA SaMD, (b) EU AI Act. Justify each placement.

## Hands-on Exercises

1. Fill out `model_card_template.md` for the risk model in `code/clinical/risk_prediction.py`.
2. Map the audit requirements of NYC Local Law 144 onto `code/io_ed/hiring_bias_audit.py`.
3. Read an FDA 510(k) summary for a mental-health device; identify what is — and is not — disclosed.

## Case Study: Pear Therapeutics' reSET

reSET, the first FDA-cleared prescription digital therapeutic for substance-use disorder (2017), demonstrated the regulatory pathway *is* navigable but commercially fragile (Pear filed for bankruptcy in 2023). Lesson: clearance is necessary but insufficient for sustainable mental-health AI deployment.

## Common Pitfalls

- Confusing FDA enforcement discretion with permission.
- Treating model cards as marketing.
- Underestimating EU obligations for US-based deployments.

## Connections to Other Chapters

- Bias audits → **Chapter 13**.
- Crisis-line governance → **Chapter 12**.
- Long-term horizon → **Chapter 24**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Should mental-health AI carry higher disclosure obligations than physical-health AI?
2. Is FDA's *enforcement discretion* the right default for wellness apps?
3. How can a research-grade tool become a regulated product without losing the open-science spirit?

## Further Reading

- Mitchell, M., et al. (2019). Model cards for model reporting. *FAT* '19.
- Gebru, T., et al. (2021). Datasheets for datasets. *CACM*.
- NIST AI Risk Management Framework 1.0 (2023).
- FDA (2023). *Predetermined Change Control Plans for AI/ML-Enabled Device Software Functions* (draft guidance).

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
