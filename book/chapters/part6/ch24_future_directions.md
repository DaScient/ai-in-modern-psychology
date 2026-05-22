# Chapter 24: Future Directions

## Learning Objectives

By the end of this chapter, you should be able to:

- Identify four near-term and three long-term inflection points for AI in psychology.
- Make grounded predictions about which methodological gaps will close — and which will widen.
- Place yourself, your team, or your institution on the *AI maturity ladder*.
- Use the workbench artefacts (`/code`, `/notebooks`, `/api`, `/ethics_toolkit`) as a basis for your own contribution.

## Overview

A "future directions" chapter that ages well makes few predictions and many observations. This chapter observes where the field's *gaps* are large enough that incremental work cannot close them, and where the workbench in this book can serve as a starting point.

## 24.1 Four Near-Term Inflection Points

1. **Multimodal LLMs in clinical assessment.** Vision + voice + text will collapse what are currently five separate research silos. Expect rapid progress; expect equally rapid premature deployment.
2. **Federated learning at scale.** A few major EHR vendors will demonstrate cross-site model training without data movement; this will unblock multi-site psychiatric ML.
3. **Live regulatory enforcement.** The EU AI Act becomes enforceable in 2025–2026; NYC Local Law 144 is being copied. Expect the first major fines within 24 months of this book's publication.
4. **Routine model cards for clinical AI.** Driven by FDA and EU AI Act, model cards stop being a nice-to-have.

## 24.2 Three Long-Term Inflection Points

1. **Closed-loop interventions.** Sensing → inference → just-in-time intervention loops will mature; the methodology gap is currently *causal inference*, not ML.
2. **Cognitive-architecture-style LLMs.** Hybrid systems pairing LLMs with memory, planning, and explicit world models will reopen the connectionist-vs-symbolic debate (Chapter 2).
3. **Participatory AI.** Data-trust and community-board governance (Chapter 23) will move from pilots to standard practice.

## 24.3 Methodological Gaps Worth Closing

- **External validation discipline.** Most published clinical-AI models still fail to externally validate.
- **Replication of LLM-based studies.** Closed-source dependencies make replication difficult; open-weight alternatives are reaching parity.
- **Construct validity in NLP-derived measures.** The field needs a "psychometric audit" for ML-derived constructs (Chapter 7).
- **Long-horizon evaluation of digital mental-health products.** RCTs at 12+ month follow-up are still rare.

## 24.4 An AI Maturity Ladder for Psychology Teams

| Level | Practice |
|-------|----------|
| 0 | Reads ML papers but does not run code. |
| 1 | Runs published notebooks locally. |
| 2 | Adapts notebooks to own data. |
| 3 | Pre-registers ML studies with externally validated splits. |
| 4 | Deploys to a real population with monitoring and retirement criteria. |
| 5 | Contributes to open-source infrastructure used by other labs. |

Most psychology departments today sit between 1 and 2. The workbench accompanying this book is designed to move readers cleanly from 1 to 3.

## 24.5 Using This Workbench

Concretely, the in-repo artefacts to build on:

- `code/foundations/` — cognitive-architecture starter kit.
- `code/research/` — digital-phenotyping and NLP feature extractors.
- `code/clinical/` — risk modelling, decision curves, safety classifiers.
- `code/social/` — ABM, network influence, fairness audits.
- `code/ethics/` — fairness metrics.
- `api/src/` — FastAPI surface bringing it all together.
- `ethics_toolkit/` — consent, model-card, data-governance, deployment-readiness templates.
- `notebooks/` — end-to-end runnable case studies.
- `curriculum/` — syllabi and assignment templates aligned to chapter numbers.

```{admonition} Try it
:class: tip
Pick one assignment from `curriculum/assignments/`. Complete it not as
a student but as a contributor: fork, improve, submit a pull request.
You will leave the field's collective workbench better than you found it.
```

## Key Terms

| Term | Working definition |
|------|---------------------|
| **Closed-loop intervention** | Sensing → inference → action → re-sense. |
| **Federated learning** | Train on-device; aggregate gradients. |
| **Open-weight model** | Model whose weights are publicly downloadable. |
| **Just-in-time adaptive intervention (JITAI)** | Intervention delivered at a moment of inferred need. |
| **AI maturity ladder** | Self-assessment ladder for team capability. |

## Worked Example: A 5-Year Roadmap

For a hypothetical psychology department starting at Maturity Level 1, sketch a 5-year roadmap reaching Level 4. Identify the three biggest obstacles and the workbench artefacts that address each.

## Hands-on Exercises

1. Pick a 2020+ AI mental-health product. Audit it against the deployment-readiness checklist (Chapter 23). What is missing?
2. Identify one *closed-loop* opportunity in your own clinical or research workflow. Sketch the sensing-to-action loop.
3. Contribute a new chapter case study to the repository. Open a pull request.

## Case Study: The CLPsych Decade

The Computational Linguistics + Clinical Psychology shared task has tracked field progress since 2014. Top-system AUC for suicide-risk classification rose from 0.65 (2014) to 0.85 (2023) — and *flatlined* after 2020. Lesson: more data and bigger models do not always move the needle; methodological innovation does.

## Common Pitfalls

- Treating LLM novelty as substantive progress.
- Underestimating the time needed to move from level 2 to level 3.
- Mistaking publication for deployment.

## Connections to Other Chapters

- Every prior chapter feeds in here; the workbench is the synthesis.
- Regulation realities → **Chapter 21**.
- Governance practice → **Chapter 23**.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. Will multimodal LLMs *replace* or *augment* clinical assessment by 2030?
2. Will participatory governance survive contact with commercial deployment incentives?
3. Where on the maturity ladder is your own current work — and what is the single biggest blocker to the next step?

## Further Reading

- Insel, T. R. (2017). Digital phenotyping: A global tool for psychiatry. *World Psychiatry*.
- Topol, E. J. (2019). High-performance medicine: The convergence of human and artificial intelligence. *Nature Medicine*.
- Marcus, G., & Davis, E. (2019). *Rebooting AI*. Pantheon.
- Stiefel, K. M., & Coggan, J. S. (2023). The energy challenges of artificial superintelligence. *Frontiers in Artificial Intelligence*.
