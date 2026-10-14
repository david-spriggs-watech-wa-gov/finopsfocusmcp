---
title: Track contract commitment burn-down over time
url: https://focus.finops.org/docs/use-cases/v1-4/track-contract-commitment-burn-down-over-time/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "2642c0fd6f940c97"
---
1. Use Cases
2. Budgeting
3. Track contract commitment burn-down over time

# Track contract commitment burn-down over time

## FOCUS Versions

v1.3
                            v1.4

## Context

Monitor the consumption of contract commitments across billing periods to track progress toward fulfilling contractual obligations and identify potential under-utilization risks.

## FOCUS SQL Query

```
SELECT
  CU.BillingPeriodStart,
  CU.ServiceProviderName,
  CU.BillingAccountId,
  JSON_VALUE(CA, '$.ContractCommitmentID') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS AppliedCost,
  SUM(CU.EffectiveCost) AS TotalEffectiveCost
 FROM focus_data_table CU
 CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
 WHERE JSON_VALUE(CA, '$.ContractCommitmentID') IS NOT NULL
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
 GROUP BY
  CU.BillingPeriodStart,
  CU.ServiceProviderName,
  CU.BillingAccountId,
  JSON_VALUE(CA, '$.ContractCommitmentID')
 ORDER BY BillingPeriodStart, ContractCommitmentId
```