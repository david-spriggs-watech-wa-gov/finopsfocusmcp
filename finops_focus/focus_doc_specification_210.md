---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/pricing-currency-list-unit-price/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b0535c5bf46deb7f
---
# 3.1.46 Pricing Currency List Unit Price

The Pricing Currency List Unit Price represents the suggested service-provider-published unit price for a single Pricing Unit of the associated *SKU*, exclusive of any discounts. This price is denominated in the Pricing Currency. The Pricing Currency List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## 3.1.46.1 Requirements

PricingCurrencyListUnitPrice MUST adhere to the following requirements:

- PricingCurrencyListUnitPrice MUST be of type Decimal.
- PricingCurrencyListUnitPrice MUST conform to NumericFormat requirements.
- PricingCurrencyListUnitPrice MUST adhere to the following nullability requirements:
  - PricingCurrencyListUnitPrice MUST be null when SkuPriceId is null.
  - PricingCurrencyListUnitPrice MUST be null when ChargeCategory is "Tax".
  - PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.
  - PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - PricingCurrencyListUnitPrice MAY be null in all other cases.
- When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice MUST adhere to the following requirements:
  - PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  - PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

## 3.1.46.2 Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## 3.1.46.5 Description

The suggested service-provider-published unit price for a single Pricing Unit of the associated *SKU*, exclusive of any discounts and expressed in Pricing Currency.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid non-negative decimal value |