---
title: Determine contracted savings by virtual currency
url: https://focus.finops.org/docs/use-cases/v1-4/determine-contracted-savings-by-virtual-currency/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "5e8600fe6581ad0d"
---
1. Use Cases
2. Planning & Estimating
3. Determine contracted savings by virtual currency

# Determine contracted savings by virtual currency

## FOCUS Versions

v1.2
                            v1.3
                            v1.4

## Context

Compare the virtual currency discounted rate to the virtual currency list price to determine the difference, as contracts can lower the virtual-currency price of certain operations.

## FOCUS SQL Query

```
SELECT 
        ServiceName,
        ServiceSubcategory,
        ChargeDescription,
        BillingCurrency,
        PricingCurrency,
        SUM(PricingCurrencyListUnitPrice-PricingCurrencyContractedUnitPrice) AS ContractedSavingsInPricingCurrency,
        SUM(ListUnitPrice - ContractedUnitPrice) AS ContractedSavingsInBillingCurrency
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
AND PricingCurrencyListUnitPrice > PricingCurrencyContractedUnitPrice
GROUP BY
        ServiceName,
        ServiceSubcategory,
        ChargeDescription,
        BillingCurrency,
        PricingCurrency
```