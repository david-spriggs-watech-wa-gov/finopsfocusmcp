---
title: Report effective cost of compute
url: https://focus.finops.org/docs/use-cases/v1-4/report-effective-cost-of-compute/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: d3d6b3f8a8a5dd85
---
1. Use Cases
2. Planning & Estimating
3. Report effective cost of compute

# Report effective cost of compute

## FOCUS Versions

v1.3
                            v1.4

## Context

Engineers and Engineering Managers want to reduce their billed cost for Compute from a specific service provider. In order to do that, they need to know the current rate of commitment-based discounts (without contracted discounts) per type of commitment. This helps to strategize further purchases.

## FOCUS SQL Query

```
SELECT
  CommitmentDiscountType,
  ServiceProviderName,
  ServiceName,
  SubAccountId,
  SubAccountName,
  BillingPeriodStart,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE BillingPeriodStart  >= ? AND BillingPeriodEnd <= ?
  AND ServiceCategory = 'Compute'
GROUP BY
  CommitmentDiscountType,
  ServiceName,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  BillingPeriodStart
```