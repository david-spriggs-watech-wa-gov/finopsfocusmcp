---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/datasets/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e8a8e6a26fea73b9
---
# 3 Datasets

Columns:
                    0

FOCUS defines many individual datasets made up of a selected set of columns which abide by the attributes outlined in this FOCUS Specification.

## Dataset List

Datasets are sorted first by Feature Level (i.e., Mandatory, then Conditional), then alphabetically by name.

| Dataset | Dataset Type | Feature Level | Description | 
|---|---|---|---|
| Cost and Usage | Transaction | Mandatory | Describes the cost and usage incurred through using or purchasing a service provider's resources or services. | 
| Billing Period | Reference | Conditional | Describes the billing periods by which cost and usage is invoiced. | 
| Contract Commitment | Reference | Conditional | Describes the terms of contracts agreed between a service provider and a customer. | 
| Invoice Detail | Transaction | Conditional | Describes the cost and usage issued on invoices. |