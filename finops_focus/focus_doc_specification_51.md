---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/null-handling/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b4b56aad6c967f85
---
# 4.12 Null Handling

Since:
                    0.5

*FOCUS dataset* records that don't have a value that can be presented for a column must be handled in a consistent way to reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## 4.12.1 Requirements

Column conforming to NullHandling attribute MUST adhere to the following requirements:

- *FOCUS dataset column* MUST use `null` for absent values when the *FOCUS dataset column* is defined as nullable.
- *FOCUS dataset column* MUST NOT contain empty strings or placeholder strings (e.g., `Not Applicable`) for absent values when the *FOCUS dataset column* contains string values.
- *FOCUS dataset column* MUST NOT contain placeholder numeric values (e.g., `0`) for absent values when the *FOCUS dataset column* contains numeric values.

## 4.12.4 Description

Indicates how to handle columns that don't have a value.