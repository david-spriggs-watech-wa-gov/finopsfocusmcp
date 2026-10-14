---
title: Reconcile Cost and Usage to Invoice Detail by Invoice ID
url: https://focus.finops.org/docs/use-cases/v1-4/reconcile-cost-and-usage-to-invoice-detail-by-invoice-id/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "2be0e5dc3440bad7"
---
1. Use Cases
2. Invoicing & Chargeback
3. Reconcile Cost and Usage to Invoice Detail by Invoice ID

# Reconcile Cost and Usage to Invoice Detail by Invoice ID

## FOCUS Versions

v1.4

## Context

Validates that the sum of costs for all service usage in the Cost and Usage dataset equals the total non-tax charges in the Invoice Detail dataset for a specific invoice.

## FOCUS SQL Query

```
SELECT
  COALESCE(ID.InvoiceId, CU.InvoiceId) AS InvoiceId,
  ID.TotalBilledCost_InvoiceDetail,
  CU.TotalBilledCost_CostAndUsage,
  (COALESCE(ID.TotalBilledCost_InvoiceDetail, 0) - COALESCE(CU.TotalBilledCost_CostAndUsage, 0)) AS Variance
FROM (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_InvoiceDetail
  FROM InvoiceDetail
  WHERE
    ChargeCategory <> 'Tax'
  GROUP BY
    InvoiceId
) AS ID
FULL OUTER JOIN (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_CostAndUsage
  FROM CostAndUsage
  WHERE
    ChargeCategory <> 'Tax'
  GROUP BY
    InvoiceId
) AS CU
  ON ID.InvoiceId = CU.InvoiceId
WHERE
  COALESCE(ID.InvoiceId, CU.InvoiceId) = ?
```