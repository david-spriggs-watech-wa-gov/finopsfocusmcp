---
title: Calculate consumption of virtual currency within a billing period
url: https://focus.finops.org/docs/use-cases/v1-4/calculate-consumption-of-virtual-currency-within-a-billing-period-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "46159db3da11ac84"
---
1. Use Cases
2. Budgeting
3. Calculate consumption of virtual currency within a billing period

# Calculate consumption of virtual currency within a billing period

## FOCUS Versions

v1.3
                            v1.4

## Context

Track virtual-currency burn throughout the billing period to forecast exhaustion dates and stay within budget.

## FOCUS SQL Query

```
SELECT 
    ServiceProviderName,
    SUM(PricingCurrencyEffectiveCost) AS TotalPricingCurrencyEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
AND PricingCurrency = ?
AND ChargeCategory = 'Usage'
GROUP BY
    ServiceProviderName
ORDER BY TotalPricingCurrencyEffectiveCost DESC
LIMIT 10
```