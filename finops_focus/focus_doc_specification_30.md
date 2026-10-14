---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-discount-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2024-01-03"
fingerprint: "786bb42e22d361f1"
---
# 3.1.24 Commitment Discount Name

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.0-preview

A Commitment Discount Name is the display name assigned to a *commitment discount*. The CommitmentDiscountName column is only applicable to *commitment discounts* and not *negotiated discounts*.

## 3.1.24.1 Requirements

CommitmentDiscountName MUST adhere to the following requirements:

- CommitmentDiscountName MUST be of type String.
- CommitmentDiscountName MUST conform to StringHandling requirements.
- CommitmentDiscountName MUST adhere to the following nullability requirements:
  - CommitmentDiscountName MUST be null when CommitmentDiscountId is null.
  - When CommitmentDiscountId is not null, CommitmentDiscountName MUST adhere to the following requirements:
    - CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    - CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

## 3.1.24.4 Description

The display name assigned to a *commitment discount*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |