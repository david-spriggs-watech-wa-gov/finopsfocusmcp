---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-model/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2014-03-03"
fingerprint: b65b10390fa1ced9
---
# 3.3.14 Contract Commitment Model

Contract Commitment Model represents the operational behavior and consumption flexibility of a *contract commitment*. This field distinguishes between rigid, "use-it-or-lose-it" obligations (typically hourly) and flexible, aggregate-based agreements that accommodate variable usage patterns.

Contract Commitment Model has two possible values: **Continuous** and **Discontinuous**. Continuous models (e.g., reserved instances, savings plans) represent a flat, constant "floor" of commitment where any dip in usage results in immediate, unrecoverable waste. Discontinuous models (e.g., enterprise agreements, SaaS minimum spend agreements) represent a broader, more flexible bucket where the commitment is "spikier": the usage can fluctuate wildly, but as long as the aggregate hits the target (or the true-up handles the variance), the commitment is satisfied. In either case, the interval of the commitment is represented by the Contract Commitment Fulfillment Interval.

## 3.3.14.1 Requirements

ContractCommitmentModel MUST adhere to the following requirements:

- ContractCommitmentModel MUST be of type String.
- ContractCommitmentModel MUST NOT be null.
- ContractCommitmentModel MUST be one of the allowed values.
- ContractCommitmentModel MUST be "Discontinuous" when ContractCommitmentFulfillmentInterval is "Full Period".

## 3.3.14.2 Allowed Values

| Value | Description | 
|---|---|
| Continuous | A flat, constant "floor" of commitment (e.g., RIs, Savings Plans). Coverage is applied at a fixed rate per Contract Commitment Fulfillment Interval (usually hourly), and benefits are not carried over to subsequent intervals. | 
| Discontinuous | A flexible, aggregate commitment (e.g., Enterprise Agreements, SaaS Minimum Spend). Coverage is measured over a broad window or against a total monetary value. | 

## 3.3.14.3 Implementation Guidance

### 3.3.14.3.1 Reporting and Analysis

- For *continuous* models: report on Utilization % to identify immediate waste.
- For *discontinuous* models: report on Burn Rate and Remaining Balance to ensure the "spikes" are not trending toward an early exhaustion of the fund or a massive year-end true-up bill.

### 3.3.14.3.2 Relationship with Fulfillment Interval

Because a `Continuous` model dictates a recurring, "use-it-or-lose-it" evaluation window, it cannot logically span an entire, cumulative contract term without a reset. Therefore, if the associated Contract Commitment Fulfillment Interval is `Full Period`, the Contract Commitment Model must be categorized as `Discontinuous`.

## 3.3.14.6 Description

Represents the operational behavior and consumption flexibility of a *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |