---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/commit-usage-and-under-usage/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "4381b3fe2b45d884"
---
# 2.4 Commit Usage and Under Usage

Since:
                    1.0

## 2.4.1 Description

FOCUS supports the tracking of commitment discounts usage and under usage, which can come in the form of commitment discounts or capacity reservations.

## 2.4.2 Directly Dependent Columns

## 2.4.3 Supporting Columns

## 2.4.4 Example SQL Query for Commitment Discounts

### Example SQL Query for Commitment Discounts

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CommitmentDiscountStatus = 'Unused'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType
```
## 2.4.5 Example SQL Query for Capacity Reservations

### Example SQL Query for Capacity Reservations

```
SELECT
  ServiceProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CapacityReservationStatus = 'Unused'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus
```