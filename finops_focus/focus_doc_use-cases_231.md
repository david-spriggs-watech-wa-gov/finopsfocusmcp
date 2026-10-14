---
title: Join contract commitment details with usage charges
url: https://focus.finops.org/docs/use-cases/v1-4/join-contract-commitment-details-with-usage-charges/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "2e4a30f44ea2c49d"
---
1. Use Cases
2. Planning & Estimating
3. Join contract commitment details with usage charges

# Join contract commitment details with usage charges

## FOCUS Versions

v1.3
                            v1.4

## Context

Combine cost and usage data with contract commitment metadata to analyze commitment terms, categories, and periods alongside actual consumption patterns.

## FOCUS SQL Query

```
SELECT
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentID') AS ContractCommitmentId,
  CC.ContractCommitmentCategory,
  CC.ContractCommitmentPeriodStart,
  CC.ContractCommitmentPeriodEnd,
  CC.ContractCommitmentCost,
  SUM(CU.EffectiveCost) AS TotalUsageCost,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS AppliedCost
 FROM focus_data_table CU
 CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
 JOIN contract_commitment CC
  ON JSON_VALUE(CA, '$.ContractCommitmentID') = CC.ContractCommitmentId
 WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
 GROUP BY
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentID'),
  CC.ContractCommitmentCategory,
  CC.ContractCommitmentPeriodStart,
  CC.ContractCommitmentPeriodEnd,
  CC.ContractCommitmentCost
```