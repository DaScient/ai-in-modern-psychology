# Sample Datasets

All datasets in this directory are **synthetic** and generated for educational
purposes only. They are designed to mimic the statistical patterns described in
*AI in Modern Psychology* without using real individual data.

## Files

| File | Generator | Used by |
|------|-----------|---------|
| `depression_synthetic.csv` | `generate_synthetic.py --depression` | Chapter 4 / digital phenotyping examples |
| `hiring_sample.csv` | `generate_synthetic.py --hiring` | Chapter 13 / notebook `03_hiring_bias_audit.ipynb` |
| `ehr_suicide_risk.csv` | `generate_synthetic.py --ehr` | Chapter 8/11 / notebook `02_suicide_risk_SHAP.ipynb` |

## Regenerating the data

```bash
python data/generate_synthetic.py --all --seed 42
```

## Why synthetic?

Real clinical or sensor data require IRB approval, consent management, and
robust de-identification. Synthetic data let learners explore the methods
without the governance burden, while still exposing them to realistic
challenges (class imbalance, missingness, bias).

## Ethical note

Even synthetic data should not be used to make claims about real populations.
Patterns embedded here reflect the educational targets of each chapter, not
empirical findings about any specific community.
