---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/invoice-issuer-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "394a6c08ae75e4bb"
---
# 3.3.27 Invoice Issuer Name

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.4

Invoice Issuer Name is the name of the entity responsible for issuing payable invoices for the *contract commitment*. It is commonly used for cost analysis, reconciliation, and reporting scenarios.

## 3.3.27.1 Requirements

InvoiceIssuerName MUST adhere to the following requirements:

- InvoiceIssuerName MUST be of type String.
- InvoiceIssuerName MUST conform to StringHandling requirements.
- InvoiceIssuerName MUST NOT be null.
- InvoiceIssuerName MUST represent the entity that issues invoices.

## 3.3.27.4 Description

The name of the entity responsible for invoicing for the *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |