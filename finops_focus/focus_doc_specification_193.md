---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/resource-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "70dd4c0aa2fe60e3"
---
# 3.1.52 Resource Name

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    0.5

The Resource Name is a display name assigned to a *resource*. It is commonly used for cost analysis, reporting, and allocation scenarios.

## 3.1.52.1 Requirements

ResourceName MUST adhere to the following requirements:

- ResourceName MUST be of type String.
- ResourceName MUST conform to StringHandling requirements.
- ResourceName MUST adhere to the following nullability requirements:
  - ResourceName MUST be null when ResourceId is null or when the *resource* does not have an assigned display name.
  - ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
- ResourceName MUST NOT duplicate ResourceId when the *resource* is not provisioned interactively or only has a system-generated ResourceId.

## 3.1.52.4 Description

Display name assigned to a *resource*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |