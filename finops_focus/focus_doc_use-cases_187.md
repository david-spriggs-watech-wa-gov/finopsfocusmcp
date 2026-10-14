---
title: Identify unused commitments
url: https://focus.finops.org/docs/use-cases/v1-4/identify-unused-commitments-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "33c4c77e89e5208e"
---
1. Use Cases
2. Rate Optimization
3. Identify unused commitments

# Identify unused commitments

## FOCUS Versions

v1.3
                            v1.4

## Context

Identify all data in a time period where CommitmentDiscountStatus is unused, thus identifying commitments that aren’t used and enabling the Practitioner to take action on either selling the commitment (if able), working with other personas on a workload that could use the commitment, or performing informed ignore (knowing it is there but ignoring it because there is nothing one can do).


## FOCUS SQL Query

```
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CommitmentDiscountStatus = 'Unused'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountStatus
```