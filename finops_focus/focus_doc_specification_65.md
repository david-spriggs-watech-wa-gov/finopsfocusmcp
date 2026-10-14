---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/sub-account-type/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f1d080ab8852202b
---
# 3.1.64 Sub Account Type

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.2

Sub Account Type is a service-provider-assigned name to identify the type of *sub account*. Sub Account Type is a readable display name and not a code. Sub Account Type is commonly used for scenarios like mapping FOCUS and service provider constructs, summarizing costs across service providers, or invoicing and chargeback.

## 3.1.64.1 Requirements

SubAccountType MUST adhere to the following requirements:

- SubAccountType MUST be of type String.
- SubAccountType MUST conform to StringHandling requirements.
- SubAccountType MUST adhere to the following nullability requirements:
  - SubAccountType MUST be null when SubAccountId is null.
  - SubAccountType MUST NOT be null when SubAccountId is not null.
- SubAccountType MUST be a consistent, readable display value.

## 3.1.64.4 Description

A service-provider-assigned name to identify the type of *sub account*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |