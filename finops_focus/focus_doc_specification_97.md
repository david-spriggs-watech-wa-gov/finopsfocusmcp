---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/payment-terms/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2020-04-03"
fingerprint: "38d374fa107f446e"
---
# 3.4.20 Payment Terms

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

Payment Terms represents the *terms* (typically focused on timeframe) by which the *invoice issuer* expects to receive payment for an invoice. These terms define the agreed-upon period for settling the invoice, helping both the provider and the customer manage financial expectations and payment schedules.

## 3.4.20.1 Requirements

PaymentTerms MUST adhere to the following requirements:

- PaymentTerms MUST be of type String.
- PaymentTerms MUST conform to StringHandling requirements.
- PaymentTerms MUST NOT be null.
- PaymentTerms MUST represent the payment terms (e.g., "Net 30") as defined on the corresponding invoice.

## 3.4.20.4 Description

The terms (typically focused on timeframe) by which the invoice issuer expects to receive payment for an invoice.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |