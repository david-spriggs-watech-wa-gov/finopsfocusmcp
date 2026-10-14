---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/delivery-handling/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f5f76b99b0ba7501
---
# 4.8 Delivery Handling

## 4.8.1 Overview

The Delivery Handling attribute defines how a *data generator* delivers a *FOCUS dataset* to a customer.

A *dataset instance* represents a specific implementation of a *FOCUS dataset*. A *dataset instance artifact* is the physical delivery of that instance, representing one or more records, independent of storage or transport boundaries (e.g., files, batches, or responses).

### 4.8.1.1 Delivery Mechanisms

FOCUS recognizes two *FOCUS dataset* delivery mechanisms:

- Overwrite: Each delivery provides a complete snapshot, superseding any previously delivered *dataset artifact* for the same *delivery scope* (e.g., temporal grouping such as a *billing period* or non-temporal, logical grouping such as a *contract*).
- Append: Each delivery adds new data, while previously delivered *dataset artifacts* are preserved.

Overwrite and Append mechanisms are not mutually exclusive, and hybrid implementations are common in practice, allowing data generators to meet specific technical and auditability requirements.

For example, for Cost and Usage *FOCUS datasets*, a data generator may use Overwrite mechanism for *dataset artifacts* corresponding to an *open billing period*, ensuring the snapshot reflects the most recent state, while using Append mechanism for *closed billing periods* to preserve historical data and support auditing of corrections to previously *closed billing periods* (i.e., *charges* with Charge Class set to "Correction").

For more information on corrections, see the Correction Handling attribute.

#### 4.8.1.1.1 Overwrite Delivery

In the Overwrite delivery mechanism, each *dataset artifact* provides a complete snapshot of data for a predefined scope (e.g., a *billing period* or a logical grouping), based on the data available at the time of delivery. Subsequent *dataset artifacts* for the same scope typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism provides delivery simplicity, but it lacks inherent auditability. Dataset artifact size typically increases within a delivery scope as underlying data accumulates, but total data volume remains the lowest compared to Append delivery as each dataset artifact supersedes previously delivered ones for the same delivery scope.

Subsequent *dataset artifacts* using the Overwrite mechanism may include the following:

- Unchanged records are carried over.
- Updated records overwrite previous values.
- Additional records supplement previously delivered data.
- Omitted records are removed if no longer applicable.

#### 4.8.1.1.2 Append Delivery

In the Append delivery mechanism, a subsequent *dataset artifact* appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained. Total data volume increases over time as all delivered dataset artifacts are preserved, and is typically higher compared to Overwrite delivery.

Subsequent *dataset artifacts* using the Append mechanism may include the following:

- Unchanged records are not included.
- Updated records are recorded as new entries, representing the net effect on aggregated quantities or costs.
- Additional records supplement previously delivered data.
- Omitted records are recorded as new entries, representing the reversal.

## 4.8.2 Requirements

Dataset conforming to DeliveryHandling attribute MUST adhere to the following requirements:

- *FOCUS dataset* MUST NOT require practitioners to deduplicate records within or across delivered dataset artifacts.
- When using Overwrite delivery mechanism, *FOCUS dataset* MUST adhere to the following additional requirements:
  - *FOCUS dataset* MUST represent a complete snapshot for a given *delivery scope*.
  - *FOCUS dataset* MUST supersede all previously delivered *dataset artifacts* for the same *delivery scope*.
- *FOCUS dataset* MUST preserve all previously delivered *dataset artifacts* when using Append delivery mechanism.
- *FOCUS dataset* SHOULD have delivered *dataset artifacts* accompanied by corresponding FOCUS Metadata.
- *FOCUS dataset* delivery mechanism documentation MUST adhere to the following requirements:
  - *FOCUS dataset* delivery mechanism documentation MUST include the delivery mechanism used (Overwrite or Append).
  - *FOCUS dataset* delivery mechanism documentation MUST include the conditions under which each delivery mechanism applies when more than one delivery mechanism is used.
  - *FOCUS dataset* delivery mechanism documentation MUST include the mechanism for correlating *dataset artifacts* with the FOCUS Metadata Schema object when the Metadata is delivered.
  - *FOCUS dataset* delivery mechanism documentation MUST be accessible to practitioners.

## 4.8.5 Description

Defines how a *data generator* delivers a *FOCUS dataset* to a customer.