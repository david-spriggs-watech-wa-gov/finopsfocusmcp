---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/dataset-instance-metadata/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e1e35b9475927183
---
# 2.12 Dataset Instance Metadata

Since:
                    1.3

## 2.12.1 Description

FOCUS supports the ability for data generators to provide metadata that describes information about the *dataset artifacts* they provide. This includes properties such as the name of the *dataset instance*, the unique identifier of the *dataset instance*, and the *FOCUS dataset* that it aligns with. This metadata can be used by consumers to understand the context of the data they are receiving, and to ensure that they are working with the correct dataset instance to execute their particular FinOps use cases.

## 2.12.2 Applicable Metadata

- Dataset Instance
  - Dataset Instance ID
  - Dataset Instance Name
  - FOCUS Dataset ID