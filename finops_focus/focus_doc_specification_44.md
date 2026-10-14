---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/json-object-format/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: f5f169d969933541
---
# 4.10 JSON Object Format

Since:
                    1.3

JSON Objects extend the Key-Value Format to add support for complex data types like arrays and nested key-value pairs. This format is used when the Key-Value Format is insufficient to represent the complexity, such as when multiple sets of key-value pairs apply to the same charge record. JSON Objects are also referred to as maps, trees, or hashtables.

## 4.10.1 Requirements

Column conforming to JsonObjectFormat attribute MUST adhere to the following requirements:

- *FOCUS dataset column* MUST contain a serialized JSON string, consistent with the ECMA 404 definition of an object.
- *FOCUS dataset column* MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the object.
- Object in *FOCUS dataset column* SHOULD NOT exceed 3 levels of nesting.
- Key in Object in *FOCUS dataset column* MUST be unique.
- Key value in Object in *FOCUS dataset column* MUST be of type number, string, boolean (`true` or `false`), array, object, or `null`.
- Object in array in *FOCUS dataset column* MUST adhere to the following requirements:
  - Object in array in *FOCUS dataset column* MUST be of a consistent type.
  - Object in array in *FOCUS dataset column* MUST NOT be repeated.
  - Object in array in *FOCUS dataset column* MUST NOT be null.

## 4.10.4 Description

Rules and formatting requirements for columns appearing in a *FOCUS dataset* that convey data as complex, hierarchical objects.