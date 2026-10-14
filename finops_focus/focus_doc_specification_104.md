---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/allocated-method-details/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "6acb2074c0b73329"
---
# 3.1.2 Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

## 3.1.2.1 Requirements

### 3.1.2.1.1 Column Requirements

AllocatedMethodDetails MUST adhere to the following requirements:

- AllocatedMethodDetails MUST be of type JSON Object (serialized as a String where necessary).
- AllocatedMethodDetails MUST conform to StringHandling requirements.
- AllocatedMethodDetails MUST conform to JsonObjectFormat requirements.
- AllocatedMethodDetails MUST adhere to the following nullability requirements:
  - AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  - AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
- AllocatedMethodDetails MUST conform to AllocatedMethodDetailsObject requirements when AllocatedMethodDetails is not null.

## 3.1.2.2 Allocated Method Details Object

Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

The following section details the normative requirements for the AllocatedMethodDetailsObject and its nested properties. For a logical overview of the expected content, see the Schema Structure and Object Example sections.

### 3.1.2.2.1 Object Requirements

The AllocatedMethodDetailsObject MUST adhere to the following requirements:

- AllocatedMethodDetailsObject MUST conform to the AllocatedMethodDetailsObjectSchema JSON Schema.
- AllocatedMethodDetailsObject.Elements\[\*\].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.
- The sum of AllocatedMethodDetailsObject.Elements\[\*\].AllocatedRatio across all allocated charges related to a single origin charge MUST be equal to 1 (100%).
- AllocatedMethodDetailsObject.Elements\[\*\].UsageUnit SHOULD conform to UnitFormat requirements.
- AllocatedMethodDetailsObject.Elements\[\*\].UsageUnit MUST represent the unit or component of data generator's documented AllocationMethod which was used to determine the AllocatedMethodDetailsObject.Elements\[\*\].AllocatedRatio value.
- AllocatedMethodDetailsObject.Elements\[\*\].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements\[\*\].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements\[\*\].AllocatedRatio value.

### 3.1.2.2.2 Object Schema Structure

AllocatedMethodDetails contains a structured JSON object defining the allocation properties used to calculate a split cost allocation.

| Property | Type | Required | Description | 
|---|---|---|---|
| `Elements` | Array | True | The parent array containing one or more objects which communicate information about how an allocated record was calculated. | 

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key | Type | Required | Description | 
|---|---|---|---|
| `AllocatedRatio` | Numeric | True | Communicates the percentage of the *Origin Charge* that this *Allocated Charge* derived from the corresponding Allocated Method Id and Usage Unit property. | 
| `UsageUnit` | String | Conditional | Communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property. **Condition:** must be present if Usage Quantity is provided. | 
| `UsageQuantity` | Numeric | False | Communicates the volume that was consumed or used, denominated in the Usage Unit property value. | 

### 3.1.2.2.3 Object Implementation Guidance

To facilitate querying data across allocations and across data generators, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `Elements`) or nested within the individual `Elements` objects. Custom keys must be prefixed with "x\_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### 3.1.2.2.4 Object Example

Here is a basic example of the object format.

- For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry here.
- For the JSON schema, please see Allocated Method Details Object Schema.

```
{
  "Elements" : [ {
    "AllocatedRatio" : 0.05,
    "UsageUnit" : "CPU",
    "UsageQuantity" : 0.5
  }, {
    "AllocatedRatio" : 0.1,
    "UsageUnit" : "Memory",
    "UsageQuantity" : 4
  } ]
}
```
### 3.1.2.2.5 Object ID

AllocatedMethodDetailsObject

### 3.1.2.2.6 Object Display Name

Allocated Method Details Object

## 3.1.2.5 Description

A set of properties describing how resources are allocated in data generator-defined split cost allocation.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension / Metric | 
| Feature Level | Recommended | 
| Allows Nulls | Yes | 
| Data Type | JSON | 
| Value Format | JSON Object Format |