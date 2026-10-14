---
title: Verify accuracy of services charges across service providers
url: https://focus.finops.org/docs/use-cases/v1-4/verify-accuracy-of-services-charges-across-service-providers/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "37ace1ddfd400487"
---
1. Use Cases
2. Data Ingestion
3. Verify accuracy of services charges across service providers

# Verify accuracy of services charges across service providers

## FOCUS Versions

v1.3
                            v1.4

## Context

In order to verify that the charges found in the FOCUS dataset match those of the service providers’ invoices a FinOps Practitioner can aggregate cost data from service providers per service for a billing period and compare it to individual service charges found inside invoices.


## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingAccountName,
  BillingAccountId,
  BillingCurrency,
  ServiceName
```