---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/billing-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2024-01-01"
fingerprint: f5dc1cfc667f54a1
---
# 2.6 Billing Period End

Billing Period End represents the *exclusive* end date and time of a *billing period*. For example, a time period where BillingPeriodStart is '2024-01-01T00:00:00Z' and BillingPeriodEnd is '2024-02-01T00:00:00Z' includes charges for January, since BillingPeriodStart is *inclusive*, but does not include charges for February since BillingPeriodEnd is *exclusive*.

The BillingPeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time Format, MUST be an *exclusive* value, and MUST NOT contain null values. The sum of the BilledCost column for *rows* in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a *billing account*.

## 2.6.3 Description

The *exclusive* end date and time of a *billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |