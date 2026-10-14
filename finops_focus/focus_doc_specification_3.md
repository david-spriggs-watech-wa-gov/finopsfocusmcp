---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/capacity-reservation-status/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2015-01-03"
fingerprint: e861f10a002648e9
---
# 3.1.15 Capacity Reservation Status

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

Capacity Reservation Status indicates whether the *charge* represents either the consumption of the *capacity reservation* identified in the CapacityReservationId column or when the *capacity reservation* is unused.

## 3.1.15.1 Requirements

CapacityReservationStatus MUST adhere to the following requirements:

- CapacityReservationStatus MUST be of type String.
- CapacityReservationStatus MUST adhere to the following nullability requirements:
  - CapacityReservationStatus MUST be null when CapacityReservationId is null.
  - CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and ChargeCategory is "Usage".
- When CapacityReservationStatus is not null, CapacityReservationStatus MUST adhere to the following requirements:
  - CapacityReservationStatus MUST be one of the allowed values.
  - CapacityReservationStatus MUST be "Unused" when the *charge* represents the unused portion of a *capacity reservation*.
  - CapacityReservationStatus MUST be "Used" when the *charge* represents the used portion of a *capacity reservation*.

## 3.1.15.2 Allowed Values

| Value | Description | 
|---|---|
| Used | *Charges* that utilized a specific amount of a *capacity reservation*. | 
| Unused | *Charges* that represent the unused portion of a *capacity reservation*. | 

## 3.1.15.5 Description

Indicates whether the *charge* represents either the consumption of a *capacity reservation* or when a *capacity reservation* is unused.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | Allowed values |