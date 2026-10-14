---
title: Analyze costs by availability zone for a subaccount
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-costs-by-availability-zone-for-a-subaccount/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "174825b6aeb69886"
---
1. Use Cases
2. Usage Optimization
3. Analyze costs by availability zone for a subaccount

# Analyze costs by availability zone for a subaccount

## FOCUS Versions

v1.3
                            v1.4

## Context

It is good practice for Engineering to monitor cost and usage of services by availability zone for all regions to ensure:

- there isn’t any cost/usage occurring outside of the expected locations
- your costs are spread according to an expected ratio

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  RegionName,
  AvailabilityZone,
  BillingPeriodStart,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE SubAccountId = ?
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
GROUP BY
  ServiceProviderName,
  RegionName,
  AvailabilityZone,
  BillingPeriodStart
 ORDER BY ServiceProviderName,
  RegionName,
  AvailabilityZone,
  BillingPeriodStart
```