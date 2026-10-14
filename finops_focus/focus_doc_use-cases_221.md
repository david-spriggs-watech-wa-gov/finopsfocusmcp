---
title: Understand the billing account or sub account entity
url: https://focus.finops.org/docs/use-cases/v1-4/understand-the-billing-account-or-sub-account-entity-2/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: e5b0d19402c12445
---
1. Use Cases
2. Invoicing & Chargeback
3. Understand the billing account or sub account entity

# Understand the billing account or sub account entity

## FOCUS Versions

v1.3
                            v1.4

## Context

List all billing and sub-accounts with charges in the period, showing service provider, account ID, name, and type. This list allows practitioners to map entity hierarchies and allocate costs.

## FOCUS SQL Query

```
SELECT DISTINCT
    ServiceProviderName,
    BillingAccountID,
    BillingAccountName,
    BillingAccountType
FROM focus_data_table
WHERE ChargePeriodStart >= ? and ChargePeriodEnd  < ?
```