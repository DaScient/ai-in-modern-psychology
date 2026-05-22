# Chapter 20: Privacy and Surveillance

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish privacy *as confidentiality*, *as control*, and *as contextual integrity* (Nissenbaum).
- Identify the surveillance affordances of common AI mental-health products.
- Apply HIPAA, FERPA, GDPR, and CCPA in plain terms to a concrete deployment.
- Reason about *differential privacy* and *federated learning* as technical mitigations.

## Overview

Mental-health data is uniquely sensitive: it can affect insurance, employment, custody, and immigration. AI applications expand both the *amount* of such data and the *inferences* drawable from it. Privacy in this chapter is not just a legal compliance task; it is a clinical-safety task.

## 20.1 Three Senses of Privacy

- **Confidentiality** — who can read the data.
- **Control** — who can decide what is done with it.
- **Contextual integrity** (Nissenbaum, 2010) — whether the use matches the *norms of the context in which the data was shared*.

Most legal frameworks address (1); psychologists routinely worry about (2); (3) is the most useful frame for AI deployments.

## 20.2 Surveillance Affordances

Common mental-health-app data flows that create surveillance risk:

- Analytics SDKs sending user IDs to third parties.
- Cloud-based crisis-detection that retains transcripts.
- Wearable APIs that expose location and heart rate to platform aggregators.
- Insurance partnerships that surface claim-time inference.

The 2022 Crisis Text Line / Loris.ai controversy is the canonical example.

## 20.3 Regulatory Landscape (Plain English)

- **HIPAA (US)** — covers covered entities and business associates; *most apps are not covered*.
- **FERPA (US)** — covers educational records; relevant to digital phenotyping in schools.
- **GDPR (EU)** — explicit consent + right to erasure + data-protection-by-design.
- **CCPA / CPRA (California)** — right to know, delete, opt out of sale.
- **Brazil LGPD, Quebec Law 25, India DPDPA** — converging on similar principles.

Map of jurisdictions every deployer should know: see also `ethics_toolkit/data_governance_policy.md`.

## 20.4 Technical Mitigations

- **Differential privacy** — bound on what a single record contributes to outputs.
- **Federated learning** — train models on-device; share gradients, not data.
- **Secure enclaves / TEEs** — encrypted compute on untrusted servers.
- **Synthetic data** — model trained on real data generates surrogates.

Each helps *some* threat models — none replaces a sound governance policy.

```{admonition} Try it
:class: tip
For the digital-phenotyping pipeline in `code/research/digital_phenotyping.py`,
list every byte that ever leaves the device. For each, name the legal regime
that applies and the *minimum-data* alternative.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Contextual integrity** | Use matches norms of the original context. |
| **De-identification** | Removal of direct identifiers (not the same as anonymisation). |
| **Re-identification** | Recovery of identity from "anonymised" data. |
| **Differential privacy** | $\varepsilon$-bound on single-record contribution. |

## Worked Example: A Privacy Threat Model

For a hypothetical depression-tracking app: enumerate the data flows, then for each flow assign *(actor, asset, threat, mitigation)*. The exercise reveals that most user-perceived privacy violations are not unauthorised reads, but *authorised uses outside contextual norms*.

## Hands-on Exercises

1. Re-identification challenge: with two of `{ZIP, DOB, gender}`, what fraction of the US population is uniquely identifiable? Look up the Sweeney result.
2. Apply differential privacy to the SHAP notebook's risk score; what $\varepsilon$ preserves clinical utility?
3. Map your favourite mental-health app against §20.2's checklist.

## Case Study: Crisis Text Line / Loris.ai (2022)

Anonymised conversation data shared with a commercial spin-off triggered widespread loss of trust and policy reversal. Lesson: even legally compliant uses can fail the *contextual-integrity* test.

## Common Pitfalls

- Equating de-identification with anonymisation.
- Treating GDPR/HIPAA compliance as a deployment ceiling.
- Forgetting that *inferences* are data.

## Connections to Other Chapters

- Consent → **Chapter 19**.
- Regulation → **Chapter 21**.
- Digital phenotyping → **Chapter 4**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Is differential privacy enough?
2. Should mental-health data sales be banned outright?
3. Who is the appropriate audience for a privacy policy — users or regulators?

## Further Reading

- Nissenbaum, H. (2010). *Privacy in Context*. Stanford University Press.
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in TCS*.
- McMahan, B., et al. (2017). Communication-efficient learning of deep networks from decentralized data. *AISTATS*.
- Solove, D. J. (2008). *Understanding Privacy*. Harvard University Press.
