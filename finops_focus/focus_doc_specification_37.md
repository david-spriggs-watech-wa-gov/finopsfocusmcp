---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-detail-last-updated/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2011-04-03"
fingerprint: fdf4c443a520a0b3
---
# 3.4.11 Invoice Detail Last Updated

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

Invoice Detail Last Updated is the timestamp when the Invoice Detail record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a record, particularly if corrections or status changes have been applied to the record after its initial creation.

## 3.4.11.1 Requirements

InvoiceDetailLastUpdated MUST adhere to the following requirements:

- InvoiceDetailLastUpdated MUST be of type Date/Time.
- InvoiceDetailLastUpdated MUST conform to DateTimeFormat requirements.
- InvoiceDetailLastUpdated MUST NOT be null.
- InvoiceDetailLastUpdated MUST represent the most recent moment in time when any column value of the record identified by InvoiceDetailId was created or modified.
- InvoiceDetailLastUpdated MUST be greater than or equal to InvoiceDetailCreated.

## 3.4.11.4 Description

The timestamp when the Invoice Detail record was last updated.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |