---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/service-categorization/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "6a14a35c281378c5"
---
# 2.21 Service Categorization

Since:
                    1.1

## 2.21.1 Description

FOCUS provides a structure for categorizing services based on their core functions. By classifying services into high-level categories and more granular subcategories, practitioners can organize costs according to functional areas. This standardized categorization provides data that practitioners can use in their cost management processes and decision making.

## 2.21.2 Directly Dependent Columns

## 2.21.3 Supporting Columns

## 2.21.4 Example SQL Query

### Example SQL Query

```
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? and BillingPeriodEnd < ?
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency
```