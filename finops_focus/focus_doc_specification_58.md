---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2021-01-03"
fingerprint: bf4805587271c8ad
---
# 3.1.21 Charge Period Start

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

Charge Period Start represents the *inclusive start bound* of a *charge period*. For example, a time period where Charge Period Start is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes *charges* for January 1 since Charge Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 since Charge Period End represents the *exclusive end bound*.

## 3.1.21.1 Requirements

ChargePeriodStart MUST adhere to the following requirements:

- ChargePeriodStart MUST be of type Date/Time.
- ChargePeriodStart MUST conform to DateTimeFormat requirements.
- ChargePeriodStart MUST NOT be null.
- ChargePeriodStart MUST be the *inclusive start bound* of the effective period of the *charge*.

## 3.1.21.4 Description

The *inclusive start bound* of a *charge period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |