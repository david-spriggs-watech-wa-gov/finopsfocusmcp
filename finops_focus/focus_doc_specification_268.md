---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/cost-and-usage/billing-account-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2026-01-01"
fingerprint: f59a882168377c81
---
# 2.3 Billing Account ID

A Billing Account ID is a provider-assigned identifier for a *billing account*. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

The BillingAccountId column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values. BillingAccountId MUST be a globally unique identifier within a provider.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 2.3.3 Description

The identifier assigned to a *billing account* by the provider.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |