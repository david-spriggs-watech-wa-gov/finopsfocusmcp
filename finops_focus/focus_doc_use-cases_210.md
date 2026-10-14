---
title: Identify Eligible Uncovered Spend by Program Type
url: https://focus.finops.org/docs/use-cases/v1-4/identify-eligible-uncovered-spend-by-program-type/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "32eea47e4125bc93"
---
1. Use Cases
2. Rate Optimization
3. Identify Eligible Uncovered Spend by Program Type

# Identify Eligible Uncovered Spend by Program Type

## FOCUS Versions

v1.4

## Context

Identifies charges that are eligible for commitment programs but are not currently covered by a commitment discount. A practitioner running relevant workloads can use this to quantify the savings opportunity per commitment program type (e.g., FlexibleSpendPlan vs. ResourceReservation) and per service. Filters to ‘Usage’ charges where CommitmentProgramEligibilityDetails is populated and CommitmentDiscountId is null. Uses BilledCost (not EffectiveCost) because the charges are uncovered, so BilledCost reflects the actual amount paid and the savings opportunity.

## FOCUS SQL Query

```
SELECT
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType') AS EligibleProgramType,
  SUM(CU.BilledCost) AS EligibleUncoveredCost
FROM focus_data_table CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
  AND CU.ChargeCategory = 'Usage'
  AND CU.CommitmentDiscountId IS NULL
  AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
  -- Replace with provider-specific discount-bearing program types
  AND JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
GROUP BY
  CU.ServiceProviderName,
  CU.ServiceName,
  JSON_VALUE(CP, '$.ProgramType')
ORDER BY EligibleUncoveredCost DESC
```