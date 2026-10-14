---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-cost/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3443a8cb3fcf6fbb"
---
# 3.3.5 Contract Commitment Cost

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

Contract Commitment Cost represents the monetary value of the *contract commitment*. Contract Commitment Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for *resources* or *services* as agreed between a service provider and a customer.

## 3.3.5.1 Requirements

ContractCommitmentCost MUST adhere to the following requirements:

- ContractCommitmentCost MUST be of type Decimal.
- ContractCommitmentCost MUST conform to NumericFormat requirements.
- ContractCommitmentCost MUST adhere to the following nullability requirements:
  - ContractCommitmentCost MUST NOT be null when ContractCommitmentCategory is "Spend".
  - ContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
- ContractCommitmentCost MUST be denominated in the BillingCurrency.

## 3.3.5.4 Description

The monetary value of the *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |