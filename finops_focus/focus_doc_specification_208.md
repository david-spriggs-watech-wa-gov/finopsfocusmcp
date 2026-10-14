---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-issue-status/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2015-04-03"
fingerprint: "5956ff9bbc61306d"
---
# 3.4.15 Invoice Issue Status

Invoice Issue Status indicates the publication state of the invoice and the reliability of its associated delivered Cost and Usage and Invoice Detail data. It distinguishes between provisional data that is subject to change, invoices that have been formally issued as valid financial obligations with finalized associated data, and invoices that have been explicitly retracted.

## 3.4.15.1 Requirements

InvoiceIssueStatus MUST adhere to the following requirements:

- InvoiceIssueStatus MUST be of type String.
- InvoiceIssueStatus MUST conform to StringHandling requirements.
- InvoiceIssueStatus MUST NOT be null.
- InvoiceIssueStatus MUST be one of the allowed values.
- InvoiceIssueStatus MUST represent the current publication state of the invoice.
- InvoiceIssueStatus MUST NOT be "Open" following a previous status of "Issued", except when explicitly requested or approved by the customer.

## 3.4.15.2 Allowed Values

| Value | Description | 
|---|---|
| Open | The invoice is provisional and subject to change. It is not a valid financial obligation and the associated delivered data is preliminary. | 
| Issued | The invoice has been formally issued by the provider. It represents a valid financial obligation with finalized associated data. | 
| Voided | The invoice was previously issued but has been retracted or nullified. It is not a valid financial obligation. | 

## 3.4.15.3 Implementation Guidance

The transition from "Open" to "Issued" typically signifies that an invoice has been finalized, invoice reconciliation has been performed, and the delivered data is accurate. However, when the delivered data is found to be inaccurate or incomplete, it may be necessary to apply corrections to records associated with the issued invoice.

If needed, a previously issued invoice may be reopened to apply such corrections, but this transition from "Issued" to "Open" must be explicitly requested or approved by the customer to maintain auditability.

Corrections to underlying records that do not impact invoice reconciliation are allowed regardless of Invoice Issue Status, but may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

FinOps tools and reporting engines should be designed to detect Invoice Issue Status transitions and corrections to records associated with issued invoices, and trigger updates to downstream processes to ensure financial accuracy.

For more information, please see the Invoice and Billing Period Handling appendix and the Correction Handling attribute.

## 3.4.15.6 Description

The publication state of the invoice and the reliability of its associated delivered data, indicating if it is provisional ("Open"), issued ("Issued"), or voided ("Voided").

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |