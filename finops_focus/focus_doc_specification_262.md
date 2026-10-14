---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/charge-period-start/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2024-01-01"
fingerprint: dd5a117af27fec8d
---
# 2.13 Charge Period Start

Charge Period Start represents the *inclusive* start date and time within a *charge period*. For example, a time period where ChargePeriodStart is '2024-01-01T00:00:00Z' and ChargePeriodEnd is '2024-01-02T00:00:00Z' includes charges for January 1, since ChargePeriodStart is *inclusive*, but does not include charges for January 2 since ChargePeriodEnd is *exclusive*.

ChargePeriodStart MUST be present in the billing data, MUST be of type Date/Time, MUST be an *inclusive* value, and MUST NOT contain null values. ChargePeriodStart MUST match the beginning date and time boundary of the effective period of the charge.

## 2.13.3 Description

The *inclusive* start date and time within a *charge period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |