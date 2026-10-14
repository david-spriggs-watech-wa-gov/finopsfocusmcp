---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/cost-and-usage/billing-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2024-01-01"
fingerprint: b45c1c7a663f5ca1
---
# 2.7 Billing Period Start

Billing Period Start represents the *inclusive* start date and time of a *billing period*. For example, a time period where BillingPeriodStart is '2024-01-01T00:00:00Z' and BillingPeriodEnd is '2024-02-01T00:00:00Z' includes charges for January, since BillingPeriodStart is inclusive, but does not include charges for February since BillingPeriodEnd is *exclusive*.

The BillingPeriodStart column MUST be present in the billing data, MUST be of type Date/Time Format, MUST be an *inclusive* value, and MUST NOT contain null values. The sum of the BilledCost metric for *rows* in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a *billing account*.

## 2.7.3 Description

The *inclusive* start date and time of a *billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |