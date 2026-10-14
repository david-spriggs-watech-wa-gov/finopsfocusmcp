---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/account-structures/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: a7b09dbd03832cc5
---
# 2.1 Account Structures

## 2.1.1 Description

Different service providers have different account constructs that FinOps practitioners use for allocation, reporting, and more. Organizations may have one or many accounts within one or more service providers and FinOps practitioners may need to review the cost broken down by each account. FOCUS has two types of accounts: a billing account and a sub account.

A billing account is the account where invoices are generated. Each billing account can have one or more sub accounts, which can be used for deploying and managing resources and services. Billing and sub accounts are often used to facilitate allocation strategies and FinOps practitioners must be able to break costs down by billing and sub account to facilitate FinOps scenarios like chargeback and budgeting.

## 2.1.2 Directly Dependent Columns

## 2.1.3 Supporting Columns

## 2.1.4 Example SQL Query

### Example SQL Query

```
SELECT
  BillingAccountId,
  BillingAccountName,
  BillingAccountType,
  SubAccountId,
  SubAccountName,
  SubAccountType,
  SUM(BilledCost)
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  BillingAccountId,
  SubAccountId
```