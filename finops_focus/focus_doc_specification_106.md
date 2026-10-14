---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/payment-currency/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2016-04-03"
fingerprint: ac1b88b21269327c
---
# 3.4.16 Payment Currency

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.4

Payment Currency represents the currency in which the *invoice issuer* requires settlement. This is the currency of the financial obligation created by the invoice, which may differ from the Billing Currency and/or the source currency of the payer's funds or bank account. Payment Currency allows FinOps practitioners to track settlement obligations and foreign exchange impacts.

## 3.4.16.1 Requirements

PaymentCurrency MUST adhere to the following requirements:

- PaymentCurrency MUST be of type String.
- PaymentCurrency MUST conform to StringHandling requirements.
- PaymentCurrency MUST NOT be null.
- PaymentCurrency MUST represent the currency in which the invoice payment was made or expected to be made.
- PaymentCurrency MUST be expressed in *national currency* (e.g., USD, EUR).

## 3.4.16.4 Description

The currency in which the invoice is paid.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Currency Format |