---
title: Analyze credit memos
url: https://focus.finops.org/docs/use-cases/v1-4/analyze-credit-memos-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: b4fdbdfc0a72c002
---
1. Use Cases
2. Unit Economics
3. Analyze credit memos

# Analyze credit memos

## FOCUS Versions

v1.3
                            v1.4

## Context

Locate Service Provider-issued credit memos in billing data and analyze how each one reduces net spend.

## FOCUS SQL Query

```
SELECT 
    ServiceProviderName,
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
AND ChargeCategory = 'Credit'
GROUP BY
    ServiceProviderName,
    InvoiceId
```