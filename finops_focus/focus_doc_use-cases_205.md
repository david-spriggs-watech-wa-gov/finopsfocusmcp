---
title: Identify anomalous daily spending by subaccount
url: https://focus.finops.org/docs/use-cases/v1-4/identify-anomalous-daily-spending-by-subaccount/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: b401e77e8f53d8a5
---
1. Use Cases
2. Anomaly Management
3. Identify anomalous daily spending by subaccount

# Identify anomalous daily spending by subaccount

## FOCUS Versions

v1.3
                            v1.4

## Context

It is important for FinOps Practitioners to track daily spend from various angles to ensure any anomalous cost trends are easily detected. Purchases can often cause false positives, for this reason, we want to monitor cost trends with up-front payments amortized. Graphing the data by day in a multiline chart can often help find the outliers.

## FOCUS SQL Query

```
SELECT
  DATE(ChargePeriodStart) AS Day,
  ServiceProviderName,
  SubAccountId,
  SUM(EffectiveCost) AS DailyEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  DATE(ChargePeriodStart) AS StartDay,
  ServiceProviderName,
  SubAccountId
```