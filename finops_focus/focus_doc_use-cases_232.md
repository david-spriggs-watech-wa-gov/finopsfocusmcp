---
title: Analyze purchase of virtual currency
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-purchase-of-virtual-currency-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: d41045fea1614003
---
1. Use Cases
2. Allocation
3. Analyze purchase of virtual currency

# Analyze purchase of virtual currency

## FOCUS Versions

v1.3
                            v1.4

## Context

Analyze virtual-currency purchase patterns (e.g., upfront) and actively monitor burn down to prevent overage charges.

## FOCUS SQL Query

v1-3

```
SELECT
    ServiceProviderName,
    PublisherName,
    ChargeDescription,
    PricingUnit,
    BillingCurrency,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
    AND ChargeCategory = 'Purchase'
     AND PricingUnit = ?
GROUP BY
    ServiceProviderName,
    PublisherName,
    ChargeDescription,
    PricingUnit,
    BillingCurrency
```
v1-4

```
SELECT
    ServiceProviderName,
    ChargeDescription,
    PricingUnit,
    BillingCurrency,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
    AND ChargeCategory = 'Purchase'
     AND PricingUnit = ?
GROUP BY
    ServiceProviderName,
    ChargeDescription,
    PricingUnit,
    BillingCurrency
```