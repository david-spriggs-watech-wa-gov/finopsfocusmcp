---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/host-provider-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f1c12a892854ac64
---
# 3.1.36 Host Provider Name

Host Provider Name is the name of the entity that provides the underlying infrastructure on which the *resources* or *services* of the Service Provider are deployed.

In some instances, the host provider and the service provider are the same entity: the provider hosts their own services. In other instances, the host provider and the service provider are separate entities, though the service provider may or may not expose the host provider and/or allow the customer to select the host provider.

## 3.1.36.1 Requirements

HostProviderName MUST adhere to the following requirements:

- HostProviderName MUST be of type String.
- HostProviderName MUST conform to StringHandling requirements.
- HostProviderName MUST adhere to the following nullability requirements:
  - HostProviderName MAY be NULL when the associated ServiceName does not involve deployment on any underlying infrastructure (e.g., professional services, software licenses).
  - HostProviderName MAY be NULL when the information about the entity providing the underlying infrastructure cannot be uniquely determined (e.g., when the ChargeCategory is "Tax" or "Adjustment").
  - HostProviderName MUST NOT be null in all other cases.
- When HostProviderName is not null, HostProviderName values MUST adhere to the following requirements:
  - HostProviderName MUST reflect the name of the host provider when explicitly selected by the customer.
  - HostProviderName MUST reflect the name of the host provider when the service provider exposes the underlying hosting provider.
  - HostProviderName MUST match ServiceProviderName in all other cases.

See Appendix: Participating Entity Identification Examples section for examples of Host Provider values across various use case scenarios.

## 3.1.36.4 Description

The name of the entity whose *resources* are used by the Service Provider to make their *resources* or *services* available.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |