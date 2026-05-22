# Deployment-Readiness Checklist

A pre-deployment review template for AI systems in psychology. Complete every
section before moving a model from research to production. Pair with the
[Model Card](./model_card_template.md), [Data Governance Policy](./data_governance_policy.md),
and [Informed Consent Template](./informed_consent_template.md).

> Companion to Chapter 23 (*Data Governance*) and Chapter 21 (*Regulation and
> Governance*). If you cannot answer "yes" with evidence for every check below,
> the system is not ready to deploy.

## 1. Intended Use

- [ ] The intended population, setting, and decision are written in one sentence.
- [ ] *Out-of-scope* populations and decisions are explicitly listed.
- [ ] The deployment is classified under FDA SaMD, EU AI Act, or other applicable regime.

## 2. Data

- [ ] Provenance, collection period, and inclusion/exclusion criteria are documented in a Datasheet.
- [ ] Sample-size justification for each subgroup of interest is included.
- [ ] Known measurement biases are listed.
- [ ] Missing-data mechanism is characterised (MCAR / MAR / MNAR).

## 3. Model

- [ ] Model architecture, hyperparameters, and random seeds are reproducibly recorded.
- [ ] Internal validation uses subject-level splits (no leakage).
- [ ] External validation has been performed on at least one out-of-distribution sample.

## 4. Calibration

- [ ] Calibration plot reported on the external test set.
- [ ] Brier score, intercept, and slope reported.
- [ ] Recalibration procedure documented if used.

## 5. Equity Audit

- [ ] Performance reported separately for every protected attribute available.
- [ ] At least one intersectional cell reported.
- [ ] Fairness metric chosen and *normatively* justified (Chapter 22).
- [ ] Mitigations documented if disparities exceed pre-specified thresholds.

## 6. Safety

- [ ] Red-team test set (≥ 50 cases) documented with rationale.
- [ ] Failure modes catalogued.
- [ ] Crisis-language detection in place where conversational (Chapter 10, 12).
- [ ] Hand-off pathway to human responder defined.

## 7. Clinical Utility

- [ ] Decision-curve analysis reported (Chapter 11).
- [ ] *Informative threshold range* identified where model beats baselines.
- [ ] Operating point defended in terms of clinical cost.

## 8. Privacy and Governance

- [ ] Data flow diagram included.
- [ ] Retention horizon specified.
- [ ] Subject access and deletion procedures tested end-to-end.
- [ ] Vendor / sub-processor list maintained.

## 9. Monitoring

- [ ] Input drift monitoring in place (e.g., PSI on each feature).
- [ ] Output drift monitoring in place.
- [ ] Subgroup performance monitoring in place.
- [ ] Alert thresholds defined.

## 10. Retirement Criteria

- [ ] Calibration drop threshold for retirement specified.
- [ ] Equity-gap widening threshold specified.
- [ ] Override-rate threshold specified.
- [ ] Owner identified for retirement decisions.

## 11. Incident Response

- [ ] Adverse-event log defined.
- [ ] Root-cause analysis procedure within 7 days.
- [ ] User / patient / family notification procedure documented.
- [ ] Public summary procedure (where appropriate) documented.

## 12. Documentation Artefacts

- [ ] Model card completed.
- [ ] Datasheet completed.
- [ ] Data governance policy completed.
- [ ] Informed-consent script completed (if research) or user disclosure (if deployment).
- [ ] This checklist signed and dated by the deployment owner.

---

**Deployment owner:** ____________________________  **Date:** _______________

**Reviewer:** ____________________________________ **Date:** _______________
