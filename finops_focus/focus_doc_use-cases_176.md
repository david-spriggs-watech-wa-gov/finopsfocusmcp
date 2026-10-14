---
title: Validate Tax Variance
url: https://focus.finops.org/docs/use-cases/v1-4/validate-tax-variance/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "74e1f5d530926a52"
---
1. Use Cases
2. Invoicing & Chargeback
3. Validate Tax Variance

# Validate Tax Variance

## FOCUS Versions

v1.4

## Context

Identifies the tax component present in the Invoice Detail dataset that is typically excluded from the Cost and Usage dataset, allowing for a complete three-way match between usage, tax, and the total invoice amount.

## FOCUS SQL Query

```
SELECT
  InvoiceId,
  SUM(CASE WHEN ChargeCategory = 'Tax' THEN BilledCost ELSE 0 END) AS TotalTaxAmount,
  SUM(CASE WHEN ChargeCategory <> 'Tax' THEN BilledCost ELSE 0 END) AS TotalServiceAmount,
  SUM(BilledCost) AS GrandTotalPayable
FROM InvoiceDetail
WHERE
  InvoiceId = ?
GROUP BY
  InvoiceId
```