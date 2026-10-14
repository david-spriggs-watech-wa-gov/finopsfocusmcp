---
title: Identify anomalous daily spending by subaccount and region
url: https://focus.finops.org/docs/use-cases/v1-4/identify-anomalous-daily-spending-by-subaccount-and-region/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: b405e776df5398a4
---
1. Use Cases
2. Anomaly Management
3. Identify anomalous daily spending by subaccount and region

# Identify anomalous daily spending by subaccount and region

## FOCUS Versions

v1.3
                            v1.4

## Context

It is important for FinOps Practitioners to track daily spend from various angles to ensure any anomalous cost trends are easily detected. Tracking by region enables further granularity in understanding the source of anomalous spend. Purchases can often cause false positives, for this reason, we want to monitor cost trends with up-front payments amortized. Graphing the data by day in a multiline chart can often help find the outliers.

## FOCUS SQL Query

```
SELECT
  DATE(ChargePeriodStart) AS Day,
  ServiceProviderName,
  SubAccountId,
  RegionId,
  RegionName,
  SUM(EffectiveCost) AS DailyEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  DATE(ChargePeriodStart) AS StartDay,
  ServiceProviderName,
  SubAccountId,
  RegionId,
  RegionName
```