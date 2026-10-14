---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/payment-due-date/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2019-04-03"
fingerprint: edc9e4da102ff5a9
---
# 3.4.19 Payment Due Date

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.4

Payment Due Date is the date by which the payment for an invoice is expected to be received by the *invoice issuer*. This date is used by FinOps practitioners and finance teams to manage cash flow, prioritize payments, and avoid late fees or service interruptions.

## 3.4.19.1 Requirements

PaymentDueDate MUST adhere to the following requirements:

- PaymentDueDate MUST be of type Date/Time.
- PaymentDueDate MUST conform to DateTimeFormat requirements.
- PaymentDueDate MAY be null.
- PaymentDueDate MUST be the date specified by the invoice issuer as the deadline for payment for the corresponding InvoiceId.

## 3.4.19.4 Description

The date by which the payment for an invoice is expected to be received by the invoice issuer.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |