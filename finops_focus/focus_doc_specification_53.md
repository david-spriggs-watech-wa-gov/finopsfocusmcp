---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/allocated-resource-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f95b28b288f728b3
---
# 3.1.3 Allocated Resource ID

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.3

An Allocated Resource ID is an identifier assigned by the data generator which cost is being allocated to in a Data Generator-Calculated Split Cost Allocation. The Allocated Resource ID is used to understand what the cost is being allocated to in *charges* where the data generator is allocating costs to something other than the *charge's* ResourceID, as is the case for allocated charges.

## 3.1.3.1 Requirements

AllocatedResourceId MUST adhere to the following requirements:

- AllocatedResourceId MUST be of type String.
- AllocatedResourceId MUST conform to StringHandling requirements.
- AllocatedResourceId MUST adhere to the following nullability requirements:
  - AllocatedResourceId MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  - AllocatedResourceId MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  - AllocatedResourceId MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
- When AllocatedResourceId is not null, AllocatedResourceId MUST adhere to the following requirements:
  - AllocatedResourceId SHOULD be a locally unique identifier within the associated ResourceId and ChargePeriod.
  - AllocatedResourceId MAY NOT be unique across ResourceId or ChargePeriod values.

## 3.1.3.4 Description

The identifier of the object to which cost is allocated in data generator-calculated split cost allocation.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |