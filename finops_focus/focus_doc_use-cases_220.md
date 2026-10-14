---
title: Discount Effectiveness by Service
url: https://focus.finops.org/docs/use-cases/v1-4/discount-effectiveness-by-service/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "204657e6ce14e43"
---
1. Use Cases
2. Rate Optimization
3. Discount Effectiveness by Service

# Discount Effectiveness by Service

## FOCUS Versions

v1.4

## Context

Compares ListCost, ContractedCost, EffectiveCost, and BilledCost per service to quantify negotiated and effective discounts. The CASE expression zeroes out ContractedCost and ListCost on Usage rows where BilledCost=0 and EffectiveCost!=0 (typical of commitment-covered usage rows whose ContractedCost/ListCost are already reflected in a separate Purchase row), avoiding double-counting.

## FOCUS SQL Query

```
WITH AggregatedData AS (
  SELECT
    ServiceProviderName,
    BillingAccountId,
    BillingAccountName,
    BillingCurrency,
    ServiceName,
    SUM(EffectiveCost) AS TotalEffectiveCost,
    SUM(BilledCost) AS TotalBilledCost,
    SUM(
      CASE
        WHEN ChargeCategory = 'Usage' AND BilledCost = 0 AND EffectiveCost <> 0
        THEN 0
        ELSE ContractedCost
      END
    ) AS TotalContractedCost,
    SUM(
      CASE
        WHEN ChargeCategory = 'Usage' AND BilledCost = 0 AND EffectiveCost <> 0
        THEN 0
        ELSE ListCost
      END
    ) AS TotalListCost
  FROM focus_data_table
  WHERE
    BillingPeriodStart >= ? AND BillingPeriodEnd < ? AND ChargeClass IS NULL
  GROUP BY
    ServiceProviderName,
    BillingAccountId,
    BillingAccountName,
    BillingCurrency,
    ServiceName
)
SELECT
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName,
  TotalEffectiveCost,
  TotalBilledCost,
  TotalListCost,
  (1 - TotalContractedCost / NULLIF(TotalListCost, 0)) * 100 AS ContractedDiscount,
  (1 - TotalEffectiveCost / NULLIF(TotalListCost, 0)) * 100 AS EffectiveDiscount
FROM AggregatedData
```