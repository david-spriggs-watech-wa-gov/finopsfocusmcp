---
title: Analyze cost per compute service for a subaccount
url: https://focus.finops.org/docs/use-cases/v1-4/cost-compute-subaccount/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "628e217cf583d185"
---
1. Use Cases
2. Usage Optimization
3. Analyze cost per compute service for a subaccount

# Analyze cost per compute service for a subaccount

## FOCUS Versions

v1.0
                            v1.1
                            v1.2
                            v1.3
                            v1.4

## Context

Compute spend tends to be the largest component of spend in most cloud bills. Drilling into the resource-level view of cost for a given day can provide a detailed view of the heaviest spending compute resources, including a view of which time periods the consumption was at its highest level.

## FOCUS SQL Query

```
SELECT
  Min(ChargePeriodStart),
  Max(ChargePeriodEnd),
  ServiceName,
  ResourceId,
  ResourceName,
  SUM(PricingQuantity),
  SUM(EffectiveCost) AS MonthlyEffectiveCost
FROM focus_data_table
WHERE SubAccountId = ?
  AND ServiceCategory = 'Compute'
  AND ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  ServiceName,
  ResourceId,
  ResourceName
ORDER BY MonthlyEffectiveCost DESC
```
## FOCUS Datasets

## FOCUS Columns

## Related Capabilities

## Related Personas

## Related KPIs

Effective Average Compute Cost per Core
                                            Track average cost, after amortization of unused commitment discounts, of each Core per calendar month.

Percent of Compute Spend Covered by Commitment Discounts
                                            Measures the percentage of compute cost (excluding Spot) covered by commitment discount for the previous month.

Percentage of Legacy Resource
                                            Measure of the percentage of resources running on ‘modern’ types (e.g. instance types, volume type).

Percentage Resource Utilization
                                            Measure of cloud compute resource utilization, e.g. Compute (EC2), Block Storage (EBS), or Object Storage (S3).