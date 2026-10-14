---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/service-provider-name/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "335922280645eeb7"
---
# 3.3.30 Service Provider Name

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.4

Service Provider Name is the name of the entity that provides the resources or services available for usage or purchase. This entity is responsible for fulfilling the terms of the *contract commitment*, such as applying discounts, managing credit pools, or guaranteeing resource availability.

**Notes:**

- In marketplace scenarios, the Service Provider represents the seller of the commitment (e.g., Datadog, MongoDB) rather than the marketplace operator (e.g., AWS, Azure), unless the marketplace operator is the entity providing the specific commitment benefit.
- In reseller scenarios, if the commitment is made directly with a reseller for white-labeled services, the Service Provider is the reseller. Otherwise, it is the entity that produced the underlying services tied to the commitment.

## 3.3.30.1 Requirements

ServiceProviderName MUST adhere to the following requirements:

- ServiceProviderName MUST be of type String.
- ServiceProviderName MUST conform to StringHandling requirements.
- ServiceProviderName MUST NOT be null.

## 3.3.30.4 Description

The name of the entity that provides the *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | \\\<not specified> |