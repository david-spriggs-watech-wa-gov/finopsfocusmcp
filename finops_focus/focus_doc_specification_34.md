---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/resource-usage/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "220d77f63db679a4"
---
# 2.19 Resource Usage

Since:
                    1.0

## 2.19.1 Description

FOCUS enables tracking of resource consumption by providing information about which resources were used, in what quantities, and with what units of measure.

## 2.19.2 Directly Dependent Columns

## 2.19.3 Supporting Columns

## 2.19.4 Example SQL Query

### Example SQL Query

```
SELECT
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit,
  SUM(ConsumedQuantity) AS TotalQuantity
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit
```