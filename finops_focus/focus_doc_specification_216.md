---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/billing-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2024-01-01"
fingerprint: a74c4d586673cdb7
---
# 3.4.5 Billing Period Start

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

Billing Period Start represents the *inclusive start bound* of a *billing period*. For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes *charges* for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since BillingPeriodEnd represents the *exclusive end bound*.

## 3.4.5.1 Requirements

BillingPeriodStart MUST adhere to the following requirements:

- BillingPeriodStart MUST be of type Date/Time.
- BillingPeriodStart MUST conform to DateTimeFormat requirements.
- BillingPeriodStart MUST NOT be null.
- BillingPeriodStart MUST be the *inclusive start bound* of the *billing period*.
- BillingPeriodStart for a given InvoiceId and InvoiceIssuerName MUST match CostAndUsage.BillingPeriodStart for the same CostAndUsage.InvoiceId and CostAndUsage.InvoiceIssuerName.

## 3.4.5.4 Description

The *inclusive start bound* of a *billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |