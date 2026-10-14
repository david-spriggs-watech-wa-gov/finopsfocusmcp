---
title: Report corrections for a previously invoiced billing period
url: https://focus.finops.org/docs/use-cases/v1-4/report-corrections-for-a-previously-invoiced-billing-period/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: d2b1bd72d8e8dc8f
---
1. Use Cases
2. Reporting & Analytics
3. Report corrections for a previously invoiced billing period

# Report corrections for a previously invoiced billing period

## FOCUS Versions

v1.3
                            v1.4

## Context

When service providers issue corrections that adjust historical invoices, practitioners must reconcile those adjustments against prior records.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  ChargeCategory,
  ServiceCategory,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass = 'Correction'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  ChargeCategory,
  ServiceCategory,
  ServiceName
```