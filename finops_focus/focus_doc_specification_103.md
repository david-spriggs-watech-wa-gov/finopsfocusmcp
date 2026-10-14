---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-detail-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2010-04-03"
fingerprint: "79f8defaa6733093"
---
# 3.4.10 Invoice Detail ID

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

Invoice Detail ID is the invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## 3.4.10.1 Requirements

InvoiceDetailId MUST adhere to the following requirements:

- InvoiceDetailId MUST be of type String.
- InvoiceDetailId MUST conform to StringHandling requirements.
- InvoiceDetailId MUST NOT be null.
- InvoiceDetailId MUST uniquely identify a record within a given InvoiceId.

## 3.4.10.4 Description

The invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |