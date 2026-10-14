---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/invoice-detail-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "7db19cbea2713481"
---
# 3.1.37 Invoice Detail ID

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.4

Invoice Detail ID is the invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## 3.1.37.1 Requirements

InvoiceDetailId MUST adhere to the following requirements:

- InvoiceDetailId MUST be of type String.
- InvoiceDetailId MUST conform to StringHandling requirements.
- InvoiceDetailId MUST adhere to the following nullability requirements:
  - InvoiceDetailId MUST be null when the charge is not associated either with an invoice or with a pre-generated provisional invoice.
  - InvoiceDetailId MUST NOT be null when the charge is associated with either an issued invoice or a pre-generated provisional invoice.
- InvoiceDetailId MAY be generated prior to an invoice being issued.
- InvoiceDetailId MUST uniquely identify a specific record within a given InvoiceId.

## 3.1.37.4 Description

The invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |