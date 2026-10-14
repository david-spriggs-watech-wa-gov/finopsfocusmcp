---
title: Allocate multi-currency charges per application
url: https://focus.finops.org/docs/use-cases/v1-4/allocate-multi-currency-charges-per-application-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: b554071eebf1ce87
---
1. Use Cases
2. Allocation
3. Allocate multi-currency charges per application

# Allocate multi-currency charges per application

## FOCUS Versions

v1.3
                            v1.4

## Context

Finance needs to allocate costs and perform chargeback for charges for all applications that come from different geographic locations and are in different currencies.


## FOCUS SQL Query

```
SELECT 
  Tags["ApplicationId"],
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE
  BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  Tags["ApplicationId"],
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency
```