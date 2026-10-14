---
title: Report commitment discount purchases
url: https://focus.finops.org/docs/use-cases/v1-4/report-commitment-discount-purchases/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "37115fc3bd59987"
---
1. Use Cases
2. Rate Optimization
3. Report commitment discount purchases

# Report commitment discount purchases

## FOCUS Versions

v1.3
                            v1.4

## Context

Tracking and reconciling commitment-based discount purchases across service providers is a key to success for FinOps.

## FOCUS SQL Query

```
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountUnit,
  CommitmentDiscountQuantity,
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
  AND CommitmentDiscountId IS NOT NULL
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountUnit,
  CommitmentDiscountQuantity,
  ChargeFrequency
```