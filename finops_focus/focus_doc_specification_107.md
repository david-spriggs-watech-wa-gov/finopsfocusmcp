---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/datasets/invoice-detail/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3ce850ca7031ba0a"
---
# 3.4 Invoice Detail

The Invoice Detail dataset is a transactional dataset that represents the financial record of *charges* as they appear on invoices provided by an *invoice issuer*. This dataset enables FinOps practitioners to perform financial reconciliation, tax reporting, and payment processing tasks. While the Cost and Usage dataset provides granular visibility into consumption, the Invoice Detail dataset ensures alignment with the physical or electronic billing documents.

## Columns in this Dataset

| Column | Type | Level | Data Type | 
|---|---|---|---|
| Billed Cost | Metric | Mandatory | Decimal | 
| Billing Account ID | Dimension | Mandatory | String | 
| Billing Currency | Dimension | Mandatory | String | 
| Billing Period End | Dimension | Mandatory | Date/Time | 
| Billing Period Start | Dimension | Mandatory | Date/Time | 
| Charge Category | Dimension | Mandatory | String | 
| Invoice Detail Created | Dimension | Mandatory | Date/Time | 
| Invoice Detail Description | Dimension | Mandatory | String | 
| Invoice Detail Grain | Dimension | Mandatory | JSON | 
| Invoice Detail ID | Dimension | Mandatory | String | 
| Invoice Detail Last Updated | Dimension | Mandatory | Date/Time | 
| Invoice ID | Dimension | Mandatory | String | 
| Invoice Issue Date | Dimension | Mandatory | Date/Time | 
| Invoice Issuer Name | Dimension | Mandatory | String | 
| Invoice Issue Status | Dimension | Mandatory | String | 
| Payment Currency | Dimension | Conditional | String | 
| Payment Currency Billed Cost | Metric | Conditional | Decimal | 
| Payment Currency Invoice Detail ID | Dimension | Conditional | String | 
| Payment Due Date | Dimension | Mandatory | Date/Time | 
| Payment Terms | Dimension | Mandatory | String | 
| Purchase Order Number | Dimension | Conditional | String | 
| Reference Invoice ID | Dimension | Mandatory | String | 

## Relationships

The Invoice Detail dataset can be joined to the Cost and Usage dataset through Invoice Issuer Name, Invoice ID, and (optionally) Invoice Detail ID. Take note: one or both datasets will need to be aggregated in order to facilitate any comparison.

The timing of Invoice ID and Invoice Detail ID availability in Cost and Usage varies across data generators. Some data generators populate these values while the *billing period* is still open, while others do not populate them until after the *billing period* is closed and invoices have been issued.

For more information, see the Invoice Reconciliation supported feature.

| Dataset A | Dataset A Column | Dataset B | Dataset B Column | 
|---|---|---|---|
| Invoice Detail | Invoice Issuer Name and Invoice ID | Cost and Usage | Invoice Issuer Name and Invoice ID | 
| Invoice Detail | Invoice Issuer Name, Invoice ID, and Invoice Detail ID | Cost and Usage | Invoice Issuer Name, Invoice ID, and Invoice Detail ID | 

## Requirements

InvoiceDetail MUST adhere to the following requirements:

- InvoiceDetail MUST be present when the invoice issuer supports payable invoices.
- The presence of columns in InvoiceDetail MUST adhere to the following requirements:
  - InvoiceDetail MUST include BilledCost.
  - InvoiceDetail MUST include BillingAccountId.
  - InvoiceDetail MUST include BillingCurrency.
  - InvoiceDetail MUST include BillingPeriodEnd.
  - InvoiceDetail MUST include BillingPeriodStart.
  - InvoiceDetail MUST include ChargeCategory.
  - InvoiceDetail MUST include InvoiceDetailCreated.
  - InvoiceDetail MUST include InvoiceDetailDescription.
  - InvoiceDetail MUST include InvoiceDetailGrain.
  - InvoiceDetail MUST include InvoiceDetailId.
  - InvoiceDetail MUST include InvoiceDetailLastUpdated.
  - InvoiceDetail MUST include InvoiceId.
  - InvoiceDetail MUST include InvoiceIssueDate.
  - InvoiceDetail MUST include InvoiceIssueStatus.
  - InvoiceDetail MUST include InvoiceIssuerName.
  - InvoiceDetail MUST include PaymentCurrency when the invoice issuer supports billing and payment in different currencies.
  - InvoiceDetail MUST include PaymentCurrencyBilledCost when the invoice issuer supports billing and payment in different currencies.
  - InvoiceDetail MUST include PaymentCurrencyInvoiceDetailId when the invoice issuer represents billing currency and payment currency at different aggregation levels on payable invoices.
  - InvoiceDetail MUST include PaymentDueDate.
  - InvoiceDetail MUST include PaymentTerms.
  - InvoiceDetail MUST include PurchaseOrderNumber when the invoice issuer supports customer input of purchase order numbers.
  - InvoiceDetail MUST include ReferenceInvoiceId.
  - InvoiceDetail MUST include *custom columns* to represent any monetary metric that appears on an invoice issued to a BillingAccountId when there is no equivalent *FOCUS column*.
- InvoiceDetail MUST conform to CorrectionHandling requirements.
- InvoiceDetail MUST conform to DatasetCompleteness requirements.
- InvoiceDetail MUST conform to DatasetConfiguration requirements.
- InvoiceDetail MUST conform to DeliveryHandling requirements.
- InvoiceDetail MUST represent all invoice line items with a non-zero BilledCost on any invoice associated with a BillingAccountId.
- InvoiceDetail *FOCUS columns* MUST conform to FocusColumnHandling requirements.
- InvoiceDetail *FOCUS columns* MUST conform to NullHandling requirements.
- InvoiceDetail *custom columns* MUST conform to CustomColumnHandling requirements.
- InvoiceDetail documentation MUST adhere to the following requirements:
  - InvoiceDetail documentation MUST specify how InvoiceDetail records correspond to invoice line items.
  - InvoiceDetail documentation MUST specify whether invoice line items with BilledCost of 0 are excluded from InvoiceDetail.
  - InvoiceDetail documentation MUST describe how columns in the CostAndUsage and InvoiceDetail *dataset instances* represent the invoice issuer's *invoice reconciliation* process.
  - InvoiceDetail documentation MUST be freely accessible to FOCUS consumers.

## Description

The financial record of *charges* as they appear on invoices provided by an invoice issuer.