---
title: Determine Effective Savings Rate
url: https://focus.finops.org/docs/use-cases/v1-4/determine-effective-savings-rate/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "22696b2792de84"
---
1. Use Cases
2. Reporting & Analytics
3. Determine Effective Savings Rate

# Determine Effective Savings Rate

## FOCUS Versions

v1.3
                            v1.4

## Context

The Effective Savings Rate (ESR) is a KPI to track the efficiency of using commitment discounts.

The KPI calculation is (Contracted Cost – Effective Cost) / Contracted Cost.

Outcome: FinOps Practitioners are able to compute the ESR, which is (Contracted Cost – Effective Cost) / Contracted Cost.

## FOCUS SQL Query

```
SELECT
  SUM(ContractedCost) AS ContractedCost,
  SUM(EffectiveCost) AS EffectiveCost,
  (SUM(ContractedCost) - SUM(EffectiveCost)) / NULLIF(SUM(ContractedCost), 0) AS EffectiveSavingsRate
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
```