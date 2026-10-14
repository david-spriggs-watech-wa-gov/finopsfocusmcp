---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/billing-period/billing-period-created/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3face519a47563a7"
---
# 3.2.1 Billing Period Created

Dataset:
                    Billing Period

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.4

Billing Period Created is the timestamp when the Billing Period record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## 3.2.1.1 Requirements

BillingPeriodCreated MUST adhere to the following requirements:

- BillingPeriodCreated MUST be of type Date/Time.
- BillingPeriodCreated MUST conform to DateTimeFormat requirements.
- BillingPeriodCreated MUST NOT be null.
- BillingPeriodCreated MUST represent the moment in time the Billing Period record was instantiated.

## 3.2.1.4 Description

The timestamp when the *Billing Period* record was first created.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |