---
title: Report service costs by providers subaccount
url: https://focus.finops.org/docs/use-cases/v1-4/report-service-costs-by-providers-subaccount-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "359881fcb8648aa6"
---
1. Use Cases
2. Reporting & Analytics
3. Report service costs by providers subaccount

# Report service costs by providers subaccount

## FOCUS Versions

v1.3
                            v1.4

## Context

Organizations wants to negotiate private pricing for a particular workload, a subaccount that carries specialized workloads, or their entire footprint. The cost metric used must amortize up-front and recurring fees to get an accurate view of the effective cost.

## FOCUS SQL Query

v1-3

```
SELECT 
  ServiceProviderName,
  ServiceName,
  SubAccountId,
  ChargePeriodStart,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND SubAccountId = ?
  AND ServiceProviderName = ?
GROUP BY 
  ServiceProviderName,
  ServiceName,
  SubAccountId,
  ChargePeriodStart
ORDER BY 
  SUM(EffectiveCost),
  BillingPeriodStart DESC
```
v1-4

```
SELECT 
  ServiceProviderName,
  ServiceName,
  SubAccountId,
  ChargePeriodStart,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND SubAccountId = ?
  AND ServiceProviderName = ?
GROUP BY 
  ServiceProviderName,
  ServiceName,
  SubAccountId,
  ChargePeriodStart
ORDER BY 
  SUM(EffectiveCost),
  BillingPeriodStart DESC
```