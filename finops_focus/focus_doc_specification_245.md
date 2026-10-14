---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-discount-quantity/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2025-01-03"
fingerprint: "2c7910ff5ed97291"
---
# 3.1.25 Commitment Discount Quantity

Commitment Discount Quantity is the amount of a *commitment discount* purchased or accounted for in *commitment discount* related *rows* that is denominated in Commitment Discount Units. The aggregated Commitment Discount Quantity across purchase records, pertaining to a particular Commitment Discount ID during its commitment *period*, represents the total Commitment Discount Units acquired with that commitment discount. For committed usage, the Commitment Discount Quantity is either the number of Commitment Discount Units consumed by a *row* that is covered by a *commitment discount* or is the unused portion of a *commitment discount* over a *charge period*. Commitment Discount Quantity is commonly used in *commitment discount* analysis and optimization use cases and only applies to *commitment discounts*, not *negotiated discounts*.

When CommitmentDiscountCategory is "Usage" (usage-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of usage purchased or consumed. If *commitment discount flexibility* is applicable, this value may be further transformed based on additional, service-provider-specific requirements. When CommitmentDiscountCategory is "Spend" (spend-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of spend purchased or consumed. See Appendix: Commitment Discount Flexibility for more details around *commitment discount flexibility*.

## 3.1.25.1 Requirements

CommitmentDiscountQuantity MUST adhere to the following requirements:

- CommitmentDiscountQuantity MUST be of type Decimal.
- CommitmentDiscountQuantity MUST conform to NumericFormat requirements.
- CommitmentDiscountQuantity MUST adhere to the following nullability requirements:
  - CommitmentDiscountQuantity MUST be null when SkuPriceId is null.
  - When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity MUST adhere to the following requirements:
    - CommitmentDiscountQuantity MUST NOT be null when ChargeClass is not "Correction".
    - CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  - CommitmentDiscountQuantity MUST be null in all other cases.
- When CommitmentDiscountQuantity is not null and ChargeCategory is "Purchase", CommitmentDiscountQuantity MUST adhere to the following requirements:
  - CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's term* when ChargeFrequency is "One-Time".
  - CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
- When CommitmentDiscountQuantity is not null and ChargeCategory is "Usage", CommitmentDiscountQuantity MUST adhere to the following requirements:
  - CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when CommitmentDiscountStatus is "Used".
  - CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".

## 3.1.25.2 Usability Constraints

**Aggregation:** When aggregating Commitment Discount Quantity for commitment utilization calculations, it's important to exclude *commitment discount* purchases (i.e., when Charge Category is "Purchase") that are paid to cover future eligible *charges* (e.g., *commitment discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e., when Charge Category is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.

## 3.1.25.5 Description

The amount of a *commitment discount* purchased or accounted for in *commitment discount* related *rows* that is denominated in Commitment Discount Units.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |