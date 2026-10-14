---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/data-granularity/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3a80eee468b3b085"
---
# 2.11 Data Granularity

Since:
                    0.5

## 2.11.1 Description

FOCUS supports multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. FOCUS also supports the ability for cost and usage data to be provided for high granularity scenarios, such as down to the individual resources. It also supports high level granularity cost and usage data, such as account level, or service level charges.

## 2.11.2 Directly Dependent Columns

## 2.11.3 Supporting Columns

## 2.11.4 Example SQL Query

### Example SQL Query

```
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost)
FROM focus_data_table
Group by
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
```