---
title: Report application cost month over month
url: https://focus.finops.org/docs/use-cases/v1-4/application-cost/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "434fa079e8b735ac"
---
1. Use Cases
2. Reporting & Analytics
3. Report application cost month over month

# Report application cost month over month

## FOCUS Versions

v1.0
                            v1.1
                            v1.2
                            v1.3
                            v1.4

## Context

As an application owner or engineering team I want to track the month over month costs of my application.

## FOCUS SQL Query

```
SELECT
  MONTH(BillingPeriodStart),
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE Tags["Application"] = ?
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
GROUP BY
  MONTH(BillingPeriodStart),
  ServiceName
```