---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2024-03-03"
fingerprint: "91d380afb0f38beb"
---
# 3.3.24 Contract ID

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

Contract ID is a service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

## 3.3.24.1 Requirements

ContractId MUST adhere to the following requirements:

- ContractId MUST be of type String.
- ContractId MUST conform to StringHandling requirements.
- ContractId MUST NOT be null.
- When ContractId is not null, ContractId MUST adhere to the following requirements:
  - ContractId MUST be a unique identifier within the service provider.
  - ContractId SHOULD be a fully-qualified identifier.

## 3.3.24.4 Description

A service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |