---
title: Calculate Commitment Discount Coverage Rate with Eligibility-Adjusted Denominator
url: https://focus.finops.org/docs/use-cases/v1-4/calculate-commitment-discount-coverage-rate-with-eligibility-adjusted-denominator/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "7b2027572fe578d1"
---
1. Use Cases
2. Rate Optimization
3. Calculate Commitment Discount Coverage Rate with Eligibility-Adjusted Denominator

# Calculate Commitment Discount Coverage Rate with Eligibility-Adjusted Denominator

## FOCUS Versions

## Context

Computes a commitment discount coverage rate using only eligible charges as the denominator. Without eligibility data, practitioners typically divide covered spend by total spend, which produces a coverage rate that includes ineligible charges (e.g., storage services, support fees) in the denominator and may not reflect the actionable coverage opportunity. Targets discount-bearing programs only. Note: Unused commitment rows (CommitmentDiscountStatus = ‘Unused’) have CommitmentDiscountId populated and will artificially inflate both the numerator and the denominator if left in the dataset; practitioners should additionally filter these out for a true utilization-adjusted rate.

## FOCUS SQL Query

```
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    CU.EffectiveCost,
    CU.CommitmentDiscountId
  FROM focus_data_table CU
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    AND (
      -- Include covered rows in the denominator
      CU.CommitmentDiscountId IS NOT NULL
      -- If uncovered, check if the JSON array contains an eligible program type
      OR EXISTS (
        SELECT 1
        FROM UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
        WHERE JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
      )
    )
)
SELECT
  ServiceProviderName,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END) AS CoveredCost,
  SUM(EffectiveCost) AS EligibleCost,
  SUM(CASE WHEN CommitmentDiscountId IS NOT NULL THEN EffectiveCost ELSE 0 END)
    / NULLIF(SUM(EffectiveCost), 0) AS CommitmentCoverageRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName
```