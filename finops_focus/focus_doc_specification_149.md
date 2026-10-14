---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-issuer-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2014-04-03"
fingerprint: b9ca6400a675eab3
---
# 3.4.14 Invoice Issuer Name

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

## 3.4.14.1 Requirements

InvoiceIssuerName MUST adhere to the following requirements:

- InvoiceIssuerName MUST be of type String.
- InvoiceIssuerName MUST conform to StringHandling requirements.
- InvoiceIssuerName MUST NOT be null.
- InvoiceIssuerName MUST represent the entity that issues invoices.

See Appendix: Participating Entity Identification Examples section for examples of Invoice Issuer Name values across various use case scenarios.

## 3.4.14.4 Description

The name of the entity responsible for invoicing for the *resources* or *services* consumed.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |