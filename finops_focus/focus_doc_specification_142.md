---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/datetime-format/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: e5f1488b60923e81
---
# 4.7 Date/Time Format

Since:
                    0.5

Columns that provide date and time information conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for both humans and systems.

## 4.7.1 Requirements

Column conforming to DateTimeFormat attribute MUST adhere to the following requirements:

- *FOCUS dataset column* MUST be expressed in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
- *FOCUS dataset column* MUST conform to the ISO 8601 standard, which provides a globally recognized format for representing dates and times (see ISO 8601-1:2019 governing document for details).
- When *FOCUS dataset column* represents a specific moment in time, it MUST adhere to the following requirements:
  - *FOCUS dataset column* MUST use the extended ISO 8601 format with UTC offset (`YYYY-MM-DDTHH:mm:ssZ`).
  - *FOCUS dataset column* MUST include both the date and time components, separated with the letter `T`.
  - *FOCUS dataset column* MUST use two-digit hours (`HH`), minutes (`mm`), and seconds (`ss`).
  - *FOCUS dataset column* MUST end with the ISO 8601 UTC designator `Z`.

## 4.7.4 Description

Rules and formatting requirements for date/time-related columns appearing in a *FOCUS dataset*.