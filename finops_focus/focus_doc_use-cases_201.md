---
title: Cash vs. Accrual Comparison by Billing Period
url: https://focus.finops.org/docs/use-cases/v1-4/cash-vs-accrual-comparison-by-billing-period/
hostname: finops.org
sitename: Cash vs. Accrual Comparison by Billing Period
date: "2026-05-01"
fingerprint: "2300157ba4715ee6"
---
1. Use Cases
2. Reporting & Analytics
3. Cash vs. Accrual Comparison by Billing Period

# Cash vs. Accrual Comparison by Billing Period

## FOCUS Versions

v1.4

## Context

Highlights billing periods where the cash-based view (BilledCost) and the accrual-based view (EffectiveCost) diverge – typical of commitment discounts or prepaid purchases where billing timing differs from consumption. Returns periods where the absolute difference exceeds $0.01 to filter out rounding noise.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(EffectiveCost) - SUM(BilledCost) AS CostBasisDifference
FROM focus_data_table
WHERE
  BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd
HAVING
  ABS(SUM(EffectiveCost) - SUM(BilledCost)) > 0.01
```