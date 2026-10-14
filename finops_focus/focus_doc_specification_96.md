---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/purchase-order-number/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2021-04-03"
fingerprint: fb51cba00c7f5c09
---
# 3.4.21 Purchase Order Number

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Conditional

Data Type:
                    String

Since:
                    1.4

Purchase Order Number is the unique customer-issued identifier for tracking the lifecycle of a purchase. This identifier is typically provided by the customer to the *invoice issuer* to ensure that charges are mapped to specific internal procurement records or purchase orders.

## 3.4.21.1 Requirements

PurchaseOrderNumber MUST adhere to the following requirements:

- PurchaseOrderNumber MUST be of type String.
- PurchaseOrderNumber MUST conform to StringHandling requirements.
- PurchaseOrderNumber MAY be null.
- PurchaseOrderNumber MUST represent the identifier used by the customer to uniquely identify the purchase order responsible for the charge.

## 3.4.21.4 Description

The unique customer-issued identifier for tracking the lifecycle of a purchase.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |