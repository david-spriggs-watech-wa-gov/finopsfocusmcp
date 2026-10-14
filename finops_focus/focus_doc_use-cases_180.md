---
title: Verify accuracy of provider invoices aka invoice reconciliation
url: https://focus.finops.org/docs/use-cases/v1-4/verify-accuracy-of-provider-invoices-aka-invoice-reconciliation/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: ddc26dd1a9b18000
---
1. Use Cases
2. Allocation
3. Verify accuracy of provider invoices aka invoice reconciliation

# Verify accuracy of provider invoices aka invoice reconciliation

## FOCUS Versions

v1.2
                            v1.3
                            v1.4

## Context

Aggregate provider billing data for each period and reconcile it against provider invoices to validate charge accuracy, flag discrepancies, and strengthen financial accountability.

## FOCUS SQL Query

```
SELECT 
    InvoiceIssuerName,
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
    InvoiceIssuerName,
    InvoiceId
```