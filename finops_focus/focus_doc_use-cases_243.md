---
title: Commitment Discount Effective Cost Breakdown
url: https://focus.finops.org/docs/use-cases/v1-4/commitment-discount-effective-cost-breakdown/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "434133fe2bf5a287"
---
1. Use Cases
2. Rate Optimization
3. Commitment Discount Effective Cost Breakdown

# Commitment Discount Effective Cost Breakdown

## FOCUS Versions

v1.4

## Context

Analyzes commitment discount amortization by charge period, capturing costs based on when resources were consumed. Filters to Usage charges with CommitmentDiscountId populated and groups by CommitmentDiscountId and CommitmentDiscountStatus to separate Used vs. Unused amortization.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE
  ChargePeriodStart >= ?
  AND ChargePeriodEnd < ?
  AND NOT CommitmentDiscountId IS NULL
  AND ChargeCategory = 'Usage'
GROUP BY
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd
```