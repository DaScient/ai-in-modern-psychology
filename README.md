# AI in Modern Psychology

[![Jupyter Book](https://img.shields.io/badge/jupyter%20book-live-blue)](https://DaScient.github.io/ai-in-modern-psychology)
[![Deploy Book](https://github.com/DaScient/ai-in-modern-psychology/actions/workflows/deploy-book.yml/badge.svg)](https://github.com/DaScient/ai-in-modern-psychology/actions/workflows/deploy-book.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DaScient/ai-in-modern-psychology/main)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Text%20License-CC%20BY--NC--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue)](https://opensource.org/licenses/MIT)

> **Computational psychology workbench** — where theories become code, and code becomes evidence.

This repository is the living companion to **"AI in Modern Psychology"** (Barnes & Noble Exclusive, DaScient Press, 2026). It transforms the book's concepts into executable models, interactive case studies, and governance toolkits.

## 📖 Quick Navigation

- **Read the Living Book** → [GitHub Pages](https://DaScient.github.io/ai-in-modern-psychology) (auto-built from `/book`)
- **Run a Notebook** → Click the Binder badge above — no installation required
- **Explore Models** → [`/code`](./code) — Python implementations of key algorithms
- **Run the API** → [`/api/src/main.py`](./api/src/main.py) — FastAPI surface (`/memory`, `/safety`, `/risk`, `/fairness`, `/learning`, `/social/abm`)
- **Ethics Toolkit** → [`/ethics_toolkit`](./ethics_toolkit) — bias audits, model cards, data governance, deployment-readiness checklist, AI disclosure template
- **Curriculum** → [`/curriculum`](./curriculum) — syllabi and seven graded assignments
- **Tests** → [`/tests`](./tests) — `pytest` smoke tests for every code module and API endpoint

## 🧠 What You'll Find Here

| Part | Focus | Example Executable |
|------|-------|---------------------|
| I | Foundations | ACT-R memory simulation, symbolic vs. connectionist comparison |
| II | AI as Research Tool | Digital-phenotyping pipeline, NLP/LIWC-style lexicon scoring, memory models |
| III | Clinical Applications | Suicide risk prediction + SHAP, therapy-chatbot safety, decision-curve analysis |
| IV | I/O & Education | Hiring-bias audit, BKT adaptive learning, burnout detection |
| V | Social & Cultural | Bounded-confidence ABM, network-influence cascades + KKT greedy seeding, cultural AI |
| VI | Real-World & Ethics | Recommender systems, privacy, regulation, ethics, data governance, future directions |

### 🆕 New since the 2026 enrichment

- **All 24 chapters** include Learning Objectives, Key Terms, Worked Examples, Hands-on Exercises, Case Studies, Common Pitfalls, Cross-Chapter Connections, and Further Reading.
- **Notebooks**: `05_polarization_and_network_influence`, `06_nlp_lexicon_for_psychology`, `07_decision_curve_analysis`.
- **Code modules**: `code/research/digital_phenotyping.py`, `code/research/nlp_psychology.py`, `code/social/network_influence.py`, `code/clinical/decision_curve.py`, plus a fleshed-out `code/foundations/symbolic_connectionist.py` and `code/io_ed/adaptive_learning.py`.
- **API**: replaces the previous off-topic protein-folding stub with a coherent **Psychology API** wired to the in-repo modules.
- **Ethics toolkit**: new `deployment_readiness_checklist.md` and `ai_disclosure_template.md`.
- **Curriculum**: assignments 04 (digital phenotyping), 05 (decision-curve analysis), 06 (polarization ABM), 07 (NLP lexicon validation), plus an index in `curriculum/assignments/README.md`.

## 🚀 Getting Started

### Option 1: Run online (no install)

Click the **Binder** badge above. Wait 2–3 minutes, then open any notebook in `/notebooks`.

### Option 2: Run locally

```bash
git clone https://github.com/DaScient/ai-in-modern-psychology.git
cd ai-in-modern-psychology
conda env create -f environment.yml
conda activate aipsych
jupyter notebook
```

Then open `notebooks/` and start with `02_suicide_risk_SHAP.ipynb`.

### Option 3: Build the book locally

```bash
pip install jupyter-book
jupyter-book build book/
open book/_build/html/index.html
```

## 🧪 Featured Notebooks

| Notebook | Chapter | Description |
|----------|---------|-------------|
| [`01_ACT_R_memory_simulation.ipynb`](./notebooks/01_ACT_R_memory_simulation.ipynb) | Ch 6 | Simulate chunk decay and retrieval |
| [`02_suicide_risk_SHAP.ipynb`](./notebooks/02_suicide_risk_SHAP.ipynb) | Ch 8 / 11 | Predict risk from EHR & explain with SHAP |
| [`03_hiring_bias_audit.ipynb`](./notebooks/03_hiring_bias_audit.ipynb) | Ch 13 | Detect and mitigate algorithmic discrimination |
| [`04_therapy_bot_safety.ipynb`](./notebooks/04_therapy_bot_safety.ipynb) | Ch 10 | Rule-based crisis escalation |

## 🤝 Contributing

We welcome contributions of all kinds:

- **Code** — Implement a model from a chapter (see [CONTRIBUTING.md](./CONTRIBUTING.md))
- **Ethics reviews** — Audit existing models for bias or suggest governance improvements
- **Pedagogy** — Create assignments, slides, or exam questions
- **Design** — Draw diagrams missing from the original PDF

Please read our [Code of Conduct](./.github/CODE_OF_CONDUCT.md) and [Contribution Guidelines](./CONTRIBUTING.md) before submitting a PR.

## 📄 License

- **Text & chapters** (Markdown files in `/book`): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Code & notebooks** (Python files, `.ipynb`): [MIT License](./LICENSE)

## 📚 Citation

```bibtex
@book{tadaya2026ai,
  title={AI in Modern Psychology},
  author={Tadaya, Don D.M.},
  year={2026},
  publisher={DaScient Press},
  note={Companion repository: https://github.com/DaScient/ai-in-modern-psychology}
}
```

## 🙏 Acknowledgements

Built upon the foundations of the original Barnes & Noble Exclusive Collection. Thanks to all early contributors and the computational psychology community.

---

Start exploring → [the living book](https://DaScient.github.io/ai-in-modern-psychology).

---

<p align="center"><sub>💛 Support <a href="https://cash.app/dascient/">DaScient, Inc.</a> — a non-profit promoting accessible intelligence and community learning.</sub></p>