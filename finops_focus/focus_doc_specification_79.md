---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/service-provider-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b310a8c98061aca5
---
# 3.1.54 Service Provider Name

Service Provider Name is the name of the entity that provides the *resources* or *services* available for usage or purchase. These services can be built on top of infrastructure provided by a Host Provider; offered as fully integrated solutions; or include complementary offerings such as support, licensing, or consulting. It is commonly used for cost analysis and reporting scenarios.

**Notes:**

- In marketplace scenarios, the Service Provider represents the seller rather than the marketplace operator, as the marketplace operator merely provides a purchasing mechanism and does not itself provide the *resources* or *services* available for usage or purchase.
- In reseller scenarios, if the reseller is selling resource or services that are white-labeled from another provider, the Service Provider is the reseller.
- In all other scenarios, the Service Provider is the entity that produced the resources or services.

## 3.1.54.1 Requirements

ServiceProviderName MUST adhere to the following requirements:

- ServiceProviderName MUST be of type String.
- ServiceProviderName MUST conform to StringHandling requirements.
- ServiceProviderName MUST NOT be null.

See Appendix: Participating Entity Identification Examples section for examples of Service Provider Name values across various use case scenarios.

## 3.1.54.4 Description

The name of the entity that made the *resources* or *services* available for purchase or consumption.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |