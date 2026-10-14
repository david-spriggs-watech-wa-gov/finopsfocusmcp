---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/participating-entity-identification/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e388677d3f53dca6
---
# 2.17 Participating Entity Identification

Since:
                    1.1

Updated:
                    1.3

## 2.17.1 Description

FOCUS allows practitioners to identify the several participating entities involved in resource or service hosting, invoicing, and data generation. The FOCUS Specification includes multiple columns to identify key participating entities, including Service Provider Name, Invoice Issuer Name, Host Provider Name, and Data Generator.

## 2.17.2 Directly Dependent Columns

## 2.17.3 Applicable Metadata

- DataGenerator

## 2.17.4 Example SQL Query

### Example SQL Query

```
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  InvoiceIssuerName,
  HostProviderName,
  ServiceName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? and BillingPeriodEnd < ?
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  InvoiceIssuerName,
  HostProviderName,
  ServiceName,
  BillingCurrency
```