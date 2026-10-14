---
title: Identify unused capacity reservations
url: https://focus.finops.org/docs/use-cases/v1-4/identify-unused-capacity-reservations-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: f205e37648d02ccd
---
1. Use Cases
2. Anomaly Management
3. Identify unused capacity reservations

# Identify unused capacity reservations

## FOCUS Versions

v1.3
                            v1.4

## Context

Identify all data in a time period where CapacityReservationStatus is ‘unused’ thus identifying capacity reservations that aren’t used and enabling the Practitioner to take action on either cancelling the reservation (if able), working with other personas on a workload that could use the reservation, or performing informed ignore (knowing it is there but ignoring it because there is nothing one can do).

## FOCUS SQL Query

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
  CapacityReservationStatus,
  CommitmentDiscountStatus
```