---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/dataset-configuration/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: a494503b34927d83
---
# 4.6 Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a *FOCUS dataset*. Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

- **Managing Scale**: Trim large exports to reduce time and cost of data preparation
- **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
- **Lowering Barriers**: Strip away technical complexity for spreadsheet users
- **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## 4.6.1 Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

- *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
- *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
- *FOCUS dataset* MAY offer a default column set.
- *FOCUS dataset* default column set MUST include all applicable *FOCUS columns* when a default column set is offered.

## 4.6.2 Example

A practitioner configures their FOCUS Cost and Usage dataset to include only these columns:

- BillingAccountId
- ServiceName
- BilledCost
- EffectiveCost
- Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant to the FOCUS specification because each included column follows all requirements for that column, including requirements that reference columns not in the dataset.

## 4.6.5 Description

Defines configuration options for controlling the structure and content of a FOCUS dataset.