---
title: Update budgets for each application
url: https://focus.finops.org/docs/use-cases/v1-4/update-budgets-for-each-application/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "525a93da0bf72cb4"
---
1. Use Cases
2. Budgeting
3. Update budgets for each application

# Update budgets for each application

## FOCUS Versions

v1.3
                            v1.4

## Context

Finance manages tracking of budgets and must update application budgets with the actual costs billed each month so the budget is not exceeded.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  Tags["Application"] AS Application,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  Tags["Application"]
```