---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-last-updated/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2012-03-03"
fingerprint: f4f7002b8fe2a4d3
---
# 3.3.12 Contract Commitment Last Updated

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

Contract Commitment Last Updated is the timestamp when the Contract Commitment record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a Contract Commitment record, particularly if corrections or status changes have been applied to the record after its initial creation.

## 3.3.12.1 Requirements

ContractCommitmentLastUpdated MUST adhere to the following requirements:

- ContractCommitmentLastUpdated MUST be of type Date/Time.
- ContractCommitmentLastUpdated MUST conform to DateTimeFormat requirements.
- ContractCommitmentLastUpdated MUST NOT be null.
- ContractCommitmentLastUpdated MUST represent the most recent moment in time when any column value of the Contract Commitment record was created or modified.
- ContractCommitmentLastUpdated MUST be greater than or equal to ContractCommitmentCreated.

## 3.3.12.4 Description

The timestamp when the contract commitment record was last updated.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |