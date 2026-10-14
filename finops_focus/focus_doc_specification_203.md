---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/custom-columns/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: a0c063762b905c8f
---
# 2.9 Custom Columns

Since:
                    0.5

## 2.9.1 Description

FOCUS supports the inclusion of custom columns to facilitate reporting capability that is not covered by the columns included in the specification. See Dataset Completeness for requirements on when custom columns should be included.

## 2.9.2 Directly Dependent Columns

x\_CustomColumn

## 2.9.3 Example SQL Query

### Example SQL Query

```
SELECT
  BillingPeriodStart,
  x_CustomColumn,
  SUM(BilledCost) AS TotalBilledCost,
FROM focus_data_table
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  x_CustomColumn
ORDER BY MonthlyCost DESC
```