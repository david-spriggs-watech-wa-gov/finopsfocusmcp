---
title: Identify sources of billed cost
url: https://focus.finops.org/docs/use-cases/v1-4/identify-sources-of-billed-cost-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: "87e1ef3eed21a8c7"
---
1. Use Cases
2. Allocation
3. Identify sources of billed cost

# Identify sources of billed cost

## FOCUS Versions

v1.3
                            v1.4

## Context

Reconcile billing data from Service Providers, Host Providers, and Invoice Issuers to pinpoint true spend and eliminate duplicate charges.

## FOCUS SQL Query

```
SELECT 
    ServiceProviderName,
    HostProviderName,
    InvoiceIssuerName,
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
GROUP BY
    ServiceProviderName,
    HostProviderName,
    InvoiceIssuerName,
    InvoiceId
```