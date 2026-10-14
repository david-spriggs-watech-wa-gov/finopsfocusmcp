---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/billing-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2024-01-01"
fingerprint: "3f4c0d58427bccb3"
---
# 3.4.4 Billing Period End

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

Billing Period End represents the *exclusive end bound* of a *billing period*. For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes *charges* for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since Billing Period End represents the *exclusive end bound*.

## 3.4.4.1 Requirements

BillingPeriodEnd MUST adhere to the following requirements:

- BillingPeriodEnd MUST be of type Date/Time.
- BillingPeriodEnd MUST conform to DateTimeFormat requirements.
- BillingPeriodEnd MUST NOT be null.
- BillingPeriodEnd MUST be the *exclusive end bound* of the *billing period*.
- BillingPeriodEnd for a given InvoiceId and InvoiceIssuerName MUST match CostAndUsage.BillingPeriodEnd for the same CostAndUsage.InvoiceId and CostAndUsage.InvoiceIssuerName.

## 3.4.4.4 Description

The *exclusive end bound* of a *billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |