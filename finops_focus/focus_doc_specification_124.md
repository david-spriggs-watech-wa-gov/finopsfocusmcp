---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/pricing-currency/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3d7a88baf667a83b"
---
# 3.3.28 Pricing Currency

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.4

Pricing Currency is the national or virtual currency denomination that a *contract commitment* was priced in. This is commonly used in scenarios where a commitment is negotiated in one currency but billed in another.

## 3.3.28.1 Requirements

PricingCurrency MUST adhere to the following requirements:

- PricingCurrency MUST be of type String.
- PricingCurrency MUST conform to StringHandling requirements.
- PricingCurrency MUST conform to CurrencyFormat requirements.
- PricingCurrency MUST NOT be null.

## 3.3.28.4 Description

The national or virtual currency denomination that the Contract Commitment Cost was priced in.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Currency Format |