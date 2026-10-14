---
title: Compare billed cost per subaccount to budget
url: https://focus.finops.org/docs/use-cases/v1-4/compare-billed-cost-per-subaccount-to-budget-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "14c92ffabc20d8a5"
---
1. Use Cases
2. Budgeting
3. Compare billed cost per subaccount to budget

# Compare billed cost per subaccount to budget

## FOCUS Versions

v1.3
                            v1.4

## Context

Product wants to confirm charges are in line with expectations (budgets) for a business which has all its cost within a single subaccount. The ChargePeriod is used for filtering to capture items that apply to the period only (excludes adjustments from previous periods that were applied in the current BillingPeriod).


## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargeCategory = 'Usage'
  AND ChargePeriodStart >= ? and ChargePeriodEnd <= ?
  AND ServiceProviderName = ?  
  AND SubAccountId = ?  
GROUP BY
  ServiceProviderName,
  SubAccountId,
  SubAccountName
```