---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/pricing-quantity/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "37c0104f70e9e0f5"
---
# 3.1.47 Pricing Quantity

The Pricing Quantity represents the volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit. Distinct from Consumed Quantity (complementary to Consumed Unit), it focuses on pricing and cost, not *resource* and *service* consumption.

## 3.1.47.1 Requirements

PricingQuantity MUST adhere to the following requirements:

- PricingQuantity MUST be of type Decimal.
- PricingQuantity MUST conform to NumericFormat requirements.
- PricingQuantity MUST adhere to the following nullability requirements:
  - PricingQuantity MUST be null when SkuPriceId is null.
  - PricingQuantity MUST be null when ChargeCategory is "Tax".
  - PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - PricingQuantity MAY be null in all other cases.
- Cost metric (e.g., ContractedCost) MUST equal the product of the corresponding unit price (e.g., ContractedUnitPrice) and PricingQuantity when the unit price is not null and PricingQuantity is not null.

## 3.1.47.2 Usability Constraints

**Aggregation:** When aggregating Pricing Quantity for commitment utilization calculations, it's important to exclude *commitment discount* purchases (i.e., when Charge Category is "Purchase") that are paid to cover future eligible *charges* (e.g., *commitment discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e., when Charge Category is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.

## 3.1.47.5 Description

The volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |