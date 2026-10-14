---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/service-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: bd06e018710b4d7d
---
# 3.1.56 Service Name

A *service* represents an offering that can be purchased from a service provider (e.g., cloud virtual machine, SaaS database, professional services from a systems integrator). A *service* offering can include various types of usage or other *charges*. For example, a cloud database *service* may include compute, storage, and networking *charges*.

The Service Name is a display name for the offering that was purchased. The Service Name is commonly used for scenarios like analyzing aggregate cost trends over time and filtering data to investigate anomalies.

## 3.1.56.1 Requirements

ServiceName MUST adhere to the following requirements:

- ServiceName MUST be of type String.
- ServiceName MUST conform to StringHandling requirements.
- ServiceName MUST NOT be null.
- The relationship between ServiceName and ServiceCategory MUST adhere to the following requirements:
  - ServiceName MUST have one and only one ServiceCategory that best aligns with its primary purpose, except when no suitable ServiceCategory is available.
  - ServiceName MUST be associated with the ServiceCategory "Other" when no suitable ServiceCategory is available.
- The relationship between ServiceName and ServiceSubcategory MUST adhere to the following requirements:
  - ServiceName SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose, except when no suitable ServiceSubcategory is available.
  - ServiceName SHOULD be associated with the ServiceSubcategory "Other" when no suitable ServiceSubcategory is available.

## 3.1.56.4 Description

An offering that can be purchased from a service provider (e.g., cloud virtual machine, SaaS database, professional *services* from a systems integrator).

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |