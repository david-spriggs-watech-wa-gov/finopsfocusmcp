---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-account-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: ad9a992b683374c1
---
# 3.1.9 Billing Account Name

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    0.5

A Billing Account Name is a display name assigned to a *billing account*. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## 3.1.9.1 Requirements

BillingAccountName MUST adhere to the following requirements:

- BillingAccountName MUST be of type String.
- BillingAccountName MUST conform to StringHandling requirements.
- BillingAccountName MUST NOT be null when the *invoice issuer* supports assigning a display name for the *billing account*.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 3.1.9.4 Description

The display name assigned to a *billing account*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |