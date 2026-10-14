---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-unit/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2023-03-03"
fingerprint: "9cd1003ab763327b"
---
# 3.3.23 Contract Commitment Unit

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.3

The Contract Commitment Unit represents a service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity. Contract Commitment Unit complements the Contract Commitment Quantity metric.

## 3.3.23.1 Requirements

ContractCommitmentUnit MUST adhere to the following requirements:

- ContractCommitmentUnit MUST be of type String.
- ContractCommitmentUnit MUST conform to StringHandling requirements.
- ContractCommitmentUnit SHOULD conform to UnitFormat requirements.
- ContractCommitmentUnit MUST adhere to the following nullability requirements:
  - ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  - ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.

## 3.3.23.4 Description

A service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | Unit Format recommended |