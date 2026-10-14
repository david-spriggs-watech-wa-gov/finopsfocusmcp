---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2011-03-03"
fingerprint: d4c5c0a936e70ee2
---
# 3.3.11 Contract Commitment ID

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

Contract Commitment ID is a service-provider-assigned identifier describing a single contract term agreed between a provider and a customer. Contracts can include commitments to a certain amount of spend or usage over an agreed period of time.

## 3.3.11.1 Requirements

ContractCommitmentId MUST adhere to the following requirements:

- ContractCommitmentId MUST be of type String.
- ContractCommitmentId MUST conform to StringHandling requirements.
- ContractCommitmentId MUST NOT be null.
- ContractCommitmentId MUST be a unique identifier within the service provider.
- ContractCommitmentId SHOULD be a fully-qualified identifier.
- ContractCommitmentId MUST have one and only one parent ContractId.
- ContractCommitmentId MAY match ContractId.

## 3.3.11.4 Description

A service-provider-assigned identifier describing a single contract term agreed between a service provider and a customer.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |