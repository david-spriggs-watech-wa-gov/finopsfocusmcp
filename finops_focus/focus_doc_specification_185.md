---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-account-type/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2010-01-03"
fingerprint: adb0880968736631
---
# 3.1.10 Billing Account Type

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

Billing Account Type is an invoice-issuer-assigned name to identify the type of *billing account*. Billing Account Type is a readable display name and not a code. Billing Account Type is commonly used for scenarios like mapping FOCUS and provider constructs, summarizing costs across providers, or invoicing and chargeback.

## 3.1.10.1 Requirements

BillingAccountType MUST adhere to the following requirements:

- BillingAccountType MUST be of type String.
- BillingAccountType MUST conform to StringHandling requirements.
- BillingAccountType MUST adhere to the following nullability requirements:
  - BillingAccountType MUST be null when BillingAccountId is null.
  - BillingAccountType MUST NOT be null when BillingAccountId is not null.
- BillingAccountType MUST be a consistent, readable display value.

## 3.1.10.4 Description

An invoice-issuer-assigned name to identify the type of *billing account*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |