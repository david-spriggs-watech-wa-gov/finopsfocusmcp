---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/sku-price-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: d6c341afb8f46961
---
# 3.1.61 SKU Price ID

SKU Price ID is a service-provider-specified unique identifier that represents a specific *SKU Price* associated with a *resource* or *service* used or purchased. It serves as a key reference for a *SKU Price* in a *price list* published by a service provider, allowing practitioners to look up detailed information about the *SKU Price*.

The composition of properties associated with the SKU Price ID may differ across service providers and across *SKUs* within the same service provider. However, the exclusion of dynamic or negotiable pricing properties - such as unit price amount; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts) - ensures that the SKU Price ID remains consistent across different billing periods and billing accounts within a service provider. This consistency enables efficient filtering of *charges* to track price fluctuations (e.g., changes in unit price amounts) over time and across billing accounts, for both list and contracted unit prices. Additionally, the SKU Price ID is commonly used to analyze costs based on pricing properties such as *periods* and tiers.

## 3.1.61.1 Requirements

SkuPriceId MUST adhere to the following requirements:

- SkuPriceId MUST be of type String.
- SkuPriceId MUST conform to StringHandling requirements.
- SkuPriceId MUST adhere to the following nullability requirements:
  - SkuPriceId MUST be null when ChargeCategory is "Tax".
  - SkuPriceId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - SkuPriceId MAY be null in all other cases.
- When SkuPriceId is not null, SkuPriceId MUST adhere to the following requirements:
  - SkuPriceId MUST have one and only one parent SkuId.
  - SkuPriceId MUST remain consistent over time.
  - SkuPriceId MUST remain consistent across *billing accounts* or contracts.
  - SkuPriceId MAY match SkuId.
  - SkuPriceId MUST be associated with a given *resource* or *service* when ChargeCategory is "Usage" or "Purchase".
  - SkuPriceId MUST reference a *SKU Price* in a service-provider-supplied *price list*, enabling the lookup of detailed information about the *SKU Price*.
  - SkuPriceId MUST be a valid reference to the ListUnitPrice when the service provider publishes unit prices exclusive of discounts.
  - SkuPriceId MUST be a valid reference to the ContractedUnitPrice when the service provider supports negotiated pricing concepts.

See Examples: Commitment Discount Flexibility for more details around *commitment discount flexibility*.

## 3.1.61.4 Description

A service-provider-specified unique identifier that represents a specific *SKU Price* associated with a *resource* or *service* used or purchased.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |