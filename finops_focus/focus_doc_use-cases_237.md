---
title: Analyze effective cost by pricing currency
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-effective-cost-by-pricing-currency-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: a19e637ea9618ca5
---
1. Use Cases
2. Allocation
3. Analyze effective cost by pricing currency

# Analyze effective cost by pricing currency

## FOCUS Versions

v1.3
                            v1.4

## Context

Break down the effective cost by each pricing currency to surface regional price differences and exchange-rate impacts.

## FOCUS SQL Query

```
SELECT
    ServiceProviderName,
    HostProviderName,
    ServiceName,
    PricingCurrency,
    SUM(PricingCurrencyEffectiveCost) AS TotalPricingCurrencyEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
    ServiceProviderName,
    HostProviderName,
    ServiceName,
    PricingCurrency
```