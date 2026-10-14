---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/list-unit-price/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2ec54d3a1094e659"
---
# 3.1.41 List Unit Price

The List Unit Price represents the suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. This price is denominated in the Billing Currency. The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## 3.1.41.1 Requirements

ListUnitPrice MUST adhere to the following requirements:

- ListUnitPrice MUST be of type Decimal.
- ListUnitPrice MUST conform to NumericFormat requirements.
- ListUnitPrice MUST adhere to the following nullability requirements:
  - ListUnitPrice MUST be null when SkuPriceId is null.
  - ListUnitPrice MUST be null when ChargeCategory is "Tax".
  - ListUnitPrice MUST NOT be null when SkuPriceId is not null.
  - ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - ListUnitPrice MAY be null in all other cases.
- When ListUnitPrice is not null, ListUnitPrice MUST adhere to the following requirements:
  - ListUnitPrice MUST be a non-negative decimal value.
  - ListUnitPrice MUST be denominated in the BillingCurrency.

## 3.1.41.2 Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## 3.1.41.5 Description

The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid non-negative decimal value |