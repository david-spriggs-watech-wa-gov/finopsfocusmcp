---
title: Identify resources with shared cost allocation
url: https://focus.finops.org/docs/use-cases/v1-4/identify-resources-with-shared-cost-allocation/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "66ca6b7ea9b3202a"
---
1. Use Cases
2. Allocation
3. Identify resources with shared cost allocation

# Identify resources with shared cost allocation

## FOCUS Versions

v1.3
                            v1.4

## Context

Find all resources that have costs split across multiple workloads or consumers, such as shared Kubernetes clusters or multi-tenant databases, to enable accurate chargeback.

## FOCUS SQL Query

```
SELECT
  DISTINCT ResourceId,
  ResourceName,
  AllocatedMethodId
 FROM focus_data_table
 WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
 ORDER BY ResourceId
```