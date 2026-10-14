---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-created/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: fdf120298ee3c49b
---
# 3.3.6 Contract Commitment Created

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.4

Contract Commitment Created is the timestamp when the Contract Commitment record was first created. This timestamp facilitates auditability of the contract commitment lifecycle.

## 3.3.6.1 Requirements

ContractCommitmentCreated MUST adhere to the following requirements:

- ContractCommitmentCreated MUST be of type Date/Time.
- ContractCommitmentCreated MUST conform to DateTimeFormat requirements.
- ContractCommitmentCreated MUST NOT be null.
- ContractCommitmentCreated MUST represent the moment in time the Contract Commitment record was instantiated.

## 3.3.6.4 Description

The timestamp when the contract commitment record was first created.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |