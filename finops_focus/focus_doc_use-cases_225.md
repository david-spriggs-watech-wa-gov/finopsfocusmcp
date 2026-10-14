---
title: Calculate average rate of a component resource
url: https://focus.finops.org/docs/use-cases/v1-4/calculate-average-rate-of-a-component-resource-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "50c2c47bd8a4bf86"
---
1. Use Cases
2. Forecasting
3. Calculate average rate of a component resource

# Calculate average rate of a component resource

## FOCUS Versions

v1.3
                            v1.4

## Context

Aggregate usage and pricing across multiple SKUs to compute the average cost per core for each virtual machine series by region. This common denominator supports benchmarking when billed and consumed units differ.

## FOCUS SQL Query

```
SELECT
    ServiceProviderName,
    ServiceName,
    PricingUnit,
    RegionName,
    JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.InstanceSeries')) AS InstanceSeries, 
    SUM(CAST(JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.CoreCount')) AS UNSIGNED)) AS TotalCoreCount,
    CASE 
        WHEN SUM(CAST(JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.CoreCount')) AS UNSIGNED)) > 0 
        THEN SUM(EffectiveCost) / SUM(CAST(JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.CoreCount')) AS UNSIGNED))
        ELSE NULL
    END AS AverageEffectiveCoreCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
AND JSON_CONTAINS_PATH(SkuPriceDetails, 'all', '$.CoreCount', '$.InstanceSeries')
GROUP BY
    ServiceProviderName,
    ServiceName,
    PricingUnit,
    RegionName,
    InstanceSeries
```