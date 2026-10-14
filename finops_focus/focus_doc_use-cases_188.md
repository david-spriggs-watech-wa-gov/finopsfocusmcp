---
title: Identify Eligible Capacity Reservation Spend
url: https://focus.finops.org/docs/use-cases/v1-4/identify-eligible-capacity-reservation-spend/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "74cfe57ee580b845"
---
1. Use Cases
2. Rate Optimization
3. Identify Eligible Capacity Reservation Spend

# Identify Eligible Capacity Reservation Spend

## FOCUS Versions

## Context

Identifies charges eligible for capacity-reservation commitment programs, distinguishing between used and unused reservations. Capacity reservations secure resource availability rather than provide discounts, and are tracked via CapacityReservationId and CapacityReservationStatus rather than the commitment discount columns. Filters CommitmentProgramEligibilityDetails to rows whose ProgramType values correspond to capacity-reservation programs (e.g., AdvanceResourceCommitment, ZonalResourceCommitment), then uses CapacityReservationId and CapacityReservationStatus to determine reservation utilization.

## FOCUS SQL Query

```
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  CU.CapacityReservationStatus,
  SUM(CU.BilledCost) AS BilledCost,
  COUNT(*) AS RowCount
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
  AND JSON_VALUE(CP, '$.ProgramType') IN ('AdvanceResourceCommitment', 'ZonalResourceCommitment')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType'),
  CU.CapacityReservationStatus
ORDER BY BilledCost DESC
```