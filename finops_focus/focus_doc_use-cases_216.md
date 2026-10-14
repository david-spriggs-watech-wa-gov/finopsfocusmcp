---
title: Analyze service costs month over month
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-service-costs-month-over-month/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "4308a173b8b221e4"
---
1. Use Cases
2. Reporting & Analytics
3. Analyze service costs month over month

# Analyze service costs month over month

## FOCUS Versions

v1.3
                            v1.4

## Context

Analyzing service-level spending trends over a time period can expose expected and unexpected growth in the consumption of various services across all providers and is a good way for the FinOps team to prioritize usage and rate optimization conversations with product, engineering and finance leaders within the organization.

## FOCUS SQL Query

```
SELECT
  MONTH(ChargePeriodStart),
  ServiceProviderName,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodStart < ?
GROUP BY 
  MONTH(ChargePeriodStart), 
  ServiceProviderName,
  ServiceName
ORDER BY
  MONTH(ChargePeriodStart),
  SUM(EffectiveCost) DESC
```