---
title: Analyze costs by service name
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-costs-by-service-name/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "798e5b4af368da7"
---
1. Use Cases
2. Anomaly Management
3. Analyze costs by service name

# Analyze costs by service name

## FOCUS Versions

v1.3
                            v1.4

## Context

Analyzing service-level spending trends over a time period can expose expected and unexpected growth in the consumption of a service, and is a good way for the FinOps team to prioritize usage and rate optimization conversations with product, engineering, and finance leaders within the organization.

## FOCUS SQL Query

```
SELECT
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName
```