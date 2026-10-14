---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/billed-cost-and-invoice-alignment/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "7b00e7d40a9a7cac"
---
# 2.2 Billed Cost and Invoice Alignment

Since:
                    0.5

## 2.2.1 Description

FOCUS data should be consistent with the costs indicated on payable invoices. This is relevant to the total cost of the invoice, as well as the period of time the invoice covers.

## 2.2.2 Directly Dependent Columns

## 2.2.3 Supporting Columns

## 2.2.4 Example SQL Query

### Example SQL Query

```
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId,
  SUM(BilledCost)
FROM focus_data_table
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId
```