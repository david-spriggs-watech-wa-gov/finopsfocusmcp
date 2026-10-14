---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/location/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "37000a760ad23884"
---
# 2.15 Location

Since:
                    1.0

## 2.15.1 Description

FOCUS provides structured location data through region and availability zone information. By documenting geographic deployment locations, practitioners can organize and analyze costs based on where resources and services are deployed. This standardized location data helps practitioners understand the geographical distribution of infrastructure across host providers.

## 2.15.2 Directly Dependent Columns

## 2.15.3 Supporting Columns

## 2.15.4 Example SQL Query

### Example SQL Query

```
SELECT
  RegionId,
  RegionName,
  AvailabilityZone,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  RegionId,
  RegionName,
  AvailabilityZone
```