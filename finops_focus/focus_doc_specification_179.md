---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/capacity-reservation-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2014-01-03"
fingerprint: "7c63f00ec8d66865"
---
# 3.1.14 Capacity Reservation ID

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.1

A Capacity Reservation ID is the identifier assigned to a *capacity reservation* by the service provider. Capacity Reservation ID is commonly used for scenarios to allocate *charges* for capacity reservation usage.

## 3.1.14.1 Requirements

CapacityReservationId MUST adhere to the following requirements:

- CapacityReservationId MUST be of type String.
- CapacityReservationId MUST conform to StringHandling requirements.
- CapacityReservationId MUST adhere to the following nullability requirements:
  - CapacityReservationId MUST be null when a *charge* is not related to a *capacity reservation*.
  - CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
  - CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
- When CapacityReservationId is not null, CapacityReservationId MUST adhere to the following requirements:
  - CapacityReservationId MUST be a unique identifier within the service provider.
  - CapacityReservationId SHOULD be a fully-qualified identifier.

## 3.1.14.4 Description

The identifier assigned to a *capacity reservation* by the service provider.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |