---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/availability-zone/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: dd515eaaaeff3871
---
# 3.1.6 Availability Zone

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Recommended

Data Type:
                    String

Since:
                    0.5

An *availability zone* is a host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where *resources* are deployed.

## 3.1.6.1 Requirements

AvailabilityZone MUST adhere to the following requirements:

- AvailabilityZone MUST be of type String.
- AvailabilityZone MUST conform to StringHandling requirements.
- AvailabilityZone MUST be null when a *charge* is not specific to an *availability zone*.

## 3.1.6.4 Description

A host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Recommended | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |