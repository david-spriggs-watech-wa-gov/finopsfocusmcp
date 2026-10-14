---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/cost-and-usage-attribution/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: bacccd6d21919dec
---
# 2.7 Cost and Usage Attribution

Since:
                    1.0

## 2.7.1 Description

Many service providers have features that allow FinOps practitioners to enrich cost and usage data with metadata that is in addition to service provider defined data, in order to analyze FinOps data using organizational, deployment, or other structures. These features may take the form of directly applied metadata or inherited metadata. FOCUS facilitates the inclusion of this metadata at a row level.

## 2.7.2 Directly Dependent Columns

## 2.7.3 Supporting Columns

## 2.7.4 Example SQL Query

### Example SQL Query

```
SELECT
  tags,
  ConsumedUnit,
  SUM(BilledCost),
  SUM(EffectiveCost),
  SUM(ConsumedQuantity)
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  tags,
  ConsumedUnit
```