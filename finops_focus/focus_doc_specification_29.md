---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/data-generator-calculated-split-cost-allocation/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2b8abf7e2abbe88c"
---
# 2.10 Data Generator-Calculated Split Cost Allocation

Since:
                    1.3

## 2.10.1 Description

FOCUS enables tracking of resources split by some internal consumption metrics. This is most common for resources supporting shared usage like compute nodes in a shared cluster (Kubernetes, databases) or storage engines that can share capacity between workloads.

## 2.10.2 Directly Dependent Columns

## 2.10.3 Supporting Columns

## 2.10.4 Example SQL Query (Find Resources with a Shared Cost)

### Example SQL Query (Find Resources with a Shared Cost)

```
SELECT
  DISTINCT ResourceId
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
```
## 2.10.5 Example SQL Query (Get Total Effective Cost by ResourceId (Ignore Shared Cost))

### Example SQL Query (Get Total Effective Cost by ResourceId (Ignore Shared Cost))

```
SELECT
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
GROUP BY
  ResourceId
```
## 2.10.6 Example SQL Query (Get Total Effective Cost by AllocatedResourceId)

### Example SQL Query (Get Total Effective Cost by AllocatedResourceId)

```
SELECT
  AllocatedResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
GROUP BY
  AllocatedResourceId
```
## 2.10.7 Example SQL Query (Find Total Unallocated Split Costs by ResourceId)

### Example SQL Query (Find Total Unallocated Split Costs by ResourceId)

```
SELECT
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL AND AllocatedResourceId IS NULL
GROUP BY
  ResourceId
```
## 2.10.8 Example SQL Query (Find How a Single Resource Has Been Split)

### Example SQL Query (Find How a Single Resource Has Been Split)

```
SELECT
  ResourceId,
  COALESCE(AllocatedResourceId, 'Unallocated') AS AllocatedResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedResourceId = ?
GROUP BY
  ResourceId,
  COALESCE(AllocatedResourceId, 'Unallocated')
```
## 2.10.9 Example SQL Query (Extract JSON from AllocatedMethodDetails)

### Example SQL Query (Extract JSON from AllocatedMethodDetails)

```
SELECT
  resource_id,
  elements.allocated_ratio,
  elements.usage_unit,
  elements.usage_quantity
FROM
  focus_data_table,
  JSON_TABLE(
    AllocatedMethodDetails,
    '$.Elements[*]' COLUMNS (
      allocated_ratio DECIMAL(10, 2) PATH '$.AllocatedRatio',
      usage_unit VARCHAR(50) PATH '$.UsageUnit',
      usage_quantity DECIMAL(10, 2) PATH '$.UsageQuantity'
    )
  ) AS elements
```