---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/resource-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "33dd4f2e88ef29a3"
---
# 3.1.51 Resource ID

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

A Resource ID is an identifier assigned to a *resource* by the service provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.

## 3.1.51.1 Requirements

ResourceId MUST adhere to the following requirements:

- ResourceId MUST be of type String.
- ResourceId MUST conform to StringHandling requirements.
- ResourceId MUST adhere to the following nullability requirements:
  - ResourceId MUST be null when a *charge* is not related to a *resource*.
  - ResourceId MUST NOT be null when a *charge* is related to a *resource*.
- When ResourceId is not null, ResourceId MUST adhere to the following requirements:
  - ResourceId MUST be a unique identifier within the service provider.
  - ResourceId SHOULD be a fully-qualified identifier.
  - ResourceId MUST be the identifier of the *resource* that received the *commitment discount* when CommitmentDiscountStatus is "Used".

## 3.1.51.4 Description

Identifier assigned to a *resource* by the service provider.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |