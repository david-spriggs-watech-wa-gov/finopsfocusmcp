---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/billing-period/invoice-issuer-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b9ca6c01a277eaa3
---
# 3.2.6 Invoice Issuer Name

Dataset:
                    Billing Period

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.4

## 3.2.6.1 Requirements

InvoiceIssuerName MUST adhere to the following requirements:

- InvoiceIssuerName MUST be of type String.
- InvoiceIssuerName MUST conform to StringHandling requirements.
- InvoiceIssuerName MUST NOT be null.
- InvoiceIssuerName MUST represent the entity that issues invoices.

See Appendix: Participating Entity Identification Examples section for examples of Invoice Issuer Name values across various use case scenarios.

## 3.2.6.4 Description

The name of the entity responsible for invoicing for the *resources* or *services* consumed.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |