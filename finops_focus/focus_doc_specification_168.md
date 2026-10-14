---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-0/columns/sku-id/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.0
date: "2026-01-01"
fingerprint: "781e4988c2f63e61"
---
# 2.39 SKU ID

A SKU ID is a unique identifier that defines a provider-supported construct for organizing properties that are common across one or more *SKU Prices*. SKU ID can be referenced on a catalog or *price list* published by a provider to look up detailed information about the SKU. The composition of the properties associated with the SKU ID may differ across providers. Some providers may not support the *SKU* construct and instead associate all such properties directly with the *SKU Price*. SKU ID is commonly used for analyzing cost based on *SKU*-related properties above the pricing constructs.

The SkuId column MUST be present in the billing data when the provider publishes a SKU list. This column MUST be of type String. It MUST NOT be null when ChargeClass is not "Correction" and ChargeCategory is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory. SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

## 2.39.3 Description

A unique identifier that defines a provider-supported construct for organizing properties that are common across one or more *SKU Prices*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |