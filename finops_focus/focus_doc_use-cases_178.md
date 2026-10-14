---
title: Quantify usage of a component resource
url: https://focus.finops.org/docs/use-cases/v1-4/quantify-usage-of-a-component-resource-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: a680c472e8252f84
---
1. Use Cases
2. Planning & Estimating
3. Quantify usage of a component resource

# Quantify usage of a component resource

## FOCUS Versions

v1.3
                            v1.4

## Context

Capture daily aggregate usage of component resources, such as core hours or gigabytes, when Service Providers bill by virtual machines or quantity provisioned. This approach allows FinOps Practitioners to account for scenarios such as analyzing usage across auto-scaled compute services when instantaneous APIs cannot capture historical trends.

## FOCUS SQL Query

```
SELECT
    ServiceProviderName,
    ServiceName,
    PricingUnit,
    RegionName,
    JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.InstanceSeries')) AS InstanceSeries, 
    SUM(CAST(JSON_UNQUOTE(JSON_EXTRACT(SkuPriceDetails, '$.CoreCount')) AS UNSIGNED)) AS TotalCoreCount
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