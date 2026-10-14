---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-detail-created/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b9e0e05bb46dbebf
---
# 3.4.7 Invoice Detail Created

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.4

Invoice Detail Created is the timestamp when the Invoice Detail record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## 3.4.7.1 Requirements

InvoiceDetailCreated MUST adhere to the following requirements:

- InvoiceDetailCreated MUST be of type Date/Time.
- InvoiceDetailCreated MUST conform to DateTimeFormat requirements.
- InvoiceDetailCreated MUST NOT be null.
- InvoiceDetailCreated MUST represent the moment in time the Invoice Detail record was instantiated.
- InvoiceDetailCreated for a given BillingPeriodStart and InvoiceIssuerName MUST be earlier than or equal to BillingPeriod.BillingPeriodLastUpdated for the same BillingPeriod.BillingPeriodStart and BillingPeriod.InvoiceIssuerName when BillingPeriod.BillingPeriodStatus is "Closed".

## 3.4.7.4 Description

The timestamp when the Invoice Detail record was first created.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |