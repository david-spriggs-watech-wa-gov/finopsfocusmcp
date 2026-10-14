---
title: Analyze marketplace vendors costs
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-marketplace-vendors-costs/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: c3402bfeaf718486
---
1. Use Cases
2. Reporting & Analytics
3. Analyze marketplace vendors costs

# Analyze marketplace vendors costs

## FOCUS Versions

v1.3
                            v1.4

## Context

FinOps Practitioners want to be able to answer the question: How much are we spending each month on vendor products that were purchased via a Cloud Service Provider’s marketplace?

## FOCUS SQL Query

```
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ServiceProviderName,
  HostProviderName,
  InvoiceIssuerName,
  ROUND(SUM(EffectiveCost),2) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND InvoiceIssuerName != ServiceProviderName
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ServiceProviderName,
  HostProviderName,
  InvoiceIssuerName
ORDER BY TotalEffectiveCost ASC
```