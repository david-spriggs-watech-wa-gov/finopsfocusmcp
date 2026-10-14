---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/recency-metadata/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e2f36e163dd1b3e3
---
# 2.18 Recency Metadata

Since:
                    1.3

## 2.18.1 Description

FOCUS supports the ability for data generators to provide metadata indicating 1) what portion of a FOCUS dataset artifact is complete (either in total, or per time sector), and 2) how recently it has been updated. This metadata allows practitioners to understand whether a given subset of FOCUS data is subject to further change, which informs when and whether they can perform various FinOps functions such as chargeback.

## 2.18.2 Applicable Metadata

- Recency
  - Dataset Instance Complete
  - Dataset Instance Last Updated
  - Dataset Instance ID
  - Recency Last Updated
  - Time Sectors
    - Time Sector Start
    - Time Sector End
    - Time Sector Complete
    - Time Sector Last Updated