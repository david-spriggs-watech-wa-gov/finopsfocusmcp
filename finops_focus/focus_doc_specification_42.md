---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/invoice-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "7d90cc9a283d7550"
---
# 3.1.38 Invoice ID

An Invoice ID is an invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding *billing period* for a given *billing account*. Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between *charges* and billing periods.

## 3.1.38.1 Requirements

InvoiceId MUST adhere to the following requirements:

- InvoiceId MUST be of type String.
- InvoiceId MUST conform to StringHandling requirements.
- InvoiceId MUST adhere to the following nullability requirements:
  - InvoiceId MUST be null when the *charge* is not associated either with an invoice or with a pre-generated provisional invoice.
  - InvoiceId MUST NOT be null when the *charge* is associated with either an issued invoice or a pre-generated provisional invoice.
- InvoiceId MAY be generated prior to an invoice being issued.
- InvoiceId MUST be associated with the related *charge* and BillingAccountId when a pre-generated invoice or provisional invoice exists.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 3.1.38.4 Description

The invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding billing period for a given billing account.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |