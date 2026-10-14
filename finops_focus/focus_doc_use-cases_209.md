---
title: Report costs by service category and subcategory
url: https://focus.finops.org/docs/use-cases/v1-4/report-costs-by-service-category-and-subcategory-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "534c85ec389424c7"
---
1. Use Cases
2. Reporting & Analytics
3. Report costs by service category and subcategory

# Report costs by service category and subcategory

## FOCUS Versions

v1.3
                            v1.4

## Context

Understanding costs across service providers, billing periods, and service categories (Analytics, Compute, Database, Storage, etc.) and service subcategories (Virtual Machines, Relational Databases, Content Delivery, etc) provides valuable insight into total costs.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  BillingCurrency,
  BillingPeriodStart,
  ServiceCategory,
  ServiceSubcategory,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? and BillingPeriodEnd  < ?
GROUP BY
  ServiceProviderName,
  BillingCurrency,
  BillingPeriodStart,
  ServiceCategory,
  ServiceSubcategory
ORDER BY TotalBilledCost DESC
```