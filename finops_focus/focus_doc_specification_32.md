---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/contract-commitments/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "426392ec3b8688a5"
---
# 2.6 Contract Commitments

## 2.6.1 Description

FOCUS supports the tracking of commitments made via contractual agreements between a service provider and a customer. Each row in the Cost and Usage dataset is associated with one or more unique identifiers representing those contracts and contract commitments, stored in a JSON column called Contract Applied. A richer amount of detail that describes those commitments is carried in a separate Contract Commitment dataset, which can be joined to the Cost and Usage dataset to facilitate various queries involving filtering and aggregation.

The Contract Applied column contains several FOCUS-defined properties. For more information, see the definition of Contract Applied here.

## 2.6.2 Directly Dependent Columns

## 2.6.3 Supporting Columns

## 2.6.4 Example SQL Queries

The FOCUS specification implements the application of contract commitments to cost and usage via the *ContractApplied* column, which is defined in *JSON object format*.

Because ANSI SQL does not inherently support the parsing of JSON, the following queries leverage the JSON functions found in BigQuery Standard SQL in order to demonstrate this feature's functionality. Similar JSON functions are available in all major SQL engines; thus, the below examples can be slightly modified to accommodate any particular database instance.

### 2.6.4.1 Report on Initial Contract Commitment

This query takes inputs of a time range via ChargePeriodStart and ChargePeriodEnd, then presents the aggregation of initial contract commitments from the CostAndUsage dataset per ServiceProviderName and ContractCommitmentId by filtering on the specified time range, along with ChargeCategory of `Purchase`.

```
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
GROUP BY ServiceProviderName, ContractCommitmentId
ORDER BY ServiceProviderName, ContractCommitmentId
```
### 2.6.4.2 Report on Usage Against Contract Commitment

This query takes inputs of a time range via ChargePeriodStart and ChargePeriodEnd, then presents the aggregation of the application of contract commitments from the CostAndUsage dataset per ServiceProviderName and ContractCommitmentId by filtering on the specified time range, along with ChargeCategory of `Usage`.

```
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
GROUP BY ServiceProviderName, ContractCommitmentId
ORDER BY ServiceProviderName, ContractCommitmentId
```
### 2.6.4.3 Report on Usage Against Contract Commitment by Category

This query takes inputs of a time range via ChargePeriodStart and ChargePeriodEnd, then presents the aggregation of the application of contract commitments from the CostAndUsage dataset per ServiceProviderName and ContractCommitmentId by filtering on the specified time range, along with ChargeCategory of `Usage`. It also joins in the ContractCommitment dataset to provide further information about each contract commitment (in this case, the start and end date/time).

```
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  CC.ContractCommitmentPeriodStart,
  CC.ContractCommitmentPeriodEnd,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
INNER JOIN
  ContractCommitment CC
ON
  JSON_VALUE(CA, '$.ContractCommitmentId') = CC.ContractCommitmentId
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
GROUP BY ServiceProviderName, ContractCommitmentId, ContractCommitmentPeriodStart, ContractCommitmentPeriodEnd
ORDER BY ServiceProviderName, ContractCommitmentId, ContractCommitmentPeriodStart, ContractCommitmentPeriodEnd
```