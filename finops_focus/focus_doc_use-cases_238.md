---
title: Analyze service costs by region
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-service-costs-by-region-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "710e574fdf2a086"
---
1. Use Cases
2. Anomaly Management
3. Analyze service costs by region

# Analyze service costs by region

## FOCUS Versions

v1.3
                            v1.4

## Context

Analyzing Service level spending trends over a time period can expose expected and unexpected growth in the consumption of various services, by region, across all service providers and is a good way for the FinOps team to prioritize usage and rate optimization conversations with product, engineering and finance leaders within the organization.

## FOCUS SQL Query

```
SELECT
  ChargePeriodStart,
  ServiceProviderName,
  RegionId,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  ChargePeriodStart,
  ServiceProviderName,
  RegionId,
  ServiceName
ORDER BY ChargePeriodStart,
  SUM(EffectiveCost) DESC
```