---
title: Update budgets with billed costs
url: https://focus.finops.org/docs/use-cases/v1-4/update-budgets-with-billed-costs/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "135ac15a0bb78dc6"
---
1. Use Cases
2. Budgeting
3. Update budgets with billed costs

# Update budgets with billed costs

## FOCUS Versions

v1.3
                            v1.4

## Context

Finance manages tracking of budgets and must update long-term budgets with the actual costs billed each month so the budget is not exceeded.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd
```