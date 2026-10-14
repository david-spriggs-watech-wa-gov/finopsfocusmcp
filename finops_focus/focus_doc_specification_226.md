---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2020-03-03"
fingerprint: "946c00381f73cdbf"
---
# 3.3.20 Contract Commitment Period Start

Contract Commitment Period Start represents the *inclusive start bound* of a contract commitment period. For example, a time period where Contract Commitment Period Start is '2024-01-01T00:00:00Z' and Contract Commitment End is '2025-01-01T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 2025 since Contract Commitment Period End represents the *exclusive end bound*.

## 3.3.20.1 Requirements

ContractCommitmentPeriodStart MUST adhere to the following requirements:

- ContractCommitmentPeriodStart MUST be of type Date/Time.
- ContractCommitmentPeriodStart MUST conform to DateTimeFormat requirements.
- ContractCommitmentPeriodStart MUST NOT be null.
- ContractCommitmentPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract commitment*.

## 3.3.20.4 Description

The *inclusive start bound* of a contract commitment period.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |