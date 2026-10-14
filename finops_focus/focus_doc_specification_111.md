---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-discount-percentage/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b059107b6db86e51
---
# 3.3.8 Contract Commitment Discount Percentage

Contract Commitment Discount Percentage represents the effective percentage reduction applied to the list price for resources or services covered by a *contract commitment*.

## 3.3.8.1 Requirements

ContractCommitmentDiscountPercentage MUST adhere to the following requirements:

- ContractCommitmentDiscountPercentage MUST be of type Decimal.
- ContractCommitmentDiscountPercentage MUST conform to NumericFormat requirements.
- ContractCommitmentDiscountPercentage MUST adhere to the following nullability requirements:
  - ContractCommitmentDiscountPercentage MUST NOT be null when ContractCommitmentBenefitCategory is "Discount".
  - ContractCommitmentDiscountPercentage MUST be null when ContractCommitmentBenefitCategory is "Availability".
- ContractCommitmentDiscountPercentage MUST be a value between 0.0 and 1.0, inclusive.
- For contracts with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), ContractCommitmentDiscountPercentage MUST adhere to the following additional requirements:
  - ContractCommitmentDiscountPercentage MUST reflect the discount percentage defined for the specific pricing tier represented by the Contract Commitment row.
  - ContractCommitmentDiscountPercentage MUST correspond to only one pricing tier per Contract Commitment row.
- ContractCommitmentDiscountPercentage SHOULD represent the net effective discount when multiple contractual layers are applicable (e.g., a negotiated discount on top of a standard commitment).

## 3.3.8.2 Implementation Guidance

### 3.3.8.2.1 Calculating the Effective Percentage

In scenarios where a commitment has "stacked" or "nested" discounts, this field should reflect the total reduction from the list price.

Discount Percentage = 1 - (Contracted Unit Price / List Unit Price)

For example, consider usage that yields a cost for which the following discounts are applicable:

- Commitment discount: 20% applied to the on-demand cost
- Negotiated discount: 10% applied to the post-commitment discount cost

The effective discount is not 30%. It is: 1 - (0.8 × 0.9) = 28%

In this scenario, ContractCommitmentDiscountPercentage should be reported as 28%.

### 3.3.8.2.2 Relationship to Benefit Category

This field provides the magnitude for the **Discount** category. While `ContractCommitmentCost` tracks the financial obligation (what you pay), `ContractCommitmentDiscountPercentage` tracks the benefit rate (what you save).

### 3.3.8.2.3 Tiered Incentives

For commitments with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), this column should represent the **active** or **base** discount percentage applicable to the current contract row.

## 3.3.8.5 Description

The effective percentage reduction applied to the list price of resources or services covered by a *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | 0.0 to 1.0 (inclusive) |