---
title: Analyze service costs by subaccount
url: https://focus.finops.org/docs/use-cases/v1-4/service-costs-subaccount/
hostname: finops.org
sitename: focus.finops.org
date: "2026-05-01"
fingerprint: f60429f4bda2a044
---
1. Use Cases
2. Reporting & Analytics
3. Analyze service costs by subaccount

# Analyze service costs by subaccount

## FOCUS Versions

v1.0
                            v1.1
                            v1.2
                            v1.3
                            v1.4

## Context

By understanding the services incurring the highest cost in a subaccount for a period of time, Engineers can get a high-level picture of where to prioritize their efforts when it comes to optimizing usage. Often, the largest optimization opportunities are in the services that incur the most cost.

## FOCUS SQL Query

```
SELECT
  ChargePeriodStart,
  SubAccountId,
  SubAccountName,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE SubAccountID = ?
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
GROUP BY
  ChargePeriodStart,
  SubAccountId,
  SubAccountName,
  ServiceName
ORDER BY SUM(EffectiveCost) DESC
LIMIT 10
```
## FOCUS Datasets

## FOCUS Columns

## Related Capabilities

## Related Personas

## Related KPIs

Power Schedule Adherence Rate
                                            Measures the practice of autoscalers or schedulers, or modifying the power state of virtual machines (VMs) or other cloud resources.

Percentage Resource Utilization
                                            Measure of cloud compute resource utilization, e.g. Compute (EC2), Block Storage (EBS), or Object Storage (S3).

Percentage of Legacy Resource
                                            Measure of the percentage of resources running on ‘modern’ types (e.g. instance types, volume type).

Percent Storage on Frequent Access Tier
                                            Measure of the percent of object storage stored on a Frequent Access Tier.

Percent of Unused Resources
                                            Measure of unused cloud resources, e.g., unattached storage volumes, load balancers, EIPS, and more.

Auto-scaling Efficiency Rate
                                            Measures effectiveness of an auto-scaling system.

Number of Monthly Active Users (MAU) for Cost Insight Products
                                            This measures any one single user accessing any insight Cost Insight Products.

Percentage of Normalized, Queryable Data within Repository
                                            Calculate percentage of normalized and queryable data in data warehouse, repository, or similar, vs Accounts Payable Invoice.