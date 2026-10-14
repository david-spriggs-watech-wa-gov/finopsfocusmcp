---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2025-03-03"
fingerprint: "1f1d1c791273cdaf"
---
# 3.3.25 Contract Period End

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.3

Contract Period End represents the *exclusive end bound* of a contract period. For example, a time period where Contract Period Start is '2024-01-01T00:00:00Z' and Contract Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Period Start represents the *inclusive start bound*, but does not include January 1 2025 since Contract Period End represents the *exclusive end bound*.

## 3.3.25.1 Requirements

ContractPeriodEnd MUST adhere to the following requirements:

- ContractPeriodEnd MUST be of type Date/Time.
- ContractPeriodEnd MUST conform to DateTimeFormat requirements.
- ContractPeriodEnd MUST NOT be null.
- ContractPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract*.

## 3.3.25.4 Description

The *exclusive end bound* of a contract period.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |