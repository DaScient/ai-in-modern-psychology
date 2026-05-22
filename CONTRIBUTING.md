# Contributing to AI in Modern Psychology

Thank you for your interest in contributing to this computational psychology workbench! This guide covers how to contribute code, chapters, notebooks, ethics reviews, and pedagogy materials.

## 🌟 Ways to Contribute

| Type | What to Do | Where |
|------|-----------|-------|
| 🐛 Bug report | Found an error in code or text | [Bug Report](./.github/ISSUE_TEMPLATE/bug_report.md) |
| 🧠 New model | Implement a model from the book | [Model Proposal](./.github/ISSUE_TEMPLATE/model_proposal.md) |
| ⚖️ Ethics concern | Found a bias or safety issue | [Ethics Concern](./.github/ISSUE_TEMPLATE/ethics_concern.md) |
| 📖 Chapter revision | Improve or update chapter content | PR to `book/chapters/` |
| 🎓 Pedagogy | Assignments, slides, exam questions | PR to `curriculum/` |
| 🖼️ Diagrams | Create figures referenced in chapters | PR to `book/figures/` |

## 🚀 Getting Started

### 1. Fork and clone

```bash
git clone https://github.com/YOUR_USERNAME/ai-in-modern-psychology.git
cd ai-in-modern-psychology
conda env create -f environment.yml
conda activate aipsych
```

### 2. Create a feature branch

```bash
git checkout -b feature/my-contribution
```

### 3. Make your changes

Follow the conventions below, then commit:

```bash
git add .
git commit -m "feat: add ACT-R memory model implementation"
git push origin feature/my-contribution
```

### 4. Open a pull request

Use the PR template and fill in all sections.

## 📋 Code Conventions

### Python

- PEP 8 style (use `ruff` for linting)
- Type hints on all public functions
- Google-style docstrings for all classes and public methods

### Notebooks

Every notebook must:

1. Have a `## Learning Objectives` section at the top
2. Include a `## Ethical Considerations` section
3. Include a `## References` section at the bottom
4. Run end-to-end without errors on Binder
5. Use only synthetic or publicly licensed data

### Markdown chapters

- Use MyST Markdown syntax (for Jupyter Book compatibility)
- Add `{note}`, `{warning}`, or `{tip}` admonitions for key concepts
- Link to the relevant notebook where applicable

## ⚖️ Ethics Review Process

Any model that:

- Uses clinical data or simulates clinical populations
- Makes predictions about mental health or behavior
- Could be used in consequential decision-making

…must pass an ethics review before merging. Open an [ethics concern issue](./.github/ISSUE_TEMPLATE/ethics_concern.md) and tag `@ethics-review-board`.

## 🌿 Branching Strategy

- `main` — stable; book is deployed from here
- `dev` — integration branch for active work
- `feature/*` — individual models or chapter edits

## 📦 Release Cadence

- **Minor release** every two months (new models, notebook fixes)
- **Major release** annually (synced with PDF updates)

## 📬 Questions?

Open a [GitHub Discussion](https://github.com/DaScient/ai-in-modern-psychology/discussions) in the appropriate category.
