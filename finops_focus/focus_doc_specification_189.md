---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-quantity/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2021-03-03"
fingerprint: "185800af1ffb667b"
---
# 3.3.21 Contract Commitment Quantity

Dataset:
                    Contract Commitment

Column Type:
                    Metric

Feature Level:
                    Mandatory

Data Type:
                    Decimal

Since:
                    1.3

Contract Commitment Quantity represents the amount associated with the *contract commitment*, denominated in a service-provider-defined Contract Commitment Unit. Contract Commitment Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for *resources* or *services* as agreed between a provider and a customer.

## 3.3.21.1 Requirements

ContractCommitmentQuantity MUST adhere to the following requirements:

- ContractCommitmentQuantity MUST be of type Decimal.
- ContractCommitmentQuantity MUST conform to NumericFormat requirements.
- ContractCommitmentQuantity MUST adhere to the following nullability requirements:
  - ContractCommitmentQuantity MUST NOT be null when ContractCommitmentCategory is "Usage".
  - ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".

## 3.3.21.4 Description

The amount associated with the *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |