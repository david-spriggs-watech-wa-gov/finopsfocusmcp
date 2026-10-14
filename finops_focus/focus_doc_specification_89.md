---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/service-provider-services/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2710e1d4b9502de7"
---
# 2.22 Service Provider Services

Since:
                    0.5

## 2.22.1 Description

FOCUS supports service providers specifying the services and product offerings that they provide their customers that align with the names practitioners are familiar with. This empowers practitioners to analyze cost by service, report service costs by subaccount, forecast based on historical trends by service, and verify accuracy of services charged across service providers.

## 2.22.2 Directly Dependent Columns

## 2.22.3 Supporting Columns

## 2.22.4 Example SQL Query

### Example SQL Query

```
SELECT
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName
ORDER BY MonthlyCost DESC
```