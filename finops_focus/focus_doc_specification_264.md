---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/cost-and-usage/sub-account-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2026-01-01"
fingerprint: fd18902528f72ca0
---
# 2.41 Sub Account ID

A Sub Account ID is a provider-assigned identifier assigned to a *sub account*. Sub Account ID is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

The SubAccountId column MUST be present in the billing data when the provider supports a *sub account* construct. This column MUST be of type String. If a charge does not apply to a *sub account*, the SubAccountId column MUST be null.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.

## 2.41.3 Description

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |