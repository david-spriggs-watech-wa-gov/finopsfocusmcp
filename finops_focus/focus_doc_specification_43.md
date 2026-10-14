---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/region-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b9c10228c0fb5abb
---
# 3.1.50 Region Name

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.0

## 3.1.50.1 Requirements

RegionName MUST adhere to the following requirements:

- RegionName MUST be of type String.
- RegionName MUST conform to StringHandling requirements.
- RegionName MUST adhere to the following nullability requirements:
  - RegionName MUST be null when RegionId is null.
  - RegionName MUST NOT be null when RegionId is not null.

## 3.1.50.4 Description

The name of an isolated geographic area where a *resource* is provisioned or a *service* is provided.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |