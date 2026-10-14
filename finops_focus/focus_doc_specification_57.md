---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/commitment-program-eligibility-details/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: afe9207ecca178c9
---
# 3.1.29 Commitment Program Eligibility Details

Commitment Program Eligibility Details identifies the *commitment programs* that could potentially cover *charges*, subject to *service provider* constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Program Eligibility Details provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include discount-bearing programs such as *commitment discounts* and *capacity reservations*, provided the service provider treats them as *commitments*.

## 3.1.29.1 Requirements

### 3.1.29.1.1 Column Requirements

CommitmentProgramEligibilityDetails MUST adhere to the following requirements:

- CommitmentProgramEligibilityDetails MUST be of type JSON Object (serialized as a String where necessary).
- CommitmentProgramEligibilityDetails MUST conform to StringHandling requirements.
- CommitmentProgramEligibilityDetails MUST conform to JsonObjectFormat requirements.
- CommitmentProgramEligibilityDetails MUST NOT be null when a charge is eligible for a *commitment program*, regardless of whether a *commitment* was actually applied to the charge.
- CommitmentProgramEligibilityDetails MUST NOT reflect restrictions (e.g., transient account configurations, quotas) that might temporarily prevent purchase or participation in a *commitment program*.
- CommitmentProgramEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
- CommitmentProgramEligibilityDetails MAY include negotiated *commitment programs* when the usage is eligible and the program is not broadly applicable across the service provider's service catalog.
- CommitmentProgramEligibilityDetails MUST NOT include data related to *commitment periods* or payment options.
- CommitmentProgramEligibilityDetails MUST conform to CommitmentProgramEligibilityDetailsObject requirements when CommitmentProgramEligibilityDetails is not null.

## 3.1.29.2 Commitment Program Eligibility Details Object

Commitment Program Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific *commitment programs* available for the usage charge.

### 3.1.29.2.1 Object Requirements

CommitmentProgramEligibilityDetailsObject MUST adhere to the following requirements:

- CommitmentProgramEligibilityDetailsObject MUST conform to the CommitmentProgramEligibilityDetailsObjectSchema JSON Schema.
- CommitmentProgramEligibilityDetailsObject.CommitmentPrograms\[\*\].ProgramType MUST correspond to a *commitment program* type supported by the service provider.
- CommitmentProgramEligibilityDetailsObject.CommitmentPrograms\[\*\].ProgramType MUST match CommitmentDiscountType for one object in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms when CommitmentDiscountType is not null.
- CommitmentProgramEligibilityDetailsObject.CommitmentPrograms\[\*\].ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

### 3.1.29.2.2 Object Schema Structure

| Property | Type | Required | Description | 
|---|---|---|---|
| `CommitmentPrograms` | Array | True | Array of objects identifying *commitment programs* for which the usage is eligible. | 

The `CommitmentPrograms` array contains one or more objects, each of which contains the following entries:

| Key | ValueType | Required | Description | 
|---|---|---|---|
| ProgramType | String | True | The specific type of commitment program (e.g., discount or capacity reservation) available for this usage. | 

### 3.1.29.2.3 Object Implementation Guidance

To facilitate querying data across allocations and across service providers, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `CommitmentPrograms`) or nested within the individual `CommitmentPrograms` objects. Custom keys must be prefixed with "x\_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### 3.1.29.2.4 Object Example

Here is a basic example of the object format.

- For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry here.
- For the JSON schema, please see Commitment Program Eligibility Details Object Schema.

```
{
  "CommitmentPrograms": [
    { "ProgramType": "Flexible Spend Plan" },
    { "ProgramType": "Resource Reservation" },
    { "ProgramType": "Advance Resource Commitment" },
    { "ProgramType": "Zonal Resource Commitment" }
  ]
}
```
### 3.1.29.2.5 Object ID

CommitmentProgramEligibilityDetailsObject

### 3.1.29.2.6 Object Display Name

Commitment Program Eligibility Details Object

## 3.1.29.5 Description

The types of *commitment programs* available for a specific usage row.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | JSON | 
| Value Format | JSON Object Format |