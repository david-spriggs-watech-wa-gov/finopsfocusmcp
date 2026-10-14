---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2012-04-03"
fingerprint: "7dd1dc8a203f7059"
---
# 3.4.12 Invoice ID

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.4

Invoice ID is an invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding *billing period* for a given *billing account*. Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between *charges* and billing periods.

## 3.4.12.1 Requirements

InvoiceId MUST adhere to the following requirements:

- InvoiceId MUST be of type String.
- InvoiceId MUST conform to StringHandling requirements.
- InvoiceId MUST NOT be null.
- InvoiceId MAY be generated prior to an invoice being issued.
- InvoiceId MUST uniquely identify the invoice as provided by the *invoice issuer*.

## 3.4.12.4 Description

The invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding billing period for a given billing account.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |