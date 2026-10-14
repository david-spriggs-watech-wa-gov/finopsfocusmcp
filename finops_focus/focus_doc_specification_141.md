---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-discount-unit/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "34f900cd2f5e51db"
---
# 3.1.28 Commitment Discount Unit

Commitment Discount Unit represents the service-provider-specified measurement unit indicating how a service provider measures the Commitment Discount Quantity of a *commitment discount*. The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not *negotiated discounts*.

## 3.1.28.1 Requirements

CommitmentDiscountUnit MUST adhere to the following requirements:

- CommitmentDiscountUnit MUST be of type String.
- CommitmentDiscountUnit MUST conform to StringHandling requirements.
- CommitmentDiscountUnit SHOULD conform to UnitFormat requirements.
- CommitmentDiscountUnit MUST adhere to the following nullability requirements:
  - CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  - CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
- When CommitmentDiscountUnit is not null, CommitmentDiscountUnit MUST adhere to the following requirements:
  - CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  - CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  - When accounting for *commitment discount flexibility*, the CommitmentDiscountUnit value SHOULD reflect this consideration.

See Examples: Commitment Discount Flexibility for more details around *commitment discount flexibility*.

## 3.1.28.4 Description

The service-provider-specified measurement unit indicating how a service provider measures the Commitment Discount Quantity of a *commitment discount*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | Unit Format |