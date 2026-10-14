---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/sub-account-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: bd11882508f73ca9
---
# 3.1.62 Sub Account ID

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

A Sub Account ID is a service-provider-assigned identifier assigned to a *sub account*. Sub Account ID is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

## 3.1.62.1 Requirements

SubAccountId MUST adhere to the following requirements:

- SubAccountId MUST be of type String.
- SubAccountId MUST conform to StringHandling requirements.
- SubAccountId MUST adhere to the following nullability requirements:
  - SubAccountId MUST be null when a *charge* is not related to a *sub account*.
  - SubAccountId MUST NOT be null when a *charge* is related to a *sub account*.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 3.1.62.4 Description

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |