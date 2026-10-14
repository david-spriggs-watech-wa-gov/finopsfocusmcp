---
title: Determine Effective Savings Rate by Service
url: https://focus.finops.org/docs/use-cases/v1-4/determine-effective-savings-rate-by-service/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "26e16ae140de84"
---
1. Use Cases
2. Reporting & Analytics
3. Determine Effective Savings Rate by Service

# Determine Effective Savings Rate by Service

## FOCUS Versions

v1.3
                            v1.4

## Context

This use cases focuses on Effective Savings Rate (ESR) per Service.

The Effective Savings Rate is a KPI to track the efficiency of using commitment-based discounts. The KPI calculation is (Contracted Cost – Effective Cost) / Contracted Cost)

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  ServiceName,
  SUM(ContractedCost) AS ContractedCost,
  SUM(EffectiveCost)  AS EffectiveCost,
  (SUM(ContractedCost) - SUM(EffectiveCost)) / NULLIF(SUM(ContractedCost), 0) AS EffectiveSavingsRate
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
GROUP BY ServiceProviderName, ServiceName
```