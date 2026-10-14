---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/contracted-cost/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: af40041a24cbccc7
---
# 3.1.33 Contracted Cost

Contracted Cost represents the cost calculated by multiplying *contracted unit price* and the corresponding Pricing Quantity. Contracted Cost is denominated in the Billing Currency and is commonly used for calculating savings based on negotiation activities, by comparing it with List Cost. If *negotiated discounts* are not applicable, the Contracted Cost defaults to the List Cost.

## 3.1.33.1 Requirements

ContractedCost MUST adhere to the following requirements:

- ContractedCost MUST be of type Decimal.
- ContractedCost MUST conform to NumericFormat requirements.
- ContractedCost MUST NOT be null.
- ContractedCost MUST be denominated in the BillingCurrency.
- When ContractedUnitPrice is null, ContractedCost MUST adhere to the following requirements:
  - ContractedCost of a *charge* calculated based on other *charges* (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  - ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST be equal to the BilledCost.
- ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.

## 3.1.33.2 Usability Constraints

**Aggregation:** When aggregating Contracted Cost for savings calculations, it's important to exclude either Charge Category "Purchase" *charges* (one-time and recurring) that are paid to cover future eligible *charges* (e.g., commitment discount) or the covered Charge Category "Usage" *charges* themselves. This exclusion helps prevent double counting of these *charges* in the aggregation. Which set of *charges* to exclude depends on whether costs are aggregated on a billed basis (exclude covered *charges*) or accrual basis (exclude Purchases for future *charges*). For instance, *charges* categorized as Charge Category "Purchase" and their related Charge Category "Tax" *charges* for a Commitment Discount might be excluded from an accrual basis cost aggregation of Contracted Cost. This is because the "Usage" and "Tax" charge records provided during the commitment *period* already specify the Contracted Cost. Purchase *charges* that cover future eligible *charges* can be identified by filtering for Charge Category "Purchase" records with a Billed Cost greater than 0 and an Effective Cost equal to 0.

## 3.1.33.5 Description

Cost calculated by multiplying *contracted unit price* and the corresponding Pricing Quantity.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Metric | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Decimal | 
| Value Format | Numeric Format | 
| Number Range | Any valid decimal value |