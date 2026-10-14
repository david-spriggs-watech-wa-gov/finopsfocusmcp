---
title: Compare resource usage month over month
url: https://focus.finops.org/docs/use-cases/v1-4/compare-resource-usage-month-over-month-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "424da479aca33fa4"
---
1. Use Cases
2. Anomaly Management
3. Compare resource usage month over month

# Compare resource usage month over month

## FOCUS Versions

v1.3
                            v1.4

## Context

FinOps Practitioners can compare usage and costs across charge periods to identify changes in usage month over month.

## FOCUS SQL Query

```
SELECT 
  MONTH(ChargePeriodStart),
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit,
  SUM(ConsumedQuantity) AS TotalConsumedQuantity
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  MONTH(ChargePeriodStart),
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit
```