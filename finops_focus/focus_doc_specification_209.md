---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/payment-currency-invoice-detail-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2018-04-03"
fingerprint: f0327863b0783cc7
---
# 3.4.18 Payment Currency Invoice Detail ID

Payment Currency Invoice Detail ID is a reference to the Invoice Detail ID of the record where the Payment Currency Billed Cost for the current row is aggregated. This identifier enables practitioners to explicitly link granular usage records to their corresponding aggregate records stated in their chosen currency for settlement, ensuring accurate reconciliation across divergent grains.

## 3.4.18.1 Requirements

PaymentCurrencyInvoiceDetailId MUST adhere to the following requirements:

- PaymentCurrencyInvoiceDetailId MUST be of type String.
- PaymentCurrencyInvoiceDetailId MUST conform to StringHandling requirements.
- PaymentCurrencyInvoiceDetailId MUST NOT be null.
- PaymentCurrencyInvoiceDetailId MUST match the InvoiceDetailId of the record representing the PaymentCurrencyBilledCost aggregation for the current row.
- PaymentCurrencyInvoiceDetailId MUST match InvoiceDetailId of the current record when PaymentCurrencyBilledCost is non-zero.

## 3.4.18.4 Description

The identifier linking a granular record to the specific Invoice Detail record where its Payment Currency Billed Cost is represented or aggregated.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |