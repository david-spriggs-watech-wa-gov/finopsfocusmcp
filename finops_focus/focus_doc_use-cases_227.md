---
title: Track marketplace purchases across providers
url: https://focus.finops.org/docs/use-cases/v1-4/track-marketplace-purchases-across-providers/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "42116174e5c48cc6"
---
1. Use Cases
2. Allocation
3. Track marketplace purchases across providers

# Track marketplace purchases across providers

## FOCUS Versions

v1.3
                            v1.4

## Context

Identify marketplace purchases where the service provider differs from the host provider to track third-party software spending and optimize vendor relationships.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  HostProviderName,
  InvoiceIssuerName,
  ServiceName,
  ChargeCategory,
  SUM(BilledCost) AS TotalBilledCost,
  COUNT(DISTINCT ResourceId) AS ResourceCount
 FROM focus_data_table
 WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ServiceProviderName != HostProviderName
  AND ChargeCategory IN ('Purchase', 'Usage')
 GROUP BY
  ServiceProviderName,
  HostProviderName,
  InvoiceIssuerName,
  ServiceName,
  ChargeCategory
 ORDER BY TotalBilledCost DESC
```