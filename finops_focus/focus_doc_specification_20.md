---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/pricing-currency-contract-commitment-cost/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3163a09f3bd7793f"
---
# 3.3.29 Pricing Currency Contract Commitment Cost

Dataset:
                    Contract Commitment

Column Type:
                    Metric

Feature Level:
                    Conditional

Data Type:
                    Decimal

Since:
                    1.4

Pricing Currency Contract Commitment Cost represents the monetary value of the *contract commitment* denominated in the *Pricing Currency*. This metric is used to track progress towards fulfilling contractual milestones using the original negotiated value, independent of currency exchange rate fluctuations.

## 3.3.29.1 Requirements

PricingCurrencyContractCommitmentCost MUST adhere to the following requirements:

- PricingCurrencyContractCommitmentCost MUST be of type Decimal.
- PricingCurrencyContractCommitmentCost MUST conform to NumericFormat requirements.
- PricingCurrencyContractCommitmentCost MUST adhere to the following nullability requirements:
  - PricingCurrencyContractCommitmentCost MUST NOT be null when ContractCommitmentCategory is "Spend" and PricingCurrency is provided.
  - PricingCurrencyContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
- PricingCurrencyContractCommitmentCost MUST be denominated in the PricingCurrency.

## 3.3.29.4 Description

The monetary value of the *contract commitment* in the Pricing Currency.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |