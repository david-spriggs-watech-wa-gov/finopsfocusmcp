---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/marketplace-purchases/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2300777c2b51b98e"
---
# 2.16 Marketplace Purchases

Since:
                    1.0

## 2.16.1 Description

FOCUS supports the analysis of cost and usage data for marketplace purchases and their associated costs. It also supports the reporting of EffectiveCost for usage from the service provider.

## 2.16.2 Directly Dependent Columns

## 2.16.3 Supporting Columns

## 2.16.4 Example SQL Query on a CSP Marketplace Using the Cost and Usage FOCUS Dataset

### Example SQL Query on a CSP Marketplace Using the Cost and Usage FOCUS Dataset

```
SELECT
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ServiceProviderName = '<Example SaaS Provider>'
  AND InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd
```
## 2.16.5 Example SQL Query on a Provider Using the Cost and Usage FOCUS Dataset

### Example SQL Query on a Provider Using the Cost and Usage FOCUS Dataset

```
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
```