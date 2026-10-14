---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-frequency/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2019-01-03"
fingerprint: ff545428d7674c86
---
# 3.1.19 Charge Frequency

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Recommended

Data Type:
                    String

Since:
                    1.0-preview

Charge Frequency indicates how often a *charge* will occur. Along with the charge period related columns, the Charge Frequency is commonly used to understand recurrence periods (e.g., monthly, yearly); forecast upcoming *charges*; and differentiate between one-time and recurring fees for purchases.

## 3.1.19.1 Requirements

ChargeFrequency MUST adhere to the following requirements:

- ChargeFrequency MUST be of type String.
- ChargeFrequency MUST NOT be null.
- ChargeFrequency MUST be one of the allowed values.
- ChargeFrequency MUST NOT be "Usage-Based" when ChargeCategory is "Purchase".

## 3.1.19.2 Allowed Values

| Value | Description | 
|---|---|
| One-Time | *Charges* that only happen once and will not repeat. One-time *charges* are typically recorded on the hour or day when the cost was incurred. | 
| Recurring | *Charges* that repeat on a periodic cadence (e.g., weekly, monthly) regardless of whether the product or *service* was used. Recurring *charges* typically happen on the same day or point within every period. The charge date does not change based on how or when the *service* is used. | 
| Usage-Based | *Charges* that repeat every time the *service* is used. Usage-based *charges* are typically recorded hourly or daily, based on the granularity of the cost data for the period when the *service* was used (referred to as *charge period*). Usage-based *charges* are not recorded when the *service* is not used. | 

## 3.1.19.5 Description

Indicates how often a *charge* will occur.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Recommended | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |