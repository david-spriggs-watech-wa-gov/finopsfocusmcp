---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-description/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2018-01-03"
fingerprint: ffc3602a20f3791b
---
# 3.1.18 Charge Description

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.0-preview

A Charge Description provides a high-level context of a *row* without requiring additional discovery. This column is a self-contained summary of the *charge's* purpose and price. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.

## 3.1.18.1 Requirements

ChargeDescription MUST adhere to the following requirements:

- ChargeDescription MUST be of type String.
- ChargeDescription MUST conform to StringHandling requirements.
- ChargeDescription SHOULD NOT be null.
- ChargeDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## 3.1.18.4 Description

Self-contained summary of the *charge's* purpose and price.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |