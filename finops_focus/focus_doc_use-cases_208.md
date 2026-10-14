---
title: Report subaccounts by region
url: https://focus.finops.org/docs/use-cases/v1-4/report-subaccounts-by-region/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "6651c3f5bca389cf"
---
1. Use Cases
2. Governance, Policy & Risk
3. Report subaccounts by region

# Report subaccounts by region

## FOCUS Versions

v1.3
                            v1.4

## Context

FinOps Practitioners must identify if there are any data residency/ localization/ sovereignty inconsistencies. In order to identify any potential anomalies, they would like to see if the resource being billed for exists in the same geography as the primary payer account. If they do not exist in the same geography, the team would like it flagged for analysis.


## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  SubAccountId,
  RegionId,
  RegionName,
  COUNT(1)
FROM focus_data_table
WHERE ChargePeriodStart  >= ? AND ChargePeriodEnd < ?
GROUP BY
  ServiceProviderName,
  SubAccountId,
  RegionId,
  RegionName
```