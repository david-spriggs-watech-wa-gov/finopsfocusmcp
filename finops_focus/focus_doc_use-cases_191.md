---
title: Report on initial contract commitments
url: https://focus.finops.org/docs/use-cases/v1-4/report-on-initial-contract-commitments/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "42c281ecdba2bcb4"
---
1. Use Cases
2. Reporting & Analytics
3. Report on initial contract commitments

# Report on initial contract commitments

## FOCUS Versions

v1.3
                            v1.4

## Context

Aggregate initial contract commitment purchases to understand total contracted spend and usage commitments by service provider and commitment ID over a specified time range.

## FOCUS SQL Query

```
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentID') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
 FROM focus_data_table CU
 CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
 WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
 GROUP BY
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentID')
```
## FOCUS Datasets

## FOCUS Columns

## Related Capabilities

## Related Personas

## Related KPIs

Forecast Accuracy Rate (Spend)
                                            This metric compares forecasted vs. actual cloud spend over a specific period (e.g., day, month, quarter).

Forecast Accuracy Rate (Usage)
                                            Compares forecasted vs. actual cloud usage (vCPUs, Memory, etc) over a specific period (e.g., day, month, quarter).