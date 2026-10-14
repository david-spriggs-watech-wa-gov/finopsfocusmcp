---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/billing-period/billing-period-status/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: bed4ad23fc238081
---
# 3.2.5 Billing Period Status

Billing Period Status represents the state of the billing period (i.e., "Open" or "Closed"). This status helps FinOps practitioners determine if the Cost and Usage and Invoice Detail data for a given period is preliminary and subject to change, or if all anticipated invoices have been issued and the delivered data is finalized and ready for formal financial reporting and showback/chargeback processes.

## 3.2.5.1 Requirements

BillingPeriodStatus MUST adhere to the following requirements:

- BillingPeriodStatus MUST be of type String.
- BillingPeriodStatus MUST NOT be null.
- BillingPeriodStatus MUST be one of the allowed values.
- BillingPeriodStatus MUST represent the state of the billing period identified by BillingPeriodStart and BillingPeriodEnd.
- BillingPeriodStatus MUST NOT be "Open" following a previous status of "Closed", except when explicitly requested or approved by the customer.

## 3.2.5.2 Allowed Values

| Value | Description | 
|---|---|
| Open | The billing period is currently active or still being processed. Records may continue to be added or revised. | 
| Closed | The billing period has ended, all anticipated invoices have been issued, and the delivered data is finalized. | 

## 3.2.5.3 Implementation Guidance

While the transition from "Open" to "Closed" typically signifies the end of a billing cycle, in scenarios such as the following, it may be necessary to provide corrections to closed billing periods:

- Retroactive adjustments: an *invoice issuer* generates credits or corrections for a period previously marked as finalized.
- Audit corrections: discrepancies are discovered during financial reconciliation that require the data to be re-processed.
- Late-arriving usage: occasional delays in usage reporting necessitate a revision of the final invoice.

Corrections to closed billing periods are generally represented in the context of a subsequent open billing period to preserve historical financial accuracy and ensure transparent tracking. Exceptionally, a previously closed billing period may be reopened to apply such corrections, but this transition from "Closed" to "Open" must be explicitly requested or approved by the customer to maintain auditability and the integrity of financial reporting.

Corrections that do not impact the integrity of the closed billing period, such as informational or metadata updates, are allowed regardless of Billing Period Status.

FinOps tools and reporting engines should be designed to detect Billing Period Status transitions and corrections to closed billing periods, and trigger updates to downstream processes (e.g., cost allocation, chargeback, reporting) to ensure financial accuracy.

For more information, please see the Invoice and Billing Period Handling appendix and the Correction Handling attribute.

## 3.2.5.6 Description

The state of the billing period (i.e., "Open" or "Closed"), indicating whether the delivered data for the period is preliminary, or if all anticipated invoices have been issued and the delivered data is finalized.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |