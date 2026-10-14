---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2012-01-03"
fingerprint: "3f4c0d584273ccb3"
---
# 3.1.12 Billing Period End

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    0.5

Billing Period End represents the *exclusive end bound* of a *billing period*. For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes *charges* for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since Billing Period End represents the *exclusive end bound*.

## 3.1.12.1 Requirements

BillingPeriodEnd MUST adhere to the following requirements:

- BillingPeriodEnd MUST be of type Date/Time.
- BillingPeriodEnd MUST conform to DateTimeFormat requirements.
- BillingPeriodEnd MUST NOT be null.
- BillingPeriodEnd MUST be the *exclusive end bound* of the *billing period*.

## 3.1.12.4 Description

The *exclusive end bound* of a *billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |