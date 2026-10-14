---
title: Analyze resource costs by SKU
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-resource-costs-by-sku/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: c75007f29b14a306
---
1. Use Cases
2. Reporting & Analytics
3. Analyze resource costs by SKU

# Analyze resource costs by SKU

## FOCUS Versions

v1.3
                            v1.4

## Context

Understanding the highest costing SKUs can help multiple personas in an organization achieve goals, such as:

1. **Contract negotiation**: Procurement teams can use this information to negotiate the best possible discounts with cloud providers.
2. **SKU-based forecasting**: Product and Finance teams can use this information to forecast future demand for SKUs and plan accordingly.
3. **High unit-cost cleanup**: FinOps teams can use this information to identify and prioritize SKUs with high unit costs, which can be optimized or eliminated to reduce overall cloud spend.

## FOCUS SQL Query

```
SELECT
  ServiceProviderName,
  ChargePeriodStart,
  ChargePeriodEnd,
  SkuId,
  SkuPriceId,
  PricingUnit,
  ListUnitPrice,
  SUM(PricingQuantity) AS TotalPricingQuantity,
  SUM(ListCost) AS TotalListCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
  ServiceProviderName,
  ChargePeriodStart,
  ChargePeriodEnd,
  SkuId,
  SkuPriceId,
  PricingUnit,
  ListUnitPrice
ORDER BY
  ChargePeriodStart ASC
LIMIT 100
```