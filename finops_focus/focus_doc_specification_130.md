---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/invoice-reconciliation/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2eb0e9d33828a8d5"
---
# 2.14 Invoice Reconciliation

## 2.14.1 Description

FOCUS supports the reconciliation of granular cloud consumption records with the formal financial documents issued by an *invoice issuer*. The Invoice Detail dataset represents the definitive financial record of *charges* as they appear on an invoice. By leveraging common identifiers, practitioners can map usage-based costs in the Cost and Usage dataset back to their corresponding line items in the Invoice Detail dataset.

This feature also supports reconciliation across divergent currency grains. When an invoice issuer represents billing and payment currencies at different aggregation levels, the `PaymentCurrencyInvoiceDetailId` provides the necessary lineage to link granular usage records to the aggregate records used for financial settlement.

## 2.14.2 Directly Dependent Columns

## 2.14.3 Supporting Columns

## 2.14.4 Example SQL Queries

Reconciliation often requires aggregating granular usage data to match the coarser grain of an invoice. The following queries demonstrate how to validate that usage records equal the billed amounts on a legal invoice.

### 2.14.4.1 Reconcile Cost and Usage to Invoice Detail by Invoice ID

This query validates that the sum of costs for all service usage in the CostAndUsage dataset equals the total non-tax charges in the InvoiceDetail dataset for a specific invoice.

```
SELECT
  COALESCE(ID.InvoiceId, CU.InvoiceId) AS InvoiceId,
  ID.TotalBilledCost_InvoiceDetail,
  CU.TotalBilledCost_CostAndUsage,
  (COALESCE(ID.TotalBilledCost_InvoiceDetail, 0) - COALESCE(CU.TotalBilledCost_CostAndUsage, 0)) AS Variance
FROM (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_InvoiceDetail
  FROM InvoiceDetail
  WHERE ChargeCategory != 'Tax'
  GROUP BY InvoiceId
) ID
FULL OUTER JOIN (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_CostAndUsage
  FROM CostAndUsage
  WHERE ChargeCategory != 'Tax'
  GROUP BY InvoiceId
) CU ON ID.InvoiceId = CU.InvoiceId
WHERE COALESCE(ID.InvoiceId, CU.InvoiceId) = ?
```
### 2.14.4.2 Reconcile Multi-Currency Settlement Using Lineage IDs

This query demonstrates how to use the `PaymentCurrencyInvoiceDetailId` to reconcile granular records (denominated in the billing currency) against the aggregate records used for payment (denominated in the payment currency). This resolves the "Divergent Grain" problem.

```
SELECT
  PaymentCurrencyInvoiceDetailId,
  SUM(BilledCost) AS TotalBilled_BillingCurrency,
  SUM(PaymentCurrencyBilledCost) AS TotalBilled_PaymentCurrency,
  -- Calculate effective exchange rate for the group
  SUM(PaymentCurrencyBilledCost) / NULLIF(SUM(BilledCost), 0) AS EffectiveExchangeRate
FROM InvoiceDetail
WHERE InvoiceId = ?
GROUP BY PaymentCurrencyInvoiceDetailId
ORDER BY PaymentCurrencyInvoiceDetailId
```
### 2.14.4.3 Validate Tax Variance

This query identifies the tax component present in the InvoiceDetail dataset that is typically excluded from the CostAndUsage dataset, allowing for a complete three-way match between usage, tax, and the total invoice amount.

```
SELECT
  InvoiceId,
  SUM(CASE WHEN ChargeCategory = 'Tax' THEN BilledCost ELSE 0 END) AS TotalTaxAmount,
  SUM(CASE WHEN ChargeCategory != 'Tax' THEN BilledCost ELSE 0 END) AS TotalServiceAmount,
  SUM(BilledCost) AS GrandTotalPayable
FROM InvoiceDetail
WHERE InvoiceId = ?
GROUP BY InvoiceId
```