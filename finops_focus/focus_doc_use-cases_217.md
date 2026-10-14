---
title: Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)
url: https://focus.finops.org/docs/use-cases/v1-4/compare-commitment-opportunities-across-providers-cross-provider-with-saas/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: b9e8a4696ef53e80
---
1. Use Cases
2. Rate Optimization
3. Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

# Compare Commitment Opportunities Across Providers (Cross-Provider with SaaS)

## FOCUS Versions

v1.4

## Context

Aggregates eligible spend and uncovered eligible spend across all providers, including SaaS platforms. A practitioner managing both CSP and SaaS workloads can identify where uncovered eligible spend is concentrated across commitment program types. When a charge is eligible for multiple commitment program types, it appears once per eligible type; removing the EligibleProgramType grouping without deduplicating would inflate totals.

## FOCUS SQL Query

```
WITH CommitmentDiscountEligible AS (
  SELECT
    CU.ServiceProviderName,
    JSON_VALUE(CP, '$.ProgramType') AS ProgramType,
    CU.EffectiveCost,
    -- EffectiveCost = BilledCost for uncovered rows; used here for ratio consistency
    CASE WHEN CU.CommitmentDiscountId IS NULL THEN CU.EffectiveCost ELSE 0 END AS UncoveredCost
  FROM focus_data_table CU
  CROSS JOIN
    UNNEST(JSON_EXTRACT_ARRAY(CU.CommitmentProgramEligibilityDetails, '$.CommitmentPrograms')) AS CP
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd < ?
    AND CU.ChargeCategory = 'Usage'
    AND CU.CommitmentProgramEligibilityDetails IS NOT NULL
    -- Replace with provider-specific discount-bearing program types
    AND JSON_VALUE(CP, '$.ProgramType') IN ('FlexibleSpendPlan', 'ResourceReservation')
)
SELECT
  ServiceProviderName,
  ProgramType AS EligibleProgramType,
  SUM(EffectiveCost) AS EligibleCost,
  SUM(UncoveredCost) AS UncoveredEligibleCost,
  SUM(UncoveredCost) / NULLIF(SUM(EffectiveCost), 0) AS UncoveredRate
FROM CommitmentDiscountEligible
GROUP BY ServiceProviderName, ProgramType
ORDER BY UncoveredEligibleCost DESC
```