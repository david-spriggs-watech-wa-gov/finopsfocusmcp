---
title: Calculate unit economics
url: https://focus.finops.org/docs/use-cases/v1-4/calculate-unit-economics/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: dea56df7a8c07c90
---
1. Use Cases
2. Reporting & Analytics
3. Calculate unit economics

# Calculate unit economics

## FOCUS Versions

v1.2
                            v1.3
                            v1.4

## Context

Calculate unit-cost metrics (e.g., cost per GB of storage) to expose cost density and target optimizations that lower overall spend.

## FOCUS SQL Query

```
SELECT
    CAST(ChargePeriodStart AS DATE) AS ChargePeriodDate,
    SUM(BilledCost) / NULLIF(SUM(CAST(ConsumedQuantity AS DECIMAL(10, 2))), 0) AS CostPerGB
FROM focus_data_table
WHERE
    ChargeDescription LIKE '%transfer%'
    AND ConsumedUnit = 'GB'
GROUP BY
    CAST(ChargePeriodStart AS DATE)
ORDER BY
    ChargePeriodDate ASC;
```