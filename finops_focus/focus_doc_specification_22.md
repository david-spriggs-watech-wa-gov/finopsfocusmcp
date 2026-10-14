---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/pricing-currency-effective-cost/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2100c97f222b3aeb"
---
# 3.1.45 Pricing Currency Effective Cost

Pricing Currency Effective Cost represents the Pricing Currency-denominated equivalent of Effective Cost. It reflects the cost of a *charge* based on the *resources* used, *services* used, or *contract commitments* recognized in a given *charge period*.

Because Pricing Currency Effective Cost differs from Effective Cost only in denomination, it follows the same pricing adjustments, amortizations, and exclusions. This column provides practitioners with a standardized baseline, allowing them to view costs in a uniform currency, whether converting from a *virtual currency* to a *national currency* (e.g., tokens to USD) or from one national currency to another (e.g., EUR to USD).

Pricing Currency Effective Cost is commonly used to support FinOps activities, including *accrual-based* reporting, forecasting, and cost allocation when pricing and billing use different currencies.

## 3.1.45.1 Requirements

PricingCurrencyEffectiveCost MUST adhere to the following requirements:

- PricingCurrencyEffectiveCost MUST be of type Decimal.
- PricingCurrencyEffectiveCost MUST conform to NumericFormat requirements.
- PricingCurrencyEffectiveCost MUST NOT be null.
- PricingCurrencyEffectiveCost MUST be denominated in the PricingCurrency.
- PricingCurrencyEffectiveCost MUST be the PricingCurrency-denominated equivalent of EffectiveCost.

## 3.1.45.4 Description

The PricingCurrency-denominated equivalent of Effective Cost, representing the cost of a *charge* based on the *resources* used, *services* used, or *contract commitments* recognized in a given *charge period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |