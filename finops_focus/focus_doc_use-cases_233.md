---
title: Determine target of virtual currency usage
url: https://focus.finops.org/docs/use-cases/v1-4/determine-target-of-virtual-currency-usage-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "6e855536ecc38c44"
---
1. Use Cases
2. Allocation
3. Determine target of virtual currency usage

# Determine target of virtual currency usage

## FOCUS Versions

v1.3
                            v1.4

## Context

Identify and rank the top charge categories driving virtual-currency consumption to target optimization efforts.

## FOCUS SQL Query

```
SELECT 
    ServiceProviderName,
    HostProviderName,
    ServiceName,
    ChargeDescription,
    SUM(PricingCurrencyEffectiveCost) AS TotalPricingCurrencyEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
AND PricingCurrency = ?
GROUP BY
    ServiceProviderName,
    HostProviderName,
    ServiceName,
    ChargeDescription
ORDER BY TotalPricingCurrencyEffectiveCost DESC
LIMIT 10
```