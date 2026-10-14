---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/cost-and-usage/billing-account-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2026-01-01"
fingerprint: f590d9032a3334c1
---
# 2.4 Billing Account Name

A Billing Account Name is a display name assigned to a *billing account*. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

The BillingAccountName column MUST be present in the billing data and MUST NOT be null when the provider supports assigning a display name for the *billing account*. This column MUST be of type String. BillingAccountName MUST be unique within a customer when a customer has more than one *billing account*.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 2.4.3 Description

The display name assigned to a *billing account*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |