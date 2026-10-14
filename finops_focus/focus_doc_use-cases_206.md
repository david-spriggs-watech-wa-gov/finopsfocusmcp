---
title: Reconcile Multi-Currency Settlement using Lineage IDs
url: https://focus.finops.org/docs/use-cases/v1-4/reconcile-multi-currency-settlement-using-lineage-ids/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "42946d3b004ba885"
---
1. Use Cases
2. Invoicing & Chargeback
3. Reconcile Multi-Currency Settlement using Lineage IDs

# Reconcile Multi-Currency Settlement using Lineage IDs

## FOCUS Versions

v1.4

## Context

Demonstrates how to use PaymentCurrencyInvoiceDetailId to reconcile granular records (denominated in the billing currency) against the aggregate records used for payment (denominated in the payment currency). Resolves the ‘Divergent Grain’ problem where billing and payment currencies are represented at different aggregation levels.

## FOCUS SQL Query

```
SELECT
  PaymentCurrencyInvoiceDetailId,
  SUM(BilledCost) AS TotalBilled_BillingCurrency,
  SUM(PaymentCurrencyBilledCost) AS TotalBilled_PaymentCurrency,
  SUM(PaymentCurrencyBilledCost) / NULLIF(SUM(BilledCost), 0) AS EffectiveExchangeRate
FROM InvoiceDetail
WHERE
  InvoiceId = ?
GROUP BY
  PaymentCurrencyInvoiceDetailId
ORDER BY
  PaymentCurrencyInvoiceDetailId
```