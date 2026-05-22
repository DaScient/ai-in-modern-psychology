# Model Card: [Model Name]

> Based on Mitchell et al. (2019) model-card framework, adapted for
> psychological AI applications. See: *AI in Modern Psychology*, Chapter 22.

---

## Model Details

| Field | Value |
|-------|-------|
| **Model name** | [Name] |
| **Version** | [v0.1.0] |
| **Model type** | [Classification / Regression / Generative] |
| **Date** | [YYYY-MM-DD] |
| **Authors** | [Names] |
| **Contact** | [Email or GitHub] |
| **License** | [MIT / CC BY-NC-SA 4.0 / Other] |

### Architecture

[Describe model architecture — e.g., XGBoost gradient boosting, 100 estimators, max depth 4.]

### Training Data

[Source, size, collection period, inclusion / exclusion criteria.]

### Intended Use

**Primary intended uses:**

- [Specific use case 1]
- [Specific use case 2]

**Out-of-scope uses:**

- ⚠️ [Explicitly prohibited use 1]
- ⚠️ [Explicitly prohibited use 2]

---

## Performance Metrics

| Metric | Overall | Group A | Group B |
|--------|---------|---------|---------|
| AUC-ROC |  |  |  |
| Sensitivity (TPR) |  |  |  |
| Specificity (TNR) |  |  |  |
| PPV |  |  |  |
| NPV |  |  |  |

### Performance Disaggregation

[Provide performance metrics broken down by age, gender, race / ethnicity, and other relevant demographic factors.]

---

## Fairness Evaluation

| Fairness Metric | Value | Threshold | Pass / Fail |
|-----------------|-------|-----------|-------------|
| Demographic Parity Difference |  | < 0.10 |  |
| Equal Opportunity Difference |  | < 0.10 |  |
| Equalized Odds Difference |  | < 0.10 |  |

---

## Ethical Considerations

### Known Limitations

- [ ] Training data is not representative of [population]
- [ ] Model has not been validated in [setting]
- [ ] May not generalize to [demographic group]

### Privacy

- [Describe what data the model processes and how]
- [Data retention policy]
- [Anonymization approach]

### Safety

- **Clinical oversight required:** [Yes / No — explain]
- **Crisis escalation protocol:** [Describe]
- **False-positive handling:** [Describe]

---

## Caveats and Recommendations

1. [Specific caveat with actionable recommendation]
2. [Specific caveat]

---

*This model card follows the template from the [AI in Modern Psychology](https://github.com/DaScient/ai-in-modern-psychology) ethics toolkit.*
