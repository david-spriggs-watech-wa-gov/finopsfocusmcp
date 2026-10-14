---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-discount-type/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b1590418ee557009
---
# 3.1.27 Commitment Discount Type

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

Commitment Discount Type is a service-provider-assigned name to identify the type of *commitment discount* applied to the *row*. The CommitmentDiscountType column is only applicable to *commitment discounts* and not *negotiated discounts*.

## 3.1.27.1 Requirements

CommitmentDiscountType MUST adhere to the following requirements:

- CommitmentDiscountType MUST be of type String.
- CommitmentDiscountType MUST conform to StringHandling requirements.
- CommitmentDiscountType MUST adhere to the following nullability requirements:
  - CommitmentDiscountType MUST be null when CommitmentDiscountId is null.
  - CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## 3.1.27.4 Description

A service-provider-assigned identifier for the type of *commitment discount* applied to the *row*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |