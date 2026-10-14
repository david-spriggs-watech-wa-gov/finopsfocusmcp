---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-03-03"
fingerprint: "960f096b0b73cdbf"
---
# 3.3.26 Contract Period Start

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

Contract Period Start represents the *inclusive start bound* of a contract period. For example, a time period where Contract Period Start is '2024-01-01T00:00:00Z' and Contract Period End is '2025-01-01T00:00:00Z' includes January 1 2024 since Contract Period Start represents the *inclusive start bound*, but does not include January 2 2025 since Contract Period End represents the *exclusive end bound*.

## 3.3.26.1 Requirements

ContractPeriodStart MUST adhere to the following requirements:

- ContractPeriodStart MUST be of type Date/Time.
- ContractPeriodStart MUST conform to DateTimeFormat requirements.
- ContractPeriodStart MUST NOT be null.
- ContractPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract*.

## 3.3.26.4 Description

The *inclusive start bound* of a contract period.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |