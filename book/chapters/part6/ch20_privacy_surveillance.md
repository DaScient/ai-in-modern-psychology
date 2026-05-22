# Chapter 20: Privacy and Surveillance

## Learning Objectives

By the end of this chapter, you should be able to:

- Understand the key concepts introduced in *Privacy and Surveillance*.
- Connect chapter content to computational implementations in `/code` and `/notebooks`.
- Identify ethical considerations relevant to this topic.

## Overview

Data minimization, re-identification risk, and consent in psychological AI.

## 20.1 Re-identification Risk

Even 'de-identified' data sets can often be re-identified via auxiliary information. k-anonymity, l-diversity, and differential privacy provide formal guarantees.

## 20.2 Data Minimization

Collect only what is necessary, retain only as long as needed — see the [data governance policy](../../../ethics_toolkit/data_governance_policy.md).

## 20.3 Surveillance Creep

Tools deployed for one purpose tend to be repurposed for others. Sunset clauses and use-binding mitigate creep.

## 20.4 Differential Privacy

Adds calibrated noise to query results; trade-off between utility and privacy is explicit.

```{note}
This chapter is part of *AI in Modern Psychology* (DaScient Press, 2026). The book is a living document — improvements via pull request are welcome.
```

## Discussion Questions

1. What aspects of privacy and surveillance are most relevant to your own area of psychology?
2. Which ethical considerations from Part VI apply most directly here?
3. What would you need to validate before deploying a system based on this chapter?

## Further Reading

- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy.
