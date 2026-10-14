---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/contracted-unit-price/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f6f88d5b4c1d7805
---
# 3.1.34 Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of *negotiated discounts*, if present, while excluding negotiated *commitment discounts* or any other discounts. This price is denominated in the Billing Currency. The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the List Unit Price.

## 3.1.34.1 Requirements

ContractedUnitPrice MUST adhere to the following requirements:

- ContractedUnitPrice MUST be of type Decimal.
- ContractedUnitPrice MUST conform to NumericFormat requirements.
- ContractedUnitPrice MUST adhere to the following nullability requirements:
  - ContractedUnitPrice MUST be null when SkuPriceId is null.
  - ContractedUnitPrice MUST be null when ChargeCategory is "Tax".
  - ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  - ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  - ContractedUnitPrice MAY be null in all other cases.
- When ContractedUnitPrice is not null, ContractedUnitPrice MUST adhere to the following requirements:
  - ContractedUnitPrice MUST be a non-negative decimal value.
  - ContractedUnitPrice MUST be denominated in the BillingCurrency.

## 3.1.34.2 Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## 3.1.34.5 Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid non-negative decimal value |