---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/pricing-currency/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3974c02ae6672a3b"
---
# 3.1.43 Pricing Currency

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.2

Pricing Currency is the *national* or *virtual currency* denomination that a *resource* or *service* was priced in. Pricing Currency is commonly used in scenarios where different currencies are used for pricing and billing.

## 3.1.43.1 Requirements

PricingCurrency MUST adhere to the following requirements:

- PricingCurrency MUST be of type String.
- PricingCurrency MUST conform to StringHandling requirements.
- PricingCurrency MUST conform to CurrencyFormat requirements.
- PricingCurrency MUST NOT be null.

## 3.1.43.4 Description

The *national* or *virtual currency* denomination that a *resource* or *service* was priced in.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Currency Format |