---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2020-01-03"
fingerprint: ff4d14580a7fcca7
---
# 3.1.20 Charge Period End

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

Charge Period End represents the *exclusive end bound* of a *charge period*. For example, a time period where Charge Period Start is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes *charges* for January 1 since Charge Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 since Charge Period End represents the *exclusive end bound*.

## 3.1.20.1 Requirements

ChargePeriodEnd MUST adhere to the following requirements:

- ChargePeriodEnd MUST be of type Date/Time.
- ChargePeriodEnd MUST conform to DateTimeFormat requirements.
- ChargePeriodEnd MUST NOT be null.
- ChargePeriodEnd MUST be the *exclusive end bound* of the effective period of the *charge*.

## 3.1.20.4 Description

The *exclusive end bound* of a *charge period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |