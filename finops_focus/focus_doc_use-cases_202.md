---
title: Get historical usage and rates to enable cost forecasting
url: https://focus.finops.org/docs/use-cases/v1-4/get-historical-usage-and-rates-to-enable-cost-forecasting/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "138cf3562ba1afce"
---
1. Use Cases
2. Forecasting
3. Get historical usage and rates to enable cost forecasting

# Get historical usage and rates to enable cost forecasting

## FOCUS Versions

v1.3
                            v1.4

## Context

While Finance will look at higher-level forecasting data such as amortized costs and total cashflow, a FinOps Practitioner needs to forecast costs from quantities of priced units and effective costs based on historical rates. Effective costs are used to account for the costs of commitment purchases.

This query extracts cost and usage data by Region and Service. More fine-grain extrapolation could be done based on further dimensions like Tags.

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
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd <= ?
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