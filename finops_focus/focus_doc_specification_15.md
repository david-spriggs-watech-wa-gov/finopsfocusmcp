---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/effective-cost-analysis/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b4003f66af2b486
---
# 2.13 Effective Cost Analysis

## 2.13.1 Description

FOCUS enables practitioners to analyze costs on an *accrual basis*, where expenses are recognized when *resources* are consumed, *services* are used, or *contract commitments* are recognized, regardless of when those costs are invoiced. The EffectiveCost column reflects all applicable pricing adjustments and distributes the cost of *covering charges* (one-time or recurring purchases) to the *covered charges* they offset.

For *charges* that are not *covered charges*, EffectiveCost reflects the same amount as BilledCost. For *covering charges* (e.g., *commitment discount* purchases, prepayments, or marketplace purchases), EffectiveCost is 0 because their cost is recognized on the *covered charges* instead. In *commitment discount* scenarios, CommitmentDiscountStatus distinguishes whether amortized cost was allocated to consumed *resources* or *services* ("Used") or remained unallocated ("Unused").

EffectiveCost is commonly used for *accrual-based* reporting, cost allocation, chargeback, and spending trend analysis. For scenarios involving *commitment discounts* across different payment models, see Examples: Commitment Discount Flexibility. For marketplace and SaaS scenarios, see Examples: SaaS.

## 2.13.2 Directly Dependent Columns

## 2.13.3 Supporting Columns

## 2.13.4 Example SQL Queries

EffectiveCost can be analyzed using *billing period* or *charge period* time filters. Billing period aligns with invoice cycles and is useful for financial reporting. Charge period captures when resources were consumed or commitments were recognized, which is more precise for consumption-based analysis.

### 2.13.4.1 Effective Cost by Service and Region

Aggregates EffectiveCost by billing period to align accrual-based cost reporting with invoice cycles.

```
SELECT
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(PricingQuantity) AS TotalPricingQuantity
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit
```
### 2.13.4.2 Commitment Discount Effective Cost Breakdown

Analyzes commitment discount amortization by charge period, capturing costs based on when resources were consumed.

```
SELECT
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CommitmentDiscountId IS NOT NULL
  AND ChargeCategory = 'Usage'
GROUP BY
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd
```