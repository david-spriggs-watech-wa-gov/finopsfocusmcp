---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-discount-status/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-03"
fingerprint: "95d447800e560a3"
---
# 3.1.26 Commitment Discount Status

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.0

Commitment Discount Status indicates whether the *charge* corresponds with the consumption of a *commitment discount* identified in the CommitmentDiscountId column or the unused portion of the committed amount. The CommitmentDiscountStatus column is only applicable to *commitment discounts* and not *negotiated discounts*.

## 3.1.26.1 Requirements

CommitmentDiscountStatus MUST adhere to the following requirements:

- CommitmentDiscountStatus MUST be of type String.
- CommitmentDiscountStatus MUST adhere to the following nullability requirements:
  - CommitmentDiscountStatus MUST be null when CommitmentDiscountId is null.
  - CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and ChargeCategory is "Usage".
- CommitmentDiscountStatus MUST be one of the allowed values.
- CommitmentDiscountStatus MUST be "Used" when the *charge* utilizes a specific amount of a given CommitmentDiscountId.
- CommitmentDiscountStatus MUST be "Unused" when the *charge* represents the unused portion of the given CommitmentDiscountId.

## 3.1.26.2 Allowed Values

| Value | Description | 
|---|---|
| Used | *Charges* that utilized a specific amount of a commitment discount. | 
| Unused | *Charges* that represent the unused portion of the commitment discount. | 

## 3.1.26.5 Description

Indicates whether the *charge* corresponds with the consumption of a *commitment discount* or the unused portion of the committed amount.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | Allowed values |