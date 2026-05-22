# Bias Impact Assessment

> Complete this checklist **before** deploying any AI model to a real population.
> Based on *AI in Modern Psychology*, Chapter 22.

## 1. Purpose

- [ ] The intended use is clearly described in plain language.
- [ ] Out-of-scope uses are explicitly listed.
- [ ] Stakeholders affected by the model have been identified.

## 2. Data

- [ ] Sources of training data are documented.
- [ ] Demographic composition of training data is reported.
- [ ] Known historical biases in training data are described.
- [ ] Data-collection consent procedures are documented.

## 3. Demographic Performance

For each protected attribute (age, gender, race / ethnicity, disability status,
socio-economic status):

- [ ] Sensitivity (TPR) computed per group.
- [ ] Specificity (TNR) computed per group.
- [ ] Calibration (Brier score, ECE) per group.
- [ ] Sample size per group sufficient for stable estimates.

## 4. Fairness Metrics

- [ ] Demographic-parity difference < 0.10
- [ ] Equal-opportunity difference < 0.10
- [ ] Equalized-odds difference < 0.10
- [ ] If any threshold fails, mitigation steps are documented.

## 5. Intersectional Analysis

- [ ] Performance reported for at least two-way intersections of protected attributes.
- [ ] Small-cell suppression policy is documented.

## 6. Mitigation

- [ ] Pre-processing, in-processing, or post-processing mitigation has been tried.
- [ ] Accuracy / fairness trade-offs are documented.

## 7. Communication

- [ ] Model card is published.
- [ ] Affected stakeholders are informed.
- [ ] Recourse process is documented.

## 8. Monitoring

- [ ] Plan for ongoing fairness monitoring exists.
- [ ] Trigger conditions for re-audit are documented.
- [ ] Sunset date is set.

---

**Sign-off**

- Modeler: ________________________  Date: __________
- Ethics reviewer: ________________  Date: __________
- Domain expert: __________________  Date: __________
