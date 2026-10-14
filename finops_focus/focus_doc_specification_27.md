---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-type/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2022-03-03"
fingerprint: d07b282ba7e7c47b
---
# 3.3.22 Contract Commitment Type

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

Contract Commitment Type is a service-provider-assigned name to identify the type of *contract commitment*. Contract Commitment Type is a readable display name and not a code. Contract Commitment Type is commonly used for displaying and aggregating the types of commitments the practitioner has made, stated in service-provider-specific terms.

## 3.3.22.1 Requirements

ContractCommitmentType MUST adhere to the following requirements:

- ContractCommitmentType MUST be of type String.
- ContractCommitmentType MUST conform to StringHandling requirements.
- ContractCommitmentType MUST NOT be null.
- ContractCommitmentType MUST be a consistent, readable display value.

## 3.3.22.4 Description

A service-provider-assigned name to identify the type of *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |