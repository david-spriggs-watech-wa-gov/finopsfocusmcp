---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/sku-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "67d4991bef46ee1"
---
# 3.1.58 SKU ID

A SKU ID is a service-provider-specified unique identifier that represents a specific *SKU*. *SKUs* are quantifiable goods or service offerings in a Cost and Usage *FOCUS dataset* that represent specific functionality and technical specifications. Examples of *SKUs* include but are not limited to:

- A product license that is purchased or subscribed to.
- Usage of a deployed resource from direct user interaction (e.g., request count).
- Usage by a deployed resource based on the resource's configuration (e.g., running hours, storage space).

Each SKU ID represents a unique set of features that can be sold at different price points or *SKU Prices*. SKU ID is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

- Date the *charge* was incurred.
- Pricing tiers (e.g., free tier or volume-based tiers).
- Commitment discount pricing *period* (e.g., 1 year, 3 years).
- Negotiated discounts or other contractual terms or conditions.

SKU ID should be consistent across pricing variations of a good or service to facilitate price comparisons for the same functionality, like where the functionality is provided or how it's paid for. SKU ID can be referenced on a catalog or *price list* published by a service provider to look up detailed information about the *SKU*. The composition of the properties associated with the SKU ID may differ across service providers. SKU ID is commonly used for analyzing and comparing costs for the same SKU across different price details (e.g., *period*, tier, location).

## 3.1.58.1 Requirements

SkuId MUST adhere to the following requirements:

- SkuId MUST be of type String.
- SkuId MUST conform to StringHandling requirements.
- SkuId MUST adhere to the following nullability requirements:
  - SkuId MUST be null when ChargeCategory is "Tax".
  - SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - SkuId MAY be null in all other cases.
- SkuId for a given *SKU* MUST adhere to the following requirements:
  - SkuId MUST remain consistent across *billing accounts* or contracts.
  - SkuId MUST remain consistent across PricingCategory values.
  - SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
- SkuId MUST be associated with a given *resource* or *service* when ChargeCategory is "Usage" or "Purchase".
- SkuId MAY match SkuPriceId.

## 3.1.58.4 Description

Service-provider-specified unique identifier that represents a specific *SKU* (e.g., a quantifiable good or service offering).

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |