---
title: Analyze total cost by allocated resource
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-total-cost-by-allocated-resource/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "22df65f2ae9008a3"
---
1. Use Cases
2. Allocation
3. Analyze total cost by allocated resource

# Analyze total cost by allocated resource

## FOCUS Versions

v1.3
                            v1.4

## Context

Aggregate effective cost by allocated resource ID to understand actual consumption costs for individual workloads or namespaces within shared infrastructure.

## FOCUS SQL Query

```
SELECT
  AllocatedResourceId,
  AllocatedResourceName,
  ResourceId AS OriginResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  COUNT(*) AS ChargeCount
 FROM focus_data_table
 WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
  AND AllocatedResourceId IS NOT NULL
 GROUP BY
  AllocatedResourceId,
  AllocatedResourceName,
  ResourceId
 ORDER BY TotalEffectiveCost DESC
```