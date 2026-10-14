---
title: Analyze costs of components of a resource
url: https://focus.finops.org/docs/use-cases/v1-4/resource-component-costs/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "65445722f862382"
---
1. Use Cases
2. Usage Optimization
3. Analyze costs of components of a resource

# Analyze costs of components of a resource

## FOCUS Versions

v1.0
                            v1.1
                            v1.2
                            v1.3
                            v1.4

## Context

Using FOCUS data, an Engineer can deep dive on cost details for a single resource.

## FOCUS SQL Query

```
SELECT ResourceId,
  ResourceName,
  ResourceType,
  ChargeDescription,
  SkuId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ?  AND ChargePeriodEnd < ?
  AND ResourceId=?
GROUP BY ResourceId,
  ResourceName,
  ResourceType, 
  ChargeDescription,
  SkuId
```