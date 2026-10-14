---
title: Analyze tag coverage
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-tag-coverage/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "6764e572f8a33006"
---
1. Use Cases
2. Allocation
3. Analyze tag coverage

# Analyze tag coverage

## FOCUS Versions

v1.0
                            v1.1
                            v1.2
                            v1.3
                            v1.4

## Context

Analyzing the amount of costs for a provider that have been tagged with a specific tag can enable the FinOps practitioner to check the amount of costs being allocated via tags.

## FOCUS SQL Query

```
SELECT 
    SUM(CASE 
        WHEN JSON_CONTAINS_PATH(tags, 'one', '$.?') 
        THEN EffectiveCost 
        ELSE 0 
    END) / SUM(EffectiveCost) * 100 AS TaggedPercentage
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
     AND EffectiveCost > 0
     AND ProviderName = ?
```
v1-4

```
SELECT 
    SUM(CASE 
        WHEN JSON_CONTAINS_PATH(tags, 'one', '$.?') 
        THEN EffectiveCost 
        ELSE 0 
    END) / SUM(EffectiveCost) * 100 AS TaggedPercentage
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
     AND EffectiveCost > 0
     AND ServiceProviderName = ?
```
## FOCUS Datasets

## FOCUS Columns

## Related Capabilities

## Related Personas

## Related KPIs

Percentage of CSP Cloud Carbon that is Tagging Policy Compliant
                                            This KPI measures the amount of compliance for cloud sustainability tagging.

Percentage of CSP Cloud Costs that are Tagging Policy Compliant
                                            This KPI measures amount of compliance for cloud cost tagging, and requires an established organizational tagging policy.