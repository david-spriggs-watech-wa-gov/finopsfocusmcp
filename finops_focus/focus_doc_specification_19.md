---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/verification-comparison-and-fluctuation-tracking-of-unit-prices/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e4c0e5ffa3b0e11c
---
# 2.23 Verification, Comparison, and Fluctuation Tracking of Unit Prices

Since:
                    1.0

## 2.23.1 Description

When a service provider supports unit pricing concepts, FOCUS allows practitioners to:

- Verify that the correct List Unit Prices and Contracted Unit Prices are applied.
- Compare applied Contracted Unit Prices across different billing accounts and with applied List Unit Prices at specific points in time.
- Track fluctuations in unit prices over time.

## 2.23.2 Directly Dependent Columns

## 2.23.3 Supporting Columns

## 2.23.4 Example SQL Query

### Example SQL Query

```
SELECT DISTINCT
  SkuId,
  SkuPriceId,
  SkuPriceDetails,
  BillingPeriodId,
  ChargePeriodStart,
  ChargePeriodEnd,
  BillingCurrency,
  ListUnitPrice,
  ContractedUnitPrice
FROM focus_data_table
WHERE
  SkuPriceId = ?
  AND ChargePeriodStart >= ?
  AND ChargePeriodEnd < ?
```