---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/region-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "79410400ccdb64b3"
---
# 3.1.49 Region ID

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

## 3.1.49.1 Requirements

RegionId MUST adhere to the following requirements:

- RegionId MUST be of type String.
- RegionId MUST conform to StringHandling requirements.
- RegionId MUST adhere to the following nullability requirements:
  - RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  - RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

## 3.1.49.4 Description

Host-provider-assigned identifier for an isolated geographic area where a *resource* is provisioned or a *service* is provided.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |