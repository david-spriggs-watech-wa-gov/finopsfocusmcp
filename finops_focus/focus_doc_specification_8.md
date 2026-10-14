---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-account-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: fd928d2b68f77e81
---
# 3.1.8 Billing Account ID

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

A Billing Account ID is an invoice-issuer-assigned identifier for a *billing account*. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## 3.1.8.1 Requirements

BillingAccountId MUST adhere to the following requirements:

- BillingAccountId MUST be of type String.
- BillingAccountId MUST conform to StringHandling requirements.
- BillingAccountId MUST NOT be null.
- BillingAccountId MUST be a unique identifier within an *invoice issuer*.
- BillingAccountId SHOULD be a fully-qualified identifier.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 3.1.8.4 Description

The identifier assigned to a *billing account* by the invoice issuer.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |