---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/consumed-quantity/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "32f1856fe8c56661"
---
# 3.1.30 Consumed Quantity

Dataset:
                    Cost and Usage

Column Type:
                    Metric

Feature Level:
                    Conditional

Data Type:
                    Decimal

Since:
                    1.0

The Consumed Quantity represents the volume of a metered SKU associated with a *resource* or *service* used, based on the Consumed Unit. Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the Pricing Quantity (complementary to Pricing Unit) and focuses on *resource* and *service* consumption, not pricing and cost.

## 3.1.30.1 Requirements

ConsumedQuantity MUST adhere to the following requirements:

- ConsumedQuantity MUST be of type Decimal.
- ConsumedQuantity MUST conform to NumericFormat requirements.
- ConsumedQuantity MUST adhere to the following nullability requirements:
  - ConsumedQuantity MUST be null when SkuPriceId is null.
  - ConsumedQuantity MUST be null when ChargeCategory is not "Usage", or when ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".
  - When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity MUST adhere to the following requirements:
    - ConsumedQuantity MUST NOT be null when ChargeClass is not "Correction".
    - ConsumedQuantity MAY be null when ChargeClass is "Correction".

## 3.1.30.4 Description

The volume of a metered SKU associated with a *resource* or *service* used, based on the Consumed Unit.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |