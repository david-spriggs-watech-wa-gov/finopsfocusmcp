---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-period-end/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2019-03-03"
fingerprint: "9e4d18390b73ccaf"
---
# 3.3.19 Contract Commitment Period End

Contract Commitment Period End represents the *exclusive end bound* of a contract commitment period. For example, a time period where Contract Commitment Period Start is '2024-01-01T00:00:00Z' and Contract Commitment Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the *inclusive start bound*, but does not include January 1 2025 since Contract Commitment Period End represents the *exclusive end bound*.

## 3.3.19.1 Requirements

ContractCommitmentPeriodEnd MUST adhere to the following requirements:

- ContractCommitmentPeriodEnd MUST be of type Date/Time.
- ContractCommitmentPeriodEnd MUST conform to DateTimeFormat requirements.
- ContractCommitmentPeriodEnd MUST NOT be null.
- ContractCommitmentPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract commitment*.

## 3.3.19.4 Description

The *exclusive end bound* of a contract commitment period.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |