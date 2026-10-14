---
title: Effective Cost by Service and Region
url: https://focus.finops.org/docs/use-cases/v1-4/effective-cost-by-service-and-region/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "6637aaa38fda6"
---
1. Use Cases
2. Reporting & Analytics
3. Effective Cost by Service and Region

# Effective Cost by Service and Region

## FOCUS Versions

v1.4

## Context

Aggregates EffectiveCost by billing period to align accrual-based cost reporting with invoice cycles.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(PricingQuantity) AS TotalPricingQuantity
FROM focus_data_table
WHERE
  BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit
```