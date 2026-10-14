---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/currency-format/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e4b7e8bf6a933c85
---
# 4.2 Currency Format

Since:
                    0.5

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

- National currency (e.g., USD, EUR).
- Virtual currency (e.g., tokens, credits).

## 4.2.1 Requirements

Column conforming to CurrencyFormat attribute MUST adhere to the following requirements:

- *FOCUS dataset column* MUST conform to ISO 4217:2015 standard.
- *FOCUS dataset column* MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).

## 4.2.4 Description

Formatting for currency columns appearing in a *FOCUS dataset*.