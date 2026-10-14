---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/resource-type/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f9d1e72a1a736bb9
---
# 3.1.53 Resource Type

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.0-preview

## 3.1.53.1 Requirements

ResourceType MUST adhere to the following requirements:

- ResourceType MUST be of type String.
- ResourceType MUST conform to StringHandling requirements.
- ResourceType MUST adhere to the following nullability requirements:
  - ResourceType MUST be null when ResourceId is null.
  - ResourceType MUST NOT be null when ResourceId is not null.

## 3.1.53.4 Description

The kind of *resource* the *charge* applies to.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |