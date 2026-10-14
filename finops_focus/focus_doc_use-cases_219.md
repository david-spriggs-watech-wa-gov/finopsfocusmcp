---
title: Report corrections by subaccount for a previously invoiced billing period
url: https://focus.finops.org/docs/use-cases/v1-4/report-corrections-by-subaccount-for-a-previously-invoiced-billing-period/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: f095bd7acee8dc86
---
1. Use Cases
2. Allocation
3. Report corrections by subaccount for a previously invoiced billing period

# Report corrections by subaccount for a previously invoiced billing period

## FOCUS Versions

v1.3
                            v1.4

## Context

Large organizations often re-allocate prior-period corrections down to individual projects, subscriptions, or resource groups. This allows each team to see the historical adjustments that affect its spend.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  ServiceCategory,
  SubAccountId,
  SubAccountName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass = 'Correction'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  SubAccountId,
  SubAccountName,
  ServiceCategory
```