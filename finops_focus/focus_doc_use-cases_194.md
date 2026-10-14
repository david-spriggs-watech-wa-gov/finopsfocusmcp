---
title: Verify accuracy of service provider invoices
url: https://focus.finops.org/docs/use-cases/v1-4/verify-accuracy-of-service-provider-invoices/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "95c465dfa1118085"
---
1. Use Cases
2. Data Ingestion
3. Verify accuracy of service provider invoices

# Verify accuracy of service provider invoices

## FOCUS Versions

v1.3
                            v1.4

## Context

In order to verify that the charges found in the FOCUS dataset match those of the service providers’ invoices a FinOps Practitioner can aggregate cost data from service providers for a billing period and compare it to invoices.


## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency
```