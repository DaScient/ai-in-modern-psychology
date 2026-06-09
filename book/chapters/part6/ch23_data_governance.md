# Chapter 23: Data Governance

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish data *stewardship*, *ownership*, and *governance*.
- Apply the data-governance policy template (`ethics_toolkit/data_governance_policy.md`) to a new project.
- Specify data-minimisation, retention, and deletion practices for an AI mental-health study.
- Reason about *participatory* data governance and when it changes the outcome.

## Overview

Data governance is the chapter where ethics meets operations. Privacy law, IRB protocols, and engineering practice converge on a small set of questions: *who decides*, *who can see*, *for how long*, *and what happens when something goes wrong*.

## 23.1 Stewardship, Ownership, Governance

- **Stewardship** — operational responsibility for the data (the team that holds it).
- **Ownership** — legal/normative claim (often: the user; sometimes the institution).
- **Governance** — the policies and processes that bind both.

Most disputes in AI mental health arise because *stewardship is operational and immediate* while *ownership is normative and slow* — and governance is supposed to mediate.

## 23.2 Data Minimisation as a First Principle

Collect the least data needed to answer the question. The single biggest reduction in risk comes not from technical mitigations but from *not collecting in the first place*.

For each data element ask:

1. What question requires it?
2. Could a coarser representation answer the same question?
3. What is the retention window?
4. What deletion triggers exist?

If you cannot answer all four, do not collect.

## 23.3 Lifecycle Stages

| Stage | Governance question |
|-------|----------------------|
| Collection | Consent, lawful basis, contextual integrity |
| Storage | Encryption at rest, access control, audit log |
| Processing | Purpose limitation, data-flow diagram |
| Sharing | Data-use agreement, recipient vetting |
| Retention | Stated horizon, deletion practice |
| Deletion | Subject-initiated and automatic; verifiability |

The `data_governance_policy.md` template ships with prompts for each stage.

## 23.4 Participatory Governance

The strongest counterweight to top-down governance is the participation of the people whose data it is:

- **Data trusts** (Open Data Institute) — fiduciary boards including data subjects.
- **Community review boards** — common in Indigenous health research.
- **Patient-and-public involvement** (PPI) — UK standard for health research.

These shift *governance* without changing *stewardship*, and they change which outcomes are even considered.

## 23.5 When Governance Fails

Common failure modes:

- **Drift in purpose** (e.g., research data later used for marketing).
- **Vendor change** (acquired company, new owner, new policies).
- **Aggregation** (innocuous-on-its-own datasets combined to reveal sensitive inferences).
- **Subpoena** (especially relevant for crisis-line data).

A governance policy must explicitly address each.

```{admonition} Try it
:class: tip
Map the entire data lifecycle for the synthetic risk model in
`code/clinical/risk_prediction.py` — from generation to deletion — and
identify *one* governance gap at each stage.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Data trust** | Independent fiduciary governing data on subjects' behalf. |
| **Purpose limitation** | Use restricted to the purposes collected for. |
| **Retention horizon** | Pre-specified deletion deadline. |
| **Audit log** | Record of who accessed what, when, why. |
| **Subject access request** | User's right to retrieve their stored data. |

## Worked Example: A Crisis-Line Data Policy

Walk through the lifecycle stages for a hypothetical crisis-text service. For each stage, write one sentence stating the rule, then one identifying its weakest enforcement point.

## Hands-on Exercises

1. Fill out `ethics_toolkit/data_governance_policy.md` for a hypothetical 12-month phenotyping study.
2. Design a *subject access request* response procedure that handles model-derived inferences as well as raw data.
3. Compare three real mental-health-app privacy policies on data minimisation. Rank them.

## Case Study: The Maori Data Sovereignty Movement

Te Mana Raraunga, the Maori Data Sovereignty Network, has driven legal and institutional changes in New Zealand around community-level ownership of data about Maori people. Lesson: governance frameworks rooted in individual consent miss collective harms; participatory governance fills the gap.

## Common Pitfalls

- Treating policy as a one-time document.
- Conflating storage encryption with governance.
- Forgetting that *derived* features (model outputs) are also data.

## Connections to Other Chapters

- Consent → **Chapter 19**'s related concepts in §23.4.
- Regulation → **Chapter 21**.
- Privacy → **Chapter 20**.
- Deployment audits → **Chapter 22**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Whose data is a depressed teenager's diary entry on a journaling app?
2. Should crisis-line data be *legally privileged* (like therapist–client communications)?
3. Can governance be retrofitted to a system that did not start with it?

## Further Reading

- Floridi, L. (2014). *The Fourth Revolution: How the Infosphere Is Reshaping Human Reality*. Oxford University Press.
- Open Data Institute (2018). Data trusts: Lessons from three pilots.
- Carroll, S. R., et al. (2020). The CARE principles for Indigenous data governance. *Data Science Journal*.
- Walter, M., Kukutai, T., Carroll, S. R., & Rodriguez-Lonebear, D. (Eds.). (2020). *Indigenous Data Sovereignty and Policy*. Routledge.

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>
