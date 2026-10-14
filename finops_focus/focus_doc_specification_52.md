---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-detail-description/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "79eac27a70677eaf"
---
# 3.4.8 Invoice Detail Description

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

Invoice Detail Description is the invoice-issuer-provided description of an invoice line item. This description provides context for the charge as it appears on the invoice, often summarizing the service, resource, or period covered by that specific line item to assist in human-readable reconciliation.

## 3.4.8.1 Requirements

InvoiceDetailDescription MUST adhere to the following requirements:

- InvoiceDetailDescription MUST be of type String.
- InvoiceDetailDescription MUST conform to StringHandling requirements.
- InvoiceDetailDescription SHOULD NOT be null.
- InvoiceDetailDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.
- InvoiceDetailDescription MUST describe the *charges* represented by the InvoiceDetailId.

## 3.4.8.4 Description

The invoice-issuer-provided description of an invoice line item.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |