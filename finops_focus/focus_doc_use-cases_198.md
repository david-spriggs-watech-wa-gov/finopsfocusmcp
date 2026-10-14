---
title: Analyze the different metered costs for a particular SKU
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-the-different-metered-costs-for-a-particular-sku-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: c7500176abb4a08c
---
1. Use Cases
2. Reporting & Analytics
3. Analyze the different metered costs for a particular SKU

# Analyze the different metered costs for a particular SKU

## FOCUS Versions

v1.3
                            v1.4

## Context

Understanding the individual metered costs of a particular SKU can help assist FinOps practitioners understand the cost breakdown of usage of a select resource. Especially in cases where a SKU has a few component charges like (Usage hours, Throughput, API requests, etc)

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  ChargePeriodStart,
  ChargePeriodEnd,
  SkuId,
  SkuPriceId,
  PricingUnit,
  ListUnitPrice,
  SUM(PricingQuantity) AS TotalPricingQuantity,
  SUM(ListCost) AS TotalListCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  ServiceProviderName,
  ChargePeriodStart,
  ChargePeriodEnd,
  SkuId,
  SkuPriceId,
  PricingUnit,
  ListUnitPrice
ORDER BY
  ChargePeriodStart ASC
LIMIT 100
```