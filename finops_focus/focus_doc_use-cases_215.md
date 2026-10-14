---
title: Forecast amortized costs month over month based on historical trends
url: https://focus.finops.org/docs/use-cases/v1-4/forecast-amortized-costs-month-over-month-based-on-historical-trends-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "437ce95baba337e4"
---
1. Use Cases
2. Forecasting
3. Forecast amortized costs month over month based on historical trends

# Forecast amortized costs month over month based on historical trends

## FOCUS Versions

v1.3
                            v1.4

## Context

Finance needs to perform month over month forecasting by extrapolating amortized costs based on historical rates. Having this data enables Finance to create amortized cost models.


## FOCUS SQL Query

```
SELECT
  MONTH(BillingPeriodStart),
  ServiceProviderName,
  ServiceCategory,
  ServiceName,
  ChargeCategory,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE BillingPeriodStart >= ?  AND BillingPeriodEnd < ?
GROUP BY
  MONTH(BillingPeriodStart),
  ServiceProviderName,
  ServiceCategory,
  ServiceName,
  ChargeCategory
```