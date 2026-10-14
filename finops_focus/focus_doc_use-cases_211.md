---
title: Analyze cost by participating entities
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-cost-by-participating-entities/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: d588413cb7814d87
---
1. Use Cases
2. Allocation
3. Analyze cost by participating entities

# Analyze cost by participating entities

## FOCUS Versions

v1.3
                            v1.4

## Context

Break down costs by service provider, invoice issuer, and host provider to understand the complete value chain and identify reseller margins or marketplace fees.

## FOCUS SQL Query

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
 WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
 GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  InvoiceIssuerName,
  HostProviderName,
  ServiceName,
  BillingCurrency
 ORDER BY TotalBilledCost DESC
```