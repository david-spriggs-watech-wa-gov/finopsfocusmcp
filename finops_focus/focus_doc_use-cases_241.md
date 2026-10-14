---
title: Forecast cashflow month over month based on historical trends by service
url: https://focus.finops.org/docs/use-cases/v1-4/forecast-cashflow-month-over-month-based-on-historical-trends-by-service-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "23ce959b92732e4"
---
1. Use Cases
2. Forecasting
3. Forecast cashflow month over month based on historical trends by service

# Forecast cashflow month over month based on historical trends by service

## FOCUS Versions

v1.3
                            v1.4

## Context

Finance needs to perform month over month forecasting of cashflow by extrapolating from historical cash costs. Having this data enables Finance to create cashflow cost models.

## FOCUS SQL Query

```
SELECT
  MONTH(BillingPeriodStart),
  ServiceProviderName,
  ServiceCategory,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  MONTH(BillingPeriodStart),
  ServiceProviderName,
  ServiceCategory,
  ServiceName
```