---
title: Verify discount accuracy for a previously invoiced billing period (corrections excluded)
url: https://focus.finops.org/docs/use-cases/v1-4/verify-discount-accuracy-for-a-previously-invoiced-billing-period-corrections-excluded/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: cccc057a59410c8d
---
1. Use Cases
2. Data Ingestion
3. Verify discount accuracy for a previously invoiced billing period (corrections excluded)

# Verify discount accuracy for a previously invoiced billing period (corrections excluded)

## FOCUS Versions

v1.3
                            v1.4

## Context

FinOps Practitioners need to confirm that negotiated, live, and commitment-based discounts were correctly applied to charges in a closed billing period.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(ListCost) AS TotalListCost,
  SUM(BilledCost) AS TotalBilledCost,
  ((SUM(ListCost) - SUM(EffectiveCost)) / NULLIF(SUM(ListCost), 0)) * 100 AS EffectiveDiscount
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass != 'Correction'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName
```