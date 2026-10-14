---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/pricing-currency-contracted-unit-price/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "1864e0db70015a6c"
---
# 3.1.44 Pricing Currency Contracted Unit Price

The Pricing Currency Contracted Unit Price represents the agreed-upon unit price for a single Pricing Unit of the associated *SKU*, inclusive of *negotiated discounts*, if present, while excluding negotiated *commitment discounts* or any other discounts. This price is denominated in the Pricing Currency. When negotiated discounts do not apply to unit prices and instead are applied to exchange rates, the Pricing Currency Contracted Unit Price defaults to the Pricing Currency List Unit Price. The Pricing Currency Contracted Unit Price is commonly used to calculate savings based on negotiation activities.

## 3.1.44.1 Requirements

PricingCurrencyContractedUnitPrice MUST adhere to the following requirements:

- PricingCurrencyContractedUnitPrice MUST be of type Decimal.
- PricingCurrencyContractedUnitPrice MUST conform to NumericFormat requirements.
- PricingCurrencyContractedUnitPrice MUST adhere to the following nullability requirements:
  - PricingCurrencyContractedUnitPrice MUST be null when SkuPriceId is null.
  - PricingCurrencyContractedUnitPrice MUST be null when ChargeCategory is "Tax".
  - PricingCurrencyContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  - PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - PricingCurrencyContractedUnitPrice MAY be null in all other cases.
- When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice MUST adhere to the following requirements:
  - PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  - PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.

## 3.1.44.2 Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## 3.1.44.5 Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of *negotiated discounts*, if present, while excluding negotiated *commitment discounts* or any other discounts, and expressed in Pricing Currency.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid non-negative decimal value |